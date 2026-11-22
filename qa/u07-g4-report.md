# Informe G4 de Autosuficiencia — U7: Fuerza magnética

- **Archivo evaluado:** `unidades/u07-fuerza-magnetica.html`
- **Contrato de referencia:** `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5, §9)
- **Perfil simulado:** Estudiante de 2.º año de ingeniería con **solo** esta unidad (sin clases, sin otras unidades, sin calculadora ni formulario).

---

## 1. Resolvibilidad de arquetipos y problemas de práctica desde la unidad

| ID | Título / Fuente | ¿Resoluble solo con la unidad? | Paso que bloquea y por qué |
|---|---|---|---|
| `u07-x1` | Arquetipo 1 · Rayo de partículas en campo magnético saliente (`Examen 2025-1 · P2`) | **Sí** | Sin bloqueos. `u07-s3` da $R = mv_\perp/(\|q\|B)$, `u07-s4` advierte $d = 2R$ y explica cómo fijar el signo de $q$ con $\vec v\times\vec B$. (Detalle menor: en la parte a se pide $q/m$ antes de fijar el signo en b.) |
| `u07-x2` | Arquetipo 2 · Alambre infinito y espira rectangular coplanar (`Examen 2024-2 · P1`) | **No (parcial: bloquea en parte c)** | Partes a) y b) son resolubles con el `Repaso exprés` de Ampère y `u07-s7`. **Bloquea la parte c (2/6 pts.)**: pide *"Calcular la inductancia mutua entre la espira y el alambre"*, pero el concepto de inductancia mutua ($M I_1 = \Phi_2$, unidades en henrios $\text{H} = \text{Wb/A}$) **no se define en ninguna parte de la unidad** antes de aparecer en la solución (`Paso 3`, línea 300). Además, `u07-s2` solo ejemplifica $\Phi_B = BA\cos\varphi$ para $\vec B$ uniforme y no muestra el cálculo de flujo por integración sobre un $\vec B(y)\propto 1/y$. |
| `u07-x3` | Arquetipo 3 · Selector de velocidades con placas y apagado de campos (`Examen 2018-2 · P3`) | **Sí** (con fricción menor en c) | Resoluble con `u07-s4` ($\vec E = -\vec v_0\times\vec B$), el `Repaso exprés` de condensador plano ($E = \|\sigma\|/\varepsilon_0$) y trabajo-energía ($W = \Delta K$), más `u07-s1` ($W_B = 0$). **Fricción menor en c)**: el enunciado no indica que las placas sean suficientemente largas para garantizar el choque (esa hipótesis recién aparece en el Paso 3, línea 321). |
| `u07-p1` | Práctica 1 · Momento dipolar, torque y energía de una bobina inclinada | **Sí** | Sin bloqueos. `u07-s6` cubre $\mu = NIA$, $\tau = \mu B\sin\varphi$, $U = -\mu B\cos\varphi$ y el equilibrio inestable en $\varphi = 180^\circ$. Números exactos a mano. |
| `u07-p2` | Práctica 2 · Partícula acelerada por $\Delta V$ entrando a una cámara magnética | **Sí** | Sin bloqueos. El `Repaso exprés` (trabajo-energía) y `u07-s4` dan $\|q\|\Delta V = \tfrac12 mv^2$, y `u07-s3` da $R$ y $T$. |
| `u07-p3` | Práctica 3 · Electrón deflectado hasta el borde de dos placas paralelas | **Sí** | Sin bloqueos. `u07-s1` y `Repaso exprés` 1 dan la dirección de deflexión; `u07-s3` da $R = mv_0/(eB)$; el resto es geometría analítica de circunferencia tangente en $(0,0)$. |
| `u07-p4` | Práctica 4 · Barrera magnética de ancho $L$: rapidez crítica y ángulo de salida | **Sí** | Sin bloqueos. `u07-s3` da $R$ y $T$; la condición tangencial $R = L$ y $\sin\alpha = L/R$ son geometría elemental con ángulos notables ($30^\circ$). |
| `u07-p5` | Práctica 5 · Fuerza sobre una espira cuadrada junto a un alambre infinito | **Sí** | Sin bloqueos. `Repaso exprés` 3 y `u07-s7` desarrollan exactamente este método. |

---

## 2. Saltos en derivaciones

1. **`u07-x2` Paso 3 (línea 300) — Inductancia mutua $M$:** introduce *"por definición, la inductancia mutua $M$ (en henrios, H = Wb/A) cumple $M I_1 = \Phi_2$"* sin haberla presentado previamente en teoría ni en un recuadro de repaso, y escoge $d\vec A_2 = dx\,dy\,\hat z$ sin explicar que el sentido de $\hat n$ se elige paralelo a $\vec B_1$ para que $M \gt 0$.
2. **`u07-s5` Paso 1 (línea 118) — Relación $I = n\|q\|v_d A$:** en la derivación de $\vec F_B = I\,\vec L\times\vec B$, afirma *"Como la corriente es $I = n|q|v_d A$, el vector $nqA\vec v_d\,L$ equivale a $I\vec L$"* sin derivar ni repasar por qué $I = n|q|v_d A$.
3. **`u07-s6` Paso 3 (línea 140) — Energía potencial $U(\varphi)$:** escribe $U(\varphi) = \int_{90^\circ}^\varphi \mu B\sin\varphi'\,d\varphi' = -\mu B\cos\varphi$ saltándose la primitiva evaluada $\big[-\mu B\cos\varphi'\big]_{90^\circ}^\varphi = -\mu B(\cos\varphi - \cos 90^\circ)$ y sin haber repasado el trabajo rotacional $W = \int \tau_{\text{ext}}\,d\varphi'$.
4. **`u07-s7` (línea 167) y `u07-s6` (línea 147) — Fuerza sobre un dipolo $\vec F = \nabla(\vec\mu\cdot\vec B)$:** se cita la fórmula $\nabla(\vec\mu\cdot\vec B)$ sin derivarla (aparece como comentario de límite/cuándo se usa).
5. **`u07-e4` Paso 4 (línea 253) — Vector normal $\hat n$:** da directamente $\hat n = -\cos\theta\,\hat x - \sin\theta\,\hat y$ sin mostrar el paso geométrico desde el vector director $\hat d = \sin\theta\,\hat x - \cos\theta\,\hat y$ o desde $\theta = 0$.

---

## 3. Símbolos usados antes de su definición o sin unidades SI

Según `SPEC-PEDAGOGICO.md` §1 y §9.2 (*"Unidades SI en la primera aparición de cada símbolo, también en repasos exprés, tablas (p. ej. $\rho$, $\vec J$) y enunciados de problemas simbólicos"*):

1. **`Repaso exprés` 1 (línea 26):** usa $\vec v$, $\vec B$, $q$ en el mini ejemplo antes de definirlos con unidades SI en `u07-s1` (línea 45).
2. **`Repaso exprés` 2 (líneas 29–30):** `a_c` aparece sin unidades SI (`m/s²`); `W` aparece sin unidad explícita (`J`) al definir $W = \int \vec F\cdot d\vec\ell$.
3. **`u07-s1` (línea 45) y `u07-s5` (línea 114) y `u07-s7` (línea 155):** en las notas de `.eq.key` no se explicita la unidad SI de $\vec F_B$, $d\vec F_B$ y $F_{\text{neta}}$ (`N`).
4. **`u07-s2` (línea 69):** en `details.deriv` usa `V` / `dV` (volumen) y `\rho` (densidad volumétrica de carga) sin unidades SI (`m³` y `C/m³`).
5. **`u07-s4` (línea 97):** menciona *"diámetro $d = 2R$"* sin explicitar `(m)` para $d$.
6. **`u07-s6` (línea 136):** introduce los lados `b` y `a` de la espira rectangular sin unidades SI `(m)`.
7. **Enunciados de problemas simbólicos sin unidades SI explícitas:**
   - `u07-e3` (línea 221): $R$, $I$, $B$.
   - `u07-e4` (línea 242): define $L$ (m) y $M$ (kg), pero omite unidades SI de $g$, $B$ e $I$.
   - `u07-x1` (línea 269): $v$, $B$, $d$.
   - `u07-x2` (línea 290): $I_1$, $I_2$, $a$, $b$, $h$ (y en la parte c pide inductancia mutua sin definir $M$ ni `H` previamente).
   - `u07-x3` (línea 311): $B$, $d$, $\pm\sigma$, $m$, $q$, $v_0$, $E_z$.
   - `u07-p2` (línea 369): da $V_0$ (en V), pero omite unidades SI de $q$, $m$, $B$.
   - `u07-p3` (línea 390): $-e$, $m$, $v_0$, $\ell$, $d$, $B$.
   - `u07-p4` (línea 411): $m$, $q$, $v$, $L$, $B$.
   - `u07-p5` (línea 432): $I$, $a$, $L$.

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

1. **Referencia colgante crítica en `u07-x2` parte c) (líneas 290 y 300):** pide calcular la **inductancia mutua** entre la espira y el alambre, remitiendo implícitamente a un concepto que pertenece a otra unidad (U9 Inducción) y que no está definido ni resumido en U7.
2. *(Menor, no bloqueante)* **`u07-s2` (línea 71):** menciona *"para calcular $\vec B$ se usa Biot-Savart o la ley de Ampère"*; Biot-Savart no se presenta en la unidad (aunque no se necesita para ningún problema de U7).

---

## 5. Prerrequisitos usados pero no cubiertos por los recuadros `Repaso exprés`

1. **Inductancia mutua ($M = \Phi_2/I_1$, en H = Wb/A):** usada en `u07-x2` parte c) (línea 300); ausente de los `Repaso exprés` y de la teoría.
2. **Torque mecánico ($\vec\tau = \vec r\times\vec F$), equilibrio rotacional ($\sum\vec\tau = \vec 0$) y trabajo rotacional ($W = \int \tau\,d\varphi$):** usados en `u07-e4` (líneas 250–252) y `u07-s6` (líneas 138, 140); no figuran en los `Repaso exprés`.
3. **Corriente microscópica ($I = n\|q\|v_d A$):** usada en `u07-s5` (línea 118); no figura en los `Repaso exprés`.
4. **Teorema de la divergencia ($\oint_S \vec B\cdot d\vec A = \int_V (\nabla\cdot\vec B)\,dV$):** usado en `u07-s2` (línea 69) en una derivación conceptual colapsada.

---

## 6. Violaciones de `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§3 (Formato de problema guiado):** Todos los ejemplos, arquetipos y prácticas cumplen los 6 componentes (enunciado + `Datos`/`Piden` + figura, `Antes de calcular`, `li.hint`, `Paso N · Título` con `Qué hago`/`Por qué`, `li.final`, `li.check` con unidades y límite).
- **§5 (Convenciones de notación):** Se respetan $d\vec\ell$ (con equivalencias $d\vec s, d\vec l$), $\Delta V = V_b - V_a = -\int_a^b \vec E\cdot d\vec\ell$, y $\vec\mu = NIA\,\hat n$ (con equivalencia $\vec m$ de Cádiz).
- **§9.1 (Números calculables a mano):** Cumplido en todos los problemas numéricos (`u07-e1`, `u07-e2`, `u07-p1`).
- **§9.2 (Unidades SI en primera aparición y en enunciados simbólicos):** **Incumplido** en varios repasos/notas y en la mayoría de enunciados simbólicos (ver lista en §3).
- **§9.3 (Forma general antes que la particular):** En `u07-s5` sí se da $d\vec F_B = I\,d\vec\ell\times\vec B$ antes de $\vec F_B = I\,\vec L\times\vec B$. En `u07-s2` (línea 67), se enuncia $\Phi_B = \int_S \vec B\cdot d\vec A$, pero solo se muestra el caso particular uniforme $\Phi_B = BA\cos\varphi$, sin ejemplo de integración para $\vec B$ no uniforme (usado en `u07-x2` c).
- **§9.4 (`li.final` debe contener todo lo pedido):**
  - **`u07-x3` (línea 323):** en b) el enunciado pide *"la magnitud $|\sigma|$ e indique qué placa lleva $+\sigma$ y cuál $-\sigma$"*, pero `li.final` escribe `+\sigma = \varepsilon_0 v_0 B (sup.), -\sigma = -\varepsilon_0 v_0 B (inf.)` sin explicitar $|\sigma| = \varepsilon_0 v_0 B$.
  - **`u07-x2` (línea 301):** en a) el enunciado pide $\vec B_1$ *"en función de la distancia al eje del alambre infinito"*, pero `li.final` solo reporta $\vec B_1(y) = \frac{\mu_0 I_1}{2\pi y}\,\hat z$ (válido en $y \gt 0, z = 0$) y no la forma radial $\vec B_1(r) = \frac{\mu_0 I_1}{2\pi r}\,\hat\phi$.
