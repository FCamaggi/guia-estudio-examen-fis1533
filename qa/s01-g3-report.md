# Gate G3 Physics Verification Report — S1 (`unidades/s01-simulacro-1.html`)

**Scope:** Independent verification of `unidades/s01-simulacro-1.html` (statements in `s01-enunciados`: `P1A`, `P1B`, `P2`, `P3`; pauta in `s01-pauta`: `s01-p1a`, `s01-p1b`, `s01-p2`, `s01-p3`, including steps, `li.final`, `li.check`, and `div.score-box` point totals).  
**Tooling:** Python `/usr/bin/python3` with SymPy `1.12` and BeautifulSoup (`/tmp/verify_s01.py`).

## Verification Table

| problem | quantity | stated | yours | OK/ERROR |
|---|---|---|---|---|
| `P1A` | a) $Q_0$ | $\dfrac{\pi\rho_0 R^3}{3}$ | $\dfrac{\pi\rho_0 R^3}{3}$ | OK |
| `P1A` | b) $\vec E(r < R)$ | $\dfrac{\rho_0}{\varepsilon_0}\left(\dfrac{r}{3} - \dfrac{r^2}{4R}\right)\hat r$ | $\dfrac{\rho_0}{\varepsilon_0}\left(\dfrac{r}{3} - \dfrac{r^2}{4R}\right)\hat r$ | OK |
| `P1A` | b) $\vec E(R < r < 2R)$ | $\dfrac{\rho_0 R^3}{12\varepsilon_0 r^2}\hat r$ | $\dfrac{\rho_0 R^3}{12\varepsilon_0 r^2}\hat r$ | OK |
| `P1A` | b) $\vec E(2R < r < 4R)$ | $0$ | $0$ | OK |
| `P1A` | b) $\vec E(r > 4R)$ | $\dfrac{\rho_0 R^3}{4\varepsilon_0 r^2}\hat r$ | $\dfrac{\rho_0 R^3}{4\varepsilon_0 r^2}\hat r$ | OK |
| `P1A` | c) $\sigma_{\text{int}}$, $\sigma_{\text{ext}}$ | $-\dfrac{\rho_0 R}{48}$, $+\dfrac{\rho_0 R}{64}$ | $-\dfrac{\rho_0 R}{48}$, $+\dfrac{\rho_0 R}{64}$ | OK |
| `P1A` | d) $V_{\text{casc}}$, $V(0)$ | $\dfrac{\rho_0 R^2}{16\varepsilon_0}$, $\dfrac{3\rho_0 R^2}{16\varepsilon_0}$ | $\dfrac{\rho_0 R^2}{16\varepsilon_0}$, $\dfrac{3\rho_0 R^2}{16\varepsilon_0}$ | OK |
| `P1A` | `li.check` & points | Units $\text{N/C}, \text{C/m}^2, \text{V}$; continuity at $r=R$; total shell charge $Q_c$; $V(0)>V_{\text{casc}}>0$; $1+2.5+1+1.5=6$ pts (steps & box) | All verified symbolically; step sum = $6.0$; score-box sum = $6.0$ | OK |
| `P1B` | a) $\vec E(r)$ | $\dfrac{Q}{\pi\varepsilon_0(\kappa_1 + \kappa_2)rL}\hat r$ (same in both) | $\dfrac{Q}{\pi\varepsilon_0(\kappa_1 + \kappa_2)rL}\hat r$ | OK |
| `P1B` | a) $\Delta V = V_a - V_b$ | $\dfrac{Q\ln(b/a)}{\pi\varepsilon_0(\kappa_1 + \kappa_2)L}$ | $\dfrac{Q\ln(b/a)}{\pi\varepsilon_0(\kappa_1 + \kappa_2)L}$ | OK |
| `P1B` | a)–b) $C$ (Gauss & parallel) | $\dfrac{\pi\varepsilon_0(\kappa_1 + \kappa_2)L}{\ln(b/a)} = C_1 + C_2$ (paralelo) | $\dfrac{\pi\varepsilon_0(\kappa_1 + \kappa_2)L}{\ln(b/a)} = C_1 + C_2$ (parallel) | OK |
| `P1B` | c) $\vec D_i$, $\vec P_i$ | $\dfrac{\kappa_i Q}{\pi(\kappa_1 + \kappa_2)rL}\hat r$, $\dfrac{(\kappa_i - 1)Q}{\pi(\kappa_1 + \kappa_2)rL}\hat r$ | $\dfrac{\kappa_i Q}{\pi(\kappa_1 + \kappa_2)rL}\hat r$, $\dfrac{(\kappa_i - 1)Q}{\pi(\kappa_1 + \kappa_2)rL}\hat r$ | OK |
| `P1B` | d) $\sigma_{f,i}(a)$, $\sigma_{f,i}(b)$ | $+\dfrac{\kappa_i Q}{\pi(\kappa_1 + \kappa_2)aL}$, $-\dfrac{\kappa_i Q}{\pi(\kappa_1 + \kappa_2)bL}$ | $+\dfrac{\kappa_i Q}{\pi(\kappa_1 + \kappa_2)aL}$, $-\dfrac{\kappa_i Q}{\pi(\kappa_1 + \kappa_2)bL}$ | OK |
| `P1B` | d) $\sigma_{b,i}(a)$, $\sigma_{b,i}(b)$, interface | $-\dfrac{(\kappa_i - 1)Q}{\pi(\kappa_1 + \kappa_2)aL}$, $+\dfrac{(\kappa_i - 1)Q}{\pi(\kappa_1 + \kappa_2)bL}$, $\sigma_b = 0$ (and $\rho_b = 0$) | $-\dfrac{(\kappa_i - 1)Q}{\pi(\kappa_1 + \kappa_2)aL}$, $+\dfrac{(\kappa_i - 1)Q}{\pi(\kappa_1 + \kappa_2)bL}$, $\sigma_b = 0$ ($\rho_b = 0$) | OK |
| `P1B` | d) $Q_{\text{sup}}$ ($\kappa_1=2, \kappa_2=4$) | $\dfrac{\kappa_1}{\kappa_1 + \kappa_2}Q = \dfrac{Q}{3}$ | $\dfrac{\kappa_1}{\kappa_1 + \kappa_2}Q = \dfrac{1}{3}Q$ | OK |
| `P1B` | `li.check` & points | Units $\text{F}, \text{C/m}^2$; $\kappa_1=\kappa_2=\kappa$ & $\kappa=1$ limits; total free charge $Q$; $2.5+1+1+1.5=6$ pts | All verified symbolically; step sum = $6.0$; score-box sum = $6.0$ | OK |
| `P2` | a) $\vec B(s)$ | $\dfrac{\mu_0 I}{2\pi s}$ (into page on the right) | $\dfrac{\mu_0 I}{2\pi s}$ azimuthal, $-\hat z$ (into page on the right) | OK |
| `P2` | b) $\Phi_B(x)$ | $\dfrac{\mu_0 I a}{2\pi}\ln\!\left(1 + \dfrac{a}{x}\right)$ ($\hat n$ into page) | $\dfrac{\mu_0 I a}{2\pi}\ln\!\left(1 + \dfrac{a}{x}\right)$ ($\hat n$ into page) | OK |
| `P2` | c) $\varepsilon$, $I_{\text{ind}}$, direction | $-\dfrac{\mu_0 I a^2 v}{2\pi x(x+a)}$, $\dfrac{\mu_0 I a^2 v}{2\pi R x(x+a)}$, antihoraria; $x=a$: $|\varepsilon| = 1{,}0\times 10^{-5}\ \text{V}$, $I_{\text{ind}} = 10\ \text{mA}$ | $-\dfrac{\mu_0 I a^2 v}{2\pi x(x+a)}$ ($\hat n$ into page), $\dfrac{\mu_0 I a^2 v}{2\pi R x(x+a)}$, CCW; $x=a$: $10^{-5}\ \text{V}$, $10^{-2}\ \text{A}$ | OK |
| `P2` | d) $\vec F_B$, $\vec F_{\text{ext}}$ | $\vec F_B = \dfrac{\mu_0^2 I^2 a^4 v}{4\pi^2 R x^2(x+a)^2}$ away from wire ($5{,}0\times 10^{-8}\ \text{N}$ at $x=a$); $\vec F_{\text{ext}} = -\vec F_B$ toward wire | $\vec F_B = \dfrac{\mu_0^2 I^2 a^4 v}{4\pi^2 R x^2(x+a)^2}\hat x$ away from wire ($5\times 10^{-8}\ \text{N}$ at $x=a$); $\vec F_{\text{ext}} = -\vec F_B$ toward wire | OK |
| `P2` | d) No $\vec F_{\text{ext}}$; parallel motion | Frena ($m\dot v = -F_B < 0$); $\varepsilon = 0$ | Decelerates; $\varepsilon = 0$ | OK |
| `P2` | `li.check` & points | Units $\text{T}, \text{V}, \text{N}$; $F_{\text{ext}}v = I_{\text{ind}}^2 R = 10^{-7}\ \text{W}$ at $x=a$; motional emf; $x\to\infty$; $1+1.5+2+1.5=6$ pts | All verified symbolically & numerically; step sum = $6.0$; score-box sum = $6.0$ | OK |
| `P3` | a) ODE, $\omega_0$, $\gamma$, regime, $q(t)$ | $L\ddot q + R\dot q + \frac{q}{C} = 0$, $\omega_0 = 1000\ \text{rad/s}$, $\gamma = 1000\ \text{s}^{-1}$, amortiguamiento crítico, $q(t) = Q_0(1+\gamma t)e^{-\gamma t}$ ($5{,}0(1+1000t)e^{-1000t}\ \text{mC}$ in Step 4) | $L\ddot q + R\dot q + \frac{q}{C} = 0$, $\omega_0 = 1000\ \text{rad/s}$, $\gamma = 1000\ \text{s}^{-1}$, critically damped, $q(t) = 0{,}005(1+1000t)e^{-1000t}\ \text{C}$ | OK |
| `P3` | b) $Z_{\text{eq}}$, $|Z_{\text{eq}}|$, $\hat I$, $i(t)$, lead/lag | $20 + 15j\ \Omega$, $25\ \Omega$, $\hat I = 2{,}0\,e^{-j\phi}\ \text{A}$ ($\tan\phi = 3/4$, $\phi \approx 37^\circ$), $i(t) = 2{,}0\cos(2000t - \phi)\ \text{A}$, atrasa | $20 + 15j\ \Omega$, $25\ \Omega$, $\hat I = 1{,}6 - 1{,}2j\ \text{A} = 2\,e^{-j\arctan(3/4)}\ \text{A}$, $i(t) = 1{,}6\cos(2000t) + 1{,}2\sin(2000t)\ \text{A}$, lags | OK |
| `P3` | c) $\omega_{\text{res}}$, $\langle P\rangle_{2000}$, $\langle P\rangle_{\text{res}}$ | $1000\ \text{rad/s}$, $40\ \text{W}$, $62{,}5\ \text{W}$ | $1000\ \text{rad/s}$, $40\ \text{W}$, $62{,}5\ \text{W}$ | OK |
| `P3` | `li.check` & points | Units $\text{s}^{-1}, \Omega$; under/overdamped limits; $q(\infty)=0, q(0)=Q_0$; $\omega<\omega_0$ leads; $40 = 62{,}5\cos^2\phi$; $2+2.5+1.5=6$ pts | All verified symbolically & numerically; step sum = $6.0$; score-box sum = $6.0$ | OK |

