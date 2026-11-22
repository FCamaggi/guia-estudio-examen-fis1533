# Reporte G4 (Autosuficiencia) — Unidad 6: Circuitos DC, Kirchhoff y RC

- **Archivo auditado:** `unidades/u06-circuitos-dc.html`
- **Contrato de referencia:** `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5, §9)
- **Perfil simulado:** Estudiante de segundo año de ingeniería que dispone **únicamente** de esta unidad (sin clases, sin otras unidades, sin calculadora y sin formulario) e intenta resolver cada problema sin abrir los pasos de solución.

---

## 1. Resolubilidad de arquetipos y problemas de práctica desde la unidad

| ID | Título / Fuente | ¿Resoluble solo con la unidad? | Paso que bloquea y por qué |
|---|---|---|---|
| `u06-x1` | Arquetipo 1 (Examen 2021-2 · Ej. 1) | **Sí** | Ninguno. La topología ($R_1$ en serie con $R_2 \parallel R_3$), la polaridad de $\mathcal{E}$ y los sentidos de $I_1, I_2, I_3$ están descritos en texto. Los métodos están en `u06-s1` y `u06-s2`; resultado simbólico. |
| `u06-x2` | Arquetipo 2 (Examen 2022-2 · P5) | **Sí** | Ninguno. La topología de dos mallas, las polaridades de $\varepsilon_1, \varepsilon_2, \varepsilon_3$, la ubicación de $P_1, P_2, P_3$ y el sentido de $I_3$ están explícitos en el enunciado. Se resuelve por LCK e independencia del camino para $\Delta V = V_2 - V_1$ (`u06-s2` y primer `Repaso exprés`); aritmética exacta a mano ($R_1 = 32\ \Omega$). |
| `u06-x3` | Arquetipo 3 (Examen 2026-1 · P1B) | **Sí** (con detalle menor en d) | No bloquea, aunque en la parte d) el enunciado dice *"Asuma conocida la carga inicial del capacitor $q(t = 0)$"* sin nombrar el símbolo $q_i$ que luego aparece en `Datos` (`$q(0)=q_i$ (C)`) y en `li.final`, y sin explicitar en d) la polaridad de esa carga inicial (se hereda de b), $V_b \gt V_c$). Topología y métodos ($t\to\infty$ en `u06-s5`, dieléctrico $\kappa$ en `Repaso exprés` 2, $R_{\text{Th}}$ y descarga en `u06-s5` y `Repaso exprés` 4) están completos. |
| `u06-p1` | Práctica 1 (Control 2, 2025-2, P1) | **No (bloqueado sin figura)** | **Bloquean Pasos 1–4.** El enunciado no describe la topología de la red: no indica cómo se conectan $R_1, R_2, R_3, R_6, R_7, R_8$ a la izquierda de $\varepsilon_1$ (cuáles van en serie y cuáles en paralelo), ni dónde se ubica $\varepsilon_2$ (rama superior o inferior del lazo derecho, lo cual cambia el significado de "+ a la derecha" respecto del sentido horario) ni cómo se conectan $R_4$ y $R_5$. |
| `u06-p2` | Práctica 2 (Pauta I2, 2025-2, P1 c–e) | **Sí** | Ninguno. La topología ($\mathcal{E}$ en serie con $S$ y $R_1$ alimentando $R_2 \parallel C$) está completamente descrita en palabras y coincide con la derivación de `u06-s5`. |
| `u06-p3` | Práctica 3 (Control 2, 2026-1, P1) | **No (bloqueado sin figura)** | **Bloquean Pasos 1–3.** El enunciado no especifica qué elemento ocupa cada rama del cuadrilátero $a$–$b$–$c$–$d$ con nodo central $e$: no dice dónde están $R_1, R_2, R_3, R_4, R_5$, ni en qué rama está $\mathcal{E}_1$ ni cuál es su polaridad, ni qué rama contiene a $\mathcal{E}_2$ ni si esa rama tiene resistencia. (El pie de figura tampoco basta: solo indica la polaridad de $\mathcal{E}_2$.) |
| `u06-p4` | Práctica 4 (Ayudantía 25, P1, 2026-2) | **No (bloqueado sin figura)** | **Bloquean Pasos 1–3.** El enunciado no describe cómo están conectados $\mathcal{E}, R_1, R_2, R_3, C_1, C_2$ ni el interruptor $S$ en las posiciones $1$ y $2$. Sin la figura, no se sabe si $R_1$ y $R_3$ están en serie o paralelo en $1$, ni si en $2$ queda una malla única $C_1$–$R_1$–$R_2$–$C_2$. |
| `u06-e3` *(nota)* | Ejemplo 3 (Red $RC$ de dos mallas) | **No (bloqueado sin figura)** | **Bloquean Pasos 1–3.** El enunciado (línea 221) no describe la topología ($\varepsilon$ y $S$ en serie con $R_1$ alimentando a $R_2 \parallel C$), ni la polaridad de $\varepsilon$, ni qué rama lleva $i_1, i_2, i_C$ y sus sentidos de referencia. |

---

## 2. Saltos en derivaciones

1. **`u06-s4` (línea 140, balance energético en carga):**
   En el cálculo de la energía disipada en $R$,
   > `$W_R = \displaystyle\int_0^\infty i^2 R\,dt = \frac{\varepsilon^2}{R}\int_0^\infty e^{-2t/\tau}\,dt = \frac{\varepsilon^2}{R}\left(\frac{\tau}{2}\right)$`
   se evalúa la integral impropia directamente sin escribir la primitiva evaluada $\Big[-\frac{\tau}{2}e^{-2t/\tau}\Big]_0^\infty$ (en contraste con `SPEC-PEDAGOGICO.md` §9.9: *"Cada derivación pasa por todos los pasos algebraicos (planteo de la integral, primitiva evaluada, separación de variables)"*).
2. **`u06-s3` (línea 113, error del voltímetro real):**
   Se afirma que sustituir $R$ por $R_\parallel = \frac{R\,r_V}{R+r_V} \lt R$ *"reduce la caída de voltaje en esa parte del circuito y el voltímetro lee menos"*, pero no se muestra la expresión algebraica del divisor con una resistencia en serie $R_s$ (aunque sí se resuelve un caso numérico en `u06-e1`).
3. **`u06-p3` (líneas 413–415, Paso 1):**
   En la primera y tercera malla se sustituyen simultáneamente $I_5 = I_2 + I_3$ e $I_1 = I_2 + I_3 + I_4$ en la misma línea sin mostrar el paso intermedio de agrupación (p. ej. `-I_5 R + \mathcal{E}_1 - I_3 R + I_4 R = 0 \implies \mathcal{E}_1 = R(2I_3 - I_4 + I_2)`).

---

## 3. Símbolos usados antes de su definición o sin unidades SI

1. **Símbolo sobrecargado $\varepsilon$ (fem vs. permitividad) y mezcla $\varepsilon / \mathcal{E}$:**
   - En `u06-mapa` (`Repaso exprés` 1, línea 23), `u06-s2`, `u06-s3`, `u06-s4`, `u06-s5`, `u06-e1..e3`, `u06-p1`, `u06-quiz-1` y `u06-formulas`, $\varepsilon$ denota **fem (V)**.
   - En `Repaso exprés` 2 (líneas 27–28), $\varepsilon = \kappa\varepsilon_0$ denota **permitividad eléctrica (F/m)**, usando el mismo símbolo $\varepsilon$ que cuatro líneas antes era fem.
   - Además, `u06-x1..x3` y `u06-p2..p4` cambian a $\mathcal{E}$ para la fem sin declarar la equivalencia $\varepsilon \equiv \mathcal{E}$.
2. **Símbolos sin definición o sin unidades SI en su primera aparición:**
   - **`Repaso exprés` 1 (líneas 22–23):** en $\Delta V = V_b - V_a = -\int_a^b \vec E\cdot d\vec\ell$, ni $\vec E$ (V/m) ni $d\vec\ell$ (m) están definidos ni llevan unidades SI. En la línea 23, $V_{\text{term}}$ no indica explícitamente su unidad `(V)`.
   - **`Repaso exprés` 2 (líneas 28 y 37):** $C_0$ en $C = \kappa C_0$ (línea 28) aparece sin definir explícitamente (capacitancia en vacío, F). En la línea 37, $i_C$ (A) y $t$ (s) se usan en $i_C = \pm dq/dt$ antes de definirse con unidades en `u06-s4`.
   - **`Repaso exprés` 4 (línea 49):** $t$ (s), $q(t)$ (C), $q_0$ (C) y $Q_0$ (C, línea 51) aparecen sin indicar unidades SI explícitas en ese recuadro.
   - **`u06-s2` (línea 102, `.why`):** *"agregando la caída $q/C$ o $L\,di/dt$"* — $L$ (inductancia, H) se usa sin haberse definido en la unidad.
   - **`u06-s3` (línea 110, `.note`):** $I_{\text{med}}$ (A) y $R_{\text{circ}}$ ($\Omega$) aparecen en la ecuación principal sin estar definidos ni con unidades SI en el `.note` de la caja.
   - **`u06-s5` (línea 159, `.note`):** $R_{\text{Th}}$ se define en el `.note`, pero falta indicar su unidad `($\Omega$)`.
   - **`u06-x1` (línea 249 y 254):** $I_2$ e $I_3$ en el enunciado no llevan `(A)` (aunque $I_1$ sí); en `Piden` (línea 254) aparece $V_3$ (V), símbolo que no se nombra en el enunciado.
   - **`u06-x3` (líneas 306–311):** `Datos` introduce `$q(0)=q_i$ (C)`, pero $q_i$ no aparece en el enunciado (que dice $q(t=0)$); y $\kappa$ en `Datos` no aclara `(adimensional)`.
   - **`u06-p4` (línea 431):** en el párrafo del enunciado, $\mathcal{E}, R_1, R_2, R_3, C_1, C_2$ aparecen sin unidades SI (solo figuran en `Datos`).
   - **`u06-formulas` (líneas 508, 511):** en la fila de descarga (508) faltan unidades de $Q_0$ (C) y $R_{\text{eq}}$ ($\Omega$); en la fila de energía de carga (511) faltan unidades de $W_\varepsilon, U_C, W_R$ (J).

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

No hay referencias externas a otras unidades o clases ("ver clase X"). Sin embargo, existen **dependencias colgantes de las figuras**:
1. **`u06-s3` (líneas 110 y 114, puente de Wheatstone):** la ecuación $R_x = R_3\,\frac{R_2}{R_1}$ y las igualdades *"luego $I_{\text{izq}} R_1 = I_{\text{der}} R_2$ y $I_{\text{izq}} R_3 = I_{\text{der}} R_x$"* invierten la numeración respecto de `u06-s1` (línea 66: $R_1/R_2 = R_3/R_4$). En `u06-s3` no se dice en texto qué posición ocupa cada resistencia ($R_1, R_3$ en la rama izquierda; $R_2, R_x$ en la derecha), por lo que el lector depende por completo del panel c) de `u06-medidores` para no contradecirse con `u06-s1`.
2. **`u06-e3`, `u06-p1`, `u06-p3`, `u06-p4`:** los enunciados dicen *"En el circuito de la figura..."* sin describir la topología ni las polaridades/sentidos en texto (ver sección 1 y 7).

---

## 5. Prerrequisitos usados pero no cubiertos por los recuadros `Repaso exprés`

1. **Conservación de la carga en placas aisladas al conmutar capacitores (`u06-p4`, líneas 438 y 442):**
   Al pasar el interruptor $S$ a la posición $2$, se usa $Q_1'(t') + Q_2(t') = \mathcal{E}C_1$ por conservación de la carga en las placas superiores conectadas entre sí y aisladas del resto. El `Repaso exprés` 2 (líneas 26–38) cubre capacitancia, energía, dieléctricos, asociación serie/paralelo y continuidad $\Delta V_C(0^+) = \Delta V_C(0^-)$, pero **no incluye** la regla de conservación de carga en placas aisladas al reconectar capacitores.
2. **Integral impropia exponencial (menor):** `u06-s4` (líneas 140 y 142) usa $\int_0^\infty e^{-2t/\tau}\,dt = \tau/2$, que no figura en `Repaso exprés` 4 (aunque es cálculo básico estándar).

---

## 6. Violaciones a `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§3 (Formato de problema guiado) y §9.6 (Enunciados autosuficientes sin figura):**
  - `u06-e3`, `u06-p1`, `u06-p3` y `u06-p4` no tienen enunciado completo sin depender de la figura.
  - `u06-x1` (`Piden` usa $V_3$, no nombrado en el enunciado) y `u06-x3` (`Datos` usa $q_i$, no nombrado en el enunciado).
