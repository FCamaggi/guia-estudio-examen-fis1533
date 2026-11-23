/* ---------- Required final-exam grade (I1 30 %, I2 30 %, exam 40 %) ---------- */
(function () {
  "use strict";
  var W_I1 = 0.3, W_I2 = 0.3, W_EX = 0.4;

  function parseGrade(text) {
    var v = parseFloat(String(text).trim().replace(",", "."));
    return isFinite(v) ? v : NaN;
  }
  function fmt(x, digits) {
    return x.toFixed(digits).replace(".", ",");
  }
  function inRange(g) {
    return g >= 1 && g <= 7;
  }

  function setup(root) {
    var i1 = root.querySelector(".nc-i1"), i2 = root.querySelector(".nc-i2");
    var meta = root.querySelector(".nc-meta"), out = root.querySelector(".nc-out");
    if (!i1 || !i2 || !meta || !out) return;

    function update() {
      var a = parseGrade(i1.value), b = parseGrade(i2.value), m = parseGrade(meta.value);
      out.classList.remove("ok", "bad");
      if (isNaN(a) || isNaN(b)) { out.textContent = "Ingresa tus notas de la I1 y la I2."; return; }
      if (!inRange(a) || !inRange(b) || isNaN(m) || !inRange(m)) {
        out.textContent = "Las notas deben estar entre 1,0 y 7,0.";
        out.classList.add("bad");
        return;
      }
      var need = (m - W_I1 * a - W_I2 * b) / W_EX;
      if (need <= 1) {
        out.textContent = "Ya tienes asegurado un " + fmt(m, 1) + ": incluso con un 1,0 en el examen tu nota final sería " +
          fmt(W_I1 * a + W_I2 * b + W_EX, 2) + ".";
        out.classList.add("ok");
      } else if (need > 7) {
        out.textContent = "No alcanza: aun con un 7,0 en el examen tu nota final sería " +
          fmt(W_I1 * a + W_I2 * b + W_EX * 7, 2) + ".";
        out.classList.add("bad");
      } else {
        out.textContent = "Necesitas al menos un " + fmt(need, 2) + " en el examen para llegar a " + fmt(m, 1) + ".";
      }
    }
    [i1, i2, meta].forEach(function (el) { el.addEventListener("input", update); });
    update();
  }

  window.Guide.onMount(function (root, first) {
    if (first) root.querySelectorAll(".nota-calc").forEach(setup);
  });
})();