- **§9.5 (Sin símbolos sobrecargados):**
  - **$V$:** potencial eléctrico ($\text{V}$) en `Repaso exprés` 2, `u07-s4`, `u07-p2` vs. volumen ($\text{m}^3$) en `u07-s2` línea 69.
  - **$L$:** largo de conductor/franja en `u07-s5`, `u07-e4`, `u07-p4` vs. distancia de la espira al alambre ($L = a/2$) en `u07-p5` línea 432.
  - **$d$:** diámetro en `u07-s4`, `u07-x1` vs. separación entre placas en `u07-x3`, `u07-p3` (y vector director $\hat d$ en `u07-e4`).
  - **$\varphi$:** ángulo entre $\vec\mu$ y $\vec B$ en `u07-s6`, `u07-p1` vs. ángulo recorrido en órbita ($\varphi = \pi$) en `u07-p2` línea 379 y `u07-p4` línea 421.
- **§9.6 (Arquetipos autosuficientes y suma de puntajes):** Los puntajes suman exactamente 6,0 pts. en `u07-x1`, `u07-x2` y `u07-x3`. Única fricción: en `u07-x3` c) falta explicitar que las placas son suficientemente largas para que el choque ocurra.
- **§9.9 (HTML `\lt`/`\gt` y pasos algebraicos):** Sin `<` crudos en fórmulas; se usa `\lt` y `\gt` correctamente.