- **§5 (Convenciones de notación):**
  - En §5 se define $\Delta V = V_b - V_a$ y $V_{ab} = V_a - V_b$. En `u06-s1` (línea 60, pie de figura) se escribe `$\Delta V_{ab}$`, mezclando ambas notaciones; en `u06-x3` (línea 320) se escribe `$\Delta V_{ad} = I_{\text{bat}} R_p$` (cuando $V_a - V_d \gt 0$, que corresponde a $V_{ad}$ o $-\Delta V_{ad}$ según §5).
- **§9.1 (Cálculos a mano sin calculadora):**
  - **Cumplido** en todos los problemas: los valores numéricos de `u06-e1`, `u06-e2`, `u06-e3`, `u06-x2`, `u06-p1` y `u06-p3` dan fracciones simples o decimales exactos a mano; `u06-x1`, `u06-x3`, `u06-p2` y `u06-p4` son simbólicos.
- **§9.2 (Unidades SI en la primera aparición de cada símbolo):**
  - Incumplimientos listados en la sección 3 (especialmente $\vec E, d\vec\ell, V_{\text{term}}, C_0, t, L, I_{\text{med}}, R_{\text{circ}}, R_{\text{Th}}$ y las unidades faltantes en el enunciado de `u06-p4` y filas de `u06-formulas`).
