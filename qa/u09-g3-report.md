# Gate G3 Physics Verification Report — U9 (`unidades/u09-induccion.html`)

**Scope:** Independent verification of `unidades/u09-induccion.html` (theory sections `u09-mapa`, `u09-s1`–`u09-s6`, 13 problems `u09-e1`–`u09-e4`, `u09-x1`–`u09-x4`, `u09-p1`–`u09-p5`, formula card `u09-formulas`, and quiz `u09-quiz`).  
**Tooling:** Python `/usr/bin/python3` with SymPy `1.12` (`/tmp/verify_u09.py`).  
**Conventions checked:** $\varepsilon = -N\,d\Phi_B/dt$ with $\hat n$ and positive circulation related by the right-hand rule; in `u09-x3`, $\hat x$ out of page, $\hat y$ right, $\hat z$ up; in `u09-x1`, `u09-x2`, `u09-e2`, `u09-p2`, `u09-p3` external $\vec B$ is into the page ($-\hat z$); in `u09-p4`, $\vec B_0$ is out of the page ($+\hat z$).

---

## Problem-by-Problem & Quantity Verification Table

| ID | quantity | guide value | your value | verdict OK/ERROR | note |
|---|---|---|---|---|---|
| `u09-e1` | $|\varepsilon|$ | $0{,}50\ \text{V}$ | $\frac{1}{2}\ \text{V} = 0{,}50\ \text{V}$ | OK | $\varphi = 90^\circ - 30^\circ = 60^\circ$, $\varepsilon = +0{,}50\ \text{V}$ |
| `u09-e1` | $I$ | $0{,}25\ \text{A}$ | $\frac{1}{4}\ \text{A} = 0{,}25\ \text{A}$ | OK | $I = |\varepsilon|/R = 0{,}50/2{,}0$ |
| `u09-e1` | sentido | refuerza a $\vec B$ dentro de la bobina | mismo sentido que $\vec B$ (RHR en torno a $\hat n$ paralela a $B_n$) | OK | $\Phi_B$ disminuye $\Rightarrow$ campo inducido a favor de $\vec B$ |
| `u09-e1` | `li.check` | $\text{T}\cdot\text{m}^2/\text{s}=\text{V}$; $\theta=0\Rightarrow\varepsilon=0$; $\cos30^\circ\Rightarrow0{,}87\ \text{V}$ | verificado ($\frac{\sqrt3}{2}\approx 0{,}8660\ \text{V}$) | OK | Todo correcto |
| `u09-e2` | $\varepsilon$ / $|\varepsilon|$ | $\varepsilon = 1{,}0\ \text{V}$ (`li.final`); $\varepsilon=-B\ell v$, $|\varepsilon|=1{,}0\ \text{V}$ (Paso 1) | $\varepsilon = -1\ \text{V}$ ($\hat n$ entrante), $|\varepsilon| = 1\ \text{V}$ | OK | `li.final` omite barras de módulo en $\varepsilon$ (ver MINOR) |
| `u09-e2` | $I$ y sentido | $0{,}50\ \text{A}$ (antihoraria) | $\frac{1}{2}\ \text{A}$, antihoraria | OK | Flujo entrante crece $\Rightarrow$ $B_{\text{ind}}$ saliente ($\varepsilon<0$ con $\hat n$ entrante) |
| `u09-e2` | $\vec F_B$ | $0{,}10\ \text{N}\leftarrow$ ($-I\ell B\hat x$) | $-\frac{1}{10}\hat x\ \text{N}$ ($0{,}10\ \text{N}$ izq.) | OK | $I\ell\hat y\times(-B\hat z) = -I\ell B\hat x$ |
| `u09-e2` | $\vec F_{\text{ext}}$ | $0{,}10\ \text{N}\rightarrow$ | $+\frac{1}{10}\hat x\ \text{N}$ ($0{,}10\ \text{N}$ der.) | OK | $\sum F = 0$ con $v$ constante |
| `u09-e2` | balance de potencia | $P_{\text{ext}} = P_R = 0{,}50\ \text{W}$ | $P_{\text{ext}} = \frac{1}{2}\ \text{W} = P_R$ | OK | Omitido en `li.final`, presente en Paso 4 y `li.check` |
| `u09-e2` | `li.check` | unidades $\text{V}, \text{N}$; $P_{\text{ext}}=P_R$; $R\to\infty\Rightarrow I=0, F_B=0$ | verificado | OK | Todo correcto |
| `u09-e3` | $v(t)$ | $v_0 e^{-t/\tau}$, $\tau = \frac{mR}{B^2\ell^2}$ | $v_0 \exp\!\left(-\frac{B^2\ell^2 t}{mR}\right)$ | OK | Solución exacta de $m\dot v = -\frac{B^2\ell^2}{R}v$, $v(0)=v_0$ |
| `u09-e3` | $x_{\text{total}}$ | $\frac{mRv_0}{B^2\ell^2}$ | $\frac{mRv_0}{B^2\ell^2}$ | OK | $\int_0^\infty v(t)\,dt$ |
| `u09-e3` | $Q_{\text{calor}}$ | $\frac{1}{2}mv_0^2$ | $\frac{1}{2}mv_0^2$ | OK | $\int_0^\infty I^2 R\,dt = \frac{1}{2}mv_0^2$ |
| `u09-e3` | `li.check` | $[\tau]=\text{s}$; $B\to0\Rightarrow\tau\to\infty, v=v_0$; $R\to0\Rightarrow\tau\to0$ | verificado | OK | Todo correcto |
| `u09-e4` | $\vec B$ (dentro) | $\mu_0 n I_0 \sin(\omega t)\,\hat z$ (Paso 1) | $\mu_0 n I_0 \sin(\omega t)\,\hat z$ | OK | Omitido en `li.final` (ver MINOR) |
| `u09-e4` | $\vec E(r<b)$ | $-\frac{\mu_0 n I_0\omega r}{2}\cos(\omega t)\,\hat\theta$ | $-\frac{\mu_0 n I_0\omega r}{2}\cos(\omega t)\,\hat\theta$ | OK | RHR: $\hat n = +\hat z$ con recorrido $+\hat\theta$ |
| `u09-e4` | $\vec E(r>b)$ | $-\frac{\mu_0 n I_0\omega b^2}{2r}\cos(\omega t)\,\hat\theta$ | $-\frac{\mu_0 n I_0\omega b^2}{2r}\cos(\omega t)\,\hat\theta$ | OK | Flujo encerrado constante $\pi b^2 B(t)$ |
| `u09-e4` | `li.check` | unidades $\text{V/m}$; continuidad en $r=b$; máx en $r=b, I=0$; Lenz | verificado | OK | `li.check` escribe magnitud en $r=b$ sin signo menos ni $\hat\theta$ (ver MINOR) |
| `u09-x1` | Etapa I ($\varepsilon, I$) | $\varepsilon = 0$, $I = 0$ | $\varepsilon = 0$, $I = 0$ | OK | $\Phi_B = 0$ |
| `u09-x1` | Etapa II ($\varepsilon, I$, sentido) | $\varepsilon = -Bav$, $I = \frac{Bav}{R}$ (antihoraria) | $\varepsilon = -Bav$ ($\hat n$ entrante), $I = \frac{Bav}{R}$, antihoraria | OK | Flujo entrante crece $\Rightarrow$ $B_{\text{ind}}$ saliente |
| `u09-x1` | Etapa III ($\varepsilon, I$) | $\varepsilon = 0$, $I = 0$ | $\varepsilon = 0$, $I = 0$ | OK | $\Phi_B = Ba^2$ constante |
| `u09-x1` | parte b ($\vec F_{\text{ext}}$) | hacia la derecha ($+\hat x$), $\frac{B^2 a^2 v}{R}$ | $\frac{B^2 a^2 v}{R}\hat x$ (hacia la derecha) | OK | $\vec F_B = -\frac{B^2 a^2 v}{R}\hat x$ |
| `u09-x1` | `li.check` | unidades; $F_{\text{ext}}v = I^2 R$; al salir $I$ horaria y frena | verificado | OK | Todo correcto |
| `u09-x2` | a) $B(s)$ | $\frac{\mu_0 I}{2\pi s}$ (entrante en el lazo) | $\frac{\mu_0 I}{2\pi s}$ | OK | Ley de Ampère en circunferencia de radio $s$ |
| `u09-x2` | b) $\Phi_B(r)$ | $\frac{\mu_0 I\ell}{2\pi}\ln\!\left(1+\frac{w}{r}\right)$ | $\frac{\mu_0 I\ell}{2\pi}\ln\!\left(\frac{r+w}{r}\right)$ | OK | Equivalente algebraico exacto ($\hat n$ entrante) |
| `u09-x2` | c) $\varepsilon$, $I_{\text{ind}}$, sentido | $\varepsilon=\frac{\mu_0 I\ell w v}{2\pi r(r+w)}$, $I_{\text{ind}}=\frac{\varepsilon}{R}$ (horaria) | $\varepsilon=\frac{\mu_0 I\ell w v}{2\pi r(r+w)}$, $I_{\text{ind}}=\frac{\mu_0 I\ell w v}{2\pi R r(r+w)}$, horaria | OK | Flujo entrante disminuye $\Rightarrow$ $B_{\text{ind}}$ entrante |
| `u09-x2` | `li.check` | cruce fem de mov. $\ell v[B(r)-B(r+w)]$; $r\to\infty\Rightarrow0$; $v=0\Rightarrow0$; unidades | verificado (diferencia simbólica $=0$) | OK | Todo correcto |
| `u09-x3` | a) $\Phi_B$ | $a^2 B_0 - \frac{1}{2}\alpha a^2(2z+a)$ | $a^2 B_0 - \frac{\alpha a^2(2z+a)}{2}$ | OK | Con $\hat n = +\hat x$ |
| `u09-x3` | b) $\varepsilon$, $I$ | $\varepsilon = -\alpha a^2|v|$, $I = \frac{\alpha a^2|v|}{R}$ | $\varepsilon = \alpha a^2 v_z = -\alpha a^2|v|$, $I = \frac{\alpha a^2|v|}{R}$ | OK | $v_z = -|v|<0$ al caer |
| `u09-x3` | c) sentido | horaria vista desde $+\hat x$ | horaria vista desde $+\hat x$ | OK | $z$ baja $\Rightarrow B_x$ sube $\Rightarrow B_{\text{ind}}$ en $-\hat x$ |
| `u09-x3` | d) $\vec F$ | $\vec F_B = \frac{\alpha^2 a^4|v|}{R}\hat z$, $\vec F_{\text{total}} = \left(\frac{\alpha^2 a^4|v|}{R}-mg\right)\hat z$ (Paso 4) | $\vec F_B = \frac{\alpha^2 a^4|v|}{R}\hat z$, $\vec F_{\text{total}} = \left(\frac{\alpha^2 a^4|v|}{R}-mg\right)\hat z$ | OK | Omitido de `li.final` (ver MINOR) |
| `u09-x3` | e) $|v_{\text{term}}|$ | $\frac{mgR}{\alpha^2 a^4}$ | $\frac{mgR}{\alpha^2 a^4}$ | OK | $F_{\text{total},z} = 0$ |
| `u09-x3` | `li.check` | $I^2R = mg v_{\text{term}}$; $\alpha\to0\Rightarrow v_{\text{term}}\to\infty$ | verificado | OK | Todo correcto |
| `u09-x4` | a) $\Phi(t)$ | $\frac{\mu_0 I R^2 \pi r^2}{2[R^2+(z-vt)^2]^{3/2}}$ | $\frac{\mu_0 I R^2 \pi r^2}{2[R^2+(z-vt)^2]^{3/2}}$ | OK | Con $\hat n$ concordante con $d\vec\ell$ (y con $I$) |
| `u09-x4` | b) $\varepsilon(t)$ | $-\frac{3\mu_0 I R^2 \pi r^2 v(z-vt)}{2[R^2+(z-vt)^2]^{5/2}}$ | $\frac{3\mu_0 I R^2 \pi r^2 v(vt-z)}{2[R^2+(z-vt)^2]^{5/2}}$ | OK | Equivalente exacto |
| `u09-x4` | c) sentido y $I_{\text{ind}}$ | izq.: opuesta a $d\vec\ell$; der.: igual a $d\vec\ell$; $I_{\text{ind}}(z/v)=0$, $I_{\text{ind}}(\infty)=0$ | $u>0\Rightarrow\varepsilon<0$ (opuesta); $u<0\Rightarrow\varepsilon>0$ (igual); $0$ y $0$ | OK | $I_{\text{ind}}=0$ en ambos casos límite sin requerir resistencia |
| `u09-x4` | `li.check` | unidades; $\varepsilon$ impar en $u=z-vt$ | verificado | OK | Todo correcto |
| `u09-p1` | $\varepsilon(t)$ | $20\sin(100\,t)\ \text{V}$ | $20\sin(100\,t)\ \text{V}$ | OK | $-N\frac{d}{dt}(BA\cos\omega t) = NBA\omega\sin\omega t$ |
| `u09-p1` | $\varepsilon_{\text{máx}}$ | $20\ \text{V}$ | $20\ \text{V}$ | OK | $10 \times 0{,}40 \times 0{,}05 \times 100$ |
| `u09-p1` | $I_{\text{máx}}$ | $5{,}0\ \text{A}$ | $5\ \text{A}$ | OK | $20 / 4{,}0$ |
| `u09-p1` | orientación | plano paralelo a $\vec B$ ($\Phi_B=0$, Paso 3) | $\omega t = \frac{\pi}{2} + k\pi$, plano paralelo a $\vec B$ | OK | Omitido en `li.final` (ver MINOR) |
| `u09-p1` | `li.check` | $\text{T}\cdot\text{m}^2\cdot\text{s}^{-1}=\text{V}$; $\omega\times2\Rightarrow\varepsilon\times2$; eje $\parallel\vec B\Rightarrow\varepsilon=0$ | verificado | OK | Todo correcto |
| `u09-p2` | $|\varepsilon|$ | $\frac{\mu_0\beta\ell}{2\pi}\ln\!\left(1+\frac{w}{r}\right)$ | $\frac{\mu_0\beta\ell}{2\pi}\ln\!\left(\frac{r+w}{r}\right)$ | OK | Equivalente exacto ($\varepsilon<0$ con $\hat n$ entrante) |
| `u09-p2` | $I_{\text{ind}}$ y sentido | $\frac{\mu_0\beta\ell}{2\pi R}\ln\!\left(1+\frac{w}{r}\right)$ (antihoraria) | $\frac{\mu_0\beta\ell}{2\pi R}\ln\!\left(\frac{r+w}{r}\right)$, antihoraria | OK | Flujo entrante crece $\Rightarrow$ $B_{\text{ind}}$ saliente |
| `u09-p2` | `li.check` | cte en $t$; unidades $\text{V}$; límite $w\ll r\Rightarrow \frac{\mu_0\beta}{2\pi r}\ell w$ | verificado (serie Taylor a orden 1 en $w$) | OK | Todo correcto |
| `u09-p3` | $v_{\text{term}}$ | $\frac{mgR}{B^2 a^2}$ | $\frac{mgR}{B^2 a^2}$ | OK | Equilibrio $mg = \frac{B^2 a^2}{R}v_{\text{term}}$ |
| `u09-p3` | $v(t)$ | $v_{\text{term}}(1-e^{-t/\tau})$, $\tau=\frac{mR}{B^2 a^2}$ | $\frac{mgR}{B^2 a^2}\left(1 - e^{-\frac{B^2 a^2 t}{mR}}\right)$ | OK | Solución exacta de $m\dot v = mg - \frac{B^2 a^2}{R}v$, $v(0)=0$ |
| `u09-p3` | sentido | antihoraria | antihoraria | OK | Flujo entrante crece $\Rightarrow$ $B_{\text{ind}}$ saliente |
| `u09-p3` | `li.check` | $mg v_{\text{term}} = I^2 R$; unidades $\text{m/s}$; $B\to0\Rightarrow$ caída libre | verificado ($\lim_{B\to0}v(t)=gt$) | OK | Todo correcto |
| `u09-p4` | $v(t)$ | $\frac{V_0}{B_0 b}(1-e^{-t/\tau})$, $\tau=\frac{mR}{B_0^2 b^2}$ | $\frac{V_0}{B_0 b}\left(1 - e^{-\frac{B_0^2 b^2 t}{mR}}\right)$ | OK | $m\dot v = \frac{B_0 b}{R}(V_0 - B_0 b v)$, $v(0)=0$ |
| `u09-p4` | $v_\infty$ | $\frac{V_0}{B_0 b}$ | $\frac{V_0}{B_0 b}$ | OK | $\lim_{t\to\infty} v(t)$ |
| `u09-p4` | $I(\infty)$ y explicación | $0$; $B_0 b v_\infty = V_0$ cancela batería | $0$; fem inducida iguala $V_0$, fuerza neta nula | OK | Sin roce mantiene $v_\infty$ con $I=0$ |
| `u09-p4` | `li.check` | unidades $\text{m/s}$; mayor $B_0\Rightarrow$ menor $v_\infty$; $t=0\Rightarrow I=V_0/R$ | verificado | OK | Todo correcto |
| `u09-p5` | $I_D$ | $i$ | $i$ | OK | $\varepsilon_0 \frac{d}{dt}(q/\varepsilon_0) = \dot q = i$ |
| `u09-p5` | $B(r<R)$ | $\frac{\mu_0 i r}{2\pi R^2}$ | $\frac{\mu_0 i r}{2\pi R^2}$ | OK | $I_{D,\text{enc}} = i r^2/R^2$ |
| `u09-p5` | $B(r>R)$ | $\frac{\mu_0 i}{2\pi r}$ | $\frac{\mu_0 i}{2\pi r}$ | OK | $I_{D,\text{enc}} = i$ |
| `u09-p5` | $B(R/2)$ | $\frac{\mu_0 i}{4\pi R}$ | $\frac{\mu_0 i}{4\pi R}$ | OK | Sustitución directa |
| `u09-p5` | `li.check` | continuidad en $r=R$ ($\frac{\mu_0 i}{2\pi R}$, máx); $B(0)=0$; unidades $\text{T}$ | verificado | OK | Todo correcto |

