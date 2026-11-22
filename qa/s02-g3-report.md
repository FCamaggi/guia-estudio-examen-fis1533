# Gate G3 Physics Verification Report — S2 (`unidades/s02-simulacro-2.html`)

**Scope:** Independent verification of `unidades/s02-simulacro-2.html` (`s02-enunciados`: `P1A`, `P1B`, `P2`, `P3`; `s02-pauta`: `s02-p1a`, `s02-p1b`, `s02-p2`, `s02-p3`, including `ol.reveal` steps, `li.final`, `li.check`, and `div.score-box` point totals).  
**Tooling:** `/usr/bin/python3` with SymPy and BeautifulSoup (`/tmp/verify_s02.py`, `/tmp/verify_p3.py`).

## Verification Table

| problem | quantity | stated | yours | OK/ERROR |
|---|---|---|---|---|
| `P1A` | a) $\vec E_{\text{anillo}}(z)$ | $\dfrac{kQz}{(z^2+a^2)^{3/2}}\,\hat z$ | $\dfrac{kQz}{(z^2+a^2)^{3/2}}\,\hat z$ | OK |
| `P1A` | a) $\vec E_{\text{total}}(z)$ ($z > 0$) | $\left[\dfrac{kQz}{(z^2+a^2)^{3/2}} - \dfrac{kQ}{8z^2}\right]\hat z$ | $\left[\dfrac{kQz}{(z^2+a^2)^{3/2}} - \dfrac{kQ}{8z^2}\right]\hat z$ | OK |
| `P1A` | b) $z_0 > 0$ and stability | $z_0 = \dfrac{a}{\sqrt{3}}$, equilibrio inestable (se aleja) | $z_0 = \dfrac{a}{\sqrt{3}}$, $\left.\dfrac{dE_z}{dz}\right|_{z_0} = \dfrac{27\sqrt{3}kQ}{32a^3} > 0$ (unstable) | OK |
| `P1A` | c) $V(z_0)$ | $\dfrac{3\sqrt{3}\,kQ}{8a}$ | $\dfrac{3\sqrt{3}\,kQ}{8a}$ | OK |
| `P1A` | d) $W_{\text{campo}}$, $v_\infty$ | $\dfrac{3\sqrt{3}\,kQq_0}{8a}$, $\sqrt{\dfrac{3\sqrt{3}\,kQq_0}{4ma}}$ | $\dfrac{3\sqrt{3}\,kQq_0}{8a}$, $\sqrt{\dfrac{3\sqrt{3}\,kQq_0}{4ma}}$ | OK |
| `P1A` | `li.check` & points | Units $\text{N/C}, \text{V}, \text{J}, \text{m/s}$; $z\gg a \to \frac{7}{8}kQ/z^2$; $z\to 0^+ \to -\hat z$; $-dV/dz = E_z$; $2+1.5+1+1.5=6$ pts | All verified symbolically; step sum = $6.0$; score-box sum = $6.0$ | OK |
| `P1B` | a) Currents at $t = 0^+$ | $I_1 = 3\ \text{A}$ (sube por $\varepsilon_1$), $I_2 = 0$, $i_C = 3\ \text{A}$ ($a\to b$) | $V_a = 6\ \text{V}$; $I_1 = 3\ \text{A}$ ($\to a$), $I_2 = 0$, $i_C = 3\ \text{A}$ ($a\to b$) | OK |
| `P1B` | b) $t\to\infty$ currents, $Q_f$, $U_f$ | $I = 1\ \text{A}$ (sube por $\varepsilon_1$, baja por $\varepsilon_2$), $i_C = 0$, $Q_f = 30\ \mu\text{C}$, $U_f = 150\ \mu\text{J}$ | $V_a = 10\ \text{V}$; $I_1 = 1\ \text{A}$ ($\to a$), $I_2 = 1\ \text{A}$ (down), $i_C = 0$, $Q_f = 30\ \mu\text{C}$, $U_f = 150\ \mu\text{J}$ | OK |
| `P1B` | c) $R_{\text{eq}}$, $\tau$, $q(t)$, $i_C(t)$ | $R_{\text{eq}} = \tfrac{10}{3}\ \Omega$, $\tau = 10\ \mu\text{s}$, $q(t) = 30\ \mu\text{C}\,(1 - e^{-t/\tau})$, $i_C(t) = 3\ \text{A}\,e^{-t/\tau}$ | $R_3 + R_1\parallel R_2 = \tfrac{10}{3}\ \Omega$, $\tau = 10\ \mu\text{s}$, $q(t) = 30(1-e^{-t/10\,\mu\text{s}})\ \mu\text{C}$, $i_C(t) = 3e^{-t/10\,\mu\text{s}}\ \text{A}$ | OK |
| `P1B` | d) $v_C(t')$, $\tau'$, $E_{\text{dis}}$ | $v_C(t') = 6 + 4e^{-t'/\tau'}\ \text{V}$, $\tau' = 18\ \mu\text{s}$, $E_{\text{dis}} = 24\ \mu\text{J}$ | $v_C(t') = 6 + 4e^{-t'/18\,\mu\text{s}}\ \text{V}$, $\tau' = 18\ \mu\text{s}$, $E_{\text{dis}} = 24\ \mu\text{J}$ | OK |
| `P1B` | `li.check` & points | Units $\Omega\cdot\text{F}=\text{s}$; $\varepsilon_2=\varepsilon_1$ & no-$\varepsilon_2$ limits; $6 < 10 < 12\ \text{V}$; direct $\int (R_2+R_3)i^2 dt' = 24\ \mu\text{J}$; $1.5+1.5+1+2=6$ pts | All verified symbolically; step sum = $6.0$; score-box sum = $6.0$ | OK |
| `P2` | a) $\vec B_{\text{arco}}$, $\vec B_{\text{sup}}$, $\vec B_{\text{inf}}$, $\vec B_{\text{der}}$ at $O$ | $\dfrac{\mu_0 I}{4a}$, $\dfrac{\sqrt2\,\mu_0 I}{8\pi a}$, $\dfrac{\sqrt2\,\mu_0 I}{8\pi a}$, $\dfrac{\sqrt2\,\mu_0 I}{4\pi a}$ (all $+\hat z$) | $\dfrac{\mu_0 I}{4a}\hat z$, $\dfrac{\sqrt2\,\mu_0 I}{8\pi a}\hat z$, $\dfrac{\sqrt2\,\mu_0 I}{8\pi a}\hat z$, $\dfrac{\sqrt2\,\mu_0 I}{4\pi a}\hat z$ | OK |
| `P2` | b) $\vec B_O$ total | $\dfrac{\mu_0 I}{4a}\left(1 + \dfrac{2\sqrt2}{\pi}\right)\hat z \approx 0{,}48\,\dfrac{\mu_0 I}{a}\hat z$ | $\dfrac{\mu_0 I(2\sqrt2+\pi)}{4\pi a}\hat z \approx 0.4751\,\dfrac{\mu_0 I}{a}\hat z$ | OK |
| `P2` | c) $\vec\mu$ | $\dfrac{(\pi+4)Ia^2}{2}\,\hat z$ | $\dfrac{(\pi+4)Ia^2}{2}\,\hat z$ | OK |
| `P2` | d) $\vec\tau$, rotation axis, stable eq., $\vec F_{\text{neta}}$ | $\dfrac{(\pi+4)Ia^2B_0}{2}\,\hat y$, axis $\parallel \hat y$, $\vec\mu\parallel\hat x$ (plane $\perp \vec B_0$), $\vec F_{\text{neta}} = 0$ | $\dfrac{(\pi+4)Ia^2B_0}{2}\,\hat y$, axis $\parallel \hat y$, $\vec\mu\parallel\hat x$ ($yz$ plane), $\vec F_{\text{neta}} = 0$ | OK |
| `P2` | `li.check` & points | Units $\text{T}, \text{A·m}^2, \text{N·m}$; half-square comparison $\frac{\sqrt2\mu_0 I}{2\pi a}$; $0.48 < 0.5$; $2.5+1+1.5+1=6$ pts | All verified symbolically; step sum = $6.0$; score-box sum = $6.0$ | OK |
| `P3` | a) $\Phi_B(s)$, $\varepsilon$, $I(v)$, direction | $\Phi_B = B\ell s\cos\theta$, $|\varepsilon| = B\ell v\cos\theta$, $I = \frac{B\ell v\cos\theta}{R} = \tfrac{\sqrt3}{2}v$, CW from above ($-\hat y$ in rod) | $\Phi_B = B\ell s\cos\theta$, $\varepsilon = -B\ell v\cos\theta$, $I = \tfrac{\sqrt3}{2}v\ \text{A}$, CW from above ($-\hat y$ in rod) | OK |
| `P3` | b) $\vec F_B$, $F_\parallel$, ODE | $\vec F_B = -\frac{B^2\ell^2 v\cos\theta}{R}\hat x$, $F_\parallel = -\frac{B^2\ell^2\cos^2\theta}{R}v$, $m\dot v = mg\sin\theta - \frac{B^2\ell^2\cos^2\theta}{R}v$ ($0.3\dot v = 1.5 - 0.375v$) | $\vec F_B = -\frac{B^2\ell^2 v\cos\theta}{R}\hat x$, $F_\parallel = -\frac{B^2\ell^2\cos^2\theta}{R}v$, $0.3\dot v = 1.5 - 0.375v$ | OK |
| `P3` | c) $v(t)$, $v_t$, $\tau$ | $v(t) = v_t(1-e^{-t/\tau})$, $v_t = 4\ \text{m/s}$, $\tau = 0{,}8\ \text{s}$ | $v(t) = v_t(1-e^{-t/\tau})$, $v_t = 4\ \text{m/s}$, $\tau = 0.8\ \text{s}$ | OK |
| `P3` | d) Power at $v_t$, $E_{\text{dis}}$ in $D=10\ \text{m}$ | $P_{\text{grav}} = I_t^2 R = 6\ \text{W}$ ($I_t = 2\sqrt3\ \text{A}$), $E_{\text{dis}} = 12{,}6\ \text{J}$ | $P_{\text{grav}} = I_t^2 R = 6\ \text{W}$ ($I_t = 2\sqrt3\ \text{A}$), $E_{\text{dis}} = 12.6\ \text{J}$ (exact ODE at $s=10\ \text{m}$: $t_D \approx 3.287\ \text{s}$, $v \approx 98.36\%\,v_t$, $E_{\text{dis}} \approx 12.68\ \text{J}$) | OK |
| `P3` | `li.check` & points | Units $\frac{B^2\ell^2}{R}\sim\text{kg/s}$; $\theta=0$, $B\to 0$, $\vec B\perp$ plane ($v_t=3\ \text{m/s}$); $t_D\approx 3.3\ \text{s}\approx 4\tau$ ($98\%$ of $v_t$); $1.5+1.5+1.5+1.5=6$ pts | All verified symbolically & numerically; step sum = $6.0$; score-box sum = $6.0$ | OK |

