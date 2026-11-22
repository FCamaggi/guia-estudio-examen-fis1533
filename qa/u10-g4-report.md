# Reporte de Revisión G4 (Autosuficiencia) — Unidad U10: Inductancia y circuitos RL, LC, RLC

- **Archivo revisado:** `unidades/u10-inductancia.html`
- **Contrato pedagógico:** `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5 y §9)
- **Perfil simulado:** Estudiante de ingeniería de segundo año con **solo** esta unidad (sin clases, sin ayudantías, sin otras unidades, sin calculadora y sin formulario externo).

---

## 1. Evaluabilidad de arquetipos (`u10-x1`..`u10-x3`) y problemas de práctica (`u10-p1`..`u10-p4`)

### Arquetipos de examen (`#u10-examen`)

#### `u10-x1` · Conmutación de circuito de dos mallas RL a LC (Examen 2026-1 · P3)
- **¿Puede resolverlo el estudiante solo con la unidad?** **Sí, casi por completo; hay una ambigüedad de signo en la parte c).**
- **Trazabilidad en la unidad:**
  - **Parte a) (`Paso 1`, línea 315):** `u10-s4` (tabla, línea 128) indica explícitamente que cuando $i_L(0^-) = 0$ el inductor actúa como circuito abierto ($i_L(0^+) = 0$), y `Repaso exprés` 2 (líneas 32–34) cubre la regla de mallas y la caída $V_{ab} = V_a - V_b$.
  - **Parte b) (`Paso 2`, línea 316):** `u10-s4` (tabla, línea 129) establece que para $t \to \infty$ se cumple $di_L/dt = 0 \implies v_L = 0$ (cortocircuito ideal).
  - **Parte c) (`Paso 3`, línea 317):** `u10-s5` (línea 160) muestra que $i(t)$ también obedece $\ddot i + \frac{1}{LC}i = 0$, `Repaso exprés` 3 (línea 42) da la solución general $A\cos(\omega_0 t) + B\sin(\omega_0 t)$, y `u10-s2`/`Repaso exprés` 2 dan continuidad de $i_L$ y $v_C$ al conmutar.
  - **Parte d) (`Paso 4`, línea 318):** `u10-s5` (`.why`, línea 175) responde textualmente por qué un circuito $LC$ ideal nunca alcanza régimen permanente.
- **Punto de fricción (sin bloqueo completo, pero cambia el signo):**
  - En la **parte c)** (línea 307), el enunciado pide *"la diferencia de potencial $v_C(t)$ sobre el condensador (entre $e$ y $f$)"* sin definir su polaridad ($V_f - V_e$ vs. $V_e - V_f$). En la parte a) (línea 305), *"entre $c$ y $d$"* significa $V_c - V_d$ (borne superior menos inferior, en el sentido de $i_L$), mientras que el `Paso 3` (línea 317) toma $v_C = V_f - V_e$ (borne inferior menos superior, en el sentido de $i_C$). Un estudiante que interprete "entre $e$ y $f$" como $V_{ef} = V_e - V_f$ obtendrá el signo contrario ($-\frac{\mathcal{E}}{R}\sqrt{\frac{L}{C}}\sin(\omega_0 t)$).

#### `u10-x2` · Alambre infinito y espira rectangular: fuerza e inductancia mutua (Examen 2024-2 · P1)
- **¿Puede resolverlo el estudiante solo con la unidad?** **No; se bloquea en la parte b).**
- **Dónde se bloquea y por qué:**
  - **Parte a) (`Paso 1`, línea 340):** Se resuelve bien con `Repaso exprés` 1 (líneas 24–26: ley de Ampère y regla de la mano derecha para alambre recto infinito) y `u10-s1` Caso B (línea 66). *(Nota menor: el enunciado pide $\vec B_1$ "en función de la distancia al eje del alambre infinito", pero la solución y `li.final` solo expresan $\vec B_1(y)$ restringido al semiplano $y \gt 0, z = 0$.)*
  - **Paso bloqueante — Parte b) (`Paso 2`, línea 341):** El enunciado pide *"la fuerza neta que ejerce la corriente $I_1$ sobre la espira rectangular que conduce la corriente $I_2$"*, y el `Paso 2` usa $\vec F = \oint I_2\,d\vec\ell\times\vec B_1(y)$ y $\hat x\times\hat z = -\hat y$. Sin embargo, **ni la fuerza magnética sobre una corriente ($d\vec F = I\,d\vec\ell\times\vec B$ o $\vec F = I\,\vec\ell\times\vec B$) ni el producto cruz entre vectores unitarios aparecen en ninguna parte de la unidad** (ni en `Repaso exprés` ni en la teoría). Un estudiante que solo tiene U10 queda completamente bloqueado en b) (2 de 6 puntos).
  - **Parte c) (`Paso 3`, línea 342):** Sí se resuelve directamente con `u10-s1` Caso B (líneas 65–70).

