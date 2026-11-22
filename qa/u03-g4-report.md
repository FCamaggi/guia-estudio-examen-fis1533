# Reporte G4 — Autosuficiencia: `unidades/u03-potencial.html`

Simulación de estudiante de segundo año de ingeniería que dispone **únicamente** de `unidades/u03-potencial.html` (sin clases, sin otras unidades, sin calculadora ni formulario), verificada contra `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5 y §9).

---

## 1. Resolubilidad de arquetipos y problemas de práctica

| ID | Problema | ¿Resoluble solo con la unidad? | Paso que bloquea y por qué |
|---|---|---|---|
| `u03-x1` | Arquetipo 1 · Examen 2018-2 P1 | **Sí** | — |
| `u03-x2` | Arquetipo 2 · Examen 2022-2 P7 | **Sí** | — |
| `u03-p1` | Práctica 1 · Campo 2D desde $V$ | **Parcialmente** (bloqueado en parte **a**) | La parte a) pide verificar que $\nabla^2 V = 0$, pero el operador laplaciano $\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2}$ no se define en `u03-s6` ni en su `Repaso exprés` (L144–149). Las partes b) y c) sí son resolubles. |
| `u03-p2` | Práctica 2 · Disco cargado | **Sí** | — |
| `u03-p3` | Práctica 3 · Semicircunferencia | **Sí** | Sin bloqueo formal (usa $d\vec E = \frac{k\,dq}{|\vec r - \vec r'|^2}\hat u$ de `u03-mapa` L23), aunque la unidad no muestra ningún ejemplo resuelto de integración vectorial de $d\vec E$. |
| `u03-p4` | Práctica 4 · Esfera + 2 cascarones | **Sí** | — |
| `u03-p5` | Práctica 5 · Alambre finito | **Sí** | — |

---

## 2. Saltos de derivación

1. **`u03-s6` (`details.deriv`, L160):**
   > *"sustituyendo $\vec E = -\nabla V$ en la ley de Gauss diferencial $\nabla\cdot\vec E = \rho/\varepsilon_0$ resulta $\nabla\cdot(-\nabla V) = -\nabla^2 V = \rho/\varepsilon_0$"*
   Ni la divergencia $\nabla\cdot\vec E$ ni el laplaciano $\nabla^2 V$ se definen en coordenadas cartesianas en `u03-s6` ni en su `Repaso exprés` (L144–149). El estudiante no puede seguir por qué $\nabla\cdot(\nabla V) = \nabla^2 V$ ni cómo calcular $\nabla^2 V$ en `u03-p1`.

2. **`u03-s1` (`div.eq.key` L49 y `details.deriv` L54–57):**
   - L49 presenta $U_{\text{sistema}} = k\sum_{i\lt j}\frac{q_i q_j}{r_{ij}} = \frac12\sum_{i=1}^N q_i\,V_i$, pero la derivación (L55–57) solo deduce $k\sum_{i\lt j}\frac{q_i q_j}{r_{ij}}$ y menciona el factor $\frac12$ para $i \neq j$, sin mostrar el paso algebraico que agrupa $\sum_{j\neq i}\frac{k q_j}{r_{ij}} = V_i$.
   - L54 contiene además una errata de notación: escribe `$U = -\Delta W_{\infty\to r}$` en lugar de `$-W_{\infty\to r}$`.

3. **`u03-p4` (Paso 4, L390):**
   > *"al cerrar $S$, ambos cascarones forman un único equipotencial ($\vec E = \vec 0$ entre $a_2$ y $b_1$). Por tanto $Q_{a_2} = Q_{b_1} = 0$"*
   Salto lógico: en general, dos conductores al mismo potencial no implican $\vec E = \vec 0$ entre ellos si hubiera carga encerrada en el espacio intermedio. Falta explicitar que, por simetría esférica y ausencia de carga en $a_2 \lt r \lt b_1$, $V(a_2) - V(b_1) = \int_{a_2}^{b_1} \frac{Q_{\text{enc}}(a_2)}{4\pi\varepsilon_0 r^2}\,dr = 0$ obliga a que $Q_{\text{enc}}(a_2) = 0$ (y recién entonces $\vec E = \vec 0$ en $a_2 \lt r \lt b_1$).

---

## 3. Símbolos usados antes de su definición o sin unidades SI

- **`u03-mapa` L23 (`Repaso exprés`):** `$\varepsilon_0$`, `$k$`, `$\rho(r')$` y `$d\vec A$` aparecen sin unidades SI (las unidades de $\varepsilon_0$ y $k$ aparecen recién en L38, y las de $\rho$ en L28).
- **`u03-s1` L47 y L49:** `$\phi$` (en `$dr = d\ell\cos\phi$`, L47) no se define en el texto; `$V_i$` ("potencial en $\vec r_i$ debido a todas las cargas excepto $q_i$ (V)", L49) se usa **antes** de definir el potencial eléctrico $V$ en `u03-s2`.
- **`u03-s4` L100 y L110:** `$r$` en `$V_{\text{línea }\infty}(r)$` no aparece listado en `.note` (L100); `$\operatorname{sgn}(x)$` (L110) se usa sin definir.
- **`u03-s6` L153:** `$\nabla^2 V$` se usa sin definición previa.
- **Enunciados simbólicos sin unidades SI explícitas (SPEC §9.2):**
  - `u03-e3` L232: `$R$`, `$Q_0$`, `$d$`.
  - `u03-x1` L258: `$Q$`, `$L$`.
  - `u03-x2` L280: `$q$`, `$d$`, `$q_0$`, `$\sigma$`, `$A$`.
  - `u03-p2` L337: `$m$` (sin `(kg)`).
  - `u03-p4` L379: `$a_1, a_2, b_1, b_2, R, Q, \beta$` (la unidad de $\beta$, `[\beta] = \text{C/m}^5`, recién aparece en `.check` L392).
  - `u03-p5` L401: `$d$` (sin `(m)`), `$m_e$` (sin `(kg)`).

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

- **Externas:** No hay referencias colgantes externas. Todas las menciones a clases, ayudantías y exámenes (`Clase 05`, `Examen 2018-2`, `I1 2026-1`, `I1 2026-2`, `Ayudantía 06`) son citas de trazabilidad o notas de errata, no dependencias.
- **Internas:**
  1. `u03-s1` L49: referencia adelantada a `$V_i$` antes de su definición en `u03-s2`.
  2. `u03-p4` L391 (`li.final`): contiene la referencia colgante `(ver campos $\vec E_1$–$\vec E_6$ y $V_2$–$V_5$ en los pasos 2 y 3)`, obligando a abrir la solución colapsada para leer la respuesta pedida.

---

## 5. Prerrequisitos usados pero no cubiertos por `Repaso exprés`

1. **Divergencia ($\nabla\cdot\vec E$) y laplaciano ($\nabla^2 V$) en coordenadas cartesianas:** usados en `u03-s6` L153, L160 y `u03-p1` L316, L324; ausentes en `Repaso exprés: derivadas parciales y gradiente` (`u03-s6` L144–149).
2. **Integrales y diferenciales polares/potencias:** `u03-p2` L345 usa el elemento de área polar $dA = r\,dr\,d\theta$; `u03-p3` L366–368 usa $d\ell = R\,d\theta$ e integrales $\int_0^\pi \sin\theta\,d\theta$ y $\int_0^\pi \cos\theta\,d\theta$; `u03-p4` L387–389 usa $\int r^n\,dr = r^{n+1}/(n+1)$, que no está en `Repaso exprés` L39.

---

## 6. Violaciones de `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§3.5 y §9.4 (`li.final` completo con unidades y todo lo pedido):**
  - **Violación grave en `u03-p4` L391:** `li.final` omite $\vec E_1$–$\vec E_6$ y $V_2$–$V_5$ usando `\dots` y remitiendo a los pasos 2 y 3.
  - **Menor en `u03-e2` L222:** `li.final` omite las unidades SI (`V/m` y `V`) de $\vec E(r)$ y $V(r)$.
  - **Menor en `u03-p1` L327:** `li.final` no incluye la confirmación explícita de $\nabla^2 V = 0$ pedida en la parte a), y escribe `(2{,}0\ \text{m},\,0)` sin unidad en la coordenada $y$.