- **§9.4 (`li.final` contiene todo lo que pide el enunciado):**
  - Cumplido en 9 de los 10 problemas (`u06-e1..e3`, `u06-x1..x3`, `u06-p1, p3, p4`).
  - **Incumplimiento menor en `u06-p2` (línea 394):** `Piden` solicita explícitamente `EDO`, pero `li.final` incluye las ecuaciones de Kirchhoff, $q(t)$, $\tau$ y $q(\infty)$, omitiendo la EDO $\tau\frac{dq}{dt} + q = \frac{R_2}{R_1+R_2}\mathcal{E}C$.
- **§9.5 (Sin símbolos sobrecargados):**
  - **Violación:** $\varepsilon$ se usa tanto para **fem (V)** como para **permitividad (F/m)** en `Repaso exprés` 2 (líneas 27–28), además de coexistir $\varepsilon$ y $\mathcal{E}$ para fem entre teoría/ejemplos y arquetipos/práctica.
- **§9.9 (HTML y derivaciones completas):**
  - Las desigualdades en fórmulas usan correctamente `\lt` y `\gt`.
  - Falta un paso explícito de primitiva evaluada en la integral de `u06-s4` (línea 140).

---

## 7. Correcciones más valiosas (ordenadas por prioridad)

1. **[Alta] Hacer autosuficiente el enunciado de `u06-p1` (línea 357):**
   Reemplazar el inicio de `<p class="stmt">` en `#u06-p1` por:
   > `(Basado en Control 2, 2025-2, P1.) En el circuito de la figura, una batería ideal central $\varepsilon_1 = 16\ \text{V}$ (borne $+$ arriba, $-$ abajo) conecta dos sectores entre el riel superior y el inferior: hacia la izquierda, el riel superior pasa por $R_3 = 4\ \Omega$ hasta un nodo en el que baja $R_6 = 8\ \Omega$ en paralelo con una subred formada por $R_1 = 2\ \Omega$ (tramo superior), el paralelo vertical $R_7 \parallel R_8$ ($R_7 = R_8 = 8\ \Omega$) y $R_2 = 2\ \Omega$ (tramo inferior de retorno); hacia la derecha de $\varepsilon_1$, un lazo en serie recorre en sentido horario $R_4 = 3\ \Omega$ (arriba), $R_5 = 1\ \Omega$ (rama derecha) y la batería ideal $\varepsilon_2 = 8\ \text{V}$ en la rama inferior (borne $+$ a la derecha, $-$ a la izquierda). Con los valores $R_1 = R_2 = 2\ \Omega$, $R_3 = 4\ \Omega$, $R_4 = 3\ \Omega$, $R_5 = 1\ \Omega$ y $R_6 = R_7 = R_8 = 8\ \Omega$: a) Calcula la resistencia equivalente...`