#### `u10-x3` · Dos alambres con corrientes opuestas variables y espira (Examen 2021-2 · Ej. 4)
- **¿Puede resolverlo el estudiante solo con la unidad?** **Mayormente sí; hay un roce menor con la convención de signo de $\varepsilon$.**
- **Trazabilidad y puntos de fricción:**
  - El campo de cada alambre viene de `Repaso exprés` 1 (línea 26), y el cálculo de flujo integrando $1/r$ viene de `u10-s1` Caso B (líneas 67–68).
  - El sentido físico de la corriente inducida (horaria para $\dot I \gt 0$, antihoraria para $\dot I \lt 0$) se deduce con la ley de Lenz (`Repaso exprés` 1, línea 23) combinada con la regla de la mano derecha aplicada a cada tramo recto de la espira.
  - **Roce en el signo de $\varepsilon$ (`Paso 3` y `Paso 4`, líneas 367–371):** `Repaso exprés` 1 (línea 23) no enseña la regla de la mano derecha que vincula la normal $\hat n$ con el sentido positivo de recorrido de la espira (ni el enunciado fija un sentido de recorrido). Como resultado, `Paso 3` elige $\hat n = +\hat z$ (circulación antihoraria) y obtiene $\varepsilon \lt 0$ cuando $\dot I \gt 0$; un estudiante que elija $\hat n = -\hat z$ obtendrá $\varepsilon$ con signo opuesto, aunque el sentido físico de la corriente inducida no cambia.

---

### Problemas de práctica (`#u10-practica`)

- **`u10-p1` (Inductancia mutua de dos solenoides concéntricos):** **Sí.** `u10-s1` Caso A (líneas 56–62) deduce exactamente $M = \frac{\mu_0 N_1 N_2 (\pi r_1^2)}{\ell}$ y la línea 53 da $\varepsilon_2 = -M\,di_1/dt$.
- **`u10-p2` (Energía magnética y autoinductancia de un cable coaxial):** **Con dificultad / requiere recordar prerrequisitos fuera de la unidad.**
  - `u10-s3` (`.why`, línea 115) da la receta general ($B(r) \to U_B = \int \frac{B^2}{2\mu_0}\,dV \to L = 2U_B/I^2$) y `Repaso exprés` 1 da Ampère.
  - **Bloqueos parciales sin abrir `li.hint`:** (1) el vector unitario cilíndrico $\hat\theta$ usado en `Paso 1` (línea 429) y `li.final` (línea 434) **nunca se define en la unidad**; (2) el elemento de volumen cilíndrico $dV = 2\pi r\ell\,dr$ (usado en `Paso 2`, línea 430) tampoco aparece en `Repaso exprés` ni en teoría (solo en `li.hint`); (3) en la parte c), el estudiante no ha visto en teoría la superficie rectangular axial ($r \in [a, b]$ por largo $\ell$) para calcular el flujo propio de un cable coaxial.
- **`u10-p3` (Circuito RL de dos mallas con conmutación):** **Sí (dependiendo de la figura para la topología).** `u10-s4` (tabla, líneas 128–129, y `.why`, línea 146) enseña exactamente que $L$ es circuito abierto en $t = 0^+$, cortocircuito en $t \to \infty$, y que $\tau = L/R_{\text{eq}}$ usa la resistencia equivalente vista por $L$ tras conmutar ($R_2$). El texto del enunciado (línea 444) no describe cómo están conectados $R_1$, $R_2$ y $L$, por lo que es indispensable mirar la figura `u10-rl-dos-mallas`.
- **`u10-p4` (Circuito RLC serie subamortiguado y pérdida de energía):** **Sí, por completo.** `u10-s5`, `u10-s6` y `u10-e4` cubren todas las fórmulas ($\omega_0$, $R_{\text{crít}}$, $2\gamma$, $\omega_d$, envolvente $Q_0 e^{-\gamma t}$) y los datos se calculan a mano ($LC = 10^{-6}\ \text{s}^2$, terna $600$–$800$–$1000$, $e^{-1} \approx 0{,}37$).

---

## 2. Saltos en derivaciones

1. **`u10-x2` `Paso 2` (línea 341) — Fuerza sobre la espira:** Salta directamente a $\vec F = \oint I_2\,d\vec\ell\times\vec B_1(y)$ y $\hat x\times\hat z = -\hat y$ sin haber deducido ni enunciado previamente la fuerza magnética sobre corrientes ni el producto cruz en la unidad.
2. **`u10-s6` `Paso 2` y `Paso 3` (líneas 198–202) — Raíces y solución subamortiguada:**
   - Línea 198: Pasa de $\lambda^2 + \frac{R}{L}\lambda + \frac{1}{LC} = 0$ a $\lambda = -\frac{R}{2L} \pm \sqrt{(\frac{R}{2L})^2 - \frac{1}{LC}}$ sin mostrar el paso previo $\frac{-R/L \pm \sqrt{(R/L)^2 - 4/(LC)}}{2}$.
   - Línea 202: Afirma que *"La combinación lineal real de $e^{(-\gamma \pm j\omega_d)t}$ es $q(t) = A\,e^{-(R/2L)t}\cos(\omega_d t + \phi)$"* sin invocar la fórmula de Euler ($e^{\pm j\omega_d t} = \cos\omega_d t \pm j\sin\omega_d t$), ni justificar por qué en el régimen de amortiguamiento débil con $i(0) = 0$ se tiene $\phi \approx 0$ y $A \approx Q_0$.
