/* ---------- Simulación de prueba: cronómetro y puntaje ---------- */
(function () {
  "use strict";
  var tEl = document.getElementById("eb-time");
  if (!tEl) return;
  var bStart = document.getElementById("eb-start"), bReset = document.getElementById("eb-reset");
  var TOTAL = 120 * 60, left = TOTAL, timer = null, KEY = "fis1533-i2-sim";
  function fmt(s) { var h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60; return h + ":" + (m < 10 ? "0" : "") + m + ":" + (x < 10 ? "0" : "") + x; }
  function paintT() { tEl.textContent = fmt(left); tEl.classList.toggle("low", left <= 600); }
  function stop() { if (timer) { clearInterval(timer); timer = null; } bStart.textContent = left < TOTAL && left > 0 ? "Reanudar" : "Iniciar"; }
  bStart.addEventListener("click", function () {
    if (timer) { stop(); return; }
    if (left <= 0) return;
    bStart.textContent = "Pausar";
    timer = setInterval(function () { left--; paintT(); if (left <= 0) { stop(); bStart.textContent = "Tiempo"; } }, 1000);
  });
  bReset.addEventListener("click", function () { stop(); left = TOTAL; paintT(); bStart.textContent = "Iniciar"; });
  paintT();

  var boxes = Array.prototype.slice.call(document.querySelectorAll(".score-box input.pts"));
  var saved = [];
  try { saved = JSON.parse(localStorage.getItem(KEY) || "[]"); } catch (e) { saved = []; }
  boxes.forEach(function (b, i) { if (saved[i]) b.checked = true; });
  function paintS() {
    var tot = 0;
    document.querySelectorAll(".score-box").forEach(function (box) {
      var sub = 0, max = 0;
      box.querySelectorAll("input.pts").forEach(function (b) { var p = +b.getAttribute("data-pts"); max += p; if (b.checked) sub += p; });
      box.querySelector(".sb-sub").textContent = sub + "/" + max;
      tot += sub;
    });
    var nota = 1 + 6 * tot / 60;
    document.getElementById("eb-pts").textContent = tot + " / 60";
    var n = document.getElementById("eb-nota");
    n.textContent = "nota " + nota.toFixed(1);
    n.classList.toggle("ok", nota >= 4);
    try { localStorage.setItem(KEY, JSON.stringify(boxes.map(function (b) { return b.checked ? 1 : 0; }))); } catch (e) {}
  }
  boxes.forEach(function (b) { b.addEventListener("change", paintS); });
  paintS();
})();
