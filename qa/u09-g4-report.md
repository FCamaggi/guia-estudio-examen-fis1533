# Reporte de Revisión G4 (Autosuficiencia) — Unidad U9: Inducción electromagnética

- **Archivo revisado:** `unidades/u09-induccion.html`
- **Contrato pedagógico:** `SPEC-PEDAGOGICO.md`
- **Perfil simulado:** Estudiante de ingeniería de segundo año con **solo** esta unidad (sin clases, sin ayudantías, sin otras unidades, sin calculadora y sin formulario externo).

---

## 1. Evaluabilidad de arquetipos (`u09-x1`..`u09-x4`) y problemas de práctica (`u09-p1`..`u09-p5`)

### Arquetipos de examen (`#u09-examen`)

#### `u09-x1` · Espira cuadrada que entra a una zona con campo (Examen 2026-1 · P2)
- **¿Puede resolverlo el estudiante solo con la unidad?** **Sí, por completo.**
- **Trazabilidad en la unidad:**
  - El flujo parcial en función del área inmersa está explícito en `u09-s1` (línea 65: *"Si el campo existe solo en una parte de la espira, usa solo el área donde hay campo"*), en `u09-s2` (línea 75) y en `u09-errores` (línea 377).
  - La fem y el sentido están cubiertos en `u09-s2` (Faraday, Lenz y regla de signos) y `u09-s3` (línea 131: *"Si la espira está completamente dentro de un campo uniforme, la fem neta es cero aunque se mueva"*).
  - La fuerza externa en la parte b) se resuelve con `u09-s2` (línea 87: *"cuando la causa es un movimiento, la fuerza magnética sobre la corriente inducida frena ese movimiento"*) y con el mini ejemplo de ejes cartesianos del `Repaso exprés` 1 (línea 25).
- **Posibles puntos de fricción (sin bloqueo):** El enunciado dice *"campo magnético constante $\vec B$ entrante"* (línea 286) usando "constante" para referirse a un campo uniforme en el espacio (y constante en el tiempo); la figura `u09-espira-entrando` lo aclara visualmente. No hay bloqueo.

#### `u09-x2` · Lazo rectangular que se aleja de un alambre infinito (Examen 2024-1 · P2)
- **¿Puede resolverlo el estudiante solo con la unidad?** **Sí, por completo.**
- **Trazabilidad en la unidad:**
  - Parte a): `Repaso exprés` 2 (líneas 29–31) deduce $B(s) = \dfrac{\mu_0 I}{2\pi s}$ con la ley de Ampère y da la regla de la mano derecha para un alambre vertical.
  - Parte b): La derivación completa del flujo está resuelta literalmente en `u09-s1` (`details.deriv`, líneas 56–62).
  - Parte c): La derivada temporal del logaritmo $\dfrac{d}{dt}\ln\!\left(\dfrac{r+w}{r}\right) = -\dfrac{w}{r(r+w)}\dfrac{dr}{dt}$ está en `Repaso exprés` 4 (línea 41), y el resultado con fem de movimiento $\varepsilon = \ell v\,[B(r) - B(r+w)]$ aparece como control cruzado en `u09-s3` (línea 115).
- **Bloqueos:** Ninguno.

#### `u09-x3` · Espira que cae en un campo que depende de la altura (Examen 2025-2 · P2)
- **¿Puede resolverlo el estudiante solo con la unidad?** **Parcialmente; riesgo de bloqueo en d) (y confusión menor en el enunciado).**
- **Dónde se bloquearía el estudiante y por qué:**
  1. **Paso bloqueante — Parte d) (`Paso 4`, línea 342):** La unidad solo enseña $\vec F = I\,\vec\ell\times\vec B$ para *"un tramo recto de cable con corriente"* (`Repaso exprés` 1, línea 24) y en la tarjeta de fórmulas especifica explícitamente validez solo con *"$\vec B$ uniforme sobre el tramo"* (`u09-formulas`, línea 546). Nunca se presenta la forma diferencial $d\vec F = I\,d\vec\ell\times\vec B$ ni ningún ejemplo previo con fuerza neta sobre una espira de cuatro lados en campo no uniforme $\vec B(z)$. Un estudiante riguroso que solo tiene la unidad se queda sin justificación formal para los lados verticales (donde $B(z)$ cambia punto a punto) y podría intentar aplicar erróneamente la fórmula de barra $F_B = B^2 a^2 v / R$ de `u09-s3` (línea 118).
  2. **Término no definido en el enunciado (línea 331):** *"de resistencia $R$ y autoinducción despreciable"*. El concepto de *autoinducción* no se define ni menciona en ninguna sección de teoría ni en `Repaso exprés`. Aunque al decir "despreciable" no impide calcular si se ignora, un estudiante que solo tiene U9 puede quedar desconcertado pensando que falta un efecto físico.
  3. **Signo de $v_z$ en b) (`Paso 2`, línea 340):** En la teoría (`u09-s2`, `u09-s3`) no se advierte explícitamente que $dz/dt = -|v|$ cuando la coordenada $z$ decrece al caer; esto solo aparece en la caja `.trap` de `u09-errores` (línea 379). Si el estudiante lee `u09-errores`, lo resuelve; si solo lee teoría, puede equivocar el signo de $\varepsilon$.

