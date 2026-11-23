/* Guided problems (.prob step reveal) and quick answers (.try). Runs once per mounted unit.
   Revealed steps persist per problem in localStorage, so a reload keeps your place. */
(function () {
  "use strict";
  var KEY = "fis1533-examen-steps";
  var steps = {};
  try { steps = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { steps = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(steps)); } catch (e) { /* storage blocked */ } }
  window.Guide.onMount(function (root, first) {
    if (first) init(root);
  });

  function init(root) {
    var unitId = root.id || (root.querySelector("section.unit") || {}).id || "u";
    root.querySelectorAll(".prob").forEach(function (p, idx) {
      var items = Array.prototype.slice.call(p.querySelectorAll(".reveal > li"));
      var ctrl = p.querySelector(".ctrl");
      if (!ctrl || !items.length) return;
      var pid = p.id || unitId + "-p" + idx;
      var k = Math.min(items.length, steps[pid] || 0);
      function remember() {
        if (k) steps[pid] = k; else delete steps[pid];
        save();
      }
      var bNext = document.createElement("button"); bNext.type = "button"; bNext.className = "primary";
      var bAll = document.createElement("button"); bAll.type = "button"; bAll.textContent = "Ver solución completa";
      var bHide = document.createElement("button"); bHide.type = "button"; bHide.textContent = "Ocultar todo";
      var cnt = document.createElement("span"); cnt.className = "count";
      ctrl.appendChild(bNext); ctrl.appendChild(bAll); ctrl.appendChild(bHide); ctrl.appendChild(cnt);
      function paint() {
        items.forEach(function (li, i) { li.classList.toggle("shown", i < k); });
        var nxt = items[k];
        if (!nxt) { bNext.style.display = "none"; }
        else {
          bNext.style.display = "";
          bNext.textContent = nxt.classList.contains("hint") ? "Ver pista" : (nxt.classList.contains("final") ? "Ver resultado" : (nxt.classList.contains("check") ? "Ver chequeo" : (k === 0 || (k === 1 && items[0].classList.contains("hint")) ? "Ver primer paso" : "Siguiente paso")));
        }
        bAll.style.display = k >= items.length ? "none" : "";
        bHide.style.display = k === 0 ? "none" : "";
        cnt.textContent = k + "/" + items.length + " visibles";
      }
      bNext.addEventListener("click", function () { k = Math.min(items.length, k + 1); paint(); remember(); });
      bAll.addEventListener("click", function () { k = items.length; paint(); remember(); });
      bHide.addEventListener("click", function () { k = 0; paint(); remember(); });
      paint();
    });
    root.querySelectorAll(".try").forEach(function (t) {
      var b = t.querySelector(".b-try");
      if (!b) return;
      b.addEventListener("click", function () {
        var open = t.classList.toggle("open");
        b.textContent = open ? "Ocultar respuesta" : "Ver respuesta";
      });
    });
  }
})();
