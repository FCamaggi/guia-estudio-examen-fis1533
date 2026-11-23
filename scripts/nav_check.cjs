// Navigation regression check for the one-unit-at-a-time shell (js/00-guide.js).
// Usage: node scripts/nav_check.cjs [index.html|dist/guia-examen.html]   (needs network for MathJax)
const path = require("path");
function loadPlaywright() {
  const candidates = ["playwright",
    `${process.env.HOME}/.nvm/versions/node/${process.version}/lib/node_modules/@playwright/cli/node_modules/playwright`];
  for (const c of candidates) { try { return require(c); } catch { /* try next */ } }
  console.error("playwright not found; set NODE_PATH or install it");
  process.exit(2);
}
const pw = loadPlaywright();
const file = process.argv[2] || "index.html";
let failed = false;
const url = "file://" + path.resolve(file);
const ok = (c, m) => { if (!c) failed = true; console.log((c ? "PASS " : "FAIL ") + m); };
(async () => {
  const b = await pw.chromium.launch();
  const page = await b.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = [];
  page.on("pageerror", e => errs.push(e.message));
  page.on("console", m => { if (m.type() === "error") errs.push(m.text()); });
  const t0 = Date.now();
  await page.goto(url);
  await page.waitForFunction(() => window.MathJax && MathJax.startup && MathJax.startup.promise && document.querySelector("#unit-host mjx-container"), null, { timeout: 60000 });
  console.log("ready ms", Date.now() - t0);
  const info = await page.evaluate(() => ({
    nodes: document.querySelectorAll("*").length,
    units: document.querySelectorAll("#unit-host section.unit").length,
    cur: Guide.current, mjx: document.querySelectorAll("mjx-container").length,
    prog: document.getElementById("prog-count").textContent,
    openToc: document.querySelectorAll(".toc-unit.open").length,
    visibleSubs: [...document.querySelectorAll(".toc a.sub")].filter(a => a.offsetParent).length,
  }));
  console.log(JSON.stringify(info));
  ok(info.units === 1 && info.cur === "r01", "only r01 mounted at start");
  // TOC click to u03 -> top
  await page.evaluate(() => window.scrollTo(0, 2000));
  await page.click('.toc a.toc-u[data-unit="u03"]');
  let s = await page.evaluate(() => ({ cur: Guide.current, y: scrollY, h: location.hash, n: document.querySelectorAll("#unit-host section.unit").length }));
  ok(s.cur === "u03" && s.y === 0 && s.h === "#u03" && s.n === 1, "TOC click opens u03 at top " + JSON.stringify(s));
  // answer a quiz question in u03
  await page.evaluate(() => document.querySelector("#u03-quiz-1 .q .opts button").click());
  // deep link to u09-s2 via hash
  await page.evaluate(() => { location.hash = "#u09-s2"; });
  await page.waitForTimeout(500);
  s = await page.evaluate(() => ({ cur: Guide.current, top: Math.round(document.getElementById("u09-s2").getBoundingClientRect().top) }));
  ok(s.cur === "u09" && Math.abs(s.top - 16) < 5, "hash deep link opens u09 at section " + JSON.stringify(s));
  // reveal 2 steps in first prob of u09
  await page.evaluate(() => { const p = document.querySelector("#unit-host .prob .ctrl button.primary"); p.click(); p.click(); });
  const shownBefore = await page.evaluate(() => document.querySelectorAll("#unit-host .prob")[0].querySelectorAll(".reveal > li.shown").length);
  await page.evaluate(() => window.scrollTo(0, 5000));
  await page.waitForTimeout(400);
  const yBefore = await page.evaluate(() => scrollY);
  // go to u03 by clicking a TOC link then back
  await page.click('.toc a.toc-u[data-unit="u03"]');
  const quizKept = await page.evaluate(() => document.querySelectorAll("#u03-quiz-1 .q.answered").length);
  ok(quizKept === 1, "u03 quiz answer kept after switching units");
  await page.goBack();
  await page.waitForTimeout(800);
  s = await page.evaluate(() => ({ cur: Guide.current, y: scrollY, shown: document.querySelectorAll("#unit-host .prob")[0].querySelectorAll(".reveal > li.shown").length }));
  ok(s.cur === "u09" && Math.abs(s.y - yBefore) < 40, `back restores u09 position (${yBefore} -> ${s.y})`);
  ok(s.shown === shownBefore && shownBefore === 2, "revealed steps kept: " + s.shown);
  // reload restores
  await page.waitForTimeout(400);
  // Compare what the reader sees (the block at a fixed viewport point), not scrollY:
  // lazy typesetting changes the height of content above, so scrollY may legitimately differ.
  const VIEW = () => { const e = document.elementFromPoint(640, 200); const b = e.closest("p,li,h2,h3,td,div") || e;
    return { y: scrollY, top: Math.round(b.getBoundingClientRect().top), t: b.textContent.trim().slice(0, 60) }; };
  const vR = await page.evaluate(VIEW);
  await page.reload();
  await page.waitForFunction(() => window.Guide && Guide.current, null, { timeout: 30000 });
  await page.waitForTimeout(2500);
  s = await page.evaluate(VIEW); s.cur = await page.evaluate(() => Guide.current);
  ok(s.cur === "u09" && s.t === vR.t && Math.abs(s.top - vR.top) < 40,
    `reload restores u09 position (same block "${vR.t.slice(0, 24)}…", top ${vR.top} -> ${s.top}, y ${vR.y} -> ${s.y})`);
  // in-content link: r01 links
  await page.click('.toc a.toc-u[data-unit="r01"]');
  const link = await page.evaluate(() => { const a = [...document.querySelectorAll('#unit-host a[href^="#u"]')].find(a => /#u\d\d-/.test(a.getAttribute("href"))); return a && a.getAttribute("href"); });
  if (link) {
    await page.click(`#unit-host a[href="${link}"]`);
    await page.waitForTimeout(500);
    s = await page.evaluate((l) => ({ cur: Guide.current, top: Math.round(document.getElementById(l.slice(1)).getBoundingClientRect().top) }), link);
    ok(Math.abs(s.top - 16) < 5 && link.slice(1, 4) === s.cur, `content link ${link} jumps ` + JSON.stringify(s));
  }
  // simulators
  await page.click('.toc a.toc-u[data-unit="t01"]');
  await page.waitForTimeout(300);
  let ro = await page.evaluate(() => document.querySelector("#t01-rl-canvas").width);
  ok(ro > 0, "t01 canvas drawn " + ro);
  // mock exam timer keeps running
  await page.click('.toc a.toc-u[data-unit="s01"]');
  await page.click("#unit-host .sim-start");
  const t1 = await page.evaluate(() => document.querySelector("#unit-host .sim-time").textContent);
  await page.click('.toc a.toc-u[data-unit="t01"]');
  await page.waitForTimeout(2200);
  await page.click('.toc a.toc-u[data-unit="s01"]');
  const t2 = await page.evaluate(() => document.querySelector("#unit-host .sim-time").textContent);
  ok(t1 !== t2, `timer kept running while hidden (${t1} -> ${t2})`);
  // pager
  const pg = await page.evaluate(() => [...document.querySelectorAll("#unit-host .unit-pager a")].map(a => a.getAttribute("href")));
  ok(pg.length >= 1, "pager links " + pg.join(","));
  // master toggle updates progress
  await page.click('.toc a.toc-u[data-unit="u01"]');
  const before = await page.textContent("#prog-count");
  await page.click("#unit-host .master");
  const after = await page.textContent("#prog-count");
  await page.click("#unit-host .master");
  ok(before !== after, `master toggles progress ${before} -> ${after}`);
  // TOC section search (S4): accent-insensitive, across all units, Enter opens, Escape clears
  const vis = () => page.evaluate(() => [...document.querySelectorAll(".toc a.sub")].filter(a => a.offsetParent).map(a => a.getAttribute("href")));
  await page.fill("#toc-q", "MUTUA");
  let hits = await vis();
  ok(hits.includes("#u10-s1"), "search 'MUTUA' finds u10 section across units: " + hits.join(","));
  await page.fill("#toc-q", "induccion");
  hits = await vis();
  ok(hits.some(h => h.startsWith("#u09")), "accent-insensitive search 'induccion' lists u09 sections (" + hits.length + ")");
  await page.fill("#toc-q", "zzzqqq");
  const emptyShown = await page.evaluate(() => !document.getElementById("toc-empty").hidden && [...document.querySelectorAll(".toc-unit")].every(u => u.hidden));
  ok(emptyShown, "no-match query shows 'Sin resultados'");
  await page.fill("#toc-q", "MUTUA");
  await page.press("#toc-q", "Enter");
  await page.waitForTimeout(400);
  s = await page.evaluate(() => ({ cur: Guide.current, h: location.hash }));
  ok(s.cur === "u10" && s.h === "#u10-s1", "Enter opens first result " + JSON.stringify(s));
  await page.press("#toc-q", "Escape");
  const cleared = await page.evaluate(() => ({ q: document.getElementById("toc-q").value,
    hidden: [...document.querySelectorAll(".toc-unit")].filter(u => u.hidden).length,
    subs: [...document.querySelectorAll(".toc a.sub")].filter(a => a.offsetParent).every(a => a.closest(".toc-unit").classList.contains("open")) }));
  ok(cleared.q === "" && cleared.hidden === 0 && cleared.subs, "Escape clears search and only the active unit stays expanded");
  ok(errs.length === 0, "no console errors " + errs.slice(0, 5).join(" | "));
  await b.close();
  process.exit(failed ? 1 : 0);
})();
