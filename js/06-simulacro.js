/* ---------- Mock exams: timer and self-scoring with the pauta ----------
   Markup contract (one or more per page):
   <div class="simulacro" id="ID" data-minutes="150" data-total="18">
     <div class="sim-bar">… .sim-time … button.sim-start … button.sim-reset … .sim-pts … .sim-nota</div>
     <div class="score-box" data-group="p1"> … <span class="sb-sub"></span>
       <label><input type="checkbox" class="pts" data-pts="0.5"> criterion</label> …
     </div>
   </div>
   Boxes sharing a data-group (e.g. P1A / P1B, answer only one) count only the best of the group.
*/
(function () {
  "use strict";

  function fmtTime(s) {
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), x = s % 60;
    return h + ":" + (m < 10 ? "0" : "") + m + ":" + (x < 10 ? "0" : "") + x;
  }
  function fmtNum(x) {
    return (Math.round(x * 10) / 10).toString().replace(".", ",");
  }

  /* A destructive button needs a second click within 4 s, but only when there is
     something to lose (needed() is true). */
  function confirmable(btn, confirmText, needed, action) {
    var label = btn.textContent, timer = null;
    function idle() { btn.classList.remove("confirming"); btn.textContent = label; if (timer) { clearTimeout(timer); timer = null; } }
    btn.addEventListener("click", function () {
      if (btn.classList.contains("confirming") || !needed()) { idle(); action(); return; }
      btn.classList.add("confirming");
      btn.textContent = confirmText;
      timer = setTimeout(idle, 4000);
    });
  }

  function setup(root) {
    var key = "fis1533-ex-sim-" + (root.id || "default");
    var total = parseFloat(root.getAttribute("data-total")) || 18;
    var full = (parseFloat(root.getAttribute("data-minutes")) || 150) * 60;
    var tEl = root.querySelector(".sim-time");
    var bStart = root.querySelector(".sim-start");
    var bReset = root.querySelector(".sim-reset");
    var state = { left: full, checks: [] };
    try {
      var saved = JSON.parse(localStorage.getItem(key) || "{}");
      if (typeof saved.left === "number") state.left = saved.left;
      if (Array.isArray(saved.checks)) state.checks = saved.checks;
    } catch (e) { /* ignore corrupt storage */ }
    var timer = null;

    function save() {
      try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) { /* storage full or blocked */ }
    }
    function paintTime() {
      if (!tEl) return;
      tEl.textContent = fmtTime(state.left);
      tEl.classList.toggle("low", state.left <= 600);
    }
    function stop() {
      if (timer) { clearInterval(timer); timer = null; }
      if (bStart) bStart.textContent = state.left <= 0 ? "Tiempo" : state.left < full ? "Reanudar" : "Iniciar";
      save();
    }
    if (bStart) bStart.addEventListener("click", function () {
      if (timer) { stop(); return; }
      if (state.left <= 0) return;
      bStart.textContent = "Pausar";
      timer = setInterval(function () {
        state.left -= 1;
        paintTime();
        if (state.left % 15 === 0) save();
        if (state.left <= 0) stop();
      }, 1000);
    });
    if (bReset) confirmable(bReset, "Confirmar reinicio", function () { return state.left !== full; }, function () {
      stop();
      state.left = full;
      paintTime();
      if (bStart) bStart.textContent = "Iniciar";
      save();
    });

    var boxes = Array.prototype.slice.call(root.querySelectorAll(".score-box input.pts"));
    boxes.forEach(function (b, i) { b.checked = !!state.checks[i]; });

    function paintScore() {
      var groups = {};
      root.querySelectorAll(".score-box").forEach(function (box, bi) {
        var sub = 0, max = 0;
        box.querySelectorAll("input.pts").forEach(function (b) {
          var p = parseFloat(b.getAttribute("data-pts")) || 0;
          max += p;
          if (b.checked) sub += p;
        });
        var out = box.querySelector(".sb-sub");
        if (out) out.textContent = fmtNum(sub) + " / " + fmtNum(max);
        var g = box.getAttribute("data-group") || "box" + bi;
        groups[g] = Math.max(groups[g] || 0, sub);
      });
      var pts = 0;
      Object.keys(groups).forEach(function (g) { pts += groups[g]; });
      var nota = 1 + 6 * pts / total;
      var pEl = root.querySelector(".sim-pts"), nEl = root.querySelector(".sim-nota");
      if (pEl) pEl.textContent = fmtNum(pts) + " / " + fmtNum(total);
      if (nEl) {
        nEl.textContent = "nota " + nota.toFixed(1).replace(".", ",");
        nEl.classList.toggle("ok", nota >= 4);
      }
      state.checks = boxes.map(function (b) { return b.checked ? 1 : 0; });
      save();
    }
    boxes.forEach(function (b) { b.addEventListener("change", paintScore); });
    var btns = bReset && bReset.parentNode;
    if (btns && boxes.length) {
      var bClear = document.createElement("button");
      bClear.type = "button";
      bClear.className = "sim-clear";
      bClear.textContent = "Limpiar pauta";
      btns.appendChild(bClear);
      confirmable(bClear, "Confirmar: borrar pauta", function () { return boxes.some(function (b) { return b.checked; }); }, function () {
        boxes.forEach(function (b) { b.checked = false; });
        paintScore();
      });
    }
    paintTime();
    stop();
    paintScore();
  }

  // The unit stays in memory when hidden, so a running timer keeps counting.
  window.Guide.onMount(function (root, first) {
    if (first) root.querySelectorAll(".simulacro").forEach(setup);
  });
})();