3. **`u10-s4` (líneas 136, 138–139 y 143) — Integrales omitiendo planteo o primitiva evaluada (contra §9.9):**
   - Línea 136: Pasa de $\int_0^i \frac{di'}{i' - I_\infty} = -\int_0^t \frac{dt'}{\tau}$ a $\ln\left(\frac{i - I_\infty}{-I_\infty}\right) = -\frac{t}{\tau}$ omitiendo la primitiva evaluada $\big[\ln|i' - I_\infty|\big]_0^i$. Lo mismo ocurre en `Repaso exprés` 3 (líneas 37–38).
   - Líneas 138–139 (decaimiento): Omite escribir la integral definida $\int_{I_0}^i \frac{di'}{i'} = -\int_0^t \frac{dt'}{\tau}$ y la primitiva evaluada antes de $\ln(i/I_0) = -t/\tau$.
   - Línea 143 (calor disipado): Pasa de $\int_0^\infty e^{-2t/\tau}\,dt$ a $(\tau/2)$ sin mostrar la primitiva evaluada $\big[-\frac{\tau}{2}e^{-2t/\tau}\big]_0^\infty$.
4. **`u10-s3` (líneas 108–112) — Energía y densidad $u_B$:**
   - Línea 108: Usa $P = V_{ab}\,i$ sin justificar la fórmula de potencia eléctrica.
   - Línea 110: Omite la primitiva evaluada $\big[\frac{1}{2}Li^2\big]_0^I$.
   - Línea 112: Salta algebraicamente de $\dfrac{\frac{1}{2}\left(\frac{\mu_0 N^2 A}{2\pi r}\right)I^2}{2\pi r A}$ a $\dfrac{1}{2\mu_0}\left(\dfrac{\mu_0 N I}{2\pi r}\right)^2$ sin mostrar el paso intermedio $\dfrac{\mu_0 N^2 I^2}{8\pi^2 r^2}$.
5. **`u10-s5` `Paso 3` y `Paso 4` (líneas 161–163) — Solución del oscilador $LC$:**
   - Línea 161: Pasa de $q(t) = A\cos(\omega_0 t) + B\sin(\omega_0 t)$ con $q(0) = Q_{\text{máx}}, i(0) = 0$ directamente a $\phi = 0$ y $q(t) = Q_{\text{máx}}\cos(\omega_0 t)$ sin mostrar la evaluación explícita de $A$ y $B$ (aunque luego sí se hace en `u10-e3` Paso 3, línea 266).
   - Línea 163: Escribe $\frac{q}{C}\dot q + Li\dot i = 0$ sin factorizar explícitamente $i = \dot q$ para mostrar $i(q/C + L\ddot q) = 0$.
6. **`u10-s2` (línea 96) — Toroide ancho:** Pasa directamente de $\Phi_B = \int_{r_1}^{r_2}\frac{\mu_0 N i}{2\pi s}h\,ds$ a $L = \frac{\mu_0 N^2 h}{2\pi}\ln(r_2/r_1)$ sin mostrar la primitiva $[\ln s]_{r_1}^{r_2}$ ni $L = N\Phi_B/i$.
7. **`u10-x1` `Paso 3` (línea 317):** Pasa de $v_C(0) = 0 \implies v_L(0) = 0$ a $\dot i_L(0) = B\omega_0 = 0$ sin escribir explícitamente $v_L(0) = L\dot i_L(0) = 0$ ni derivar $i_L(t)$; luego pasa de $\frac{\mathcal{E}}{RC\omega_0}$ a $\frac{\mathcal{E}}{R}\sqrt{\frac{L}{C}}$ sin sustituir $\omega_0 = 1/\sqrt{LC}$.
8. **`u10-p2` `Paso 2` y `Paso 3` (líneas 431 y 433):** En ambas integrales ($\int_a^b dr/r$) omite mostrar la primitiva evaluada $[\ln r]_a^b$, y en `Paso 3` no explica por qué el flujo a través de un rectángulo axial de largo $\ell$ y ancho $b-a$ corresponde al flujo enlazado del cable coaxial.

---

## 3. Símbolos usados antes de definirse o definidos sin unidades SI

Según `SPEC-PEDAGOGICO.md` §1 (*"Cada símbolo se define la primera vez que aparece en la unidad, con unidades SI"*) y §9.2 (*"Unidades SI en la primera aparición de cada símbolo, también en repasos exprés, tablas y enunciados de problemas simbólicos"*):

1. **`u10-mapa` (líneas 7–19):**
   - Aparecen sin unidades SI en su primera mención: $i(t)$ (A), $\varepsilon_L$ (V), $L$ (H; ni siquiera se nombra en línea 7 sino en línea 10), $t$ (s), $U_B$ (J), $I$ (A), $M$ (H), $\varepsilon_2$ (V), $i_1$ (A), $\Phi_B$ (Wb), $V_{ab}$ (V), $u_B$ ($\text{J/m}^3$), $\vec B$ (T), $\tau$ (s), $R_{\text{eq}}$ ($\Omega$), $r$ (m).
   - Aparecen **antes de definirse** y sin unidades SI: $\mu_0$ (línea 11, definida recién en línea 24), $N$ (línea 10, definida en línea 23), $i_L$ (línea 12), $\omega_0$ (línea 13, nombrada recién en línea 153), $C$ y $R$ (líneas 13–14, definidos en línea 32), $\gamma$ (línea 14, nombrada en línea 182), $\dot I$ (línea 18), $\omega_d$ (línea 19, definida recién en líneas 188/200) y $R_{\text{crít}}$ (línea 19, definida en línea 182).
2. **`Repaso exprés` 1 (líneas 23–28):**
   - Línea 23: $\vec B$ no declara su unidad `(T)` explícitamente (solo aparece dentro de $1\ \text{Wb} = 1\ \text{T·m}^2$; recién recibe unidad explícita en línea 106 para $B$); $d\vec A$ ($\text{m}^2$) y $t$ (s) sin unidades SI.
   - Línea 24: $d\vec\ell$ (m) e $I_{\text{enc}}$ (A) sin unidades SI.
   - Líneas 27–28: $\ell$ (m), $A$ ($\text{m}^2$) y $r$ (m) sin unidades SI.
3. **`Repaso exprés` 2 y 3 (líneas 34–43):**
   - Línea 34: $V_{ab}, V_a, V_b, \Delta V$ sin unidad SI (V).
   - Línea 37: $I_\infty$ e $i_0$ sin unidad SI (A), e $i_0$ sin definición explícita (solo "en $t=0$ (donde $i = i_0$)").
   - Líneas 40–43: $\gamma$ ($\text{s}^{-1}$), $\omega_0$ (rad/s) y $\phi$ (rad) sin unidades SI en su primera definición formal en el repaso.
4. **`u10-s1` y `u10-s2` (líneas 56, 65, 82–83, 96):**
   - Línea 56: $\ell, r_1, r_2$ (m) y líneas 58/65: $A_1, A_2$ ($\text{m}^2$), $a, b, h, x, y$ (m) sin unidades SI.
   - Líneas 82–83: $v_L$ (V) e $i_L$ (A) se usan en las ecuaciones sin definición formal explícita ni unidades SI.
   - Línea 96: $h, r_1, r_2, s$ (m) sin unidades SI.
5. **`u10-s3` (líneas 104–108):**
   - Línea 104: $E$ (V/m) y $\varepsilon_0$ ($\text{C}^2/(\text{N·m}^2)$ o F/m) aparecen en $u_E = \frac{1}{2}\varepsilon_0 E^2$ **sin definirse ni llevar unidades SI en toda la unidad**; $V$ (voltaje, V) en línea 104 choca inmediatamente con $V$ (volumen, sin unidad $\text{m}^3$) en líneas 105–106.
   - Línea 108: $P$ (*"potencia instantánea"*) sin unidad SI (W).
6. **`u10-s4` y `u10-s5` (líneas 143, 153, 167–172):**
   - Línea 143: $Q_{\text{disipado}}$ (*"calor total disipado"*) sin unidad SI (J).
   - Línea 153 (`.note`): $U$ (J) y $Q_{\text{máx}}$ (C) aparecen en las fórmulas sin entrada explícita con unidad SI en `.note`.
   - Líneas 167–172 (tabla analogía): $m$ (kg), $x$ (m), $v$ (m/s), $k$ (N/m) sin unidades SI.
7. **`u10-s6` (líneas 182–200):**
   - Línea 182: $V(t)$ (*"fuente alterna $V(t)$"*) sin unidad SI (V).
   - Línea 188: $\omega_d$ aparece en la tabla **antes de ser nombrada** en la línea 200 (*"frecuencia angular amortiguada"*), y nunca recibe unidad SI `(rad/s)` hasta la tarjeta de fórmulas (línea 542).
   - Línea 188: $j = \sqrt{-1}$ se usa en la tabla antes de definirse en la línea 200.
   - Líneas 188–190: $A, B, A_1, A_2$ (constantes de la solución de $q(t)$, C) sin unidades SI.
8. **Enunciados simbólicos (`u10-x1`..`u10-x3`, `u10-p1`, `u10-p2`) — incumplimiento de §9.2:**
   - `u10-x1` (líneas 304–308): $\mathcal{E}$ (V), $R$ ($\Omega$), $L$ (H), $C$ (F), $v_L$ (V), $i_R, i_L, i_C$ (A), $v_C$ (V) sin unidades SI en el enunciado ni en `Datos`.
   - `u10-x2` (líneas 329–333): $I_1, I_2$ (A), $a, b, h$ (m), $\vec F_{\text{neta}}$ (N) sin unidades SI en el enunciado.
   - `u10-x3` (líneas 353–354): $I$ (A), $\dot I$ (A/s), $L, d, a$ (m) sin unidades SI en el enunciado.
   - `u10-p1` (líneas 400–401): $\ell, R$ (m), $I_0$ (A), $\omega$ (rad/s) sin unidades SI en el enunciado.
   - `u10-p2` (líneas 421–422): $a, b$ (m), $I$ (A) sin unidades SI en el enunciado; además **`\hat\theta`** (líneas 429 y 434) **no se define en toda la unidad**.
9. **Tarjeta de fórmulas (`u10-formulas`, líneas 526–543) — incumplimiento de §2.9:**
   - Varias filas omiten significado y/o unidades SI de símbolos presentes en la fórmula de esa fila: p. ej., $N_1, N_2, \Phi_{12}$ (Wb) en línea 528; $\mu_0$ (H/m), $r_1, r_2, \ell$ (m) en línea 530; $a, b, h$ (m) en línea 531; $A$ ($\text{m}^2$), $\ell$ (m) en línea 534; $A$ ($\text{m}^2$), $r, a, b, \ell$ (m) en línea 535; $L$ (H), $I$ (A), $B$ (T), $\mu_0$ (H/m), $V$ ($\text{m}^3$) en línea 536; $\varepsilon$ (V), $i$ (A), $R$ ($\Omega$) en línea 537; $I_0$ (A) en línea 538; $q$ (C), $C$ (F), $Q_{\text{máx}}$ (C), $\phi$ (rad), $I_{\text{máx}}$ (A) en línea 539; $R_{\text{crít}}$ ($\Omega$) en línea 541; $A$ (C), $\phi$ (rad) en línea 542.

---

## 4. Referencias colgantes

- **No se encontraron referencias colgantes externas** necesarias para seguir el razonamiento (no hay "ver clase...", "como vimos en U...", ni "como se vio antes").
- Las menciones a `(unidad U11)` en `u10-s6` (línea 204) y `Biot–Savart` en `u10-s1` (línea 51) son solo contexto informativo y no se requieren para resolver ningún problema.
- Las citas a exámenes, ayudantías y pauta oficial (`Examen 2026-1 · P3`, `Examen 2024-2 · P1`, `Examen 2021-2 · Ej. 4`, `Ayudantía 23 P2, 2026-2`, `pauta oficial`) cumplen rol de trazabilidad y corrección de erratas de origen según `SPEC-PEDAGOGICO.md` §6.
- *(Nota: en `u10-p3`, línea 444, el enunciado dice *"En el circuito de la figura..."* remitiendo a `u10-rl-dos-mallas` dentro del mismo problema; no es referencia externa, pero deja la topología sin describir en texto.)*

---

## 5. Prerrequisitos usados pero no cubiertos por `Repaso exprés` (`details.prereq`)

Los tres recuadros `details.prereq` existentes (líneas 22–45) cubren Faraday–Lenz básico, Ampère para alambre/solenoide/toroide, Kirchhoff/capacitores/continuidad y EDOs lineales de 1.º y 2.º orden. Sin embargo, la unidad usa los siguientes prerrequisitos **sin** cobertura en `Repaso exprés`:

1. **Fuerza magnética sobre corrientes ($d\vec F = I\,d\vec\ell\times\vec B$) y producto cruz cartesiano:**
   - Usado en `u10-x2` `Paso 2` (línea 341): $\vec F = \oint I_2\,d\vec\ell\times\vec B_1(y)$ y $\hat x\times\hat z = -\hat y$. Su ausencia **bloquea** la parte b) de `u10-x2` y contraviene explícitamente `SPEC-PEDAGOGICO.md` §1 y §9.3.
