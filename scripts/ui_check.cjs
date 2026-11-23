// UI regression check for S5 (mobile shell, derivations, study loop, accessibility, hierarchy).
// Usage: node scripts/ui_check.cjs [index.html|dist/guia-examen.html]   (needs network for MathJax)
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
const url = "file://" + path.resolve(file);
let failed = false;
const ok = (c, m) => { if (!c) failed = true; console.log((c ? "PASS " : "FAIL ") + m); };

// Contrast helpers evaluated in the page.
const CONTRAST = `
  window.__lum = c => { const m = c.match(/[\\d.]+/g).map(Number).slice(0, 3).map(v => v / 255)
    .map(v => v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4)); return 0.2126 * m[0] + 0.7152 * m[1] + 0.0722 * m[2]; };
  window.__ratio = (a, b) => { const x = __lum(a), y = __lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
`;

async function open(ctx, hash, w = 1280, h = 900) {
  const page = await ctx.newPage();
  await page.setViewportSize({ width: w, height: h });
  await page.goto(url + (hash || ""));
  await page.waitForFunction(() => window.Guide && Guide.current, null, { timeout: 30000 });
  await page.waitForTimeout(600);
  await page.addScriptTag({ content: CONTRAST });
  return page;
}

async function reload(page) {
  await page.reload();
  await page.waitForFunction(() => window.Guide && Guide.current, null, { timeout: 30000 });
  await page.waitForTimeout(500);
  await page.addScriptTag({ content: CONTRAST });
}