#### `u09-x4` · Espira grande que se acerca a una espira pequeña coaxial (Examen 2024-2 · P4)
- **¿Puede resolverlo el estudiante solo con la unidad?** **Mayormente sí, con dos roces en a) y c) que no llegan a bloquear si se usa Lenz.**
- **Dónde podría frenarse el estudiante y por qué:**
  1. **Dirección de $\vec B$ a ambos lados de la espira (`Paso 1` y `Paso 3`, líneas 362–364):** `Repaso exprés` 3 (líneas 35–36) da la magnitud $B(d) = \dfrac{\mu_0 I R^2}{2(R^2 + d^2)^{3/2}}$ *"a lo largo del eje"*, pero **no indica** la regla de la mano derecha para una espira circular ni que $\vec B$ apunta en el mismo sentido a ambos lados del plano de la espira ($d \gt 0$ y $d \lt 0$). Al cruzar al lado derecho ($t \gt z/v$), el estudiante tiene que inferirlo por su cuenta (aunque la tabla de `u09-s2`, líneas 88–93, muestra ejemplos de mano derecha para espira y Lenz basta para el sentido en c)).
  2. **Ambigüedad de símbolo $z$ y resistencia faltante (líneas 354–355):** El enunciado usa $z$ como la distancia inicial en $t = 0$ (*"En $t = 0$ la distancia entre ambas es $z$"*) mientras que $\hat z$ (y el eje $z$ de la figura) es la coordenada espacial. Además, no define ningún símbolo para la resistencia de la espira pequeña (la letra $R$ ya es el radio de la espira grande), lo que puede confundir al intentar escribir $I_{\text{ind}}(t)$ antes de evaluar los casos donde $\varepsilon = 0$.

---

### Problemas de práctica (`#u09-practica`): ¿se resuelven solo con la teoría, sin abrir los pasos?

- **`u09-p1` (Generador de corriente alterna):** **Sí.** `u09-s5` (líneas 156–157) entrega las expresiones exactas $\Phi_B = BA\cos(\omega t)$, $\varepsilon(t) = NBA\omega\sin(\omega t)$, $\varepsilon_{\text{máx}} = NBA\omega$ y explica cuándo ocurre el máximo. La aritmética es directa sin calculadora.
- **`u09-p2` (Espira fija junto a un alambre con corriente creciente):** **Sí.** `u09-s1` (líneas 56–61) deduce el flujo exacto del alambre sobre la espira, y `u09-s2` enseña a derivar respecto del tiempo y obtener corriente y sentido por Lenz.
- **`u09-p3` (Espira larga que cae entrando a un campo):** **Sí.** `u09-s1` (línea 65) cubre el flujo sobre el área inmersa; `u09-s3` (líneas 125–128) y `Repaso exprés` 4 (línea 43) resuelven exactamente la ecuación $m\dot v = mg - \dfrac{B^2 a^2}{R}v$ y $v_{\text{term}}$.
- **`u09-p4` (Barra impulsada por una batería: velocidad límite):** **Con dificultad / salto desde la teoría.** La teoría en `u09-s5` (línea 158) menciona solo de forma cualitativa la fuerza contraelectromotriz (*"la bobina induce una fem que, por Lenz, se opone a la corriente de la fuente"*), y ni la teoría ni los ejemplos `e1..e4` muestran un circuito con batería + barra móvil ni plantean la regla de mallas $I = (V_0 - \varepsilon_{\text{ind}})/R$. El estudiante debe conectar por sí solo la nota cualitativa de `u09-s5` con la fem de movimiento de `u09-s3` y la EDO de `Repaso exprés` 4.
- **`u09-p5` (Campo magnético entre las placas de un condensador):** **Sí.** `u09-s6` (`details.deriv`, líneas 167–172) deduce exactamente las mismas expresiones para $I_D$ y $B(r)$ en $r \lt R$ y $r \gt R$.

---

## 2. Saltos en derivaciones