2. **Coordenadas cilíndricas ($\hat\theta$ y elemento de volumen $dV = 2\pi r\ell\,dr$):**
   - Usados en `u10-p2` `Paso 1`–`Paso 2` (líneas 429–431) y `li.final` (línea 434). Ejemplo explícito de prerrequisito en `SPEC-PEDAGOGICO.md` §1 (*"integral en coordenadas cilíndricas"*).
3. **Regla de la mano derecha para espiras / convención de signo de Faraday ($\hat n$ respecto al sentido de recorrido):**
   - Usada en `u10-x3` `Paso 3` y `Paso 6` (líneas 367 y 374) y en la convención de signos de `SPEC-PEDAGOGICO.md` §5. `Repaso exprés` 1 (línea 26) solo da la regla para un alambre recto.
4. **Potencia eléctrica instantánea ($P = V_{ab}\,i$ y $P_R = i^2 R$):**
   - Usada en `u10-s3` (línea 108), `u10-s4` (líneas 141–143) y `u10-s6` (línea 194).
5. **Fórmula de Euler ($e^{\pm j\omega_d t} = \cos\omega_d t \pm j\sin\omega_d t$) y cálculo elemental ($\frac{d}{dt}\sin\omega t$, $\int_0^\infty e^{-at}dt = 1/a$):**
   - Usados en `u10-s6` (línea 202), `u10-p1` (línea 410), `u10-s4` (línea 143) y `u10-p3` (línea 456).

