/* ---------- Guide shell: mounts one unit at a time ----------
   The build emits every unit inside <template id="tpl-UNIT"> plus a JSON block (#guide-data)
   with the unit order, section ids and an id -> unit map. This module:
   - mounts only the open unit into #unit-host and keeps mounted units in memory, so timers,
     quizzes and revealed steps survive switching units;
   - typesets formulas lazily, one block at a time, as it approaches the viewport;
   - routes hashes: #UNIT opens a unit at the top, any other id opens its unit and scrolls to it;
   - restores the reading position on reload and back/forward;
   - appends previous/next links at the end of each unit.
   Other modules register with Guide.onMount(fn); fn(root, first) runs every time a unit is shown,
   with first === true only the first time that unit is mounted.
   Without #guide-data (single-fragment preview) hooks run once on <main>. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  var hooks = [];
  var Guide = (window.Guide = {
    data: null,
    current: null,
    onMount: function (fn) { hooks.push(fn); },
    unitOf: function (id) { return Guide.data && Guide.data.ids[id]; }
  });

  /* ---------- Lazy MathJax ---------- */
  var mathIO = null;
  var mathChain = new Promise(function (resolve) {
    var tries = 0;
    (function poll() {
      var mj = window.MathJax;
      if (mj && mj.typesetPromise && mj.startup && mj.startup.promise) { mj.startup.promise.then(resolve); return; }
      if (++tries < 600) setTimeout(poll, 100); // offline: give up after ~60 s, formulas stay as TeX
    })();
  });

  function typeset(els) {
    els = els.filter(function (el) {
      if (el.hasAttribute("data-typeset")) return false;
      el.setAttribute("data-typeset", "");
      return true;
    });
    if (!els.length) return Promise.resolve();
    mathChain = mathChain.then(function () {
      // A unit may have been switched out while queued; typeset it again when it comes back.
      var live = els.filter(function (el) {
        if (el.isConnected) return true;
        el.removeAttribute("data-typeset");
        return false;
      });
      return live.length ? window.MathJax.typesetPromise(live).then(function () { live.forEach(markPunctuation); }) : null;
    }).then(function () { applyPin(); }).catch(function (e) { console.error("MathJax", e); });
    return mathChain;
  }

  /* Readability: punctuation glued to an inline formula reads as part of it, and sentence
     breaks get lost in formula-dense prose. After typesetting, wrap that punctuation in
     <span class="pn"> so CSS can separate it (.pn-math) and widen sentence gaps (.pn-gap).
     Runs only after MathJax, because splitting text nodes earlier would break $...$ delimiters. */
  var SKIP = /^(MJX-CONTAINER|CODE|PRE|SCRIPT|STYLE|SVG|TEXTAREA|INPUT|BUTTON|SELECT)$/;
  function markPunctuation(block) {
    if (!block.isConnected) return;
    var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        for (var p = n.parentNode; p && p !== block; p = p.parentNode) {
          if (SKIP.test(p.nodeName.toUpperCase()) || (p.classList && p.classList.contains("pn"))) return NodeFilter.FILTER_REJECT;
        }
        return /[.,;:]/.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      var text = node.nodeValue;
      var prev = node.previousSibling;
      var afterMath = prev && prev.nodeName.toUpperCase() === "MJX-CONTAINER" && prev.getAttribute("display") !== "true";
      var cuts = [];
      if (afterMath && /^[.,;:]/.test(text)) cuts.push({ i: 0, math: true, gap: /^[.;:](\s|$)/.test(text) });
      // Sentence gaps: ". X" (capital next, so "Ej. 3" stays tight), and every "; " or ": ".
      var re = /([.;:])(\s+)(\S)/g, m;
      while ((m = re.exec(text))) {
        if (m[1] === "." && !/[A-ZÁÉÍÓÚÑ¿¡(]/.test(m[3])) continue;
        if (cuts.length && cuts[0].i === m.index) continue;
        cuts.push({ i: m.index, math: false, gap: true });
      }
      if (!cuts.length) return;
      var frag = document.createDocumentFragment(), last = 0;
      cuts.forEach(function (c) {
        if (c.i > last) frag.appendChild(document.createTextNode(text.slice(last, c.i)));
        var s = document.createElement("span");
        s.className = "pn" + (c.math ? " pn-math" : "") + (c.gap ? " pn-gap" : "");
        s.textContent = text.charAt(c.i);
        frag.appendChild(s);
        last = c.i + 1;
      });
      if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
      node.parentNode.replaceChild(frag, node);
    });
  }

  function mathBlocks(root) {
    // Direct children of the unit are the natural chunks (header, exam map, sections).
    var unit = root.matches && root.matches("section.unit") ? root : root.querySelector("section.unit");
    var kids = unit ? unit.children : root.children;
    return Array.prototype.slice.call(kids);
  }

  function observeMath(root) {
    var blocks = mathBlocks(root);
    if (!("IntersectionObserver" in window)) { typeset(blocks); return; }
    if (!mathIO) {
      mathIO = new IntersectionObserver(function (entries) {
        var hit = entries.filter(function (e) { return e.isIntersecting; }).map(function (e) { return e.target; });
        hit.forEach(function (el) { mathIO.unobserve(el); });
        typeset(hit);
      }, { rootMargin: "1200px 0px 1200px 0px" });
    }
    blocks.forEach(function (el) { if (!el.hasAttribute("data-typeset")) mathIO.observe(el); });
  }

  function typesetAround(el) {
    // Typeset the block holding el (and its neighbours) before scrolling to it.
    var block = el;
    while (block && block.parentElement && !(block.parentElement.matches("section.unit") || block.parentElement.id === "unit-host")) {
      block = block.parentElement;
    }
    var list = [block, block && block.previousElementSibling, block && block.nextElementSibling].filter(Boolean);
    return typeset(list);
  }

  /* While formulas above a jump target are being typeset, the content shifts. A short-lived
     pin keeps the target at the same viewport offset until math settles or the user scrolls. */
  var pin = null;
  function scrollToY(y) { window.scrollTo({ top: Math.max(0, Math.round(y)), behavior: "instant" }); }
  function applyPin() {
    if (!pin) return;
    if (!pin.el.isConnected || Date.now() > pin.until) { pin = null; return; }
    scrollToY(pin.el.getBoundingClientRect().top + window.scrollY - pin.margin + pin.off);
  }
  function pinTo(el, off) {
    var margin = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
    pin = { el: el, off: off || 0, margin: off ? 0 : margin, until: Date.now() + 4000 };
    applyPin();
    typesetAround(el).then(applyPin);
  }
  ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (t) {
    window.addEventListener(t, function () { pin = null; }, { passive: true });
  });

  function runHooks(root, first) {
    hooks.forEach(function (fn) {
      try { fn(root, first); } catch (e) { console.error(e); }
    });
  }

  /* ---------- Preview mode (single fragment, no templates) ---------- */
  function bootPreview() {
    var main = document.querySelector("main") || document.body;
    runHooks(main, true);
    observeMath(main);
  }

  /* ---------- Units ---------- */
  var host, cache = {};

  function pager(uid) {
    var list = Guide.data.units;
    var i = list.findIndex(function (u) { return u.id === uid; });
    var nav = document.createElement("nav");
    nav.className = "unit-pager";
    nav.setAttribute("aria-label", "Navegación entre unidades");
    [[list[i - 1], "prev", "Anterior"], [list[i + 1], "next", "Siguiente"]].forEach(function (p) {
      var u = p[0];
      if (!u) { nav.appendChild(document.createElement("span")); return; }
      var a = document.createElement("a");
      a.className = "pager-" + p[1];
      a.href = "#" + u.id;
      a.innerHTML = '<span class="pager-dir"></span><span class="pager-title"></span>';
      a.firstChild.textContent = p[2] + " · " + u.num;
      a.lastChild.textContent = u.title;
      nav.appendChild(a);
    });
    return nav;
  }

  function mount(uid) {
    if (Guide.current === uid) return cache[uid];
    var first = !cache[uid];
    if (first) {
      var tpl = document.getElementById("tpl-" + uid);
      if (!tpl) return null;
      var frag = document.importNode(tpl.content, true);
      var node = frag.querySelector("section.unit");
      if (!node) return null;
      node.appendChild(pager(uid));
      cache[uid] = node;
    }
    if (Guide.current && cache[Guide.current] && cache[Guide.current].parentNode) {
      cache[Guide.current].parentNode.removeChild(cache[Guide.current]);
    }
    host.appendChild(cache[uid]);
    Guide.current = uid;
    document.querySelectorAll(".toc-unit").forEach(function (t) {
      t.classList.toggle("open", t.getAttribute("data-unit") === uid);
    });
    var u = Guide.data.units.find(function (x) { return x.id === uid; });
    if (u) document.title = u.num + " · " + u.title + " — Guía de estudio FIS1533";
    syncShell(u, cache[uid], first);
    runHooks(cache[uid], first);
    observeMath(cache[uid]);
    document.dispatchEvent(new CustomEvent("guide:unit", { detail: { unit: uid, root: cache[uid], first: first } }));
    return cache[uid];
  }

  /* ---------- Shell: top bar, announcements, TOC position, derivations ---------- */
  var booted = false;
  var DERIV_KEY = "fis1533-deriv-open";

  function syncShell(u, root, first) {
    if (!u) return;
    var label = u.num + " · " + u.title;
    var top = document.getElementById("topbar-unit");
    if (top) top.textContent = label;
    var sr = document.getElementById("sr-status");
    if (sr && booted) sr.textContent = "Unidad " + label;
    revealTocUnit(u.id);
    setupDerivations(root, first);
  }

  function revealTocUnit(uid) {
    var toc = document.getElementById("toc");
    var item = toc && toc.querySelector('.toc-unit[data-unit="' + uid + '"]');
    if (!item) return;
    var head = toc.querySelector(".toc-head");
    var off = (head ? head.offsetHeight : 0) + 12; // the sticky header covers the top of the list
    var tr = toc.getBoundingClientRect(), r = item.getBoundingClientRect();
    if (r.top < tr.top + off || r.top > tr.bottom - 120) toc.scrollTop += r.top - tr.top - off;
  }

  // Derivations are closed by default; one button per unit opens or closes them all and the
  // choice is remembered across units and visits.
  function derivPref() { try { return localStorage.getItem(DERIV_KEY) === "1"; } catch (e) { return false; } }
  function setupDerivations(root, first) {
    var list = root.querySelectorAll("details.deriv");
    if (!list.length) return;
    var btn = root.querySelector(".deriv-all");
    if (first && !btn) {
      btn = document.createElement("button");
      btn.type = "button";
      btn.className = "deriv-all";
      btn.addEventListener("click", function () {
        var open = btn.getAttribute("aria-pressed") !== "true";
        try { localStorage.setItem(DERIV_KEY, open ? "1" : "0"); } catch (e) { /* storage blocked */ }
        apply(root, open);
      });
      var head = root.querySelector(".unit-head") || root;
      head.appendChild(btn);
    }
    apply(root, derivPref());
  }
  function apply(root, open) {
    root.querySelectorAll("details.deriv").forEach(function (d) { d.open = open; });
    var btn = root.querySelector(".deriv-all");
    if (!btn) return;
    btn.setAttribute("aria-pressed", open ? "true" : "false");
    btn.textContent = open ? "Cerrar todas las derivaciones" : "Abrir todas las derivaciones";
  }

  /* ---------- Mobile index panel ---------- */
  function setupDrawer() {
    var btn = document.querySelector(".toc-toggle");
    var toc = document.getElementById("toc");
    var scrim = document.querySelector(".toc-scrim");
    if (!btn || !toc) return;
    var main = document.querySelector("main");
    function isOpen() { return document.body.classList.contains("toc-open"); }
    function set(open, focusBack) {
      document.body.classList.toggle("toc-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      if (scrim) scrim.hidden = !open;
      if (main) main.inert = open;
      if (open) {
        var cur = toc.querySelector(".toc-unit.open a.toc-u") || toc.querySelector("a");
        if (cur) setTimeout(function () { cur.focus({ preventScroll: true }); }, 30);
        if (Guide.current) revealTocUnit(Guide.current);
      } else if (focusBack) {
        btn.focus();
      }
    }
    btn.addEventListener("click", function () { set(!isOpen(), true); });
    if (scrim) scrim.addEventListener("click", function () { set(false, true); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && isOpen() && !e.defaultPrevented) set(false, true);
    });
    toc.addEventListener("click", function (e) {
      if (isOpen() && e.target.closest && e.target.closest('a[href^="#"]')) set(false, false);
    });
    var mq = window.matchMedia && window.matchMedia("(max-width: 900px)");
    if (mq && mq.addEventListener) mq.addEventListener("change", function () { if (!mq.matches) set(false, false); });
  }

  /* ---------- Reading position ---------- */
  function readingAnchor() {
    var root = cache[Guide.current];
    if (!root) return null;
    var secs = root.querySelectorAll("section.sec[id]");
    var best = null;
    for (var i = 0; i < secs.length; i++) {
      if (secs[i].getBoundingClientRect().top <= 80) best = secs[i]; else break;
    }
    if (!best) return { unit: Guide.current, y: window.scrollY };
    return { unit: Guide.current, sec: best.id, off: Math.round(-best.getBoundingClientRect().top) };
  }

  var saveTimer = null;
  function savePosition() {
    var a = readingAnchor();
    if (!a) return;
    try { history.replaceState(a, "", location.href); } catch (e) { /* ignore */ }
  }
  window.addEventListener("scroll", function () {
    if (saveTimer) clearTimeout(saveTimer);
    saveTimer = setTimeout(savePosition, 200);
  }, { passive: true });
  window.addEventListener("pagehide", savePosition);

  function restore(pos) {
    var root = mount(pos.unit);
    if (!root) return false;
    var el = pos.sec && document.getElementById(pos.sec);
    if (!el) { pin = null; scrollToY(pos.y || 0); return true; }
    pinTo(el, pos.off || 0.001); // non-zero offset: restore the exact saved position, no scroll padding
    return true;
  }

  /* ---------- Routing ---------- */
  function resolve(id) {
    var units = Guide.data.units;
    if (!id) return { unit: units[0].id, target: null };
    if (units.some(function (u) { return u.id === id; })) return { unit: id, target: null };
    var uid = Guide.data.ids[id];
    return uid ? { unit: uid, target: id } : null;
  }

  function go(id) {
    var r = resolve(id);
    if (!r) return false;
    var changed = Guide.current !== r.unit;
    mount(r.unit);
    if (!r.target) {
      pin = null;
      scrollToY(0);
      if (changed && host) host.focus({ preventScroll: true });
      return true;
    }
    var el = document.getElementById(r.target);
    if (!el) return false;
    var details = el.closest("details:not([open])");
    if (details) details.open = true;
    pinTo(el, 0);
    return true;
  }

  function idFromHash() {
    try { return decodeURIComponent(location.hash.slice(1)); } catch (e) { return location.hash.slice(1); }
  }

  var popHash = null;
  function onPop(e) {
    popHash = location.hash;
    if (e.state && e.state.unit && restore(e.state)) return;
    go(idFromHash());
  }

  function onHashChange() {
    if (popHash === location.hash) { popHash = null; return; } // already handled by popstate
    popHash = null;
    go(idFromHash());
  }

  function onClick(e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute("href").slice(1);
    if (!resolve(id) || !id) return;
    e.preventDefault();
    savePosition();
    history.pushState(null, "", "#" + id);
    go(id);
  }

  function boot() {
    var raw = document.getElementById("guide-data");
    host = document.getElementById("unit-host");
    if (!raw || !host) { bootPreview(); return; }
    Guide.data = JSON.parse(raw.textContent);
    if (!Guide.data.units.length) return;
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";
    var st = history.state;
    if (!(st && st.unit && restore(st))) {
      if (!go(idFromHash())) go("");
    }
    window.addEventListener("popstate", onPop);
    window.addEventListener("hashchange", onHashChange);
    document.addEventListener("click", onClick);
    setupDrawer();
    booted = true;
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else setTimeout(boot, 0);
})();
