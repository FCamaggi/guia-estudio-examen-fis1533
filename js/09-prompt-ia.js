/* ---------- Ask-an-AI prompt builder ----------
   A floating bubble opens a side panel and turns on "pick mode": clicking a statement, data box,
   figure, solution step or paragraph adds it to the prompt context. One picked block can be
   marked as "the step I did not understand". Picking a step also pulls in its problem statement
   and data, and optionally the steps before it.
   Formulas are exported as their TeX source (from MathJax items, or raw $...$ when not typeset
   yet). Figures are exported as a text description plus an optional PNG on the clipboard.
   Nothing is sent anywhere: the student copies the prompt or opens an LLM chat in a new tab. */
(function () {
  "use strict";

  var PICK = [
    { sel: "figure.fig", kind: "figura" },
    { sel: ".reveal > li", kind: "paso" },
    { sel: ".prob .stmt", kind: "enunciado" },
    { sel: ".prob .given", kind: "datos" },
    { sel: ".predict", kind: "pregunta previa" },
    { sel: ".try", kind: "ejercicio" },
    { sel: ".q", kind: "pregunta de quiz" },
    { sel: "table", kind: "tabla" },
    { sel: ".sec li", kind: "texto" },
    { sel: ".sec p", kind: "texto" }
  ];
  var LLMS = [
    { id: "chatgpt", label: "ChatGPT", url: "https://chatgpt.com/", q: "https://chatgpt.com/?q=" },
    { id: "claude", label: "Claude", url: "https://claude.ai/new", q: "https://claude.ai/new?q=" },
    { id: "gemini", label: "Gemini", url: "https://gemini.google.com/app", q: null }
  ];
  var MAX_URL_PROMPT = 6000;

  var picks = []; // { el, kind, auto }
  var stuck = null; // el marked as "no entendí"
  var picking = false;
  var hoverEl = null;
  var fab, panel, list, empty, note, withPrev, preview, status, bImg, bCopy;

  /* ---------- Text extraction ---------- */
  function texMap(el) {
    var map = new Map();
    var mj = window.MathJax;
    if (!mj || !mj.startup || !mj.startup.document || !mj.startup.document.getMathItemsWithin) return map;
    try {
      mj.startup.document.getMathItemsWithin(el).forEach(function (it) {
        if (it.typesetRoot) map.set(it.typesetRoot, it.display ? "$$" + it.math + "$$" : "$" + it.math + "$");
      });
    } catch (e) { /* MathJax internals unavailable: fall back to visible text */ }
    return map;
  }

  function blockText(el) {
    var map = texMap(el);
    var orig = el.querySelectorAll("mjx-container");
    var clone = el.cloneNode(true);
    var copies = clone.querySelectorAll("mjx-container");
    for (var i = 0; i < copies.length; i++) {
      var tex = map.get(orig[i]);
      var display = orig[i].getAttribute("display") === "true";
      var txt = tex || orig[i].textContent;
      copies[i].replaceWith(document.createTextNode(display ? "\n" + txt + "\n" : txt));
    }
    clone.querySelectorAll("svg, button, .ctrl, .count, script, style, .ai-badge").forEach(function (n) { n.remove(); });
    clone.querySelectorAll("p, div, li, tr, br, h1, h2, h3, h4, h5, figcaption, .rl").forEach(function (n) {
      n.appendChild(document.createTextNode("\n"));
    });
    clone.querySelectorAll("td, th").forEach(function (n) { n.appendChild(document.createTextNode(" | ")); });
    return clone.textContent.replace(/[ \t ]+/g, " ").replace(/ *\n */g, "\n").replace(/\n{3,}/g, "\n\n").trim();
  }

  function figText(fig) {
    var svg = fig.querySelector("svg");
    var label = svg && svg.getAttribute("aria-label");
    var cap = fig.querySelector("figcaption");
    var parts = [];
    if (label) parts.push(label);
    if (cap) parts.push(blockText(cap));
    return parts.join(". ") || "Figura del problema";
  }

  function textOf(p) {
    if (p.kind === "figura") return figText(p.el);
    if (p.kind !== "paso" || !p.el.querySelector(".rl")) return blockText(p.el);
    var body = blockText(p.el);
    var label = stepLabel(p.el);
    return body.indexOf(label) === 0 ? body.slice(label.length).trim() : body; // label is already the heading
  }

  function stepLabel(li) {
    var rl = li.querySelector(".rl");
    if (rl) return blockText(rl);
    if (li.classList.contains("hint")) return "Pista";
    if (li.classList.contains("final")) return "Resultado";
    if (li.classList.contains("check")) return "Verificación";
    return "Paso";
  }

  /* ---------- Picks ---------- */
  function candidate(target) {
    var host = document.getElementById("unit-host") || document.querySelector("main");
    if (!host || !host.contains(target)) return null;
    for (var i = 0; i < PICK.length; i++) {
      var el = target.closest(PICK[i].sel);
      if (el && host.contains(el)) return { el: el, kind: PICK[i].kind };
    }
    return null;
  }

  function indexOf(el) {
    for (var i = 0; i < picks.length; i++) if (picks[i].el === el) return i;
    return -1;
  }

  function add(el, kind, auto) {
    if (indexOf(el) >= 0) return;
    picks.push({ el: el, kind: kind, auto: !!auto });
    el.classList.add("ai-picked");
  }

  function remove(el) {
    var i = indexOf(el);
    if (i < 0) return;
    picks.splice(i, 1);
    el.classList.remove("ai-picked", "ai-stuck");
    if (stuck === el) stuck = null;
  }

  function toggle(c) {
    if (indexOf(c.el) >= 0) { remove(c.el); render(); return; }
    add(c.el, c.kind, false);
    if (c.kind === "paso") {
      var prob = c.el.closest(".prob");
      if (prob) {
        var stmt = prob.querySelector(".stmt");
        var given = prob.querySelector(".given");
        var fig = prob.querySelector("figure.fig");
        if (stmt) add(stmt, "enunciado", true);
        if (given) add(given, "datos", true);
        if (fig) add(fig, "figura", true);
      }
      if (!stuck) setStuck(c.el);
    }
    render();
  }

  function setStuck(el) {
    if (stuck) stuck.classList.remove("ai-stuck");
    stuck = el;
    if (el) el.classList.add("ai-stuck");
  }

  function clearAll() {
    picks.slice().forEach(function (p) { remove(p.el); });
    stuck = null;
    if (note) note.value = "";
    render();
  }

  function docOrder(a, b) {
    return a.el.compareDocumentPosition(b.el) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
  }

  /* ---------- Prompt ---------- */
  function unitTitle() {
    var d = window.Guide && window.Guide.data;
    if (!d || !window.Guide.current) return "";
    for (var i = 0; i < d.units.length; i++) {
      if (d.units[i].id === window.Guide.current) return d.units[i].num + " · " + d.units[i].title;
    }
    return "";
  }

  function previousSteps(li) {
    var out = [];
    var prev = li.previousElementSibling;
    while (prev) {
      if (prev.matches("li") && indexOf(prev) < 0) out.unshift(prev);
      prev = prev.previousElementSibling;
    }
    return out;
  }

  function buildPrompt() {
    var sorted = picks.slice().sort(docOrder);
    var probs = [];
    sorted.forEach(function (p) {
      var prob = p.el.closest(".prob");
      if (prob && probs.indexOf(prob) < 0) probs.push(prob);
    });
    var lines = [];
    var unit = unitTitle();
    lines.push("Estoy estudiando para el examen de Electricidad y Magnetismo (FIS1533, UC)." + (unit ? " Unidad: " + unit + "." : ""));
    probs.forEach(function (prob) {
      var title = prob.querySelector(".prob-head .ptitle");
      var tag = prob.querySelector(".prob-head .tag");
      if (title) lines.push("Problema: " + (tag ? blockText(tag) + " · " : "") + blockText(title) + ".");
    });

    var hasFig = false;
    sorted.forEach(function (p) {
      if (p.el === stuck) return;
      if (p.kind === "figura") {
        hasFig = true;
        lines.push("", "## Figura", "(Te adjunto la figura como imagen.) Descripción: " + figText(p.el));
        return;
      }
      var head = p.kind === "paso" ? stepLabel(p.el) : p.kind.charAt(0).toUpperCase() + p.kind.slice(1);
      if (p.kind === "paso" && stuck && stuck.closest(".reveal") === p.el.closest(".reveal")) head += " (sí lo entiendo)";
      lines.push("", "## " + head, textOf(p));
    });

    if (stuck && withPrev.checked && stuck.matches(".reveal > li")) {
      var prev = previousSteps(stuck);
      if (prev.length) {
        lines.push("", "## Pasos anteriores (los entiendo)");
        prev.forEach(function (li) { lines.push(blockText(li)); });
      }
    }

    if (stuck) {
      var sp = picks[indexOf(stuck)];
      lines.push("", "## Lo que no entiendo: " + (sp.kind === "paso" ? stepLabel(stuck) : sp.kind), textOf(sp));
    }

    var doubt = note.value.trim();
    lines.push("", "## Mi duda", doubt || (stuck ? "No entiendo de dónde sale este paso ni por qué se hace así." : "Explícame este contenido."));
    lines.push(
      "",
      "Actúa como tutor de física universitaria. " +
        (stuck
          ? "Explícame ese paso en concreto: qué principio o ley se aplica, de dónde sale cada término, y qué pasos algebraicos intermedios se omitieron. "
          : "Explícame la idea física y cómo se usa en un problema de examen. ") +
        "Usa la misma notación del material, que está en LaTeX. No resuelvas el resto del problema salvo que te lo pida. " +
        "Termina con una pregunta corta para comprobar que entendí."
    );
    return { text: lines.join("\n"), hasFig: hasFig };
  }

  /* ---------- Clipboard ---------- */
  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).catch(function () { return legacyCopy(text); });
    }
    return legacyCopy(text);
  }

  function legacyCopy(text) {
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
      ta.remove();
      if (ok) resolve(); else reject(new Error("copy blocked"));
    });
  }

  var STYLE_PROPS = ["fill", "fill-opacity", "stroke", "stroke-width", "stroke-opacity", "stroke-dasharray",
    "stroke-linecap", "stroke-linejoin", "opacity", "font-family", "font-size", "font-weight", "font-style",
    "text-anchor", "dominant-baseline", "visibility", "display"];

  function figurePng(fig) {
    var svg = fig.querySelector("svg");
    if (!svg) return Promise.reject(new Error("no svg"));
    var clone = svg.cloneNode(true);
    var src = [svg].concat(Array.prototype.slice.call(svg.querySelectorAll("*")));
    var dst = [clone].concat(Array.prototype.slice.call(clone.querySelectorAll("*")));
    src.forEach(function (node, i) {
      var cs = getComputedStyle(node);
      var css = STYLE_PROPS.map(function (p) { return p + ":" + cs.getPropertyValue(p); }).join(";");
      dst[i].setAttribute("style", css);
    });
    var vb = svg.viewBox && svg.viewBox.baseVal;
    var w = vb && vb.width ? vb.width : svg.getBoundingClientRect().width;
    var h = vb && vb.height ? vb.height : svg.getBoundingClientRect().height;
    var scale = 2;
    clone.setAttribute("width", w);
    clone.setAttribute("height", h);
    var bg = getComputedStyle(fig).backgroundColor || "#ffffff";
    var data = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(new XMLSerializer().serializeToString(clone));
    return new Promise(function (resolve, reject) {
      var img = new Image();
      img.onload = function () {
        var pad = 16;
        var c = document.createElement("canvas");
        c.width = Math.round((w + 2 * pad) * scale);
        c.height = Math.round((h + 2 * pad) * scale);
        var ctx = c.getContext("2d");
        ctx.fillStyle = bg;
        ctx.fillRect(0, 0, c.width, c.height);
        ctx.drawImage(img, pad * scale, pad * scale, w * scale, h * scale);
        c.toBlob(function (blob) { if (blob) resolve(blob); else reject(new Error("toBlob failed")); }, "image/png");
      };
      img.onerror = function () { reject(new Error("svg load failed")); };
      img.src = data;
    });
  }

  function copyImage() {
    var fig = null;
    picks.slice().sort(docOrder).some(function (p) { if (p.kind === "figura") { fig = p.el; return true; } return false; });
    if (!fig) return Promise.reject(new Error("no figure"));
    var blob = figurePng(fig);
    if (navigator.clipboard && window.ClipboardItem && window.isSecureContext) {
      return navigator.clipboard.write([new window.ClipboardItem({ "image/png": blob })])
        .then(function () { return "copied"; })
        .catch(function () { return blob.then(download); });
    }
    return blob.then(download);
  }

  function download(blob) {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = (window.Guide && window.Guide.current ? window.Guide.current + "-" : "") + "figura.png";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
    return "downloaded";
  }

  function say(msg) { status.textContent = msg; }

  /* ---------- UI ---------- */
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text) n.textContent = text;
    return n;
  }

  function build() {
    fab = el("button", "ai-fab");
    fab.type = "button";
    fab.setAttribute("aria-expanded", "false");
    fab.setAttribute("aria-controls", "ai-panel");
    fab.innerHTML = '<span class="ai-fab-icon" aria-hidden="true">IA</span><span class="ai-fab-txt">Preguntar a una IA</span>';
    fab.addEventListener("click", function () { open(!picking); });

    panel = el("aside", "ai-panel");
    panel.id = "ai-panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", "Constructor de prompt para preguntar a una IA");
    panel.hidden = true;

    var head = el("div", "ai-head");
    head.appendChild(el("strong", null, "Preguntar a una IA"));
    var bClose = el("button", "ai-x", "×");
    bClose.type = "button";
    bClose.setAttribute("aria-label", "Cerrar");
    bClose.addEventListener("click", function () { open(false); });
    head.appendChild(bClose);
    panel.appendChild(head);

    panel.appendChild(el("p", "ai-hint", "Haz clic en la guía para elegir el contexto: enunciado, figura, datos o el paso que no entendiste. Al elegir un paso se agregan su enunciado, datos y figura."));

    list = el("ol", "ai-list");
    panel.appendChild(list);
    empty = el("p", "ai-empty", "Todavía no elegiste nada.");
    panel.appendChild(empty);

    var lp = el("label", "ai-check");
    withPrev = el("input");
    withPrev.type = "checkbox";
    withPrev.checked = true;
    withPrev.addEventListener("change", refresh);
    lp.appendChild(withPrev);
    lp.appendChild(document.createTextNode(" Incluir los pasos anteriores al paso marcado"));
    panel.appendChild(lp);

    var ln = el("label", "ai-label", "¿Qué no entiendes? (opcional)");
    ln.setAttribute("for", "ai-note");
    panel.appendChild(ln);
    note = el("textarea", "ai-note");
    note.id = "ai-note";
    note.rows = 2;
    note.placeholder = "Ej.: ¿por qué el signo cambia al pasar al otro lado?";
    note.addEventListener("input", refresh);
    panel.appendChild(note);

    var det = el("details", "ai-preview");
    det.appendChild(el("summary", null, "Ver prompt"));
    preview = el("pre");
    det.appendChild(preview);
    panel.appendChild(det);

    var acts = el("div", "ai-acts");
    bCopy = el("button", "primary", "Copiar prompt");
    bCopy.type = "button";
    bCopy.addEventListener("click", function () {
      copyText(buildPrompt().text).then(function () { say("Prompt copiado. Pégalo en tu chat."); }, function () { say("No se pudo copiar. Ábrelo en \"Ver prompt\" y cópialo a mano."); });
    });
    bImg = el("button", null, "Copiar imagen");
    bImg.type = "button";
    bImg.addEventListener("click", function () {
      say("Preparando la imagen…");
      copyImage().then(function (how) {
        say(how === "copied" ? "Imagen copiada. Pégala en el chat con Ctrl+V." : "Imagen descargada. Adjúntala en el chat.");
      }, function () { say("No se pudo generar la imagen."); });
    });
    var bClear = el("button", null, "Limpiar");
    bClear.type = "button";
    bClear.addEventListener("click", clearAll);
    acts.appendChild(bCopy);
    acts.appendChild(bImg);
    acts.appendChild(bClear);
    panel.appendChild(acts);

    var go = el("div", "ai-go");
    go.appendChild(el("span", "ai-go-l", "Abrir en"));
    LLMS.forEach(function (m) {
      var b = el("button", null, m.label);
      b.type = "button";
      b.addEventListener("click", function () { openLlm(m); });
      go.appendChild(b);
    });
    panel.appendChild(go);

    status = el("p", "ai-status");
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");
    panel.appendChild(status);

    document.body.appendChild(fab);
    document.body.appendChild(panel);
  }

  function openLlm(m) {
    var p = buildPrompt();
    var viaUrl = m.q && !p.hasFig && p.text.length <= MAX_URL_PROMPT;
    // Copy before opening the tab: clipboard writes need this document to keep focus.
    copyText(p.text).then(function () {
      say(viaUrl
        ? "Abrí " + m.label + " con el prompt (también quedó copiado)."
        : "Prompt copiado. Pégalo en " + m.label + (p.hasFig ? " y luego usa \"Copiar imagen\" para adjuntar la figura." : "."));
    }, function () { say("Abrí " + m.label + ". Copia el prompt desde \"Ver prompt\"."); });
    window.open(viaUrl ? m.q + encodeURIComponent(p.text) : m.url, "_blank", "noopener");
  }

  function render() {
    list.innerHTML = "";
    var sorted = picks.slice().sort(docOrder);
    sorted.forEach(function (p) {
      var li = el("li", "ai-item" + (p.el === stuck ? " is-stuck" : ""));
      var top = el("div", "ai-item-top");
      var kind = el("span", "ai-kind", p.kind === "paso" ? stepLabel(p.el) : p.kind);
      top.appendChild(kind);
      if (p.auto) top.appendChild(el("span", "ai-auto", "auto"));
      var x = el("button", "ai-rm", "×");
      x.type = "button";
      x.setAttribute("aria-label", "Quitar " + p.kind);
      x.addEventListener("click", function () { remove(p.el); render(); });
      top.appendChild(x);
      li.appendChild(top);
      var t = textOf(p);
      li.appendChild(el("p", "ai-snip", t.length > 140 ? t.slice(0, 140) + "…" : t));
      if (p.kind !== "figura") {
        var lab = el("label", "ai-stuck-l");
        var r = el("input");
        r.type = "radio";
        r.name = "ai-stuck";
        r.checked = p.el === stuck;
        r.addEventListener("change", function () { setStuck(p.el); render(); });
        lab.appendChild(r);
        lab.appendChild(document.createTextNode(" No entendí esto"));
        li.appendChild(lab);
      }
      list.appendChild(li);
    });
    empty.hidden = picks.length > 0;
    var hasFig = picks.some(function (p) { return p.kind === "figura"; });
    bImg.hidden = !hasFig;
    withPrev.parentNode.hidden = !(stuck && stuck.matches(".reveal > li") && stuck.previousElementSibling);
    fab.classList.toggle("has-picks", picks.length > 0);
    fab.setAttribute("data-count", picks.length || "");
    refresh();
  }

  function refresh() { preview.textContent = picks.length ? buildPrompt().text : ""; }

  function open(on) {
    picking = on;
    panel.hidden = !on;
    fab.setAttribute("aria-expanded", on ? "true" : "false");
    document.documentElement.classList.toggle("ai-picking", on);
    if (!on && hoverEl) { hoverEl.classList.remove("ai-hover"); hoverEl = null; }
    if (on) { render(); say(""); }
  }

  /* ---------- Pick mode events ---------- */
  function isUi(t) { return t.closest(".ai-panel, .ai-fab, button, a, input, select, textarea, label, summary, .ctrl"); }

  document.addEventListener("mouseover", function (e) {
    if (!picking) return;
    var c = isUi(e.target) ? null : candidate(e.target);
    var next = c ? c.el : null;
    if (next === hoverEl) return;
    if (hoverEl) hoverEl.classList.remove("ai-hover");
    hoverEl = next;
    if (hoverEl) hoverEl.classList.add("ai-hover");
  });

  document.addEventListener("click", function (e) {
    if (!picking || isUi(e.target)) return;
    var c = candidate(e.target);
    if (!c) return;
    e.preventDefault();
    e.stopPropagation();
    toggle(c);
  }, true);

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && picking) open(false);
  });

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build);
  else build();
})();