1. **`u09-s3` (línea 123) — Barra lanzada:** Se pasa directamente de $m\dfrac{dv}{dt} = -\dfrac{B^2\ell^2}{R}\,v$ a $v(t) = v_0\,e^{-t/\tau}$ con $\tau = \dfrac{mR}{B^2\ell^2}$, sin mostrar el reordenamiento $\dfrac{dv}{dt} = -\dfrac{v}{\tau}$ ni la separación de variables dentro de esa derivación (aunque luego sí aparece en `Repaso exprés` 4, línea 42, y en `u09-e3` Paso 2, línea 247).
2. **`u09-s3` (línea 124) — Distancia total:** Se escribe $\displaystyle\int_0^\infty v_0 e^{-t/\tau}\,dt = v_0\tau$ omitiendo la primitiva evaluada $[-\tau e^{-t/\tau}]_0^\infty$.
3. **`u09-s4` (línea 140) — Simetría de $\vec E$ en el solenoide:** Se descarta la componente radial usando Gauss (*"No puede ser radial, porque entonces habría flujo eléctrico neto a través de un cilindro coaxial sin carga dentro, lo que contradice la ley de Gauss. Entonces $\vec E$ es tangente a circunferencias coaxiales"*), pero **se omite descartar la componente axial $E_z$** antes de concluir que $\vec E$ es puramente tangencial.
4. **`u09-s4` (línea 146) — Paso a forma diferencial:** Se aplica *"por el teorema de Stokes, $\oint_C\vec E\cdot d\vec\ell = \int_S(\nabla\times\vec E)\cdot d\vec A$"* sin haber definido el operador rotacional $\nabla\times$ ni enunciado el teorema de Stokes previamente en la unidad.
5. **`u09-s6` (líneas 168 y 170) — Condensador y corriente de desplazamiento:**
   - Línea 168: Se afirma sin deducción *"Entre placas de área $A = \pi R^2$ con carga $q$: $E = \dfrac{q}{\varepsilon_0 A}$ (uniforme, despreciando bordes)"*.
   - Línea 170: Se salta directamente de la simetría a *"Una curva de radio $r \lt R$ encierra la fracción $r^2/R^2$ del flujo eléctrico, así que $I_{D,\text{enc}} = i\,r^2/R^2$"*, sin escribir explícitamente $\Phi_E(r) = E\,\pi r^2 = \dfrac{q}{\varepsilon_0}\dfrac{r^2}{R^2}$.