- **§3.6 y §9.8 (Verificación: dimensiones + un límite o caso conocido):**
  - `u03-e1` L201, `u03-e2` L223, `u03-e3` L244, `u03-x1` L271, `u03-p1` L328, `u03-p3` L370 y `u03-p4` L392 incluyen dimensiones y/o signo, pero **carecen de un límite o caso conocido**.
  - `u03-p5` L413 incluye el límite $z \gg d$ y signo, pero **carece de análisis dimensional** (por ejemplo, de $v_f$).
- **§5 (Convenciones de notación):** Cumplida ($k = 1/(4\pi\varepsilon_0)$ con $k_e$, $\Delta V = V_b - V_a = -\int_a^b \vec E\cdot d\vec\ell$, $V_{ab} = V_a - V_b$, $d\vec\ell$).
- **§9.1 (Cálculos a mano):** Cumplida en todos los problemas numéricos (`u03-e1`, `u03-p1`, `u03-quiz` #3).
- **§9.2 (Unidades SI en primera aparición):** Violada en `u03-mapa` L23 (`\varepsilon_0`, `k`, `\rho`, `d\vec A`) y en los enunciados simbólicos listados en §3 de este reporte.
- **§9.5 (Sin símbolos sobrecargados):**
  - `$r_0$` significa radio de referencia donde $V(r_0) = 0$ en `u03-s4` L100 y `u03-formulas` L470, pero en `u03-p2` L337 designa el radio del disco (en lugar de $R$).
  - `$a$` en `u03-s4` L100 (`.note`) designa dos cosas distintas en la misma nota: radio del anillo y distancia al extremo de la barra.
  - `$r'$` en `u03-s4` L98–100 denota distancia en L98, radio del anillo en L99 y vector fuente $\vec r'$ en L100.
- **§9.6 (Arquetipos autosuficientes sin figura y puntaje por paso):** Cumplida en `u03-x1`, `u03-x2` y `u03-p1`–`u03-p5`; los puntajes suman exactamente 6,0 pts.
- **§9.9 (HTML `\lt`/`\gt` en fórmulas):** Cumplida (0 ocurrencias de `<` seguido de letra o `>` dentro de `$...$` / `$$...$$`).

---

## 7. Los 5 arreglos más valiosos (ordenados por impacto)

1. **Definir divergencia y laplaciano en el `Repaso exprés` de `u03-s6` (desbloquea `u03-p1` a) y elimina salto en L160)**
   - **Ubicación:** `unidades/u03-potencial.html`, `#u03-s6`, `<details class="prereq">` (L144–149).
   - **Texto propuesto (agregar al final de L147, antes del mini ejemplo):**
     > `La <b>divergencia</b> de $\vec E$ es $\nabla\cdot\vec E = \dfrac{\partial E_x}{\partial x} + \dfrac{\partial E_y}{\partial y} + \dfrac{\partial E_z}{\partial z}$ (en $\text{V/m}^2$). Aplicada al gradiente da el <b>laplaciano</b> de $V$: $\nabla^2 V = \nabla\cdot(\nabla V) = \dfrac{\partial^2 V}{\partial x^2} + \dfrac{\partial^2 V}{\partial y^2} + \dfrac{\partial^2 V}{\partial z^2}$ (en $\text{V/m}^2$).`