---

## Theory, Formula Card & Quiz Audit

| Section / Item | Result | Verdict | Notes |
|---|---|---|---|
| `u09-s1` Flux of infinite wire through coplanar rectangle | $\Phi_B = \frac{\mu_0 I\ell}{2\pi}\ln\left(\frac{r+w}{r}\right)$; limit $w\ll r \Rightarrow B(r)\ell w$ | OK | Verified symbolically & by series expansion |
| `u09-s3` Terminal velocity & braking formulas | $v(t)=v_0 e^{-t/\tau}$, $x_{\text{tot}}=v_0\tau$, $v_{\text{term}}=\frac{FR}{B^2\ell^2}$, $v(t)=v_{\text{term}}(1-e^{-t/\tau})$, $[\tau]=\text{s}$ | OK | Verified by `dsolve`, integration, and SI dimensional analysis |
| `u09-s4` Induced $E$ inside/outside solenoid | $E = \frac{r}{2}|dB/dt|$ ($r<b$), $E = \frac{b^2}{2r}|dB/dt|$ ($r>b$), continuous at $r=b$ | OK | Verified symbolically; direction CCW for growing inward $B$ |
| `u09-s6` Displacement current & $B$ between circular plates | $I_D = \varepsilon_0\frac{d\Phi_E}{dt} = i$; $B=\frac{\mu_0 i r}{2\pi R^2}$ ($r<R$), $\frac{\mu_0 i}{2\pi r}$ ($r>R$) | OK | Verified symbolically; continuous at $r=R$ |
| `u09-formulas` (15 rows) | All 15 formulas and validity conditions consistent with theory | OK | Minor phrasing note on last row (`campo uniforme entre ellas` refers to $\vec E$) |
| `u09-quiz` Q1–Q7 | `Q1:c`, `Q2:a`, `Q3:b`, `Q4:c`, `Q5:a`, `Q6:b`, `Q7:c` | OK | All `data-correct` keys and all 21 option feedback texts (`p.fb`) are physically accurate |