6. **`u09-e3` Paso 4 (línea 249) — Calor disipado:** Se escribe $Q_{\text{calor}} = \dfrac{B^2\ell^2 v_0^2}{R}\cdot\dfrac{\tau}{2}$ sin mostrar explícitamente el planteo de la integral $Q_{\text{calor}} = \displaystyle\int_0^\infty P_R\,dt = \displaystyle\int_0^\infty \dfrac{B^2\ell^2 v_0^2}{R}e^{-2t/\tau}\,dt$.
7. **`u09-x3` Paso 1 (línea 339) — Flujo de $\vec B(z)$:** Salta directamente a la primitiva evaluada $\Phi_B = a\left[B_0 z' - \tfrac{\alpha}{2}z'^2\right]_z^{z+a}$ sin escribir la integral $\displaystyle\int_z^{z+a}(B_0 - \alpha z')\,a\,dz'$ en el paso (la integral doble solo está en la pista colapsable `li.hint`).
8. **`u09-x3` Paso 4 (línea 342) — Fuerza neta sobre lados verticales:** Afirma *"Lados verticales: fuerzas $\pm\hat y$ iguales y opuestas, se cancelan"* aplicando $\vec F = I\vec\ell\times\vec B$ sin pasar por el elemento diferencial $d\vec F = I\,d\vec\ell\times\vec B(z')$, pese a que $\vec B$ varía con $z'$ a lo largo de esos lados.
9. **`u09-p4` Paso 1 (línea 464) — Corriente con batería y barra móvil:** Escribe directamente $I = \dfrac{V_0 - B_0 bv}{R}$ sin plantear la regla de mallas de Kirchhoff ($V_0 - \varepsilon_{\text{ind}} - IR = 0$) ni mostrar el signo de $\varepsilon_{\text{ind}}$ mediante Lenz/Faraday en el circuito de la figura.

---

## 3. Símbolos usados antes de definirse o definidos sin unidades SI

De acuerdo con `SPEC-PEDAGOGICO.md` §1 (*"Cada símbolo se define la primera vez que aparece en la unidad, con unidades SI"*):

1. **Bloque `u09-mapa` (líneas 7–19):** Aparecen $\varepsilon$, $\Phi_B$, $t$, $\vec B$, $Bax$, $v_{\text{term}}$ sin definición ni unidades SI al mencionarse por primera vez en la unidad.
2. **`Repaso exprés` 1 (línea 24):** En $\vec F = q\,\vec v\times\vec B$ y $\vec F = I\,\vec\ell\times\vec B$, aparecen $\vec F$ (N), $q$ (C), $\vec v$ (m/s), $\vec B$ (T), $I$ (A) y $\vec\ell$ (m) **sin unidades SI** (y $\vec F, q, \vec v, \vec B, I$ ni siquiera se nombran).
3. **`Repaso exprés` 2 (líneas 29–32):** $I_{\text{enc}}$ (A) y $s$ (*"radio $s$"*, falta m) aparecen sin unidades SI; $\vec B$ sigue sin unidad SI hasta la línea 53.
4. **`Repaso exprés` 3 (línea 35):** $R$ (*"radio $R$"*, falta m) y $d$ (*"distancia $d$"*, falta m) aparecen sin unidades SI.
5. **`Repaso exprés` 4 (líneas 40–43):**
   - Línea 40: $r$ y $w$ se usan en $\int_r^{r+w} ds/s$ antes de definirse (recién se definen en la línea 57, y sin unidades SI).
   - Líneas 42–43: $v$ (m/s), $v_0$ (m/s), $\tau$ (s), $v_\infty$ (m/s) y $g$ ($\text{m/s}^2$) aparecen sin definición ni unidades SI.
6. **`u09-s1` (línea 57):** $\ell$, $w$, $r$ y $s$ se definen en el pie de figura sin unidades SI (m).
7. **`u09-s2` (líneas 71, 96–97):**
   - Línea 71: $\vec E$ (V/m), $d\vec\ell$ (m) y $t$ (s) se usan en $\varepsilon = \oint\vec E\cdot d\vec\ell = -N\,\frac{d\Phi_B}{dt}$ sin definirse ni llevar unidades SI ($\vec E$ recién recibe la unidad V/m en la línea 272 durante la verificación de `e4`, y explícitamente en `u09-formulas`, línea 550).
   - Línea 96: *"resistencia total $R$"* se define sin unidad SI ($\Omega$); *"la carga total es $Q$"* (línea 96–97) se define sin unidad SI (C).
8. **`u09-s3` (líneas 107, 118–119, 123):**
   - Línea 107: $x$ (m) sin unidad SI.
   - Líneas 118–119: $F_B$ (N), $F_{\text{ext}}$ (N) y *"potencia"* $P$ (W) se usan sin declarar sus unidades SI (W solo aparece en `e2`, línea 227, y en `u09-formulas`, línea 547).
   - Línea 123: $m$ (kg) se usa sin declarar su unidad SI, y $\tau$ (s) aparece sin nombrarse ("constante de tiempo") ni dar su unidad en la definición (solo se comprueba después en la línea 129).
9. **`u09-s4` (líneas 138, 140):** El operador $\nabla\times$ nunca se define; *"potencial $V$"* (línea 138) y el radio $b$ del solenoide (línea 137) aparecen sin unidades SI.
10. **`u09-s6` (líneas 164, 168, 177–180, 183):**
    - Línea 164: $i$ (*"corriente $i$"*) sin unidad SI (A).
    - Línea 168: $q$ (*"carga $q$"*) sin unidad SI (C), $R$ (m) sin unidad SI.
    - Líneas 177–180 (tabla de Maxwell): $Q_{\text{enc}}$ (C) sin unidad SI; **$\rho$** (densidad volumétrica de carga, $\text{C/m}^3$) y **$\vec J$** (densidad de corriente, $\text{A/m}^2$) aparecen **sin ninguna definición ni unidad SI en toda la unidad**.
    - Línea 183: $c$ aparece sin nombre explícito (*"rapidez de la luz en el vacío"*) ni unidad SI (m/s).
11. **`u09-x3` (línea 331), `u09-p2` (línea 413), `u09-p4` (línea 457):**
    - `u09-x3`: $\alpha$ se introduce sin unidades SI ($\text{T/m}$); $B_0$ (T), $a$ (m), $m$ (kg), $R$ ($\Omega$) y $g$ ($\text{m/s}^2$) no declaran unidades en el problema simbólico.
    - `u09-p2`: $\beta$ se introduce sin unidades SI ($\text{A/s}$).
    - `u09-p4`: $v_\infty$ se usa en `Piden` y Paso 3 sin definirse formalmente como $\lim_{t\to\infty} v(t)$ (aunque el texto habla de "velocidad límite").

---

## 4. Referencias colgantes

- **No se encontraron referencias colgantes explícitas** a clases, ayudantías u otras unidades necesarias para seguir el razonamiento (no hay "ver clase...", "como vimos en U...", ni "como se vio antes").
- Las menciones a otras unidades son únicamente de contexto futuro y están permitidas: `(unidad U11)` en `u09-s5` (línea 157) y en `u09-s6` (línea 183).
- Las citas a exámenes y ayudantías (`Examen 2026-1 · P2`, `Ayudantía 21, 2026-2`, `pauta oficial`, etc.) cumplen función de trazabilidad o corrección de erratas de origen según `SPEC-PEDAGOGICO.md` §6, no de dependencia.
- *(Nota: sí hay resultados previos invocados sin recuadro `Repaso exprés` —como la ley de Gauss en la línea 140 y $E = q/(\varepsilon_0 A)$ en la línea 168—, que se detallan en la sección 5 por corresponder a prerrequisitos no embebidos.)*

---

## 5. Prerrequisitos usados pero no cubiertos por `Repaso exprés` (`details.prereq`)

Los cuatro recuadros `details.prereq` existentes (líneas 22–45) cubren producto cruz y regla de la mano derecha (cables y circulaciones), Ampère para alambre infinito y solenoide, magnitud de $B$ en el eje de una espira circular, y logaritmos / EDOs de primer orden. Sin embargo, la unidad utiliza los siguientes prerrequisitos **sin** recuadro `Repaso exprés`:

1. **Ley de Gauss eléctrica y campo eléctrico de un condensador de placas paralelas:**
   - Usada en `u09-s4` (línea 140) para descartar $E_r \neq 0$ mediante un cilindro coaxial sin carga encerrada.
   - Usada en `u09-s6` (línea 168) para afirmar $E = \dfrac{q}{\varepsilon_0 A}$ entre las placas.
   - *(La ley de Gauss aparece recién al final de `u09-s6` en la tabla de Maxwell, línea 177, y nunca se deduce $E = q/(\varepsilon_0 A)$.)*
2. **Regla de la mano derecha para el sentido de $\vec B$ creado por una espira circular (y simetría a ambos lados):**
   - `Repaso exprés` 2 (línea 31) da la regla para un *alambre recto* y `Repaso exprés` 3 (líneas 35–36) da solo la *magnitud* de $B(d)$ en el eje de una espira. Falta indicar que, al curvar los dedos con la corriente $I$ de una espira, el pulgar señala la dirección de $\vec B$ sobre el eje a **ambos lados** de la espira (necesario en `u09-s2`, líneas 88–93, y en `u09-x4`, líneas 362–364).
3. **Regla de mallas de Kirchhoff / fem en serie con una batería y potencia eléctrica ($P = I^2 R$):**
   - Usada en `u09-p4` (línea 464): $I = (V_0 - B_0 bv)/R$.
   - $P = I^2 R = \varepsilon^2/R$ usada en `u09-s3` (línea 119), `u09-e2` (línea 227), `u09-e3` (línea 249) y `u09-x3` (línea 345).
4. **Forma diferencial de la fuerza magnética ($d\vec F = I\,d\vec\ell\times\vec B$):**
   - Necesaria para integrar o argumentar cancelaciones en conductores inmersos en un campo no uniforme, como los lados verticales de `u09-x3` Paso 4 (línea 342).
5. **Cálculo vectorial básico ($\nabla\times$, $\nabla\cdot$ y teorema de Stokes):**
   - Usados en `u09-s4` (líneas 138, 146) y en la tabla de Maxwell de `u09-s6` (líneas 177–180).
6. **Derivadas de potencias con regla de la cadena y derivadas trigonométricas (cálculo I):**
   - $\dfrac{d}{dt}[R^2 + (z-vt)^2]^{-3/2}$ en `u09-x4` (línea 363) y $\dfrac{d}{dt}\cos(\omega t)$ en `u09-s5` (línea 156); `Repaso exprés` 4 solo repasa la derivada de $\ln((r+w)/r)$.

---

## 6. Violaciones al contrato respecto a `SPEC-PEDAGOGICO.md`

### A. Estructura obligatoria (§2) y Arquetipos con pauta (§2.5)
- **Bloques 1–9:** Los 9 bloques están presentes y cumplen los mínimos cuantitativos (1 mapa, 6 subtemas de teoría, 13 figuras, 4 ejemplos resueltos, 4 arquetipos, 7 cajas `.trap`, 5 prácticas, 7 preguntas en el quiz, 1 tarjeta de fórmulas).
- **Descuadre de puntajes en `u09-x2` (`§2.5`, líneas 309 vs 317–320):** El enunciado asigna `a) (2 pts.)`, `b) (2 pts.)`, `c) (2 pts.)` (total 6 pts), pero los pasos de solución suman solo **3,0 pts** (`Paso 1: 0,75 + 0,25 = 1,0`, `Paso 2: 0,5 + 0,5 = 1,0`, `Paso 3: 0,5 + 0,5 = 1,0`, `Paso 4`: sin puntaje asignado).
- **Tarjeta de fórmulas incompleta (`§2.9`, líneas 539–556):** El contrato exige *"Cada fórmula con significado de cada símbolo, condiciones de validez y unidades"*. En la tabla actual faltan significado y/o unidades en la columna `Significado` para varios símbolos introducidos en filas específicas (p. ej., $\vec v$ en línea 545; $F_B$, $R$, $P$ en línea 547; $v_0, \tau, m, x_{\text{total}}$ en línea 548; $v_{\text{term}}, F$ en línea 549; $r, b$ en línea 551; $f, A, t$ en línea 552; $I_D, \varepsilon_0, \Phi_E, I_{\text{enc}}$ en línea 554; $i, r, R, B$ en línea 555).
- **Subtema `u09-s5` sin derivación desplegada ni límite explícito (`§2.2`):** En `u09-s5` (línea 156) se escribe directamente $\Phi_B = BA\cos(\omega t) \to \varepsilon(t) = NBA\omega\sin(\omega t)$ sin bloque de derivación ni verificación de límites (más allá de mencionar eje paralelo en la línea 159).

### B. Formato de problema guiado (§3)
Todos los problemas tienen enunciado, `Datos`/`Piden`, figura, `Antes de calcular`, `li.hint` y pasos `Qué hago`/`Por qué`. Las violaciones puntuales a §3.5 (*"Resultado final recuadrado, con unidades y dirección si es vector"*) y §3.6 (*"Verificación: análisis dimensional + al menos un límite o caso conocido"*) son:

1. **`u09-e2` (`li.final`, línea 228):** `Piden` solicita `potencias`, pero la caja final recuadrada omite $P_{\text{ext}} = P_R = 0{,}50\ \text{W}$.
2. **`u09-e4` (`li.final`, línea 271; `li.check`, línea 272):** `Piden` solicita `$\vec B$ (dentro), $\vec E(r)$ dentro y fuera`, pero `li.final` omite $\vec B$ (y no indica unidades $\text{V/m}$ para $\vec E$). Además, `li.check` comprueba continuidad en $r=b$, pero no un caso límite (p. ej., $r\to 0$, $r\to\infty$ o $\omega\to 0$).
3. **`u09-x1` (`li.check`, línea 300):** Tiene análisis dimensional y balance de energía, pero **falta al menos un límite o caso conocido** (p. ej., $v = 0$ o $R\to\infty$).
4. **`u09-x2` (`li.final`, línea 321):** Recuadra $B = \dfrac{\mu_0 I}{2\pi s}$ **sin su dirección** ("azimutal / entrando a la hoja" en la zona de la espira), pese a que es un vector y el Paso 1 otorga `+ 0,25 por la dirección`.
5. **`u09-x3` (`li.final`, línea 344; `li.check`, línea 345):**
   - `li.final` **omite completamente $\vec F$** (o $\vec F_{\text{total}}$), a pesar de figurar en `Piden` y en la parte d) del enunciado.
   - `li.check` **omite el análisis dimensional** (solo verifica balance de potencia y límite $\alpha\to 0$).
6. **`u09-x4` (`li.final`, línea 366; `li.check`, línea 367):**
   - `li.final` **omite el sentido de la corriente inducida** a la izquierda y a la derecha de la espira pequeña, pese a figurar en `Piden` y en la parte c).
   - `li.check` verifica unidades y simetría impar, pero **no explicita un caso límite** (p. ej., $v = 0$ o el comportamiento asintótico $t\to\infty$ dentro de la verificación).