## ERRORS

None. All four problems (`P1A`, `P1B`, `P2`, `P3`) are physically well posed, self-contained without relying on the figures, hand-computable without a calculator, mathematically and physically consistent across statements, steps, `li.final`, and `li.check`, and have exact point-sum alignment (6 points per problem across statements, pauta steps, and `div.score-box` checkboxes).

## MINOR

1. **`P2` normal convention in `li.final` vs. statement:** The statement (`s01-enunciados`) asks for $\Phi_B(x)$ and the induced emf without fixing an orientation for the surface normal $\hat n$; the choice $\hat n$ into the page (clockwise positive circulation) is only declared in the pauta figure caption (`s01-p2` `<figcaption>`) and in Steps 2 and 4. In `li.final`, $\Phi_B = +\frac{\mu_0 I a}{2\pi}\ln(1 + a/x)$ and $\varepsilon = -\frac{\mu_0 I a^2 v}{2\pi x(x+a)}$ are written without restating "(con $\hat n$ entrante)". A student choosing $\hat n$ out of the page legitimately obtains the opposite signs for $\Phi_B$ and $\varepsilon$, while $|\varepsilon|$, $I_{\text{ind}}$, and the physical counterclockwise current direction are invariant.
2. **`P1B` part (d) wording in `li.final`:** Part (d) asks for "la carga ligada en la interfaz plana entre ellos" and "¿qué fracción de la carga libre $Q$ del conductor interno está en su mitad superior?". `li.final` reports $\sigma_b = 0$ on the planar interface (which immediately implies zero bound charge $q_b = 0$) and $Q_{\text{sup}} = \frac{\kappa_1}{\kappa_1 + \kappa_2}Q = \frac{Q}{3}$ (equivalent to the fraction $1/3$).
3. **`P3` part (a) symbolic-only $q(t)$ in `li.final`:** Step 4 gives both $Q_0(1+\gamma t)e^{-\gamma t}$ and the numerical form $5{,}0(1+1000t)e^{-1000t}\ \text{mC}$, whereas `li.final` writes only the symbolic form $q(t) = Q_0(1+\gamma t)e^{-\gamma t}$ (with $\gamma = 1000\ \text{s}^{-1}$ in the same box and $Q_0 = 5{,}0\ \text{mC}$ in the statement). This is valid under the exam's rule ("las respuestas simbólicas valen completas").