---

## 7. Los 5 arreglos más valiosos (priorizados)

1. **[Crítico · desbloquea `u07-x2` parte c] Definir inductancia mutua $M$ y agregar nota de flujo no uniforme.**
   - **Ubicación:** `unidades/u07-fuerza-magnetica.html`, en `#u07-s2` (línea 67, dentro de `.note` o justo después de `details.deriv`) y en `#u07-formulas` (tras línea 497).
   - **Texto propuesto (en `#u07-s2`, después de línea 67):**
     ```html
     <p><b>Flujo en campo no uniforme e inductancia mutua.</b> Cuando $\vec B$ varía sobre la superficie (por ejemplo $\vec B(y) \propto 1/y$ junto a un alambre), $\Phi_B = \int_S \vec B\cdot d\vec A$ se integra elemento a elemento. Si el flujo $\Phi_2$ a través de una espira 2 proviene de la corriente $I_1$ (A) de otro circuito 1, ambos son proporcionales y se define la <b>inductancia mutua</b> $M$ (en henrios, $\text{H} = \text{Wb/A}$) mediante $\Phi_2 = M I_1$, donde $M$ depende solo de la geometría.</p>
     ```
   - **Fila propuesta (en `#u07-formulas`, tras línea 497):**
     ```html
     <tr><td>$M = \dfrac{\Phi_2}{I_1}$</td><td>Inductancia mutua ($\text{H} = \text{Wb/A}$) entre circuito 1 ($I_1$ en A) y espira 2 ($\Phi_2$ en Wb)</td><td>Solo depende de la geometría; $\hat n$ elegido para $M \gt 0$</td></tr>
     ```