7. **`u09-p1` (`li.final`, línea 403):** `Piden` solicita `orientación`, pero la caja final la omite (solo recuadra $\varepsilon(t)$, $\varepsilon_{\text{máx}}$ e $I_{\text{máx}}$).

### C. Convenciones de notación (§5)
- En general, la unidad respeta bien §5 (`d\vec\ell`, $\varepsilon = -d\Phi_B/dt$, amplitudes $I_0$, $\Delta V = -\int\vec E\cdot d\vec\ell$).
- **Inconsistencia menor en `u09-x4` (líneas 354–367):** Escribe el flujo magnético como `$\Phi(t)$` y `$\Phi$` sin el subíndice $B$ (a diferencia de `$\Phi_B$` usado en todo el resto de la unidad y en §5).
- **Uso variable de $i$ vs $I$ y doble uso de $z$ y $R$:** `u09-s6` y `u09-p5` usan $i$ minúscula para corriente mientras el resto usa $I$ (mezclando ambos en la línea 164: $I_{\text{enc}} = i$); en `u09-x4` (línea 354), $z$ denota a la vez la distancia inicial y la coordenada del eje $\hat z$.

### D. Español neutro
- **`u09-practica` (línea 386):** `Ejercicios para "pautear":` — *"pautear"* es un chilenismo/localismo universitario que no corresponde a español neutro.
- **Error gramatical en `u09-e1` (línea 199):** `¿qué ángulo va en el coseno de $\Phi_B = BA\cos\varphi$, el de $30^\circ$ o otro?` — debe ser **`u otro`**.

