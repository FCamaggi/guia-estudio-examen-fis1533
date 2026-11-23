/* Interactive RL, RLC and AC phasor simulators (unit t01).
   Initialised the first time t01 is mounted; redrawn every time it is shown again
   (canvas sizes are only measurable while attached). */
(function () {
  "use strict";
  var redraws = [];

  window.Guide.onMount(function (root, first) {
    if (first) {
      if (!root.querySelector("#t01-rl-canvas")) return;
      var r = init(root);
      if (r) redraws.push(r);
      return;
    }
    redraws.forEach(function (fn) { fn(); });
  });

  function init(root) {
    var el = function (id) { return root.querySelector("#" + id); };
    if (!el("t01-rl-canvas") || !el("t01-rlc-canvas") || !el("t01-ca-phasor")) return null;

    function fmt(x, unit) {
      if (!isFinite(x)) return "—";
      var a = Math.abs(x);
      var pre = [[1e-9, "n"], [1e-6, "μ"], [1e-3, "m"], [1, ""], [1e3, "k"], [1e6, "M"]];
      var p = pre[3];
      for (var i = pre.length - 1; i >= 0; i--) {
        if (a >= pre[i][0] * 0.9995) { p = pre[i]; break; }
      }
      if (a === 0) p = pre[3];
      var v = x / p[0];
      var s = Math.abs(v) >= 100 ? v.toFixed(0) : Math.abs(v) >= 10 ? v.toFixed(1) : v.toFixed(2);
      return s + " " + p[1] + unit;
    }

    function css(name) {
      return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    }

    function renderReadouts(containerId, items) {
      el(containerId).innerHTML = items.map(function (it) {
        return '<div><div class="k">' + it[0] + '</div><div class="v">' + it[1] + "</div></div>";
      }).join("");
    }

    function setupCanvas(canvas, aspect) {
      var dpr = window.devicePixelRatio || 1;
      var W = canvas.clientWidth || 720;
      var H = Math.round(W * aspect);
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      canvas.style.height = H + "px";
      var ctx = canvas.getContext("2d");
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, H);
      return { ctx: ctx, W: W, H: H };
    }

    /* =========================================================
       1. SIMULADOR RL SERIE
       ========================================================= */
    var rlMode = "grow";
    var rlEps = el("t01-rl-eps"), rlR = el("t01-rl-r"), rlL = el("t01-rl-l");
    var rlCanvas = el("t01-rl-canvas");

    function computeRL(eps, R, L_mH, mode) {
      var L = L_mH * 1e-3;
      var tau = L / R;
      var Iinf = eps / R;
      var iTau = mode === "grow" ? Iinf * (1 - Math.exp(-1)) : Iinf * Math.exp(-1);
      var UL = 0.5 * L * Iinf * Iinf;
      return { tau: tau, Iinf: Iinf, iTau: iTau, UL: UL };
    }

    function updateRL() {
      var eps = +rlEps.value, R = +rlR.value, L_mH = +rlL.value;
      el("t01-rl-eps-o").textContent = eps.toFixed(1).replace(/\.0$/, "") + " V";
      el("t01-rl-r-o").textContent = R + " Ω";
      el("t01-rl-l-o").textContent = L_mH + " mH";

      var res = computeRL(eps, R, L_mH, rlMode);
      var iLabel = rlMode === "grow" ? "I∞ = ε/R" : "I₀ = ε/R";
      var tauLabel = rlMode === "grow" ? "i(τ) ≈ 0,63 I∞" : "i(τ) ≈ 0,37 I₀";
      renderReadouts("t01-rl-read", [
        ["τ = L/R", fmt(res.tau, "s")],
        [iLabel, fmt(res.Iinf, "A")],
        [tauLabel, fmt(res.iTau, "A")],
        ["U_L = ½LI∞²", fmt(res.UL, "J")]
      ]);
      drawRL();
    }

    function drawRL() {
      var g = setupCanvas(rlCanvas, 0.42);
      var ctx = g.ctx, W = g.W, H = g.H;
      var ink = css("--ink"), muted = css("--muted"), line = css("--line"), acc = css("--accent"), cop = css("--copper");

      var isGrow = rlMode === "grow";
      var yMin = isGrow ? 0 : -1;
      var yMax = 1;
      var L = 48, Rr = 16, T = 20, B = 34;
      var pw = W - L - Rr, ph = H - T - B;
      var X = function (x) { return L + pw * x / 5; };
      var Y = function (y) { return T + ph * (yMax - y) / (yMax - yMin); };

      ctx.font = '12px "JetBrains Mono", ui-monospace, monospace';
      ctx.lineWidth = 1;
      ctx.textAlign = "right";
      ctx.textBaseline = "middle";

      var yTicks = isGrow ? [0, 0.25, 0.5, 0.75, 1] : [-1, -0.5, 0, 0.5, 1];
      yTicks.forEach(function (y) {
        ctx.strokeStyle = y === 0 ? muted : line;
        ctx.beginPath(); ctx.moveTo(L, Y(y)); ctx.lineTo(W - Rr, Y(y)); ctx.stroke();
        ctx.fillStyle = muted;
        ctx.fillText(y.toFixed(2).replace(/\.?0+$/, ""), L - 6, Y(y));
      });

      ctx.textAlign = "center";
      ctx.textBaseline = "top";
      for (var k = 0; k <= 5; k++) {
        ctx.strokeStyle = line;
        ctx.beginPath(); ctx.moveTo(X(k), T); ctx.lineTo(X(k), T + ph); ctx.stroke();
        ctx.fillStyle = muted;
        ctx.fillText(k === 0 ? "0" : k + "τ", X(k), T + ph + 8);
      }

      // Marcador t = tau
      var yMark = isGrow ? 1 - Math.exp(-1) : Math.exp(-1);
      ctx.save();
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = muted;
      ctx.beginPath(); ctx.moveTo(X(1), T); ctx.lineTo(X(1), T + ph); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(L, Y(yMark)); ctx.lineTo(X(1), Y(yMark)); ctx.stroke();
      ctx.restore();

      function plot(fn, color) {
        ctx.strokeStyle = color;
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        for (var p = 0; p <= 250; p++) {
          var x = 5 * p / 250;
          var yy = fn(x);
          if (p === 0) ctx.moveTo(X(x), Y(yy));
          else ctx.lineTo(X(x), Y(yy));
        }
        ctx.stroke();
      }

      var fi = isGrow ? function (x) { return 1 - Math.exp(-x); } : function (x) { return Math.exp(-x); };
      var fv = isGrow ? function (x) { return Math.exp(-x); } : function (x) { return -Math.exp(-x); };

      plot(fv, cop);
      plot(fi, acc);

      // Punto en t = tau
      ctx.fillStyle = acc;
      ctx.beginPath(); ctx.arc(X(1), Y(yMark), 4.5, 0, 2 * Math.PI); ctx.fill();

      // Etiqueta t = tau
      ctx.font = '600 12px "Source Sans 3", system-ui, sans-serif';
      ctx.fillStyle = ink;
      ctx.textAlign = "left";
      ctx.textBaseline = "bottom";
      ctx.fillText(isGrow ? "t = τ (0,63 I∞)" : "t = τ (0,37 I₀)", X(1) + 6, Y(yMark) - 4);

      // Leyenda superior derecha
      ctx.font = '600 13px "Source Sans 3", system-ui, sans-serif';
      ctx.textAlign = "right";
      ctx.textBaseline = "top";
      ctx.fillStyle = acc;
      ctx.fillText(isGrow ? "i(t) / I∞" : "i(t) / I₀", W - Rr - 6, T + 4);
      ctx.fillStyle = cop;
      ctx.fillText("v_L(t) / ε", W - Rr - 6, T + 22);
    }

    function setRLMode(m) {
      rlMode = m;
      el("t01-rl-grow").classList.toggle("on", m === "grow");
      el("t01-rl-decay").classList.toggle("on", m === "decay");
      el("t01-rl-grow").setAttribute("aria-pressed", String(m === "grow"));
      el("t01-rl-decay").setAttribute("aria-pressed", String(m === "decay"));
      updateRL();
    }
    el("t01-rl-grow").addEventListener("click", function () { setRLMode("grow"); });
    el("t01-rl-decay").addEventListener("click", function () { setRLMode("decay"); });
    [rlEps, rlR, rlL].forEach(function (s) { s.addEventListener("input", updateRL); });

    /* =========================================================
       2. SIMULADOR RLC SERIE TRANSITORIO
       ========================================================= */
    var rlcR = el("t01-rlc-r"), rlcL = el("t01-rlc-l"), rlcC = el("t01-rlc-c"), rlcQ0 = el("t01-rlc-q0");
    var rlcCanvas = el("t01-rlc-canvas");

    function computeRLC(R, L_mH, C_uF) {
      var L = L_mH * 1e-3;
      var C = C_uF * 1e-6;
      var omega0 = 1 / Math.sqrt(L * C);
      var gamma = R / (2 * L);
      var Rcrit = 2 * Math.sqrt(L / C);
      var rel = Math.abs(gamma - omega0) / omega0;
      var regime, omegaD = null, l1 = null, l2 = null;
      if (rel <= 1e-3) {
        regime = "crit";
      } else if (gamma < omega0) {
        regime = "under";
        omegaD = Math.sqrt(omega0 * omega0 - gamma * gamma);
      } else {
        regime = "over";
        var beta = Math.sqrt(gamma * gamma - omega0 * omega0);
        l1 = -gamma + beta;
        l2 = -gamma - beta;
      }
      return { omega0: omega0, gamma: gamma, Rcrit: Rcrit, regime: regime, omegaD: omegaD, l1: l1, l2: l2 };
    }

    function evalRLC(res, t) {
      if (res.regime === "under") {
        return Math.exp(-res.gamma * t) * (Math.cos(res.omegaD * t) + (res.gamma / res.omegaD) * Math.sin(res.omegaD * t));
      }
      if (res.regime === "crit") {
        return (1 + res.gamma * t) * Math.exp(-res.gamma * t);
      }
      var denom = res.l2 - res.l1;
      return (res.l2 * Math.exp(res.l1 * t) - res.l1 * Math.exp(res.l2 * t)) / denom;
    }

    function updateRLC() {
      var R = +rlcR.value, L_mH = +rlcL.value, C_uF = +rlcC.value, Q0 = +rlcQ0.value;
      el("t01-rlc-r-o").textContent = R.toFixed(1).replace(/\.0$/, "") + " Ω";
      el("t01-rlc-l-o").textContent = L_mH + " mH";
      el("t01-rlc-c-o").textContent = C_uF + " μF";
      el("t01-rlc-q0-o").textContent = Q0 + " μC";

      var res = computeRLC(R, L_mH, C_uF);
      var regText = res.regime === "under" ? "Subamortiguado" : res.regime === "crit" ? "Crítico" : "Sobreamortiguado";
      renderReadouts("t01-rlc-read", [
        ["ω₀ = 1/√(LC)", fmt(res.omega0, "s⁻¹")],
        ["γ = R/(2L)", fmt(res.gamma, "s⁻¹")],
        ["ω_d", res.omegaD !== null ? fmt(res.omegaD, "s⁻¹") : "—"],
        ["R_crít", fmt(res.Rcrit, "Ω")],
        ["Régimen", regText]
      ]);

      var noteEl = el("t01-rlc-formula");
      if (noteEl) {
        if (res.regime === "under") {
          noteEl.textContent = "Régimen subamortiguado (γ < ω₀): q(t) = Q₀ e^(−γt) [cos(ω_d t) + (γ/ω_d) sen(ω_d t)].";
        } else if (res.regime === "crit") {
          noteEl.textContent = "Amortiguamiento crítico (γ = ω₀): q(t) = Q₀ (1 + γt) e^(−γt). Retorno más rápido sin oscilar.";
        } else {
          noteEl.textContent = "Régimen sobreamortiguado (γ > ω₀): q(t) = Q₀ (λ₂ e^(λ₁t) − λ₁ e^(λ₂t)) / (λ₂ − λ₁), con λ₁,₂ = −γ ± √(γ² − ω₀²).";
        }
      }
      drawRLC(res, Q0);
    }

    function drawRLC(res, Q0) {
      var g = setupCanvas(rlcCanvas, 0.42);
      var ctx = g.ctx, W = g.W, H = g.H;
      var ink = css("--ink"), muted = css("--muted"), line = css("--line"), acc = css("--accent"), cop = css("--copper");

      var T0 = 2 * Math.PI / res.omega0;
      var tmax;
      if (res.regime === "under") {
        tmax = Math.max(4 * T0, Math.min(5 / Math.max(res.gamma, 1e-3), 8 * T0));
      } else if (res.regime === "crit") {
        tmax = 6 / res.gamma;
      } else {
        tmax = Math.min(5 / Math.abs(res.l1), 16 * T0);
      }

      var L = 48, Rr = 16, T = 20, B = 34;
      var pw = W - L - Rr, ph = H - T - B;
      var X = function (t) { return L + pw * (t / tmax); };
      var Y = function (y) { return T + ph * (1 - y) / 2; };

      ctx.font = '12px "JetBrains Mono", ui-monospace, monospace';
      ctx.lineWidth = 1;
      ctx.textAlign = "right";
      ctx.textBaseline = "middle";
      [-1, -0.5, 0, 0.5, 1].forEach(function (y) {
        ctx.strokeStyle = y === 0 ? muted : line;
        ctx.beginPath(); ctx.moveTo(L, Y(y)); ctx.lineTo(W - Rr, Y(y)); ctx.stroke();
        ctx.fillStyle = muted;
        ctx.fillText(y.toFixed(1).replace(/\.0$/, ""), L - 6, Y(y));
      });

      ctx.textAlign = "center";
      ctx.textBaseline = "top";
      for (var k = 0; k <= 4; k++) {
        var tk = tmax * k / 4;
        ctx.strokeStyle = line;
        ctx.beginPath(); ctx.moveTo(X(tk), T); ctx.lineTo(X(tk), T + ph); ctx.stroke();
        ctx.fillStyle = muted;
        ctx.textAlign = k === 0 ? "left" : k === 4 ? "right" : "center";
        ctx.fillText(k === 0 ? "0" : fmt(tk, "s"), X(tk), T + ph + 8);
      }

      // Envolvente en subamortiguado
      if (res.regime === "under") {
        ctx.save();
        ctx.setLineDash([4, 4]);
        ctx.strokeStyle = cop;
        ctx.lineWidth = 1.4;
        [1, -1].forEach(function (sgn) {
          ctx.beginPath();
          for (var p = 0; p <= 200; p++) {
            var t = tmax * p / 200;
            var env = sgn * Math.exp(-res.gamma * t);
            if (p === 0) ctx.moveTo(X(t), Y(env));
            else ctx.lineTo(X(t), Y(env));
          }
          ctx.stroke();
        });
        ctx.restore();
      }

      // Curva q(t) / Q0
      ctx.strokeStyle = acc;
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var p = 0; p <= 320; p++) {
        var t = tmax * p / 320;
        var q = evalRLC(res, t);
        if (p === 0) ctx.moveTo(X(t), Y(q));
        else ctx.lineTo(X(t), Y(q));
      }
      ctx.stroke();

      // Leyenda
      ctx.font = '600 13px "Source Sans 3", system-ui, sans-serif';
      ctx.textAlign = "right";
      ctx.textBaseline = "top";
      ctx.fillStyle = acc;
      ctx.fillText("q(t) / Q₀  (Q₀ = " + Q0 + " μC)", W - Rr - 6, T + 4);
      if (res.regime === "under") {
        ctx.fillStyle = cop;
        ctx.fillText("±e^(−γt)", W - Rr - 6, T + 22);
      }
      ctx.fillStyle = ink;
      ctx.textAlign = "left";
      var badge = res.regime === "under" ? "Subamortiguado" : res.regime === "crit" ? "Amortiguamiento crítico" : "Sobreamortiguado";
      ctx.fillText(badge, L + 16, T + 4);
    }

    el("t01-rlc-crit").addEventListener("click", function () {
      var L = +rlcL.value * 1e-3;
      var C = +rlcC.value * 1e-6;
      var Rcrit = 2 * Math.sqrt(L / C);
      rlcR.value = Rcrit.toFixed(1);
      updateRLC();
    });
    [rlcR, rlcL, rlcC, rlcQ0].forEach(function (s) { s.addEventListener("input", updateRLC); });

    /* =========================================================
       3. SIMULADOR CA: FASORES Y RESONANCIA
       ========================================================= */
    var caV0 = el("t01-ca-v0"), caW = el("t01-ca-w"), caR = el("t01-ca-r"), caL = el("t01-ca-l"), caC = el("t01-ca-c");
    var caPhasor = el("t01-ca-phasor"), caRes = el("t01-ca-res");

    function computeCA(V0, omega, R, L_mH, C_uF) {
      var L = L_mH * 1e-3;
      var C = C_uF * 1e-6;
      var XL = omega * L;
      var XC = 1 / (omega * C);
      var X = XL - XC;
      var Zmag = Math.sqrt(R * R + X * X);
      var phi = Math.atan2(X, R);
      var phiDeg = phi * 180 / Math.PI;
      var I0 = V0 / Zmag;
      var cosphi = R / Zmag;
      var Pavg = 0.5 * V0 * I0 * cosphi;
      var omega0 = 1 / Math.sqrt(L * C);
      return {
        XL: XL, XC: XC, X: X, Zmag: Zmag, phi: phi, phiDeg: phiDeg,
        I0: I0, cosphi: cosphi, Pavg: Pavg, omega0: omega0,
        VR: I0 * R, VL: I0 * XL, VC: I0 * XC
      };
    }

    function updateCA() {
      var V0 = +caV0.value;
      var omega = Math.pow(10, +caW.value);
      var R = +caR.value, L_mH = +caL.value, C_uF = +caC.value;

      el("t01-ca-v0-o").textContent = V0 + " V";
      el("t01-ca-w-o").textContent = omega.toFixed(0) + " rad/s";
      el("t01-ca-r-o").textContent = R + " Ω";
      el("t01-ca-l-o").textContent = L_mH + " mH";
      el("t01-ca-c-o").textContent = C_uF + " μF";

      var res = computeCA(V0, omega, R, L_mH, C_uF);
      var tipo = Math.abs(res.phiDeg) < 0.2 ? "resonancia" : res.phiDeg > 0 ? "inductivo" : "capacitivo";
      var phiStr = (res.phiDeg >= 0 ? "+" : "") + res.phiDeg.toFixed(2) + "° (" + tipo + ")";

      renderReadouts("t01-ca-read", [
        ["X_L = ωL", fmt(res.XL, "Ω")],
        ["X_C = 1/(ωC)", fmt(res.XC, "Ω")],
        ["|Z|", fmt(res.Zmag, "Ω")],
        ["φ", phiStr],
        ["I₀ = V₀/|Z|", fmt(res.I0, "A")],
        ["⟨P⟩", fmt(res.Pavg, "W")],
        ["cos φ", res.cosphi.toFixed(3)]
      ]);

      drawCAPhasor(V0, res);
      drawCARes(V0, omega, R, L_mH, C_uF, res);
    }

    function drawArrow(ctx, x1, y1, x2, y2, color, width) {
      var dx = x2 - x1, dy = y2 - y1;
      var len = Math.hypot(dx, dy);
      if (len < 2) return;
      var ang = Math.atan2(dy, dx);
      var head = Math.min(10, Math.max(6, len * 0.2));
      ctx.strokeStyle = color;
      ctx.fillStyle = color;
      ctx.lineWidth = width;
      ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(x2, y2);
      ctx.lineTo(x2 - head * Math.cos(ang - 0.42), y2 - head * Math.sin(ang - 0.42));
      ctx.lineTo(x2 - head * Math.cos(ang + 0.42), y2 - head * Math.sin(ang + 0.42));
      ctx.closePath();
      ctx.fill();
    }

    function drawCAPhasor(V0, res) {
      var g = setupCanvas(caPhasor, 0.78);
      var ctx = g.ctx, W = g.W, H = g.H;
      var ink = css("--ink"), muted = css("--muted"), line = css("--line"), acc = css("--accent"), cop = css("--copper");

      var ox = W * 0.24, oy = H * 0.52;
      var maxX = Math.max(V0, res.VR, 1);
      var maxY = Math.max(res.VL, res.VC, Math.abs(res.VL - res.VC), V0 * 0.6, 1);
      var scaleX = (W * 0.66) / maxX;
      var scaleY = (H * 0.38) / maxY;
      var sc = Math.min(scaleX, scaleY);

      // Ejes de referencia
      ctx.strokeStyle = line;
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(14, oy); ctx.lineTo(W - 14, oy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox, 16); ctx.lineTo(ox, H - 16); ctx.stroke();

      // Fasor I de referencia (longitud fija proporcional)
      var iLen = Math.min(W * 0.32, 90);
      drawArrow(ctx, ox, oy, ox + iLen, oy, acc, 2.2);

      var vxR = ox + res.VR * sc;
      var vyL = oy - res.VL * sc;
      var vyC = oy + res.VC * sc;
      var vyNet = oy - (res.VL - res.VC) * sc;

      // V_R, V_L, V_C
      drawArrow(ctx, ox, oy, vxR, oy, acc, 3);
      drawArrow(ctx, ox, oy, ox, vyL, cop, 2.2);
      drawArrow(ctx, ox, oy, ox, vyC, muted, 2.2);

      // Guías punteadas hacia V total
      ctx.save();
      ctx.setLineDash([3, 4]);
      ctx.strokeStyle = muted;
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(vxR, oy); ctx.lineTo(vxR, vyNet); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox, vyNet); ctx.lineTo(vxR, vyNet); ctx.stroke();
      ctx.restore();

      // Fasor V total
      drawArrow(ctx, ox, oy, vxR, vyNet, cop, 3);

      // Arco de ángulo phi
      if (Math.abs(res.phiDeg) > 1) {
        var rArc = Math.min(34, Math.hypot(vxR - ox, vyNet - oy) * 0.45);
        ctx.strokeStyle = ink;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(ox, oy, rArc, 0, -res.phi, res.phi > 0);
        ctx.stroke();
        ctx.font = '600 12px "Source Sans 3", system-ui, sans-serif';
        ctx.fillStyle = ink;
        ctx.textAlign = "left";
        ctx.textBaseline = "middle";
        ctx.fillText("φ", ox + rArc + 5, oy - Math.sin(res.phi / 2) * rArc);
      }

      // Etiquetas
      ctx.font = '600 12.5px "Source Sans 3", system-ui, sans-serif';
      ctx.textAlign = "left";
      ctx.textBaseline = "top";
      ctx.fillStyle = ink;
      ctx.fillText("Diagrama fasorial", 12, 10);

      ctx.fillStyle = acc;
      ctx.textAlign = "left";
      ctx.textBaseline = "bottom";
      ctx.fillText("Î, V̂_R", Math.min(vxR + 6, W - 52), oy - 4);

      ctx.fillStyle = cop;
      ctx.textAlign = "right";
      ctx.textBaseline = "middle";
      ctx.fillText("V̂_L", ox - 6, Math.max(vyL, 26));

      ctx.fillStyle = muted;
      ctx.fillText("V̂_C", ox - 6, Math.min(vyC, H - 20));

      ctx.fillStyle = cop;
      ctx.textAlign = "left";
      ctx.fillText("V̂", Math.min(vxR + 6, W - 24), vyNet);
    }

    function drawCARes(V0, omega, R, L_mH, C_uF, res) {
      var g = setupCanvas(caRes, 0.78);
      var ctx = g.ctx, W = g.W, H = g.H;
      var ink = css("--ink"), muted = css("--muted"), line = css("--line"), acc = css("--accent"), cop = css("--copper");

      var wMin = 100, wMax = 10000;
      var logMin = Math.log10(wMin), logMax = Math.log10(wMax);
      var Imax = V0 / R;

      var L = 46, Rr = 16, T = 32, B = 34;
      var pw = W - L - Rr, ph = H - T - B;
      var X = function (w) { return L + pw * (Math.log10(w) - logMin) / (logMax - logMin); };
      var Y = function (I) { return T + ph * (1 - I / Imax); };

      ctx.font = '11.5px "JetBrains Mono", ui-monospace, monospace';
      ctx.lineWidth = 1;
      ctx.textAlign = "right";
      ctx.textBaseline = "middle";
      [0, 0.25, 0.5, 0.75, 1].forEach(function (f) {
        var Iv = f * Imax;
        ctx.strokeStyle = f === 0 ? muted : line;
        ctx.beginPath(); ctx.moveTo(L, Y(Iv)); ctx.lineTo(W - Rr, Y(Iv)); ctx.stroke();
        ctx.fillStyle = muted;
        ctx.fillText(f === 0 ? "0" : fmt(Iv, "A"), L - 5, Y(Iv));
      });

      ctx.textAlign = "center";
      ctx.textBaseline = "top";
      [100, 300, 1000, 3000, 10000].forEach(function (wTick) {
        ctx.strokeStyle = line;
        ctx.beginPath(); ctx.moveTo(X(wTick), T); ctx.lineTo(X(wTick), T + ph); ctx.stroke();
        ctx.fillStyle = muted;
        ctx.fillText(String(wTick), X(wTick), T + ph + 8);
      });

      // Marcador en omega0
      if (res.omega0 >= wMin && res.omega0 <= wMax) {
        ctx.save();
        ctx.setLineDash([4, 4]);
        ctx.strokeStyle = muted;
        ctx.beginPath(); ctx.moveTo(X(res.omega0), T); ctx.lineTo(X(res.omega0), T + ph); ctx.stroke();
        ctx.restore();
        ctx.font = '600 11.5px "Source Sans 3", system-ui, sans-serif';
        ctx.fillStyle = muted;
        ctx.textAlign = "center";
        ctx.textBaseline = "bottom";
        ctx.fillText("ω₀", X(res.omega0), T - 4);
      }

      // Curva I0(omega)
      ctx.strokeStyle = acc;
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (var p = 0; p <= 240; p++) {
        var w = Math.pow(10, logMin + (logMax - logMin) * p / 240);
        var Iw = computeCA(V0, w, R, L_mH, C_uF).I0;
        if (p === 0) ctx.moveTo(X(w), Y(Iw));
        else ctx.lineTo(X(w), Y(Iw));
      }
      ctx.stroke();

      // Marcador en omega actual
      var xCur = X(omega), yCur = Y(res.I0);
      ctx.save();
      ctx.setLineDash([2, 3]);
      ctx.strokeStyle = cop;
      ctx.beginPath(); ctx.moveTo(xCur, T + ph); ctx.lineTo(xCur, yCur); ctx.stroke();
      ctx.restore();
      ctx.fillStyle = cop;
      ctx.beginPath(); ctx.arc(xCur, yCur, 5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = css("--surface");
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.font = '600 12.5px "Source Sans 3", system-ui, sans-serif';
      ctx.fillStyle = ink;
      ctx.textAlign = "left";
      ctx.textBaseline = "top";
      ctx.fillText("Resonancia I₀(ω) [rad/s]", 12, 8);
    }

    [caV0, caW, caR, caL, caC].forEach(function (s) { s.addEventListener("input", updateCA); });

    /* =========================================================
       ACTUALIZACIÓN GLOBAL Y TEMA
       ========================================================= */
    function updateAll() {
      updateRL();
      updateRLC();
      updateCA();
    }

    // Redraw only while the simulators are on screen; the unit may be kept detached in memory.
    function redraw() { if (root.isConnected) updateAll(); }
    window.addEventListener("resize", redraw);
    if (window.matchMedia) {
      var mq = window.matchMedia("(prefers-color-scheme: dark)");
      if (mq.addEventListener) mq.addEventListener("change", redraw);
    }
    new MutationObserver(redraw).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(redraw);
    redraw();
    return redraw;
  }
})();