---

## ERRORS

No real physics or mathematics errors were found in `unidades/u09-induccion.html`. All symbolic derivatives, integrals, ODE solutions, cross products, signs (right-hand rule / Lenz's law), numerical evaluations, unit checks, limiting cases, formula card entries, and quiz answers match independent verification.

---

## MINOR

1. **`u09-e1` (`div.predict`, line 199):** Spanish conjunction typo: `"¿qué ángulo va en el coseno de $\Phi_B = BA\cos\varphi$, el de $30^\circ$ o otro?"` — `"o otro"` should be `"u otro"`.
2. **`u09-e2` (`li.final`, line 228):** Writes `$\varepsilon = 1{,}0\ \text{V}$` without absolute value bars, whereas Paso 1 (line 224) writes `$\varepsilon = -\dfrac{d}{dt}(B\ell x) = -B\ell v$` (negative with $\hat n$ into the page) and `$|\varepsilon| = B\ell v = \dots = 1{,}0\ \text{V}$` (contrast with `u09-e1` and `u09-p2` which write `$|\varepsilon|$` in `li.final`, and `u09-x1` which writes `$\varepsilon = -Bav$`). Also, the requested power balance (`"y comprueba el balance de potencia"`) is shown in Paso 4 and `li.check` rather than in `li.final`.
3. **`u09-e4` (`li.final` & `li.check`, lines 271–272):** The statement asks for both the magnetic field inside and the induced electric field (`"Encuentra el campo magnético dentro del solenoide y el campo eléctrico inducido dentro ($r \lt b$) y fuera ($r \gt b$)."`), while `li.final` only boxes $\vec E$ and omits `$\vec B = \mu_0 n I_0\sin(\omega t)\,\hat z$` (computed in Paso 1). In `li.check`, `"Continuidad: en $r = b$ ambas dan $\tfrac{b}{2}\mu_0 nI_0\omega\cos\omega t$."` drops the minus sign and $\hat\theta$ (stating only the coefficient/amplitude).
4. **`u09-x2` (`p.stmt`, line 309):** The statement text alone does not specify the sense of $I$ in the wire or which side the loop is on (`"alejándose de un alambre recto infinitamente largo que lleva una corriente $I$, en el plano del lazo"`), relying on the associated figure (`u09-alambre-espira`) to fix $\vec B$ into the page and hence the clockwise (`"horaria"`) current direction.
5. **`u09-x3` (`li.final`, line 344):** Part d) asks for `"la fuerza que experimenta la espira"`, which is derived in Paso 4 ($\vec F_{\text{mag}} = \frac{\alpha^2 a^4|v|}{R}\hat z$ and $\vec F_{\text{total}} = (\frac{\alpha^2 a^4|v|}{R} - mg)\hat z$), but omitted from the `li.final` box; additionally, `li.final` boxes `$\varepsilon = -\alpha a^2|v|$` without restating the chosen normal $\hat n = +\hat x$ inside the box.
6. **`u09-x4` (`p.stmt` & Paso 4, lines 354, 365):** Notation overload of $z$: `"se le acerca con velocidad constante $\vec v = v\hat z$ ... En $t = 0$ la distancia entre ambas es $z$."` uses $z$ as the positive initial separation while $\hat z$ is the coordinate unit vector. Also, part c) asks for $I_{\text{ind}}$ without defining a resistance symbol for the small loop (harmless since $\varepsilon = 0$ at $t=z/v$ and $t\to+\infty$ for any nonzero resistance). In Paso 4, `"el numerador crece como $u$"` refers to $|u|$ growing ($u = z - vt \to -\infty$).
7. **`u09-p1` (`li.final`, line 403):** The statement asks `"e indica en qué orientación ocurre la fem máxima"`, which is answered in Paso 3 (`"el plano de la bobina es paralelo al campo y el flujo es cero"`), but omitted from `li.final`.
8. **`u09-p2` (`p.stmt`, line 413):** The dimensions $\ell$ and $w$ are not introduced in the wording of `p.stmt` (`"La espira rectangular de la figura está en reposo, con su lado cercano a distancia $r$ de un alambre infinito."`), appearing only in `div.given` and in the shared `u09-alambre-espira` figure caption.
9. **`u09-p3` (`figcaption` & Paso 3, lines 437, 444):** Notation overload between `$y$` in the caption (`"$y$ es la longitud de la espira que ya está dentro del campo"`, measured downward) and `$\hat y$` in Paso 3 (`"$\vec F = Ia\,\hat x\times(-B\hat z) = IaB\,\hat y$, hacia arriba"`), where $\hat y$ points upward. The vector algebra and physical result are correct.
10. **`u09-formulas` (line 555):** In `"Placas de radio $R$, campo uniforme entre ellas"`, writing `"campo eléctrico uniforme entre ellas"` would avoid ambiguity with $\vec B$ (which depends on $r$).