---

## 7. Las 5 mejoras más valiosas (ordenadas por prioridad)

### 1. Desbloquear `u09-x3` (fuerza en campo no uniforme, integral explícita y "autoinducción")
- **Ubicación:** `u09-mapa` (`Repaso exprés` 1, línea 24), `u09-x3` enunciado (línea 331) y `u09-x3` Pasos 1 y 4 (líneas 339 y 342).
- **Por qué:** Es el único arquetipo donde el estudiante enfrenta un salto conceptual no cubierto por la teoría (aplicar $\vec F = I\vec\ell\times\vec B$ cuando $\vec B(z)$ varía a lo largo de los lados verticales y entender qué implica "autoinducción despreciable").
- **Texto propuesto (en `Repaso exprés` 1, al final de la línea 24):**
  > Si el campo $\vec B$ varía a lo largo del cable, la fórmula general es diferencial: $d\vec F = I\,d\vec\ell\times\vec B$, y la fuerza total se obtiene sumando (integrando) tramo a tramo: $\vec F = \int I\,d\vec\ell\times\vec B$.
- **Texto propuesto (en `u09-x3`, añadiendo una nota breve al final del enunciado, línea 331, y completando Pasos 1 y 4, líneas 339 y 342):**
  - En línea 331 (tras "autoinducción despreciable"):
    > *(Esto significa que se ignora el flujo magnético creado por la propia corriente inducida en la espira.)*
  - En Paso 1 (línea 339):
    > **Qué hago:** con $\hat n = \hat x$, dividimos la espira en franjas horizontales de ancho $a$ y altura $dz'$: $\Phi_B = \displaystyle\int_z^{z+a} (B_0 - \alpha z')\,a\,dz' = a\left[B_0z' - \tfrac{\alpha}{2}z'^2\right]_z^{z+a} = a^2B_0 - \dfrac{\alpha a^2(2z+a)}{2}$.
  - En Paso 4 (línea 342, al inicio):
    > En los lados verticales, a cada altura $z'$, un elemento $dz'$ del lado derecho lleva corriente $-I\,dz'\,\hat z$ y el elemento opuesto del lado izquierdo lleva $+I\,dz'\,\hat z$; como ambos están al mismo $B(z')$, sus fuerzas $d\vec F = I\,d\vec\ell\times\vec B(z')$ en $\pm\hat y$ son iguales y opuestas y se cancelan tramo a tramo.