## ERRORS

None. All four problems (`P1A`, `P1B`, `P2`, `P3`) are physically well posed, self-contained without relying on the figures, hand-computable without a calculator, mathematically and physically consistent across statements, steps, `li.final`, and `li.check`, and have exact point alignment (6.0 points per problem across statement parts, corresponding pauta steps, and `div.score-box` checkboxes).

## MINOR

1. **`P2` Paso 3 integration limits phrasing:** For the top straight segment from $(a, a)$ to $(0, a)$, Paso 3 writes "el pie de la perpendicular es $(0, a)$, así que $u$ va de $0$ a $a$". While Paso 2 writes the integral as a positive magnitude $|d\vec\ell\times\hat r|$ and gives the correct positive result $B_{\text{sup}} = \frac{\sqrt2\,\mu_0 I}{8\pi a}$, if $u$ is taken as the signed coordinate along the current direction from $(0, a)$ as used for the right segment, $u$ runs from $-a$ to $0$.
2. **`P2` implicit positive signs on $I$ and $B_0$:** Unlike `P1A` (which states $Q > 0$ and $q_0 > 0$), `P2` writes "corriente $I$ (en A)" and "$\vec B_0 = B_0\,\hat x$ (en T)" without explicitly stating $I > 0$ and $B_0 > 0$; the signs of $\vec B_O$, $\vec\mu$, $\vec\tau$, and the stable equilibrium ($\vec\mu \parallel +\hat x$) assume $I > 0$ and $B_0 > 0$.
3. **`P3` part (a) symbolic vs. numerical reporting in `li.final`:** `li.final` reports $\Phi_B = B\ell s\cos\theta$ and $|\varepsilon| = B\ell v\cos\theta$ symbolically without their numerical expressions ($\frac{\sqrt3}{4}s\ \text{Wb}$ and $\frac{\sqrt3}{4}v\ \text{V}$, while giving $I = \frac{\sqrt3}{2}v$), and uses the upward normal $\hat n = \sin\theta\,\hat x + \cos\theta\,\hat z$ declared in Paso 1 rather than in the statement.