2. **Completar `li.final` en `u03-p4` para cumplir SPEC §9.4**
   - **Ubicación:** `unidades/u03-potencial.html`, `#u03-p4`, `<li class="final">` (L391).
   - **Texto propuesto (reemplazar la segunda caja y el texto final de L391):**
     > `$$\boxed{\vec E(r) = \begin{cases}\dfrac{Q r^3}{2\pi\varepsilon_0 R^5}\hat r, & r \lt R \\ \dfrac{Q}{2\pi\varepsilon_0 r^2}\hat r, & R \lt r \lt a_1\ \text{y}\ a_2 \lt r \lt b_1 \\ \vec 0, & a_1 \lt r \lt a_2\ \text{y}\ b_1 \lt r \lt b_2 \\ \dfrac{3Q}{4\pi\varepsilon_0 r^2}\hat r, & r \gt b_2\end{cases}}$$`
     > `$$\boxed{V(r) = \frac{Q}{4\pi\varepsilon_0}\begin{cases}\dfrac{3}{b_2} - \dfrac{2}{b_1} + \dfrac{2}{a_2} - \dfrac{2}{a_1} + \dfrac{2}{R} - \dfrac{r^4 - R^4}{2R^5}, & r \le R \\ \dfrac{3}{b_2} - \dfrac{2}{b_1} + \dfrac{2}{a_2} - \dfrac{2}{a_1} + \dfrac{2}{r}, & R \le r \le a_1 \\ \dfrac{3}{b_2} - \dfrac{2}{b_1} + \dfrac{2}{a_2}, & a_1 \le r \le a_2 \\ \dfrac{3}{b_2} - \dfrac{2}{b_1} + \dfrac{2}{r}, & a_2 \le r \le b_1 \\ \dfrac{3}{b_2}, & b_1 \le r \le b_2 \\ \dfrac{3}{r}, & r \ge b_2\end{cases}}$$`
     > `Conexión ($S$ cerrado): $Q_{a_2} = Q_{b_1} = 0$, $Q_{a_1} = -2Q$ y $Q_{b_2} = 3Q$ ($\sigma_{a_2} = \sigma_{b_1} = 0$, $\sigma_{a_1} = -\frac{Q}{2\pi a_1^2}$, $\sigma_{b_2} = \frac{3Q}{4\pi b_2^2}$).`