---

## SymPy Verification Code & Output

Script run: `/usr/bin/python3 /tmp/verify_u09.py`

```python
import sympy as sp

print("SymPy version:", sp.__version__)

# ==============================================================================
# 0. DIMENSIONAL ANALYSIS HELPER (SI base: kg, m, s, A)
# ==============================================================================
kg, m_u, s_u, A_u = sp.symbols("kg m s A", positive=True)
N_u = kg * m_u / s_u**2
J_u = N_u * m_u
W_u = J_u / s_u
C_u = A_u * s_u
V_u = J_u / C_u
Wb_u = V_u * s_u
T_u = Wb_u / m_u**2
Ohm_u = V_u / A_u
mu0_u = T_u * m_u / A_u
eps0_u = C_u**2 / (N_u * m_u**2)

print("\n=== UNIT CHECKS ===")
print("T * m^2 / s == V:", sp.simplify(T_u * m_u**2 / s_u / V_u) == 1)
print("T * m * (m/s) == V:", sp.simplify(T_u * m_u * (m_u / s_u) / V_u) == 1)
print("A * m * T == N:", sp.simplify(A_u * m_u * T_u / N_u) == 1)
print("tau = kg*Ohm/(T^2*m^2) == s:", sp.simplify((kg * Ohm_u / (T_u**2 * m_u**2)) / s_u) == 1)
print("T * s^-1 * m == V/m:", sp.simplify((T_u * s_u**-1 * m_u) / (V_u / m_u)) == 1)
print("mu0 * (A/s) * m == V:", sp.simplify((mu0_u * (A_u / s_u) * m_u) / V_u) == 1)
print("v_term = kg*(m/s^2)*Ohm/(T^2*m^2) == m/s:", sp.simplify((kg * (m_u / s_u**2) * Ohm_u / (T_u**2 * m_u**2)) / (m_u / s_u)) == 1)
print("v_inf = V/(T*m) == m/s:", sp.simplify((V_u / (T_u * m_u)) / (m_u / s_u)) == 1)
print("B_cap = mu0*A/m == T:", sp.simplify((mu0_u * A_u / m_u) / T_u) == 1)
print("eps0 * dPhi_E/dt == A:", sp.simplify((eps0_u * (V_u * m_u) / s_u) / A_u) == 1)

# ==============================================================================
# 1. THEORY FORMULAS
# ==============================================================================
print("\n=== THEORY FORMULAS ===")
mu0, I, l, w, r, s, t = sp.symbols("mu0 I l w r s t", positive=True)
Phi_wire = sp.integrate(mu0 * I / (2 * sp.pi * s) * l, (s, r, r + w))
print("Theory wire flux:", sp.simplify(Phi_wire))
print("Theory wire flux (w<<r series):", sp.series(Phi_wire, w, 0, 2))

b_sol, B0 = sp.symbols("b_sol B0", positive=True)
B_t = sp.Function("B")(t)
r_cyl = sp.symbols("r_cyl", positive=True)
E_in = -sp.diff(B_t * sp.pi * r_cyl**2, t) / (2 * sp.pi * r_cyl)
E_out = -sp.diff(B_t * sp.pi * b_sol**2, t) / (2 * sp.pi * r_cyl)
print("Theory solenoid E_in:", sp.simplify(E_in))
print("Theory solenoid E_out:", sp.simplify(E_out))
print("Continuity at r=b:", sp.simplify(E_in.subs(r_cyl, b_sol) - E_out.subs(r_cyl, b_sol)))

eps0, R_cap, i_curr = sp.symbols("eps0 R_cap i_curr", positive=True)
q_t = sp.Function("q")(t)
E_cap = q_t / (eps0 * sp.pi * R_cap**2)
Phi_E_tot = E_cap * sp.pi * R_cap**2
I_D_tot = eps0 * sp.diff(Phi_E_tot, t)
print("Theory I_D total:", I_D_tot)
Phi_E_r = E_cap * sp.pi * r_cyl**2
I_D_enc = eps0 * sp.diff(Phi_E_r, t).subs(sp.diff(q_t, t), i_curr)
B_cap_in = mu0 * I_D_enc / (2 * sp.pi * r_cyl)
B_cap_out = mu0 * i_curr / (2 * sp.pi * r_cyl)
print("Theory B_cap (r<R):", B_cap_in)
print("Theory B_cap (r>R):", B_cap_out)
print("Continuity at r=R:", sp.simplify(B_cap_in.subs(r_cyl, R_cap) - B_cap_out.subs(r_cyl, R_cap)))

m, R_res, B_sym, F_const = sp.symbols("m R_res B_sym F_const", positive=True)
v_fn = sp.Function("v")
ode_term = sp.Eq(m * sp.diff(v_fn(t), t), F_const - B_sym**2 * l**2 / R_res * v_fn(t))
sol_term = sp.dsolve(ode_term, v_fn(t), ics={v_fn(0): 0})
print("Theory terminal velocity ODE sol:", sp.simplify(sol_term))
print("Theory v_term (t->inf):", sp.limit(sol_term.rhs, t, sp.oo))

# ==============================================================================
# 2. PROBLEMS
# ==============================================================================

# --- u09-e1 ---
print("\n=== u09-e1 ===")
N_e1 = 200
side_e1 = sp.Rational(10, 100)
A_e1 = side_e1**2
theta_e1 = 30 * sp.pi / 180
phi_e1 = sp.pi / 2 - theta_e1
dBdt_e1 = sp.Rational(-1, 2)
R_e1 = sp.Rational(2, 1)
dPhidt_e1 = A_e1 * sp.cos(phi_e1) * dBdt_e1
eps_e1 = -N_e1 * dPhidt_e1
I_e1 = abs(eps_e1) / R_e1
eps_e1_wrong30 = abs(-N_e1 * A_e1 * sp.cos(theta_e1) * dBdt_e1)
print(f"e1: dPhi/dt = {dPhidt_e1} = {float(dPhidt_e1)}, eps = {eps_e1} V, I = {I_e1} A")
print(f"e1 wrong cos30 check: {float(eps_e1_wrong30):.4f} V")

# --- u09-e2 ---
print("\n=== u09-e2 ===")
l_e2 = sp.Rational(4, 10)
R_e2 = sp.Rational(2, 1)
B_e2 = sp.Rational(1, 2)
v_e2 = sp.Rational(5, 1)
x_t = v_e2 * t
Phi_e2 = B_e2 * l_e2 * x_t  # n into page
eps_e2 = -sp.diff(Phi_e2, t)
I_e2 = abs(eps_e2) / R_e2
F_B_e2_vec = I_e2 * sp.Matrix([0, l_e2, 0]).cross(sp.Matrix([0, 0, -B_e2]))
F_ext_e2_vec = -F_B_e2_vec
P_ext_e2 = F_ext_e2_vec.dot(sp.Matrix([v_e2, 0, 0]))
P_R_e2 = I_e2**2 * R_e2
print(f"e2: eps = {eps_e2} V, |eps| = {abs(eps_e2)} V, I = {I_e2} A")
print(f"e2: F_B = {F_B_e2_vec.T} N, F_ext = {F_ext_e2_vec.T} N")
print(f"e2: P_ext = {P_ext_e2} W, P_R = {P_R_e2} W")

# --- u09-e3 ---
print("\n=== u09-e3 ===")
v0 = sp.symbols("v0", positive=True)
ode_e3 = sp.Eq(m * sp.diff(v_fn(t), t), -B_sym**2 * l**2 / R_res * v_fn(t))
sol_e3 = sp.dsolve(ode_e3, v_fn(t), ics={v_fn(0): v0})
v_e3 = sol_e3.rhs
x_tot_e3 = sp.integrate(v_e3, (t, 0, sp.oo))
P_R_e3 = (B_sym * l * v_e3)**2 / R_res
Q_e3 = sp.integrate(P_R_e3, (t, 0, sp.oo))
print("e3: v(t) =", sp.simplify(v_e3))
print("e3: x_total =", sp.simplify(x_tot_e3))
print("e3: Q_calor =", sp.simplify(Q_e3))
print("e3 limit B->0 of v(t):", sp.limit(v_e3, B_sym, 0))
print("e3 limit R->0 of tau:", sp.limit(m * R_res / (B_sym**2 * l**2), R_res, 0))

# --- u09-e4 ---
print("\n=== u09-e4 ===")
n_turn, I0, omega, b_e4, r_e4 = sp.symbols("n I0 omega b r", positive=True)
B_e4 = mu0 * n_turn * I0 * sp.sin(omega * t)  # along +z inside
Phi_in_e4 = B_e4 * sp.pi * r_e4**2
E_theta_in_e4 = -sp.diff(Phi_in_e4, t) / (2 * sp.pi * r_e4)
Phi_out_e4 = B_e4 * sp.pi * b_e4**2
E_theta_out_e4 = -sp.diff(Phi_out_e4, t) / (2 * sp.pi * r_e4)
print("e4: B_inside (z-comp) =", B_e4)
print("e4: E_theta (r<b) =", sp.simplify(E_theta_in_e4))
print("e4: E_theta (r>b) =", sp.simplify(E_theta_out_e4))
print("e4 continuity at r=b:", sp.simplify(E_theta_in_e4.subs(r_e4, b_e4) - E_theta_out_e4.subs(r_e4, b_e4)))

# --- u09-x1 ---
print("\n=== u09-x1 ===")
a_x1, v_x1 = sp.symbols("a v", positive=True)
x_imm = v_x1 * t
Phi_I = sp.Integer(0)
Phi_II = B_sym * a_x1 * x_imm
eps_II = -sp.diff(Phi_II, t)
I_II = abs(eps_II) / R_res
F_B_x1 = I_II * sp.Matrix([0, a_x1, 0]).cross(sp.Matrix([0, 0, -B_sym]))
F_ext_x1 = -F_B_x1
Phi_III = B_sym * a_x1**2
eps_III = -sp.diff(Phi_III, t)
print("x1 Stage I: eps =", -sp.diff(Phi_I, t))
print("x1 Stage II: eps =", eps_II, ", I =", I_II, ", F_B =", F_B_x1.T, ", F_ext =", F_ext_x1.T)
print("x1 Stage III: eps =", eps_III)
print("x1 Power check:", sp.simplify(F_ext_x1.dot(sp.Matrix([v_x1, 0, 0])) - I_II**2 * R_res))

# --- u09-x2 ---
print("\n=== u09-x2 ===")
v_x2 = sp.symbols("v", positive=True)
r_fn = sp.Function("r")(t)
B_wire = mu0 * I / (2 * sp.pi * s)
Phi_x2_r = sp.integrate(B_wire * l, (s, r, r + w))
Phi_x2_t = Phi_x2_r.subs(r, r_fn)
eps_x2 = -sp.diff(Phi_x2_t, t).subs(sp.diff(r_fn, t), v_x2).subs(r_fn, r)
I_x2 = eps_x2 / R_res
eps_x2_motional = l * v_x2 * (B_wire.subs(s, r) - B_wire.subs(s, r + w))
print("x2: B(s) =", B_wire)
print("x2: Phi_B(r) =", sp.simplify(Phi_x2_r))
print("x2: eps =", sp.simplify(eps_x2))
print("x2: I_ind =", sp.simplify(I_x2))
print("x2 motional cross-check diff =", sp.simplify(eps_x2 - eps_x2_motional))
print("x2 limit r->oo of eps:", sp.limit(eps_x2, r, sp.oo))

# --- u09-x3 ---
print("\n=== u09-x3 ===")
alpha, g_sym, z_var, zp = sp.symbols("alpha g z zp", positive=True)
v_abs = sp.symbols("v_abs", positive=True)
z_t = sp.Function("z")(t)
Phi_x3 = sp.integrate(sp.integrate(B0 - alpha * zp, (zp, z_var, z_var + a_x1)), (s, 0, a_x1))
eps_x3 = -sp.diff(Phi_x3.subs(z_var, z_t), t)
v_z = sp.symbols("v_z", real=True)
eps_x3_vz = sp.simplify(eps_x3.subs(sp.diff(z_t, t), v_z))
eps_x3_fall = sp.simplify(eps_x3_vz.subs(v_z, -v_abs))
I_x3 = abs(eps_x3_fall) / R_res
F_top = I_x3 * sp.Matrix([0, a_x1, 0]).cross(sp.Matrix([B0 - alpha * (z_var + a_x1), 0, 0]))
F_bot = I_x3 * sp.Matrix([0, -a_x1, 0]).cross(sp.Matrix([B0 - alpha * z_var, 0, 0]))
F_right = I_x3 * sp.integrate(sp.Matrix([0, 0, -1]).cross(sp.Matrix([B0 - alpha * zp, 0, 0])), (zp, z_var, z_var + a_x1))
F_left = I_x3 * sp.integrate(sp.Matrix([0, 0, 1]).cross(sp.Matrix([B0 - alpha * zp, 0, 0])), (zp, z_var, z_var + a_x1))
F_B_net = sp.simplify(F_top + F_bot + F_right + F_left)
F_tot_x3 = F_B_net + sp.Matrix([0, 0, -m * g_sym])
v_term_x3 = sp.solve(F_tot_x3[2], v_abs)[0]
print("x3: Phi_B =", sp.factor(Phi_x3))
print("x3: eps(v_z) =", eps_x3_vz)
print("x3: eps(falling, |v|) =", eps_x3_fall)
print("x3: I =", I_x3)
print("x3: F_B_net =", F_B_net.T)
print("x3: F_total =", F_tot_x3.T)
print("x3: |v_term| =", v_term_x3)
print("x3 power check (I^2*R - m*g*v_term):", sp.simplify((I_x3**2 * R_res - m * g_sym * v_abs).subs(v_abs, v_term_x3)))
print("x3 limit alpha->0 of |v_term|:", sp.limit(v_term_x3, alpha, 0))

# --- u09-x4 ---
print("\n=== u09-x4 ===")
r_sm, R_lg, z_init = sp.symbols("r_sm R_lg z_init", positive=True)
v_x4 = sp.symbols("v", positive=True)
d_t = z_init - v_x4 * t
B_axis_x4 = mu0 * I * R_lg**2 / (2 * (R_lg**2 + d_t**2)**sp.Rational(3, 2))
Phi_x4 = B_axis_x4 * sp.pi * r_sm**2
eps_x4 = sp.simplify(-sp.diff(Phi_x4, t))
print("x4: Phi(t) =", Phi_x4)
print("x4: eps(t) =", eps_x4)
print("x4: eps at t=z/v:", eps_x4.subs(t, z_init / v_x4))
print("x4: eps as t->oo:", sp.limit(eps_x4, t, sp.oo))

# --- u09-p1 ---
print("\n=== u09-p1 ===")
N_p1 = 10
A_p1 = sp.Rational(5, 100)
omega_p1 = 100
B_p1 = sp.Rational(4, 10)
R_p1 = 4
Phi_p1 = B_p1 * A_p1 * sp.cos(omega_p1 * t)
eps_p1 = -N_p1 * sp.diff(Phi_p1, t)
eps_max_p1 = N_p1 * B_p1 * A_p1 * omega_p1
I_max_p1 = eps_max_p1 / R_p1
print("p1: eps(t) =", eps_p1, "V")
print("p1: eps_max =", eps_max_p1, "V, I_max =", I_max_p1, "A")

# --- u09-p2 ---
print("\n=== u09-p2 ===")
beta = sp.symbols("beta", positive=True)
Phi_p2 = sp.integrate(mu0 * (beta * t) / (2 * sp.pi * s) * l, (s, r, r + w))
eps_p2 = -sp.diff(Phi_p2, t)
I_p2 = abs(eps_p2) / R_res
print("p2: Phi(t) =", sp.simplify(Phi_p2))
print("p2: eps =", sp.simplify(eps_p2))
print("p2: I_ind =", sp.simplify(I_p2))
print("p2 limit w<<r:", sp.series(abs(eps_p2), w, 0, 2))

# --- u09-p3 ---
print("\n=== u09-p3 ===")
y_t = sp.Function("y")(t)
Phi_p3 = B_sym * a_x1 * y_t
eps_p3 = -sp.diff(Phi_p3, t)
F_bot_p3 = (B_sym * a_x1 * v_fn(t) / R_res) * sp.Matrix([a_x1, 0, 0]).cross(sp.Matrix([0, 0, -B_sym]))
print("p3: F_bot (in x-right, y-up, z-out) =", F_bot_p3.T)
ode_p3 = sp.Eq(m * sp.diff(v_fn(t), t), m * g_sym - B_sym**2 * a_x1**2 / R_res * v_fn(t))
sol_p3 = sp.dsolve(ode_p3, v_fn(t), ics={v_fn(0): 0})
v_term_p3 = sp.limit(sol_p3.rhs, t, sp.oo)
print("p3: v(t) =", sp.simplify(sol_p3.rhs))
print("p3: v_term =", v_term_p3)
print("p3 limit B->0 of v(t):", sp.limit(sol_p3.rhs, B_sym, 0))
print("p3 power check:", sp.simplify(m * g_sym * v_term_p3 - (B_sym * a_x1 * v_term_p3)**2 / R_res))

# --- u09-p4 ---
print("\n=== u09-p4 ===")
V0, b_p4 = sp.symbols("V0 b", positive=True)
I_p4 = (V0 - B0 * b_p4 * v_fn(t)) / R_res
ode_p4 = sp.Eq(m * sp.diff(v_fn(t), t), I_p4 * b_p4 * B0)
sol_p4 = sp.dsolve(ode_p4, v_fn(t), ics={v_fn(0): 0})
v_inf_p4 = sp.limit(sol_p4.rhs, t, sp.oo)
I_inf_p4 = sp.limit(I_p4.subs(v_fn(t), sol_p4.rhs), t, sp.oo)
print("p4: v(t) =", sp.simplify(sol_p4.rhs))
print("p4: v_inf =", v_inf_p4)
print("p4: I(t->inf) =", I_inf_p4)
print("p4: I(0) =", I_p4.subs(v_fn(t), sol_p4.rhs.subs(t, 0)))

# --- u09-p5 ---
print("\n=== u09-p5 ===")
print("p5: I_D =", I_D_tot.subs(sp.diff(q_t, t), i_curr))
print("p5: B(r<R) =", B_cap_in)
print("p5: B(r>R) =", B_cap_out)
print("p5: B(R/2) =", B_cap_in.subs(r_cyl, R_cap / 2))
print("p5 continuity at r=R:", sp.simplify(B_cap_in.subs(r_cyl, R_cap) - B_cap_out.subs(r_cyl, R_cap)))
```