### 2. Añadir los prerrequisitos faltantes a `details.prereq` (Gauss/condensador, RHR de espira circular y mallas de Kirchhoff)
- **Ubicación:** `u09-mapa`, después de la línea 38 (ampliando el tercer `details.prereq` y agregando uno nuevo tras la línea 45).
- **Por qué:** Elimina las dependencias implícitas de `u09-s4` (ley de Gauss), `u09-s6` ($E = q/(\varepsilon_0 A)$), `u09-x4` (sentido de $\vec B$ en ambos lados de una espira) y `u09-p4` (regla de mallas con batería y fem inducida).
- **Texto propuesto (agregar al final de `Repaso exprés: campo en el eje de una espira circular`, línea 37):**
  > **Dirección:** por la regla de la mano derecha, si los dedos siguen el sentido de la corriente $I$, el pulgar apunta en el sentido de $\vec B$ a lo largo del eje, **en la misma dirección a ambos lados de la espira** (antes y después de su plano).
- **Texto propuesto (nuevo `<details class="prereq">` tras la línea 45):**
  > `<details class="prereq"><summary>Repaso exprés: ley de Gauss, condensador plano y regla de mallas</summary>`
  > `<p><b>Ley de Gauss eléctrica:</b> el flujo de $\vec E$ a través de cualquier superficie cerrada es $\oint\vec E\cdot d\vec A = Q_{\text{enc}}/\varepsilon_0$, donde $Q_{\text{enc}}$ es la carga encerrada (C) y $\varepsilon_0 = 8{,}85\times10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$. Entre dos placas paralelas de área $A$ ($\text{m}^2$) con cargas $\pm q$, el campo es uniforme y vale $E = \dfrac{q}{\varepsilon_0 A}$ (despreciando bordes).</p>`
  > `<p><b>Regla de mallas (Kirchhoff):</b> en un circuito cerrado de resistencia total $R$ ($\Omega$) con una fuente de fem $V_0$ (V) y una fem inducida $\varepsilon_{\text{ind}}$ (V) que se opone a ella, la corriente es $I = \dfrac{V_0 - |\varepsilon_{\text{ind}}|}{R}$.</p>`
  > `</details>`

