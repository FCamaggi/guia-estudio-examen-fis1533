/* Exam guide runtime: per-unit quizzes, per-unit progress, active TOC link.
   Guided problems (.prob) and quick answers (.try) are handled by 01-problemas-guiados.js. */
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

  /* ---------- Quizzes scoped per .quiz block ---------- */
  document.querySelectorAll(".quiz").forEach(function (quiz) {
    var qid = quiz.id;
    var qs = quiz.querySelectorAll(".q");
    var score = document.createElement("div");
    score.className = "quiz-score";
    var reset = document.createElement("button");
    reset.type = "button";
    reset.textContent = "Reiniciar";
    var bar = document.createElement("div");
    bar.className = "quiz-bar";
    bar.appendChild(score);
    bar.appendChild(reset);
    quiz.appendChild(bar);

    function paint() {
      var ok = quiz.querySelectorAll(".q.correct").length;
      var ans = quiz.querySelectorAll(".q.answered").length;
      score.textContent = ok + "/" + qs.length + " correctas" + (ans < qs.length ? " · " + (qs.length - ans) + " sin responder" : "");
      if (ans === qs.length && qid) { state.quiz[qid] = ok + "/" + qs.length; store.set(state); }
    }
    qs.forEach(function (q) {
      var correct = q.getAttribute("data-correct");
      q.querySelectorAll(".opts button").forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (q.classList.contains("answered")) return;
          q.classList.add("answered");
          var pick = btn.getAttribute("data-o");
          q.querySelectorAll(".opts button").forEach(function (b) {
            b.disabled = true;
            if (b.getAttribute("data-o") === correct) b.classList.add("right");
          });
          if (pick === correct) q.classList.add("correct"); else btn.classList.add("wrong");
          q.querySelectorAll(".fb").forEach(function (fb) {
            fb.classList.toggle("shown", fb.getAttribute("data-o") === pick || fb.getAttribute("data-o") === correct);
          });
          paint();
        });
      });
    });
    reset.addEventListener("click", function () {
      qs.forEach(function (q) {
        q.classList.remove("answered", "correct");
        q.querySelectorAll(".opts button").forEach(function (b) { b.disabled = false; b.classList.remove("right", "wrong"); });
        q.querySelectorAll(".fb").forEach(function (fb) { fb.classList.remove("shown"); });
      });
      paint();
    });
    paint();
  });

  /* ---------- Progress: one "dominado" toggle per section ---------- */
  var masters = document.querySelectorAll(".master");
  function paintProgress() {
    var perUnit = {};
    masters.forEach(function (b) {
      var id = b.getAttribute("data-sec");
      var unit = b.getAttribute("data-unit");
      var on = !!state.done[id];
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.textContent = on ? "Dominado" : "Marcar como dominado";
      perUnit[unit] = perUnit[unit] || { n: 0, tot: 0 };
      perUnit[unit].tot++;
      if (on) perUnit[unit].n++;
    });
    var all = 0, tot = 0;
    Object.keys(perUnit).forEach(function (u) {
      all += perUnit[u].n; tot += perUnit[u].tot;
      var el = document.querySelector('.toc [data-unit-progress="' + u + '"]');
      if (el) el.textContent = perUnit[u].n + "/" + perUnit[u].tot;
      var link = document.querySelector('.toc a[data-unit="' + u + '"]');
      if (link) link.classList.toggle("done", perUnit[u].n === perUnit[u].tot);
    });
    var c = document.getElementById("prog-count");
    var barEl = document.getElementById("prog-bar");
    if (c) c.textContent = all + "/" + tot;
    if (barEl) barEl.style.width = (100 * all / Math.max(tot, 1)) + "%";
  }
  masters.forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.getAttribute("data-sec");
      state.done[id] = !state.done[id];
      store.set(state);
      paintProgress();
    });
  });
  paintProgress();

  /* ---------- Active TOC link ---------- */
  var links = {};
  document.querySelectorAll(".toc a[href^='#']").forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && links[e.target.id]) {
          Object.keys(links).forEach(function (k) { links[k].classList.remove("active"); });
          links[e.target.id].classList.add("active");
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    document.querySelectorAll("section.unit, section.sec").forEach(function (s) { if (s.id) io.observe(s); });
  }
})();