2. **[Alto · cumple `SPEC-PEDAGOGICO.md` §9.2] Agregar unidades SI en la primera aparición de cada símbolo en `Repaso exprés`, `.eq.key` y enunciados simbólicos.**
   - **Ubicación:** `u07-mapa` (líneas 29–30), `u07-s1` (línea 45), `u07-s2` (línea 69), `u07-s4` (línea 97), `u07-s5` (línea 114), `u07-s6` (línea 136), `u07-s7` (línea 155), y enunciados de `u07-e3`, `u07-e4`, `u07-x1`, `u07-x2`, `u07-x3`, `u07-p2`, `u07-p3`, `u07-p4`, `u07-p5`.
   - **Texto propuesto (ejemplo para `u07-x2`, línea 290):**
     > *"Considere un alambre infinito sobre el eje $x$ por el que circula una corriente $I_1$ (A) hacia $+\hat x$, y una espira rectangular coplanar (en el primer cuadrante del plano $xy$, con $\hat z$ saliendo de la hoja) de ancho horizontal $a$ (m, paralelo al alambre, de $x = 0$ a $x = a$) y altura $b$ (m, de $y = h$ a $y = h+b$, con $h$ en m). Por la espira circula una corriente $I_2$ (A) en sentido horario."*
   - **Texto propuesto (ejemplo para `Repaso exprés` 2, líneas 29–30):**
     > *"tiene aceleración centrípeta $a_c = \dfrac{v^2}{R} = \omega^2 R$ ($\text{m/s}^2$) hacia el centro"* y *"el trabajo de una fuerza $\vec F$ (N) a lo largo de una trayectoria es $W = \int \vec F\cdot d\vec\ell = \Delta K = K_f - K_i$ (J)"*.