---

## 6. Violaciones a `SPEC-PEDAGOGICO.md` §3, §5 y §9

### A. Formato de problema guiado (§3) y reglas de verificabilidad (§9.4, §9.8)
- **§3.1 (`u10-p3`, línea 444):** El enunciado depende de la figura (*"En el circuito de la figura..."*) para saber que $R_1$ está en la rama izquierda con $S$ y $\varepsilon$, y que $R_2$ está en paralelo con $L$. (Los arquetipos `u10-x1`–`u10-x3` sí describen todo en texto según §9.6.)
- **§3.5 y §9.4 (`li.final` debe contener todo lo pedido):**
  - **`u10-x1` (`li.final`, línea 319):** Las partes a) y b) piden explícitamente *"Justifique físicamente"* y *"Justifique"* (líneas 305–306), pero `li.final` solo incluye la justificación de d) (las de a) y b) quedan solo en los `Paso 1` y `Paso 2`).
  - **`u10-x2` (`li.final`, línea 343):** La parte a) pide $\vec B_1$ *"en función de la distancia al eje del alambre infinito"* (línea 330), pero `li.final` recuadra solo $\vec B_1(y) = \frac{\mu_0 I_1}{2\pi y}\,\hat z\ (y \gt 0)$ (restringido al plano $z=0, y>0$).