(async () => {
  const b = await pw.chromium.launch();
  const errs = [];
  const ctx = await b.newContext();
  ctx.on("page", p => { p.on("pageerror", e => errs.push(e.message)); });

  /* ---------- S5a mobile shell ---------- */
  for (const h of ["", "#u09-s2", "#s01", "#t01"]) {
    const p = await open(ctx, h, 390, 844);
    const o = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
    ok(o.sw <= o.cw, `390px no horizontal overflow ${h || "#r01"} (${o.sw} <= ${o.cw})`);
    await p.close();
  }
  let p = await open(ctx, "#u09-s2", 390, 844);
  let m = await p.evaluate(() => {
    const bar = document.querySelector(".topbar"), toc = document.getElementById("toc");
    const r = toc.getBoundingClientRect();
    return { bar: bar ? Math.round(bar.getBoundingClientRect().height) : -1, label: bar ? bar.textContent : "",
      tocOff: r.right <= 0 || getComputedStyle(toc).visibility === "hidden" };
  });
  ok(m.bar > 0 && m.bar <= 64, "mobile top bar present and compact (" + m.bar + "px)");
  ok(/U9/.test(m.label), "top bar names the current unit: " + m.label.trim().replace(/\s+/g, " ").slice(0, 60));
  ok(m.tocOff, "TOC is off-canvas on mobile until opened");
  await p.click(".topbar .toc-toggle");
  await p.waitForTimeout(400);
  m = await p.evaluate(() => ({ exp: document.querySelector(".toc-toggle").getAttribute("aria-expanded"),
    left: Math.round(document.getElementById("toc").getBoundingClientRect().left),
    targets: [...document.querySelectorAll(".toc-unit.open a, .toc a.toc-u")].filter(a => a.offsetParent)
      .map(a => Math.round(a.getBoundingClientRect().height)) }));
  ok(m.exp === "true" && m.left >= 0, "menu button opens the TOC panel");
  ok(m.targets.length > 0 && Math.min(...m.targets) >= 44, "TOC links >= 44px tall on mobile (min " + Math.min(...m.targets) + ")");
  await p.keyboard.press("Escape");
  await p.waitForTimeout(400);
  m = await p.evaluate(() => ({ exp: document.querySelector(".toc-toggle").getAttribute("aria-expanded"),
    focus: document.activeElement && document.activeElement.classList.contains("toc-toggle") }));
  ok(m.exp === "false" && m.focus, "Escape closes the panel and returns focus to the menu button");
  await p.click(".topbar .toc-toggle");
  await p.waitForTimeout(300);
  await p.click('.toc a.toc-u[data-unit="u03"]');
  await p.waitForTimeout(400);
  m = await p.evaluate(() => ({ cur: Guide.current, exp: document.querySelector(".toc-toggle").getAttribute("aria-expanded") }));
  ok(m.cur === "u03" && m.exp === "false", "choosing a unit in the panel navigates and closes it");
  m = await p.evaluate(() => [...document.querySelectorAll("#unit-host .master, #unit-host .ctrl button, #unit-host .opts button")]
    .filter(e => e.offsetParent).map(e => Math.round(e.getBoundingClientRect().height)));
  ok(m.length > 0 && Math.min(...m) >= 44, "content controls >= 44px tall on mobile (min " + Math.min(...m) + ")");
  await p.close();
  p = await open(ctx, "#s01-enunciados", 390, 844);
  await p.waitForTimeout(400);
  m = await p.evaluate(() => ({ bar: document.querySelector(".topbar").getBoundingClientRect().bottom,
    sim: document.querySelector("#unit-host .sim-bar").getBoundingClientRect().top }));
  ok(m.sim >= m.bar - 1, `mock-exam bar sits below the top bar (${Math.round(m.sim)} >= ${Math.round(m.bar)})`);
  await p.close();

  /* ---------- S5b derivations ---------- */
  p = await open(ctx, "#u09");
  m = await p.evaluate(() => ({ n: document.querySelectorAll("#unit-host details.deriv").length,
    open: document.querySelectorAll("#unit-host details.deriv[open]").length, btn: !!document.querySelector("#unit-host .deriv-all") }));
  ok(m.n > 0 && m.open === 0, `u09 derivations closed by default (${m.open}/${m.n} open)`);
  ok(m.btn, "u09 has an open-all-derivations button");
  await p.click("#unit-host .deriv-all");
  await reload(p);
  m = await p.evaluate(() => [document.querySelectorAll("#unit-host details.deriv[open]").length, document.querySelectorAll("#unit-host details.deriv").length]);
  ok(m[0] === m[1], `open-all choice is remembered after reload (${m[0]}/${m[1]})`);
  await p.click("#unit-host .deriv-all");
  m = await p.evaluate(() => document.querySelectorAll("#unit-host details.deriv[open]").length);
  ok(m === 0, "the same button closes them all again");

  /* ---------- S5c study loop ---------- */
  await p.evaluate(() => { location.hash = "#u03-quiz-1"; });
  await p.waitForTimeout(400);
  await p.evaluate(() => {
    const q = document.querySelector("#u03-quiz-1 .q");
    const wrong = [...q.querySelectorAll(".opts button")].find(x => x.getAttribute("data-o") !== q.getAttribute("data-correct"));
    wrong.click();
  });
  m = await p.evaluate(() => [...document.querySelectorAll("#u03-quiz-1 .q")[0].querySelectorAll(".fb.shown")].map(f => f.textContent.slice(0, 40)));
  ok(m.some(t => /Tu respuesta/.test(t)) && m.some(t => /Respuesta correcta/.test(t)), "wrong answer shows labelled feedback: " + m.join(" | "));
  await p.evaluate(() => { location.hash = "#u09-e1"; });
  await p.waitForTimeout(400);
  await p.evaluate(() => { const bt = document.querySelector("#u09-e1 .ctrl button.primary"); bt.click(); bt.click(); });
  await reload(p);
  m = await p.evaluate(() => document.querySelectorAll("#u09-e1 .reveal > li.shown").length);
  ok(m === 2, "revealed steps survive reload (" + m + ")");
  await p.evaluate(() => { location.hash = "#u03-quiz-1"; });
  await p.waitForTimeout(400);
  m = await p.evaluate(() => {
    const q = document.querySelectorAll("#u03-quiz-1 .q")[0];
    return { answered: q.classList.contains("answered"), retry: !!q.querySelector(".q-retry") };
  });
  ok(m.answered, "quiz answer survives reload");
  ok(m.retry, "answered question offers a per-question retry");
  if (m.retry) {
    await p.click("#u03-quiz-1 .q .q-retry");
    m = await p.evaluate(() => document.querySelectorAll("#u03-quiz-1 .q")[0].classList.contains("answered"));
    ok(!m, "retry clears only that question");
  }
  m = await p.evaluate(() => { const qz = document.getElementById("u03-quiz-1"); const bar = qz.querySelector(".quiz-bar");
    return bar && qz.querySelector(".q") ? !!(bar.compareDocumentPosition(qz.querySelector(".q")) & Node.DOCUMENT_POSITION_FOLLOWING) : false; });
  ok(m, "quiz score bar sits above the questions");
  await p.evaluate(() => { location.hash = "#s01"; });
  await p.waitForTimeout(400);
  await p.click("#unit-host .sim-start");
  await p.waitForTimeout(1300);
  await p.click("#unit-host .sim-reset");
  m = await p.evaluate(() => ({ t: document.querySelector("#unit-host .sim-time").textContent, txt: document.querySelector("#unit-host .sim-reset").textContent }));
  ok(m.t !== "2:30:00" && /confirm/i.test(m.txt), "first reset click asks for confirmation (" + m.txt + ")");
  await p.click("#unit-host .sim-reset");
  m = await p.evaluate(() => document.querySelector("#unit-host .sim-time").textContent);
  ok(m === "2:30:00", "second click resets the timer");
  await p.evaluate(() => { const c = document.querySelector("#unit-host .score-box input.pts"); c.click(); });
  m = await p.evaluate(() => !!document.querySelector("#unit-host .sim-clear"));
  ok(m, "mock exam offers a clear-pauta button");
  if (m) {
    await p.click("#unit-host .sim-clear");
    await p.click("#unit-host .sim-clear");
    m = await p.evaluate(() => document.querySelectorAll("#unit-host .score-box input.pts:checked").length);
    ok(m === 0, "clear-pauta (confirmed) unchecks every criterion");
  }

  /* ---------- S5d accessibility ---------- */
  await p.evaluate(() => { location.hash = "#u09"; });
  await p.waitForTimeout(500);
  m = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll("#unit-host .eq.key .lbl, #unit-host .exam-map h3, #unit-host .predict b").forEach(el => {
      let bg = el, c = "rgba(0, 0, 0, 0)";
      while (bg && (c = getComputedStyle(bg).backgroundColor) === "rgba(0, 0, 0, 0)") bg = bg.parentElement;
      out.push(__ratio(getComputedStyle(el).color, c));
    });
    return out.length ? Math.min(...out) : 0;
  });
  ok(m >= 4.5, "copper labels contrast >= 4.5:1 (min " + m.toFixed(2) + ")");
  m = await p.evaluate(() => ({ h4: document.querySelectorAll("#unit-host .exam-map h4").length, h3: document.querySelectorAll("#unit-host .exam-map h3").length }));
  ok(m.h4 === 0 && m.h3 === 1, "exam map heading is h3 (no h2 -> h4 skip)");
  m = await p.evaluate(() => {
    const els = [...document.querySelectorAll("#unit-host .lbl, #unit-host .tag, #unit-host .src, #unit-host .goals-t, .toc-block, .toc .up, #unit-host .gl")].filter(e => e.offsetParent);
    return Math.min(...els.map(e => parseFloat(getComputedStyle(e).fontSize)));
  });
  ok(m >= 12, "no label below 12px (min " + m + "px)");
  m = await p.evaluate(() => { const a = parseFloat(getComputedStyle(document.body).fontSize);
    document.documentElement.style.fontSize = "200%"; const z = parseFloat(getComputedStyle(document.body).fontSize);
    document.documentElement.style.fontSize = ""; return [a, z]; });
  ok(m[1] >= m[0] * 1.9, `body text scales with the root font size (${m[0]} -> ${m[1]}px)`);
  await p.click('.toc a.toc-u[data-unit="u10"]');
  await p.waitForTimeout(300);
  m = await p.evaluate(() => { const s = document.getElementById("sr-status"); return s ? s.getAttribute("aria-live") + "|" + s.textContent : ""; });
  ok(/^polite\|.*Inductancia/.test(m), "unit change is announced: " + m);
  await p.close();
  p = await open(ctx, "#r01-nota");
  m = await p.evaluate(() => { const i = document.querySelector("#unit-host .nc-i1"); if (!i) return 0;
    const ph = getComputedStyle(i, "::placeholder").color; let bg = i, c;
    while (bg && (c = getComputedStyle(bg).backgroundColor) === "rgba(0, 0, 0, 0)") bg = bg.parentElement;
    return __ratio(ph, c); });
  ok(m >= 4.5, "placeholder contrast >= 4.5:1 (" + m.toFixed(2) + ")");

  /* ---------- S5e hierarchy ---------- */
  m = await p.evaluate(() => ({ r01: document.querySelectorAll("#unit-host .master").length, prog: document.getElementById("prog-count").textContent }));
  ok(m.r01 === 0, "no dominado button in r01");
  ok(/\/132$/.test(m.prog), "progress counts only the 132 study sections (" + m.prog + ")");
  await p.click('.toc a.toc-u[data-unit="u09"]');
  await p.waitForTimeout(300);
  m = await p.evaluate(() => {
    const secs = [...document.querySelectorAll("#unit-host section.sec")];
    const masters = [...document.querySelectorAll("#unit-host .master")];
    const inline = masters.every(b => b.parentElement.classList.contains("sec-head") && b.parentElement.querySelector("h2"));
    const mapa = document.querySelector('#unit-host section.sec[data-block="mapa"] .master');
    return { secs: secs.length, masters: masters.length, inline, mapa: !!mapa };
  });
  ok(m.masters === m.secs - 1 && !m.mapa, `u09: dominado on study sections only (${m.masters}/${m.secs})`);
  ok(m.inline, "dominado sits on the title line (.sec-head with the h2)");
  m = await p.evaluate(() => [...document.querySelectorAll("#unit-host .key, #unit-host .trap, #unit-host .eq.key, #unit-host .predict")]
    .map(e => parseFloat(getComputedStyle(e).borderLeftWidth)));
  ok(m.length > 0 && Math.max(...m) <= 1, "callouts have no thick left stripe (max " + Math.max(...m) + "px)");
  m = await p.evaluate(() => { const pr = document.querySelector("#unit-host .prob .predict"); const cs = getComputedStyle(pr);
    // Not a frame inside the frame: either unfilled, or a full-bleed band (no side borders, edge to edge).
    const box = pr.getBoundingClientRect(), outer = pr.closest(".prob").getBoundingClientRect();
    const noSides = parseFloat(cs.borderRightWidth) === 0 && parseFloat(cs.borderLeftWidth) === 0;
    const fullBleed = Math.abs(box.left - outer.left) <= 3 && Math.abs(box.right - outer.right) <= 3;
    return noSides && (cs.backgroundColor === "rgba(0, 0, 0, 0)" || fullBleed); });
  ok(m, "prediction inside a problem is not a nested frame (unfilled or full-bleed band)");
  await p.evaluate(() => { location.hash = "#u11-s2"; });
  await p.waitForTimeout(500);
  m = await p.evaluate(() => [...document.querySelectorAll("#unit-host .eq.key")].filter(e => e.scrollWidth > e.clientWidth + 2).length);
  ok(m === 0, "formula cards are not narrowed by the callout width cap (" + m + " clipped)");
  m = await p.evaluate(() => { const toc = document.getElementById("toc").getBoundingClientRect();
    const a = document.querySelector('.toc a.toc-u[data-unit="u11"]').getBoundingClientRect();
    return a.top >= toc.top && a.bottom <= toc.bottom; });
  ok(m, "active unit is scrolled into view in the desktop TOC");
  await p.close();

  ok(errs.length === 0, "no page errors " + errs.slice(0, 3).join(" | "));
  await b.close();
  process.exit(failed ? 1 : 0);
})();