### 3. Completar las cajas `li.final` y verificaciones `li.check` según `SPEC-PEDAGOGICO.md` §3.5–3.6
- **Ubicación:** `u09-x3` (líneas 344–345), `u09-x4` (líneas 366–367), `u09-x2` (línea 321), `u09-p1` (línea 403), `u09-e2` (línea 228), `u09-e4` (línea 271).
- **Por qué:** Garantiza que todo resultado pedido en `Piden` aparezca recuadrado con dirección/unidades y que todo arquetipo incluya análisis dimensional y caso límite en `li.check`.
- **Texto propuesto:**
  - En `u09-x3` `li.final` (línea 344):
    > `$$\boxed{\Phi_B = a^2B_0 - \tfrac12\alpha a^2(2z+a),\quad \varepsilon = -\alpha a^2|v|,\quad I = \frac{\alpha a^2|v|}{R}\ \text{(horaria)},\quad \vec F_{\text{mag}} = \frac{\alpha^2 a^4|v|}{R}\hat z,\quad |v_{\text{term}}| = \frac{mgR}{\alpha^2a^4}}$$`
    > (con fuerza neta $\vec F_{\text{total}} = \left(\dfrac{\alpha^2 a^4|v|}{R} - mg\right)\hat z$).
  - En `u09-x3` `li.check` (línea 345, agregar al inicio):
    > **Verificación:** dimensiones de $v_{\text{term}}$: como $[\alpha] = \text{T/m} = \text{N}/(\text{A}\cdot\text{m}^2)$, $[\alpha^2 a^4] = \text{N}^2/\text{A}^2$, y $[mgR/(\alpha^2 a^4)] = \dfrac{\text{N}\cdot(\text{V/A})}{\text{N}^2/\text{A}^2} = \dfrac{\text{V}\cdot\text{A}}{\text{N}} = \dfrac{\text{W}}{\text{N}} = \text{m/s}$.
  - En `u09-x4` `li.final` (línea 366) y cambiar $\Phi(t)\to\Phi_B(t)$ en líneas 355–366:
    > `$$\boxed{\Phi_B(t) = \frac{\mu_0IR^2\pi r^2}{2[R^2+(z-vt)^2]^{3/2}},\quad \varepsilon(t) = -\frac{3\mu_0IR^2\pi r^2\,v\,(z-vt)}{2[R^2+(z-vt)^2]^{5/2}},\quad I_{\text{ind}}(z/v) = 0,\ I_{\text{ind}}(\infty) = 0}$$`
    > Sentido de $I_{\text{ind}}$: opuesto a $d\vec\ell$ cuando la espira grande está a la izquierda ($t \lt z/v$), y en el mismo sentido que $d\vec\ell$ cuando está a la derecha ($t \gt z/v$).
  - En `u09-x2` `li.final` (línea 321): reemplazar $B = \dfrac{\mu_0 I}{2\pi s}$ por `B = \frac{\mu_0 I}{2\pi s}\ \text{(azimutal; entra a la hoja en el lazo)}`.
  - En `u09-p1` `li.final` (línea 403): agregar `, \text{ máxima con plano paralelo a }\vec B` al final de la fórmula recuadrada.

### 4. Corregir el desglose de puntajes en `u09-x2` para que sume los 6 puntos de la pauta
- **Ubicación:** `u09-x2`, Pasos 1–4 (líneas 317–320).
- **Por qué:** El enunciado (línea 309) declara `a) (2 pts.)`, `b) (2 pts.)`, `c) (2 pts.)`, pero actualmente los pasos suman 3,0 puntos y el Paso 4 carece de puntaje.
- **Texto propuesto:**
  - Línea 317: `Paso 1 · Campo por Ampère (1,5 + 0,5 por la dirección)` (total parte a: 2,0 pts.)
  - Línea 318: `Paso 2 · Flujo (1,0 + 1,0)` (total parte b: 2,0 pts.)
  - Línea 319: `Paso 3 · Fem (1,0)`
  - Línea 320: `Paso 4 · Corriente y sentido (0,5 + 0,5)` (total parte c: 2,0 pts.; total del problema: 6,0 pts.)

### 5. Definir símbolos faltantes con unidades SI en su primera aparición y corregir el español no neutro / errata
- **Ubicación:** `u09-mapa` (`Repaso exprés` 1, línea 24), `u09-s6` (tabla, líneas 177–180), `u09-e1` (línea 199) y `u09-practica` (línea 386).
- **Por qué:** Cumple `SPEC-PEDAGOGICO.md` §1 (*"Cada símbolo se define la primera vez que aparece en la unidad, con unidades SI"*) y elimina el único chilenismo y la única errata gramatical del texto.
- **Texto propuesto:**
  - En línea 24 (`Repaso exprés` 1, añadir tras las fórmulas):
    > Aquí $\vec F$ es la fuerza (N), $q$ la carga (C), $\vec v$ la velocidad (m/s), $\vec B$ el campo magnético (T), $I$ la corriente (A) y $\vec\ell$ el vector longitud del tramo (m).
  - En línea 180 (`u09-s6`, debajo de la tabla de Maxwell):
    > En la tabla: $Q_{\text{enc}}$ es la carga encerrada (C), $\rho$ la densidad volumétrica de carga ($\text{C/m}^3$), $\vec J$ la densidad de corriente ($\text{A/m}^2$) y $\vec E$ el campo eléctrico (V/m).
  - En línea 199 (`u09-e1`): cambiar `el de $30^\circ$ o otro?` por **`el de $30^\circ$ u otro?`**.
  - En línea 386 (`u09-practica`): cambiar `Ejercicios para "pautear": resuélvelos completos en papel, sin calculadora, y compara después con la solución paso a paso.` por **`Ejercicios para resolver con formato de examen: hazlos completos en papel, sin calculadora, y compara después con la solución paso a paso.`**.