- **§3.6 y §9.8 (`li.check`: análisis dimensional + al menos un límite o caso conocido, más balance de energía cuando aplique):**
  - **`u10-e2` (línea 247):** Tiene unidades y balance energético, pero **falta un caso límite** (p. ej. $R \to \infty$ o $t \to \infty$).
  - **`u10-e3` (línea 268):** Tiene balance energético y análisis de escala ($L \to 2L$), pero **falta análisis dimensional** explícito ($[\omega_0] = \text{s}^{-1}$, $[I_{\text{máx}}] = \text{A}$).
  - **`u10-x1` (línea 320):** Tiene unidades de $v_C$ y conservación de energía, pero **falta un caso límite** (p. ej. $C \to \infty$ o $R \to \infty$).
  - **`u10-x3` (línea 376):** Tiene límites ($L \to 0$ y $L \to \infty$), pero **falta análisis dimensional** (`[M]`, `[\varepsilon]`).
  - **`u10-p3` (línea 456):** Tiene balance energético ($Q = U_B$), pero **faltan análisis dimensional y caso límite**.
  - **`u10-p4` (línea 477):** Tiene unidades de la EDO y balance energético en $t=0$, pero **falta un caso límite** (p. ej. $R \to 0 \implies \omega_d \to \omega_0$).

### B. Convenciones de notación (§5) y símbolos sobrecargados (§9.5)
- **Ambigüedad de polaridad en `u10-x1` parte c) (§5, líneas 307 y 317):** En `u10-x1`, *"la diferencia de potencial $v_L$ sobre la inductancia (entre $c$ y $d$)"* corresponde a $V_c - V_d$, mientras que *"la diferencia de potencial $v_C(t)$ sobre el condensador (entre $e$ y $f$)"* se resuelve en `Paso 3` como $V_f - V_e$ (invertido respecto al orden $e \to f$). Debe explicitarse la polaridad ($V_f - V_e$ o $V_e - V_f$) en el enunciado.
- **Convención de Faraday (§5, línea 23):** `Repaso exprés` 1 no declara la regla de la mano derecha que relaciona la normal $\hat n$ con el sentido de recorrido en $\varepsilon = -d\Phi_B/dt$.
- **Símbolos sobrecargados (§9.5):**
  - **$V$ (voltaje vs. volumen):** En `u10-s3` (líneas 104–106), $V$ denota voltaje en $U_E = \frac{1}{2}CV^2$ (línea 104) y volumen en $V = 2\pi r A$ y $dV$ (líneas 105–106).
  - **$R$ (radio vs. resistencia):** $R$ es resistencia en casi toda la unidad, pero designa radio en `u10-p1` ($r_1 = R, r_2 = 2R$, línea 400) y `u10-quiz` P2 (radio $R, 3R$, línea 492) — caso citado explícitamente en §9.5.
  - **$L$ (distancia vs. autoinductancia):** En `u10-x3` (línea 353), el segundo alambre está en $x = L$, aunque en toda la unidad $L$ es autoinductancia.
  - **$Q$ (carga vs. calor disipado):** $Q, Q_0, Q_{\text{máx}}$ es carga (C) en `u10-s5`, `u10-s6`, `u10-e3`, `u10-p4`, pero $Q_{\text{disipado}}$ / $Q_{\text{dis}}$ es calor (J) en `u10-s4` (línea 143) y `u10-e2` (líneas 236–247).
  - **$B$ (campo magnético vs. constante de integración):** $B$ es constante de integración en `Repaso exprés` 3 (línea 42), `u10-s5` (línea 161), `u10-s6` (línea 189), `u10-e3` (línea 266) y `u10-x1` (línea 317).
  - **Inconsistencias menores de notación:** $\varepsilon$ vs. $\mathcal{E}$ en `u10-x1` (líneas 304–320); $\phi$ (fase en `u10-s5`/`u10-s6`) vs. $\phi_1, \phi_2$ (flujos parciales en `u10-x3`); $\Phi_2$ en `u10-x2` (línea 342) vs. $\Phi_{21}$ en `u10-s1`; $r$ reutilizado como distancia a dos alambres distintos en `u10-x3` `Paso 1` y `Paso 2` (líneas 362 y 365).

### C. Cálculos a mano (§9.1), HTML (§9.9) y otros aspectos de §9
- **§9.1 (sin calculadora):** Cumplido íntegramente. Todos los ejercicios numéricos (`u10-e1`..`u10-e4`, `u10-p3`, `u10-p4`) usan potencias de 10, ternas pitagóricas ($3$–$4$–$5$, $600$–$800$–$1000$) y constantes dadas ($e^{-1} \approx 0{,}37$, $\ln 2 \approx 0{,}69$, $\pi \approx 3{,}14$).
- **§9.6 (puntajes en arquetipos):** Cumplido (`u10-x1` suma `2,0 + 2,0 + 1,0 + 1,0 = 6,0`; `u10-x2` suma `2,0 + 2,0 + 2,0 = 6,0`; `u10-x3` asigna `1,0 pto.` × 6 pasos = `6,0`).
- **§9.9 (HTML):** Sin `<` ni `>` crudos dentro de delimitadores `$` o `$$`. Los saltos algebraicos en derivaciones se detallaron en la Sección 2.

