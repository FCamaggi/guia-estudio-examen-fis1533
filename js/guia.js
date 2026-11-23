/* Exam guide runtime: per-unit quizzes, per-unit progress, active TOC link.
   Guided problems (.prob) and quick answers (.try) are handled by 01-problemas-guiados.js.
   Units are mounted lazily by 00-guide.js, so progress totals come from the build data
   (Guide.data.units[].sections), not from the buttons currently in the DOM. */
(function () {
  "use strict";
  var KEY = "fis1533-examen-2026-2";
  var store = {
    get: function () { try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { return {}; } },
    set: function (v) { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {} }
  };
  var state = store.get();
  state.done = state.done || {};
  state.quiz = state.quiz || {};

  /* ---------- Quizzes scoped per .quiz block ----------
     Answers persist per quiz (state.quizAns[quizId][questionIndex] = option) and are restored
     on mount. Each answered question offers its own retry; the bar on top resets the quiz. */
  state.quizAns = state.quizAns || {};

  function tag(fb, text) {
    var t = fb.querySelector(".fb-tag");
    if (!t) {
      t = document.createElement("span");
      t.className = "fb-tag";
      fb.insertBefore(t, fb.firstChild);
    }
    t.textContent = text;
  }

  function setupQuiz(quiz) {
    var qid = quiz.id;
    var qs = Array.prototype.slice.call(quiz.querySelectorAll(".q"));
    if (!qs.length) return;
    var saved = (qid && state.quizAns[qid]) || {};
    var score = document.createElement("div");
    score.className = "quiz-score";
    score.setAttribute("aria-live", "polite");
    var reset = document.createElement("button");
    reset.type = "button";
    reset.textContent = "Reiniciar quiz";
    var bar = document.createElement("div");
    bar.className = "quiz-bar";
    bar.appendChild(score);
    bar.appendChild(reset);
    qs[0].parentNode.insertBefore(bar, qs[0]);

    function persist() {
      if (!qid) return;
      state.quizAns[qid] = saved;
      store.set(state);
    }
    function paint() {
      var ok = quiz.querySelectorAll(".q.correct").length;
      var ans = quiz.querySelectorAll(".q.answered").length;
      score.textContent = ok + "/" + qs.length + " correctas" + (ans < qs.length ? " · " + (qs.length - ans) + " sin responder" : "");
      if (ans === qs.length && qid) { state.quiz[qid] = ok + "/" + qs.length; store.set(state); }
    }
    function clear(q) {
      q.classList.remove("answered", "correct");
      q.querySelectorAll(".opts button").forEach(function (b) { b.disabled = false; b.classList.remove("right", "wrong"); });
      q.querySelectorAll(".fb").forEach(function (fb) { fb.classList.remove("shown", "fb-pick", "fb-correct"); });
      var r = q.querySelector(".q-retry");
      if (r) r.remove();
    }
    function answer(q, i, pick) {
      if (q.classList.contains("answered")) return;
      var correct = q.getAttribute("data-correct");
      q.classList.add("answered");
      if (pick === correct) q.classList.add("correct");
      q.querySelectorAll(".opts button").forEach(function (b) {
        var o = b.getAttribute("data-o");
        b.disabled = true;
        if (o === correct) b.classList.add("right");
        else if (o === pick) b.classList.add("wrong");
      });
      q.querySelectorAll(".fb").forEach(function (fb) {
        var o = fb.getAttribute("data-o");
        var isPick = o === pick, isCorrect = o === correct;
        fb.classList.toggle("shown", isPick || isCorrect);
        fb.classList.toggle("fb-pick", isPick && !isCorrect);
        fb.classList.toggle("fb-correct", isCorrect);
        if (isCorrect) tag(fb, pick === correct ? "Correcto" : "Respuesta correcta");
        else if (isPick) tag(fb, "Tu respuesta");
      });
      var retry = document.createElement("button");
      retry.type = "button";
      retry.className = "q-retry";
      retry.textContent = "Reintentar esta pregunta";
      retry.addEventListener("click", function () {
        clear(q);
        delete saved[i];
        persist();
        paint();
        var first = q.querySelector(".opts button");
        if (first) first.focus();
      });
      q.appendChild(retry);
    }

    qs.forEach(function (q, i) {
      q.querySelectorAll(".opts button").forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (q.classList.contains("answered")) return;
          var pick = btn.getAttribute("data-o");
          answer(q, i, pick);
          saved[i] = pick;
          persist();
          paint();
        });
      });
      if (saved[i] != null) answer(q, i, saved[i]);
    });
    reset.addEventListener("click", function () {
      qs.forEach(clear);
      saved = {};
      persist();
      paint();
    });
    paint();
  }

  /* ---------- Progress: one "dominado" toggle per section ---------- */
  function sectionsByUnit() {
    var out = {};
    if (window.Guide.data) {
      window.Guide.data.units.forEach(function (u) { out[u.id] = u.study || []; });
      return out;
    }
    document.querySelectorAll(".master").forEach(function (b) { // preview: only the DOM is available
      var u = b.getAttribute("data-unit");
      (out[u] = out[u] || []).push(b.getAttribute("data-sec"));
    });
    return out;
  }

  function paintProgress() {
    document.querySelectorAll(".master").forEach(function (b) {
      var on = !!state.done[b.getAttribute("data-sec")];
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.textContent = on ? "Dominado" : "Marcar como dominado";
    });
    var units = sectionsByUnit();
    var all = 0, tot = 0;
    Object.keys(units).forEach(function (u) {
      var secs = units[u];
      var n = secs.filter(function (id) { return state.done[id]; }).length;
      all += n; tot += secs.length;
      var el = document.querySelector('.toc [data-unit-progress="' + u + '"]');
      if (el) el.textContent = secs.length ? n + "/" + secs.length : "";
      var link = document.querySelector('.toc a[data-unit="' + u + '"]');
      if (link) link.classList.toggle("done", secs.length > 0 && n === secs.length);
    });
    var c = document.getElementById("prog-count");
    var barEl = document.getElementById("prog-bar");
    if (c) c.textContent = all + "/" + tot;
    var tp = document.getElementById("topbar-prog");
    if (tp) tp.textContent = all + "/" + tot;
    if (barEl) barEl.style.width = (100 * all / Math.max(tot, 1)) + "%";
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".master");
    if (!b) return;
    var id = b.getAttribute("data-sec");
    state.done[id] = !state.done[id];
    store.set(state);
    paintProgress();
  });

  /* ---------- Active TOC link ---------- */
  var io = null;
  function activate(id) {
    document.querySelectorAll(".toc a.active").forEach(function (a) { a.classList.remove("active"); });
    var a = document.querySelector('.toc a[href="#' + id + '"]');
    if (a) a.classList.add("active");
  }
  function observeSections(root) {
    if (!("IntersectionObserver" in window)) return;
    if (!io) {
      io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting && e.target.isConnected) activate(e.target.id); });
      }, { rootMargin: "-20% 0px -70% 0px" });
    }
    root.querySelectorAll("section.sec[id]").forEach(function (s) { io.observe(s); });
    var unit = root.matches("section.unit") ? root : root.querySelector("section.unit");
    if (unit && unit.id) { io.observe(unit); activate(unit.id); }
  }

  /* ---------- TOC section search ----------
     Ctrl+F only reaches the mounted unit, so the TOC filters section titles of every unit.
     Matching ignores case and accents. Enter opens the first result, Escape clears. */
  function norm(t) {
    return t.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/\s+/g, " ").trim();
  }
  function setupSearch() {
    var input = document.getElementById("toc-q");
    var nav = document.getElementById("toc-nav");
    var toc = document.getElementById("toc");
    var empty = document.getElementById("toc-empty");
    if (!input || !nav || !toc) return;
    var units = Array.prototype.slice.call(nav.querySelectorAll(".toc-unit"));
    units.forEach(function (u) {
      u.querySelectorAll("a").forEach(function (a) {
        var label = a.cloneNode(true);
        label.querySelectorAll(".n, .up").forEach(function (x) { x.remove(); });
        a.setAttribute("data-q", norm(label.textContent));
      });
    });

    function filter() {
      var q = norm(input.value);
      toc.classList.toggle("searching", !!q);
      var any = false;
      units.forEach(function (u) {
        var head = u.querySelector("a.toc-u");
        var unitHit = !!q && head.getAttribute("data-q").indexOf(q) >= 0;
        var subHit = false;
        u.querySelectorAll("a.sub").forEach(function (a) {
          var hit = !!q && (unitHit || a.getAttribute("data-q").indexOf(q) >= 0);
          a.classList.toggle("match", hit);
          subHit = subHit || hit;
        });
        var show = !q || unitHit || subHit;
        u.hidden = !show;
        any = any || (q && show);
      });
      nav.querySelectorAll(".toc-block").forEach(function (b) {
        var n = b.nextElementSibling, vis = false;
        while (n && !n.classList.contains("toc-block")) {
          if (!n.hidden) vis = true;
          n = n.nextElementSibling;
        }
        b.hidden = !!q && !vis;
      });
      if (empty) empty.hidden = !q || any;
    }

    input.addEventListener("input", filter);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && input.value) { input.value = ""; filter(); e.preventDefault(); }
      else if (e.key === "Enter") {
        var first = nav.querySelector(".toc-unit:not([hidden]) a.sub.match") || nav.querySelector(".toc-unit:not([hidden]) a.toc-u");
        if (first && input.value.trim()) { e.preventDefault(); first.click(); }
      }
    });
  }
  setupSearch();

  window.Guide.onMount(function (root, first) {
    if (first) {
      root.querySelectorAll(".quiz").forEach(setupQuiz);
      observeSections(root);
    }
    paintProgress();
  });
})();
