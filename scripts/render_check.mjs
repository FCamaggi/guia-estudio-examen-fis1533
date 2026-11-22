#!/usr/bin/env node
// Visual QA: renders SVG figures or HTML pages to PNG with headless Chromium
// and reports console errors, MathJax errors and broken images.
//
// Usage:
//   node scripts/render_check.mjs <file...> [--out qa/render] [--dark] [--width 900]
//
// Output: one PNG per input in --out, plus a JSON summary on stdout.
// Exit code 1 if any page reports errors.

import { createRequire } from "node:module";
import { mkdirSync, readFileSync } from "node:fs";
import { basename, resolve } from "node:path";
import { pathToFileURL } from "node:url";

const require = createRequire(import.meta.url);
const PW_CANDIDATES = [
  "playwright",
  `${process.env.HOME}/.nvm/versions/node/${process.version}/lib/node_modules/@playwright/cli/node_modules/playwright`,
];

function loadPlaywright() {
  for (const p of PW_CANDIDATES) {
    try {
      return require(p);
    } catch {
      /* try next */
    }
  }
  console.error("playwright not found; set NODE_PATH or install it");
  process.exit(2);
}

const args = process.argv.slice(2);
const files = [];
let outDir = "qa/render";
let dark = false;
let width = 900;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--out") outDir = args[++i];
  else if (args[i] === "--dark") dark = true;
  else if (args[i] === "--width") width = Number(args[++i]);
  else files.push(args[i]);
}
if (files.length === 0) {
  console.error("usage: render_check.mjs <file...> [--out dir] [--dark] [--width px]");
  process.exit(2);
}

mkdirSync(outDir, { recursive: true });
const { chromium } = loadPlaywright();
const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width, height: 800 },
  deviceScaleFactor: 2,
  colorScheme: dark ? "dark" : "light",
});

const results = [];
let failed = false;
for (const f of files) {
  const page = await ctx.newPage();
  const errors = [];
  page.on("console", (m) => m.type() === "error" && errors.push(`console: ${m.text()}`));
  page.on("pageerror", (e) => errors.push(`pageerror: ${e.message}`));
  const isSvg = f.endsWith(".svg");
  if (isSvg) {
    // Screenshots of bare SVG documents hang in Chromium; embed in a page instead.
    const svg = readFileSync(resolve(f), "utf8");
    const bg = dark ? "#0e131a" : "#f4f6f9";
    await page.setContent(
      `<!doctype html><html><body style="margin:0;padding:16px;background:${bg}">${svg}</body></html>`,
    );
  } else {
    await page.goto(pathToFileURL(resolve(f)).href, { waitUntil: "networkidle" });
  }
  if (f.endsWith(".html")) {
    // Wait for MathJax to finish typesetting when present.
    await page
      .evaluate(() => window.MathJax?.startup?.promise ?? null)
      .catch(() => null);
    const mathErrors = await page.$$eval("mjx-merror, .MathJax_Error", (els) =>
      els.map((e) => e.getAttribute("data-mjx-error") || e.textContent).slice(0, 20),
    );
    mathErrors.forEach((m) => errors.push(`mathjax: ${m}`));
    const broken = await page.$$eval("img", (imgs) =>
      imgs.filter((i) => !i.complete || i.naturalWidth === 0).map((i) => i.src),
    );
    broken.forEach((b) => errors.push(`broken-img: ${b}`));
  }
  const png = `${outDir}/${basename(f).replace(/\.(svg|html)$/, "")}${dark ? ".dark" : ""}.png`;
  if (isSvg) await page.locator("svg").first().screenshot({ path: png });
  else await page.screenshot({ path: png, fullPage: true });
  results.push({ file: f, png, errors });
  if (errors.length) failed = true;
  await page.close();
}
await browser.close();
console.log(JSON.stringify(results, null, 2));
process.exit(failed ? 1 : 0);