3. **Declarar unidades SI en la primera aparición de símbolos en `u03-mapa` L23 y en enunciados simbólicos (SPEC §9.2)**
   - **Ubicación:** `unidades/u03-potencial.html`, `#u03-mapa` L23 y `#u03-p4` L379 (y análogos en `u03-e3` L232, `u03-x1` L258, `u03-x2` L280, `u03-p2` L337, `u03-p5` L401).
   - **Texto propuesto para L23:**
     > `...ley de Gauss $\oint \vec E\cdot d\vec A = Q_{\text{enc}}/\varepsilon_0$ (con $d\vec A$ en $\text{m}^2$, $\varepsilon_0 = 8{,}85\times10^{-12}\ \text{C}^2/(\text{N·m}^2)$, $k = \frac{1}{4\pi\varepsilon_0}$ en $\text{N·m}^2/\text{C}^2$, y $Q_{\text{enc}} = \int_0^r \rho(r')\,4\pi r'^2\,dr'$ con $\rho$ en $\text{C/m}^3$ si $\rho$ es esféricamente simétrica)...`
   - **Texto propuesto para `u03-p4` L379:** agregar `(en m)`, `(en C)` y `con $\beta$ en $\text{C/m}^5$` tras `$\rho(r) = \beta r^2$`.

4. **Cerrar los saltos en `u03-p4` Paso 4 (L390) y `u03-s1` (L49, L54, L57)**
   - **Ubicación:** `unidades/u03-potencial.html`, `#u03-p4` L390 y `#u03-s1` L54, L57.
   - **Texto propuesto para `u03-p4` L390:**
     > `al cerrar $S$, ambos cascarones forman un único equipotencial ($V(a_2) = V(b_1)$). Como entre $a_2$ y $b_1$ no hay carga y la simetría es esférica, $V(a_2) - V(b_1) = \int_{a_2}^{b_1} \frac{Q_{\text{enc}}(a_2)}{4\pi\varepsilon_0 r^2}\,dr = 0$ implica $Q_{\text{enc}}(a_2) = 0$ y, por tanto, $\vec E = \vec 0$ entre $a_2$ y $b_1$.`
   - **Texto propuesto para `u03-s1` L54:** reemplazar `$U = -\Delta W_{\infty\to r}$` por `$U = -W_{\infty\to r}$`. En L57 agregar: `Como el potencial creado en $\vec r_i$ por las demás cargas será $V_i = k\sum_{j\neq i} \frac{q_j}{r_{ij}}$ (definido en la siguiente sección), resulta $U = \frac12\sum_{i=1}^N q_i V_i$.`

5. **Completar límites/dimensiones en `li.check` (SPEC §3.6, §9.8) y evitar sobrecarga de `$r_0$` en `u03-p2`**
   - **Ubicación:** `u03-p5` L413 (agregar análisis dimensional de $v_f$), `u03-e1` L201, `u03-e2` L223, `u03-e3` L244, `u03-x1` L271, `u03-p1` L328, `u03-p3` L370, `u03-p4` L392 (agregar un límite); y `u03-p2` L337 (usar $R$ en lugar de $r_0$ para el radio del disco, reservando $r_0$ para la referencia de distribuciones infinitas).
   - **Texto propuesto para `u03-p5` L413 (agregar al final):**
     > `Unidades de $v_f$: $\sqrt{\frac{\text{C}\cdot(\text{C/m})}{(\text{C}^2/\text{N·m}^2)\cdot\text{kg}}} = \sqrt{\frac{\text{N·m}}{\text{kg}}} = \text{m/s}$.`
   - **Texto propuesto para `u03-e3` L244 (agregar al final):**
     > `Límite $R_2 \gg R_1$: $q_1 \to 0$, $q_2 \to Q_0$ y $\Delta U \to -\frac{kQ_0^2}{2R} = -U_i$ (toda la energía inicial se disipa al pasar la carga a una esfera enorme de potencial nulo).`