2. **[Alta] Hacer autosuficiente el enunciado de `u06-p3` (línea 404):**
   Reemplazar `<p class="stmt">` en `#u06-p3` por:
   > `(Basado en Control 2, 2026-1, P1.) En el circuito plano de la figura, un cuadrilátero de nodos $a$–$b$–$c$–$d$ tiene un nodo central $e$ conectado a $a$, $b$ y $d$ del modo siguiente: la rama $a$–$d$ contiene a $R_1$, la rama $b$–$a$ a $R_2$, la rama $b$–$e$ a $R_3$, la rama $d$–$e$ a $R_4$, la rama $d$–$c$–$b$ contiene a $R_5$ (entre $d$ y $c$) en serie con la fem ideal $\mathcal{E}_1 = 10\ \text{V}$ (entre $c$ y $b$, borne $+$ hacia $b$ y $-$ hacia $c$), y la rama $e$–$a$ contiene únicamente la fem ideal $\mathcal{E}_2 = 6\ \text{V}$ (borne $+$ hacia $a$ y $-$ hacia $e$). Todas las resistencias son iguales: $R_1 = R_2 = R_3 = R_4 = R_5 = R = 1\ \Omega$. Con los sentidos de corriente dibujados ($I_1$: $a\to d$; $I_2$: $b\to a$; $I_3$: $b\to e$; $I_4$: $d\to e$; $I_5$: $d\to c\to b$): a) calcula las corrientes $I_1, I_2, I_3, I_4, I_5$ (en A). b) Determina la diferencia de potencial $V_b - V_d$ (en V).`