---

## 7. Las 5 mejoras más valiosas (ordenadas por prioridad)

### 1. Desbloquear `u10-x2` parte b): añadir fuerza magnética diferencial y producto cruz cartesiano en `Repaso exprés` 1
- **Ubicación:** `u10-mapa`, dentro de `<details class="prereq">` 1 (después de la línea 29), y `u10-x2` `li.final` (línea 343).
- **Por qué:** Es el único bloqueo total en los arquetipos de examen: sin $d\vec F = I\,d\vec\ell\times\vec B$ ni las reglas de producto cruz ($\hat x\times\hat z = -\hat y$), el estudiante con solo U10 no puede resolver `u10-x2` b).
- **Texto propuesto (agregar al final de `Repaso exprés` 1, tras la línea 29):**
  > `<p><b>Fuerza magnética sobre una corriente y producto cruz:</b> sobre un elemento de cable $d\vec\ell$ ($\text{m}$) con corriente $I$ ($\text{A}$) en un campo $\vec B$ ($\text{T}$), actúa la fuerza diferencial $d\vec F = I\,d\vec\ell\times\vec B$ ($\text{N}$); para un tramo recto de vector $\vec\ell$ en campo uniforme, $\vec F = I\,\vec\ell\times\vec B$. En base cartesiana derecha: $\hat x\times\hat y = \hat z$, $\hat y\times\hat z = \hat x$, $\hat z\times\hat x = \hat y$ (invertir el orden cambia el signo).</p>`
- **Texto propuesto en `u10-x2` `li.final` (línea 343, precisar la restricción al plano $xy$):**
  > Reemplazar `\vec B_1(y) = \frac{\mu_0 I_1}{2\pi y}\,\hat z\ \ (y\gt 0)` por: `\vec B_1(y) = \frac{\mu_0 I_1}{2\pi y}\,\hat z\ \ (\text{en el plano }z=0,\ y\gt 0;\ \text{magnitud }B_1(r) = \frac{\mu_0 I_1}{2\pi r})`

### 2. Completar los prerrequisitos faltantes en `Repaso exprés`: coordenadas cilíndricas ($\hat\theta$, $dV$), RHR de Faraday ($\hat n$ vs. $d\vec\ell$) y potencia eléctrica
- **Ubicación:** `u10-mapa`, en `Repaso exprés` 1 (línea 23) y `Repaso exprés` 2 (después de la línea 34).
- **Por qué:** Desbloquea `u10-p2` sin depender de `li.hint` (define $\hat\theta$ y $dV = 2\pi r\ell\,dr$), elimina el roce de signos en `u10-x3` (regla de $\hat n$ para Faraday) y respalda $P = V_{ab}\,i = i^2 R$ en `u10-s3` y `u10-s4`.
- **Texto propuesto (ampliar la línea 23 en `Repaso exprés` 1):**
  > `...induce una fem $\varepsilon = -N\,\dfrac{d\Phi_B}{dt}$ (en V) que se opone al cambio del flujo. La normal $\hat n$ de $d\vec A = \hat n\,dA$ ($\text{m}^2$) sigue la regla de la mano derecha respecto al sentido positivo de recorrido $d\vec\ell$ ($\text{m}$) de la espira (si $\hat n = +\hat z$, el recorrido positivo es antihorario). En coordenadas cilíndricas alrededor del eje $z$, $\hat\theta$ es el vector unitario azimutal (sentido antihorario visto desde $+z$) y el volumen de un cascarón de radio $r$ ($\text{m}$), espesor $dr$ y largo $\ell$ ($\text{m}$) es $dV = 2\pi r\ell\,dr$.`
- **Texto propuesto (agregar al final de `Repaso exprés` 2, tras la línea 34):**
  > `<p><b>Potencia eléctrica:</b> cuando una corriente $i$ ($\text{A}$) atraviesa un elemento con caída $V_{ab}$ ($\text{V}$), la potencia entregada al elemento es $P = V_{ab}\,i$ ($\text{W}$); en particular, en una resistencia $R$ ($\Omega$) se disipa $P_R = i^2 R$.</p>`

### 3. Eliminar la ambigüedad de signo en `u10-x1` parte c) y completar su `li.final` (y el enunciado de `u10-p3`)
- **Ubicación:** `u10-x1` enunciado (línea 307) y `li.final` (línea 319); `u10-p3` enunciado (línea 444).
- **Por qué:** Evita que un estudiante obtenga $-v_C(t)$ en `u10-x1` c) por interpretar "entre $e$ y $f$" como $V_e - V_f$ en vez de $V_f - V_e$, y cumple §9.4 (incluir las justificaciones pedidas en a) y b)) y §3.1 (enunciado completo en `u10-p3`).
- **Texto propuesto en `u10-x1` (línea 307):**
  > Cambiar `la diferencia de potencial $v_C(t)$ sobre el condensador (entre $e$ y $f$)` por: `la diferencia de potencial $v_C(t) = V_f - V_e$ sobre el condensador`.
- **Texto propuesto en `u10-x1` `li.final` (línea 319):**
  > Agregar tras la caja: `Justificaciones: en a) $i_L(0^+)=i_L(0^-)=0$ (continuidad en $L$, circuito abierto), luego $v_R(0^+)=0$ y $v_L(0^+)=\mathcal{E}$; en b) en régimen permanente DC $di_L/dt=0 \implies v_L=0$ (cortocircuito); en d) no hay resistencia que disipe energía, por lo que esta oscila indefinidamente entre $L$ y $C$.`