### Output

```text
SymPy version: 1.12

=== UNIT CHECKS ===
T * m^2 / s == V: True
T * m * (m/s) == V: True
A * m * T == N: True
tau = kg*Ohm/(T^2*m^2) == s: True
T * s^-1 * m == V/m: True
mu0 * (A/s) * m == V: True
v_term = kg*(m/s^2)*Ohm/(T^2*m^2) == m/s: True
v_inf = V/(T*m) == m/s: True
B_cap = mu0*A/m == T: True
eps0 * dPhi_E/dt == A: True

=== THEORY FORMULAS ===
Theory wire flux: log(((r + w)/r)**(I*l*mu0/(2*pi)))
Theory wire flux (w<<r series): I*l*mu0*w/(2*pi*r) + O(w**2)
Theory solenoid E_in: -r_cyl*Derivative(B(t), t)/2
Theory solenoid E_out: -b_sol**2*Derivative(B(t), t)/(2*r_cyl)
Continuity at r=b: 0
Theory I_D total: Derivative(q(t), t)
Theory B_cap (r<R): i_curr*mu0*r_cyl/(2*pi*R_cap**2)
Theory B_cap (r>R): i_curr*mu0/(2*pi*r_cyl)
Continuity at r=R: 0
Theory terminal velocity ODE sol: Eq(v(t), F_const*R_res/(B_sym**2*l**2) - F_const*R_res*exp(-B_sym**2*l**2*t/(R_res*m))/(B_sym**2*l**2))
Theory v_term (t->inf): F_const*R_res/(B_sym**2*l**2)

=== u09-e1 ===
e1: dPhi/dt = -1/400 = -0.0025, eps = 1/2 V, I = 1/4 A
e1 wrong cos30 check: 0.8660 V

=== u09-e2 ===
e2: eps = -1 V, |eps| = 1 V, I = 1/2 A
e2: F_B = Matrix([[-1/10, 0, 0]]) N, F_ext = Matrix([[1/10, 0, 0]]) N
e2: P_ext = 1/2 W, P_R = 1/2 W

=== u09-e3 ===
e3: v(t) = v0*exp(-B_sym**2*l**2*t/(R_res*m))
e3: x_total = R_res*m*v0/(B_sym**2*l**2)
e3: Q_calor = m*v0**2/2
e3 limit B->0 of v(t): v0
e3 limit R->0 of tau: 0

=== u09-e4 ===
e4: B_inside (z-comp) = I0*mu0*n*sin(omega*t)
e4: E_theta (r<b) = -I0*mu0*n*omega*r*cos(omega*t)/2
e4: E_theta (r>b) = -I0*b**2*mu0*n*omega*cos(omega*t)/(2*r)
e4 continuity at r=b: 0

=== u09-x1 ===
x1 Stage I: eps = 0
x1 Stage II: eps = -B_sym*a*v , I = B_sym*a*v/R_res , F_B = Matrix([[-B_sym**2*a**2*v/R_res, 0, 0]]) , F_ext = Matrix([[B_sym**2*a**2*v/R_res, 0, 0]])
x1 Stage III: eps = 0
x1 Power check: 0

=== u09-x2 ===
x2: B(s) = I*mu0/(2*pi*s)
x2: Phi_B(r) = log(((r + w)/r)**(I*l*mu0/(2*pi)))
x2: eps = I*l*mu0*v*w/(2*pi*r*(r + w))
x2: I_ind = I*l*mu0*v*w/(2*pi*R_res*r*(r + w))
x2 motional cross-check diff = 0
x2 limit r->oo of eps: 0

=== u09-x3 ===
x3: Phi_B = -a**2*(-2*B0 + a*alpha + 2*alpha*z)/2
x3: eps(v_z) = a**2*alpha*v_z
x3: eps(falling, |v|) = -a**2*alpha*v_abs
x3: I = a**2*alpha*v_abs/R_res
x3: F_B_net = Matrix([[0, 0, a**4*alpha**2*v_abs/R_res]])
x3: F_total = Matrix([[0, 0, -g*m + a**4*alpha**2*v_abs/R_res]])
x3: |v_term| = R_res*g*m/(a**4*alpha**2)
x3 power check (I^2*R - m*g*v_term): 0
x3 limit alpha->0 of |v_term|: oo

=== u09-x4 ===
x4: Phi(t) = pi*I*R_lg**2*mu0*r_sm**2/(2*(R_lg**2 + (-t*v + z_init)**2)**(3/2))
x4: eps(t) = 3*pi*I*R_lg**2*mu0*r_sm**2*v*(t*v - z_init)/(2*(R_lg**2 + (t*v - z_init)**2)**(5/2))
x4: eps at t=z/v: 0
x4: eps as t->oo: 0

=== u09-p1 ===
p1: eps(t) = 20*sin(100*t) V
p1: eps_max = 20 V, I_max = 5 A

=== u09-p2 ===
p2: Phi(t) = log(((r + w)/r)**(beta*l*mu0*t/(2*pi)))
p2: eps = log((r/(r + w))**(beta*l*mu0/(2*pi)))
p2: I_ind = beta*l*mu0*Abs(log(r/(r + w)))/(2*pi*R_res)
p2 limit w<<r: beta*l*mu0*w/(2*pi*r) + O(w**2)

=== u09-p3 ===
p3: F_bot (in x-right, y-up, z-out) = Matrix([[0, B_sym**2*a**2*v(t)/R_res, 0]])
p3: v(t) = R_res*g*m/(B_sym**2*a**2) - R_res*g*m*exp(-B_sym**2*a**2*t/(R_res*m))/(B_sym**2*a**2)
p3: v_term = R_res*g*m/(B_sym**2*a**2)
p3 limit B->0 of v(t): g*t
p3 power check: 0

=== u09-p4 ===
p4: v(t) = V0/(B0*b) - V0*exp(-B0**2*b**2*t/(R_res*m))/(B0*b)
p4: v_inf = V0/(B0*b)
p4: I(t->inf) = 0
p4: I(0) = V0/R_res

=== u09-p5 ===
p5: I_D = i_curr
p5: B(r<R) = i_curr*mu0*r_cyl/(2*pi*R_cap**2)
p5: B(r>R) = i_curr*mu0/(2*pi*r_cyl)
p5: B(R/2) = i_curr*mu0/(4*pi*R_cap)
p5 continuity at r=R: 0
```