3. **[Alta] Hacer autosuficiente el enunciado de `u06-p4` (línea 431) + añadir unidades SI:**
   Reemplazar `<p class="stmt">` en `#u06-p4` por:
   > `(Basado en Ayudantía 25, P1, 2026-2.) En el circuito de la figura, una rama central conecta el riel inferior con el polo móvil de un interruptor $S$ de dos posiciones mediante un capacitor $C_1$ (F) en serie con un resistor $R_1$ ($\Omega$, junto a $S$). En la posición $1$, $S$ cierra una malla izquierda que conecta dicha rama central con una fuente ideal de fem $\mathcal{E}$ (V, borne $+$ arriba, $-$ abajo) en serie con un resistor $R_3$ ($\Omega$); en la posición $2$, $S$ aísla la fuente y cierra una malla derecha que conecta la rama $C_1$–$R_1$ en serie con un resistor $R_2$ ($\Omega$) y un segundo capacitor $C_2$ (F). Ambos capacitores $C_1$ y $C_2$ están inicialmente descargados. En $t = 0$ el interruptor $S$ pasa a la posición $1$. Determina: a) la corriente $I_0$ que entrega la fuente $\mathcal{E}$ en $t = 0^+$; b) la carga máxima $Q_{\text{máx}}$ de $C_1$; c) $q_1(t)$ en $C_1$ mientras $S$ está en $1$. Luego de mucho tiempo, en un nuevo $t' = 0$, $S$ se pasa a la posición $2$: d) halla la carga $Q_1'(t')$ en $C_1$ para $t' \gt 0$.`