- **Texto propuesto en `u10-p3` (línea 444):**
  > Cambiar `En el circuito de la figura,` por: `En el circuito de la figura, la rama izquierda tiene una fuente $\varepsilon = 18\ \text{V}$ en serie con un interruptor $S$ y una resistencia $R_1 = 6{,}0\ \Omega$, alimentando el paralelo formado por $R_2 = 3{,}0\ \Omega$ y un inductor $L = 12\ \text{mH}$.`

### 4. Completar las verificaciones `li.check` (§3.6, §9.8) y pasos algebraicos en derivaciones (§9.9)
- **Ubicación:** `u10-e2` (línea 247), `u10-e3` (línea 268), `u10-x1` (línea 320), `u10-x3` (línea 376), `u10-p3` (línea 456), `u10-p4` (línea 477), más `u10-s4` (líneas 136, 139, 143) y `u10-s6` (líneas 198, 202).
- **Por qué:** Todos los problemas deben verificar **dimensiones + al menos un límite**, y las derivaciones deben mostrar primitivas evaluadas, fórmula cuadrática y paso por Euler.
- **Texto propuesto (ejemplos concretos para `li.check`):**
  - En `u10-x1` (línea 320, agregar): `Límite: si $C \to \infty$ (condensador gigante sin caída de voltaje), $\omega_0 \to 0$ y $i_C(t) \to \mathcal{E}/R$ constante.`
  - En `u10-x3` (línea 376, agregar al inicio): `Unidades: $[M] = (\text{H/m})\cdot\text{m} = \text{H}$; $[\varepsilon] = (\text{H/m})\cdot\text{m}\cdot(\text{A/s}) = \text{V}$.`
  - En `u10-p3` (línea 456, agregar al inicio): `Unidades: $[\tau_{\text{desc}}] = \text{H}/\Omega = \text{s}$. Límite: si $R_2 \to \infty$ (sin rama paralela en descarga), $\tau_{\text{desc}} \to 0$.`
  - En `u10-p4` (línea 477, agregar): `Límite: si $R \to 0$, $\gamma \to 0$ y $\omega_d \to \omega_0$.`
  - En `u10-s6` (línea 202, añadir tras $\lambda = -\gamma \pm j\omega_d$): `Por la fórmula de Euler $e^{\pm j\omega_d t} = \cos(\omega_d t) \pm j\sin(\omega_d t)$, la combinación lineal real de $e^{(-\gamma \pm j\omega_d)t}$ es $q(t) = A\,e^{-(R/2L)t}\cos(\omega_d t + \phi)$.`

### 5. Eliminar símbolos sobrecargados (§9.5) y completar unidades SI en `u10-s3`, enunciados simbólicos y `u10-formulas` (§2.9, §9.2)
- **Ubicación:** `u10-s3` (línea 104), `u10-p1` (línea 400), `u10-quiz` P2 (línea 492), `u10-x3` (línea 353), enunciados de `u10-x1`..`u10-p2`, y tabla `u10-formulas` (líneas 528–542).
- **Por qué:** Evita colisiones entre $V$ (voltaje vs. volumen), $R$ (radio vs. resistencia), $L$ (distancia vs. autoinductancia) y $Q$ (carga vs. calor), y cumple §1, §2.9 y §9.2 en todas las apariciones y en la tarjeta de fórmulas.
- **Texto propuesto:**
  - En `u10-s3` (línea 104): cambiar `($U_E = \frac{1}{2}CV^2$, $u_E = \frac{1}{2}\varepsilon_0 E^2$)` por `($U_E = \frac{1}{2}C v_C^2$, $u_E = \frac{1}{2}\varepsilon_0 E^2$, con $\varepsilon_0$ permitividad del vacío en $\text{F/m}$ y $E$ campo eléctrico en $\text{V/m}$)`, y en línea 106 añadir `(m³)` al definir el volumen $V$.
  - En `u10-p1` (línea 400) y `u10-quiz` P2 (línea 492): renombrar el radio $R$ a $r_0$ (o $a$, evitando usar $R$ de resistencia) e indicar unidades SI en el enunciado simbólico (p. ej., `largo $\ell$ (m), radios $r_1 = a$ y $r_2 = 2a$ (m), corriente $I_0$ (A) y frecuencia angular $\omega$ (rad/s)`).
  - En `u10-x3` (línea 353): renombrar la posición $x = L$ a $x = D$ (m) o aclarar explícitamente `(donde $L$ es una distancia fija en m, no una inductancia)`, e indicar `($I$ en A, $d, a$ en m)`.
  - En `u10-formulas` (líneas 528–542): añadir la unidad SI faltante junto a cada símbolo de la columna `Significado y unidades SI` (por ejemplo, $\ell, r_1, r_2, a, b, h$ en m; $A$ en $\text{m}^2$; $V$ en $\text{m}^3$; $\mu_0$ en H/m; $q, Q_{\text{máx}}, A$ en C; $\phi$ en rad; $I_0, I_{\text{máx}}$ en A; $R_{\text{crít}}$ en $\Omega$).