3. **[Medio-Alto · cubre prerrequisito de `u07-e4` y `u07-s6`] Añadir repaso de torque mecánico y completar la primitiva de $U(\varphi)$ en `u07-s6`.**
   - **Ubicación:** `unidades/u07-fuerza-magnetica.html`, en `#u07-mapa` dentro del `Repaso exprés` 2 (tras línea 29) y en `#u07-s6` (línea 140).
   - **Texto propuesto (en `#u07-mapa`, tras línea 29):**
     > *"<p><b>Torque y equilibrio rotacional:</b> el torque de una fuerza $\vec F$ (N) aplicada en $\vec r$ (m) respecto a un eje es $\vec\tau = \vec r\times\vec F$ ($\text{N·m}$), con magnitud $rF\sin\alpha$. En equilibrio estático, $\sum\vec\tau = \vec 0$. El trabajo de un torque externo para girar un ángulo $d\varphi'$ es $dW = \tau_{\text{ext}}\,d\varphi'$ (J).</p>"*
   - **Texto propuesto (en `#u07-s6`, línea 140):**
     > *"$U(\varphi) = \int_{90^\circ}^\varphi \mu B\sin\varphi'\,d\varphi' = \big[-\mu B\cos\varphi'\big]_{90^\circ}^\varphi = -\mu B(\cos\varphi - \cos 90^\circ) = -\mu B\cos\varphi = -\vec\mu\cdot\vec B$."*

4. **[Medio · completitud de `li.final` e hipótesis en `u07-x3` y `u07-x2`] Explicitar $|\sigma|$ en `u07-x3` `li.final`, largo suficiente en `u07-x3` c) y $\vec B_1(r)$ general en `u07-x2` `li.final`.**
   - **Ubicación:** `u07-x3` (líneas 311 y 323) y `u07-x2` (línea 301).
   - **Texto propuesto (`u07-x3` c, línea 311):**
     > *"c) <b>(1,5 pts.)</b> si se apaga $\vec E$ ($\vec E = \vec 0$) y se mantiene $\vec B = B\hat y$ (suponiendo placas suficientemente largas), con qué placa choca y con qué rapidez;"*
   - **Texto propuesto (`u07-x3` `li.final`, línea 323):**
     > *"`\text{b) }|\sigma| = \varepsilon_0 v_0 B:\ +\sigma\ (\text{sup.}),\ -\sigma\ (\text{inf.});`"*
   - **Texto propuesto (`u07-x2` `li.final`, línea 301):**
     > *"`\vec B_1(r) = \frac{\mu_0 I_1}{2\pi r}\,\hat\phi\ \left(\text{en }z=0, y\gt 0:\ \frac{\mu_0 I_1}{2\pi y}\,\hat z\right)`"*

5. **[Medio · eliminar símbolos sobrecargados, SPEC §9.5] Desambiguar $V$ (volumen) en `u07-s2` y $L$ (distancia) en `u07-p5`.**
   - **Ubicación:** `u07-s2` (línea 69) y `u07-p5` (línea 432).
   - **Texto propuesto (`u07-s2`, línea 69):**
     > *"Por el teorema de la divergencia, $\oint_S \vec B\cdot d\vec A = \int_{\mathcal{V}} (\nabla\cdot\vec B)\,d\mathcal{V} = 0$ para cualquier volumen $\mathcal{V}$ ($\text{m}^3$)."*
   - **Texto propuesto (`u07-p5`, línea 432):**
     > *"tiene su lado inferior paralelo al alambre a distancia $h = a/2$ (denotada $L = a/2$ en el examen original)"*.
