(function () {
  "use strict";
  /* ---------- Simulador RC ---------- */
  var mode = "charge";
  var el = function (id) { return document.getElementById(id); };
  var sEps = el("s-eps"), sR = el("s-r"), sC = el("s-c"), sT = el("s-t");
  var canvas = el("sim-canvas"), ctx = canvas.getContext("2d");

  function fmt(x, unit) {
    var a = Math.abs(x);
    var pre = [[1e-9, "n"], [1e-6, "μ"], [1e-3, "m"], [1, ""], [1e3, "k"]];
    var p = pre[3];
    for (var i = pre.length - 1; i >= 0; i--) { if (a >= pre[i][0] * 0.9995) { p = pre[i]; break; } }
    if (a === 0) p = pre[3];
    var v = x / p[0];
    var s = Math.abs(v) >= 100 ? v.toFixed(0) : Math.abs(v) >= 10 ? v.toFixed(1) : v.toFixed(2);
    return s + " " + p[1] + unit;
  }
  function css(name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }

  function update() {
    var eps = +sEps.value, R = +sR.value * 1e3, C = +sC.value * 1e-6, tt = +sT.value;
    var tau = R * C, Q = C * eps, I0 = eps / R, t = tt * tau;
    el("o-eps").textContent = eps + " V";
    el("o-r").textContent = sR.value + " kΩ";
    el("o-c").textContent = sC.value + " μF";
    el("o-t").textContent = tt.toFixed(2) + " τ";
    var ex = Math.exp(-tt);
    var q = mode === "charge" ? Q * (1 - ex) : Q * ex;
    var i = I0 * ex;
    var Vc = q / C, Vr = i * R, U = q * q / (2 * C);
    var items = [
      ["τ = RC", fmt(tau, "s")],
      ["t", fmt(t, "s")],
      ["q(t)", fmt(q, "C") + " (" + (100 * q / Q).toFixed(1) + "%)"],
      ["|I(t)|", fmt(i, "A")],
      ["V_C", fmt(Vc, "V")],
      ["V_R", fmt(Vr, "V")],
      ["U_C", fmt(U, "J")]
    ];
    el("sim-read").innerHTML = items.map(function (it) {
      return '<div><div class="k">' + it[0] + '</div><div class="v">' + it[1] + "</div></div>";
    }).join("");
    draw(tt);
  }

  function draw(tt) {
    var dpr = window.devicePixelRatio || 1;
    var W = canvas.clientWidth || 720, H = Math.round(W * 0.42);
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    canvas.style.height = H + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    var ink = css("--ink"), muted = css("--muted"), line = css("--line"), acc = css("--accent"), cop = css("--copper");
    var L = 44, Rr = 14, T = 16, B = 34;
    var pw = W - L - Rr, ph = H - T - B;
    var X = function (x) { return L + pw * x / 5; }, Y = function (y) { return T + ph * (1 - y); };
    ctx.font = '12px "JetBrains Mono", ui-monospace, monospace';
    ctx.lineWidth = 1; ctx.strokeStyle = line; ctx.fillStyle = muted;
    ctx.textAlign = "right"; ctx.textBaseline = "middle";
    [0, 0.25, 0.5, 0.75, 1].forEach(function (y) {
      ctx.beginPath(); ctx.moveTo(L, Y(y)); ctx.lineTo(W - Rr, Y(y)); ctx.stroke();
      ctx.fillText((y * 100) + "%", L - 6, Y(y));
    });
    ctx.textAlign = "center"; ctx.textBaseline = "top";
    for (var k = 0; k <= 5; k++) {
      ctx.beginPath(); ctx.moveTo(X(k), T); ctx.lineTo(X(k), T + ph); ctx.stroke();
      ctx.fillText(k === 0 ? "0" : k + "τ", X(k), T + ph + 8);
    }
    // 63.2% y 36.8% marcas
    ctx.setLineDash([3, 4]); ctx.strokeStyle = muted;
    [0.632, 0.368].forEach(function (y) { ctx.beginPath(); ctx.moveTo(L, Y(y)); ctx.lineTo(X(1), Y(y)); ctx.stroke(); });
    ctx.setLineDash([]);

    function curve(f, color, width) {
      ctx.strokeStyle = color; ctx.lineWidth = width; ctx.beginPath();
      for (var p = 0; p <= 300; p++) { var x = 5 * p / 300; var yy = f(x); if (p === 0) ctx.moveTo(X(x), Y(yy)); else ctx.lineTo(X(x), Y(yy)); }
      ctx.stroke();
    }
    var fq = mode === "charge" ? function (x) { return 1 - Math.exp(-x); } : function (x) { return Math.exp(-x); };
    var fi = function (x) { return Math.exp(-x); };
    curve(fi, cop, 2.5);
    curve(fq, acc, 2.5);

    // cursor de tiempo
    ctx.strokeStyle = ink; ctx.lineWidth = 1; ctx.setLineDash([2, 3]);
    ctx.beginPath(); ctx.moveTo(X(tt), T); ctx.lineTo(X(tt), T + ph); ctx.stroke(); ctx.setLineDash([]);
    [[fq(tt), acc], [fi(tt), cop]].forEach(function (pt) {
      ctx.fillStyle = pt[1]; ctx.beginPath(); ctx.arc(X(tt), Y(pt[0]), 5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = css("--surface"); ctx.lineWidth = 2; ctx.stroke();
    });

    // leyenda directa
    ctx.textAlign = "right"; ctx.textBaseline = "bottom"; ctx.font = '600 13px "Source Sans 3", system-ui, sans-serif';
    var qy = mode === "charge" ? Y(fq(4.6)) + 18 : Y(fq(0.35)) - 6;
    ctx.fillStyle = acc; ctx.fillText(mode === "charge" ? "q / Q" : "q / Q₀", mode === "charge" ? X(4.95) : X(1.2), qy);
    ctx.fillStyle = cop; ctx.textAlign = "left"; ctx.fillText("|I| / I₀", X(1.6), Y(fi(1.6)) - 6);
    if (mode === "discharge") { ctx.fillStyle = muted; ctx.font = '12px "Source Sans 3", system-ui, sans-serif'; ctx.fillText("(en descarga coinciden)", X(1.6), Y(fi(1.6)) + 16); }
  }

  [sEps, sR, sC, sT].forEach(function (s) { s.addEventListener("input", update); });
  function setMode(m) {
    mode = m;
    el("mode-charge").classList.toggle("on", m === "charge");
    el("mode-discharge").classList.toggle("on", m === "discharge");
    el("mode-charge").setAttribute("aria-pressed", m === "charge");
    el("mode-discharge").setAttribute("aria-pressed", m === "discharge");
    update();
  }
  el("mode-charge").addEventListener("click", function () { setMode("charge"); });
  el("mode-discharge").addEventListener("click", function () { setMode("discharge"); });
  window.addEventListener("resize", update);
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    if (mq.addEventListener) mq.addEventListener("change", update);
  }
  new MutationObserver(update).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(update);
  update();
})();