4. **[Alta] Hacer autosuficiente el enunciado de `u06-e3` (línea 221):**
   Reemplazar el inicio de `<p class="stmt">` en `#u06-e3` por:
   > `En el circuito de la figura, una fuente ideal de fem $\varepsilon = 12\ \text{V}$ (borne positivo arriba, negativo abajo) está conectada en serie con un interruptor $S$ y un resistor $R_1 = 6{,}0\ \Omega$ en el tramo superior hacia un nodo donde la corriente $i_1$ (A, hacia la derecha por $R_1$) se divide en dos ramas verticales en paralelo hacia el riel inferior de retorno: $R_2 = 3{,}0\ \Omega$ (con corriente $i_2$ hacia abajo) y el condensador $C = 5{,}0\ \mu\text{F}$ inicialmente descargado (con corriente $i_C$ hacia abajo entrando a su placa superior). En $t = 0$ se cierra el interruptor $S$. a) Halla las corrientes...`

5. **[Media] Eliminar la sobrecarga de $\varepsilon$ en `Repaso exprés` 2 (líneas 27–28) y aclarar $\varepsilon \equiv \mathcal{E}$:**
   En la línea 27, reemplazar `con $\varepsilon = \kappa\varepsilon_0$ permitividad en $\text{F/m}$` por `con $\varepsilon_{\text{diel}} = \kappa\varepsilon_0$ permitividad en $\text{F/m}$ (no confundir con la fem $\varepsilon$ o $\mathcal{E}$)` y actualizar la fórmula de la línea 28 a `= \frac{\varepsilon_{\text{diel}} A}{d}`, declarando además en la línea 23 `$\varepsilon$ (o $\mathcal{E}$, en V)`.

6. **[Media] Aclarar la posición de las resistencias en el puente de `u06-s3` (línea 114) para no depender de la figura:**
   En la línea 114, añadir después de `hasta que la corriente por el galvanómetro central sea exactamente $I_G = 0$.`:
   > `En el esquema del panel c), $R_1$ (arriba) y $R_3$ (abajo) forman la rama izquierda, mientras $R_2$ (arriba) y $R_x$ (abajo) forman la rama derecha.`

7. **[Media] Añadir conservación de carga en placas aisladas al `Repaso exprés` 2 (antes de línea 37):**
   Insertar un párrafo breve en el segundo `Repaso exprés`:
   > `<p><b>Redistribución de carga:</b> si dos capacitores cargados se conectan entre sí tras desconectar las fuentes, la carga neta en las placas unidas y aisladas del resto se conserva: $q_1 + q_2 = \text{cte.}$, y en equilibrio igualan sus voltajes ($q_1/C_1 = q_2/C_2$).</p>`

8. **[Baja] Completar `li.final` de `u06-p2`, primitiva en `u06-s4` y unidades SI menores:**
   - En `u06-p2` (línea 394), agregar `\tau\frac{dq}{dt} + q = \frac{R_2}{R_1+R_2}\mathcal{E}C` al recuadro de `li.final`.
   - En `u06-s4` (línea 140), insertar `= \frac{\varepsilon^2}{R}\Big[-\frac{\tau}{2}e^{-2t/\tau}\Big]_0^\infty` antes de `= \frac{\varepsilon^2}{R}\left(\frac{\tau}{2}\right)`.
   - En `u06-x3` (línea 310), escribir `carga inicial $q_i = q(t=0)$` para alinear el enunciado con `Datos` y `li.final`.
   - Añadir las unidades faltantes en `Repaso exprés` 1 ($\vec E$ en V/m, $d\vec\ell$ en m, $V_{\text{term}}$ en V), `Repaso exprés` 2 ($C_0$ en F), `Repaso exprés` 4 ($t$ en s, $q, q_0, Q_0$ en C), `u06-s2` ($L$ en H), `u06-s3` ($I_{\text{med}}$ en A, $R_{\text{circ}}$ en $\Omega$) y `u06-s5` ($R_{\text{Th}}$ en $\Omega$).
