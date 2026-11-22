# Reporte de Revisión G4 (Autosuficiencia) — U2: Ley de Gauss y conductores

**Archivo revisado:** `unidades/u02-gauss.html`  
**Contrato:** `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5, §9)  
**Rol simulado:** Estudiante de 2.º año de ingeniería con acceso **únicamente** a esta unidad (sin clases, sin otras unidades, sin calculadora, sin formulario externo).

---

## 1. Evaluabilidad por arquetipo de examen y problema de práctica

| ID | Título | ¿Soluble solo con la unidad? | Paso bloqueante y motivo |
|---|---|---|---|
| `u02-x1` | Arquetipo 1: Esfera no conductora con $\rho = -3\beta r^3$ en cascarón conductor (2025-1 P1) | **Sí** | Ninguno. El `Repaso exprés` 2 (línea 36) da $Q_{\text{enc}}(r) = 4\pi\int_0^r \rho(r'){r'}^2\,dr'$, `u02-s3` cubre $\rho(r)$ radial y `u02-s6` (líneas 202–205) cubre $q_{\text{int}} = -Q_{\text{enc}}$ y $q_{\text{ext}} = Q_{\text{cond}} + Q_{\text{enc}}$. *(Detalle menor: el enunciado en línea 332 no indica $\beta \gt 0$, aunque `Antes de calcular` en línea 337 lo asume.)* |
| `u02-x2` | Arquetipo 2: Dos cilindros infinitos paralelos con campo nulo en un punto (2021-2 Ej. 2) | **Sí** | Ninguno. `u02-s4` entrega $\vec E_{\text{cil, int}}$ y $\vec E_{\text{cil, ext}}$, y la aritmética ($\frac{8\cdot 30^2}{9\cdot 81} = \frac{800}{81} \approx 9{,}88$) es calculable a mano. El enunciado es autosuficiente sin la figura. |
| `u02-x3` | Arquetipo 3: Esfera no conductora con cavidad esférica rellena con carga $Q$ (2022-2 P11) | **Sí** | Ninguno. `u02-s7` (línea 218 y `.note`) da explícitamente $\vec E_{\text{cav, esf}} = \frac{\rho}{3\varepsilon_0}\vec a$ y la regla para añadir el relleno $\vec E_Q = \frac{\rho_Q}{3\varepsilon_0}(\vec r - \vec a)$. |
| `u02-p1` | Práctica 1: Cilindro infinito con $\rho(r) = \alpha r$ | **Sí** | Ninguno. El `Repaso exprés` 2 (línea 40) resuelve incluso el mismo mini ejemplo $\rho(r') = \alpha r'$ y `u02-s4` Caso C da la fórmula general. |
| `u02-p2` | Práctica 2: Esfera de dos capas con densidades opuestas | **Sí** | Ninguno. `u02-s3` cubre el cálculo por regiones con Gauss esférico. |
| `u02-p3` | Práctica 3: Dos cascarones conductores concéntricos conectados por un cable | **Sí** | Ninguno. `Repaso exprés` 3 (línea 46) y `u02-s6` (línea 207) establecen que al unir dos conductores sin carga intermedia $\vec E = \vec 0$ entre ellos y las cargas enfrentadas se neutralizan. El texto describe la función del interruptor $S$ sin depender de la figura. |
| `u02-p4` | Práctica 4: Cilindros infinitos traslapados con densidades opuestas | **Sí** | Ninguno. `u02-s7` (línea 216) da $\vec E_{\text{cil}}(\vec r_\perp) = \frac{\rho}{2\varepsilon_0}\vec r_\perp$ y `u02-x3` ejemplifica vectores relativos. |
| `u02-p5` | Práctica 5: Ley de Gauss diferencial: campo eléctrico atmosférico | **Sí** | Ninguno. `u02-s7` (línea 221) da $\nabla\cdot\vec E = \rho/\varepsilon_0$ en cartesianas, y `u02-s6` (línea 197) da el salto normal $E_n^+ - E_n^- = \sigma/\varepsilon_0$. |

---

## 2. Saltos en derivaciones

1. **`u02-e4` (`Paso 2` y `Paso 4`, líneas 314 y 316):** Se evalúan integrales de $r^{-2}$ directamente sin escribir la primitiva evaluada (contra SPEC §9.9: *"Cada derivación pasa por todos los pasos algebraicos (planteo de la integral, primitiva evaluada...)"*):
   - Línea 314: `$V(R_3) = -\displaystyle\int_\infty^{R_3} \dfrac{q_3}{4\pi\varepsilon_0 r^2}\,dr = \dfrac{q_3}{4\pi\varepsilon_0 R_3}$` (falta el paso intermedio $\frac{q_3}{4\pi\varepsilon_0}\left[\frac{1}{r}\right]_\infty^{R_3}$).
   - Línea 316: `$V(R_1) - V(R_2) = -\displaystyle\int_{R_2}^{R_1} \dfrac{Q}{4\pi\varepsilon_0 r^2}\,dr = \dfrac{Q}{4\pi\varepsilon_0}\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$` (falta $\frac{Q}{4\pi\varepsilon_0}\left[\frac{1}{r}\right]_{R_2}^{R_1}$).
2. **`u02-p5` (`Paso 2`, línea 537):** En `$Q = \displaystyle\int_0^\infty \rho(z)\,A\,dz = \varepsilon_0 A\left[a\alpha\cdot\frac1\alpha + b\beta\cdot\frac1\beta\right] = \varepsilon_0 A(a + b)$` se omite la primitiva evaluada $\varepsilon_0 A\left[-a e^{-\alpha z} - b e^{-\beta z}\right]_0^\infty$.
3. **`u02-p3` (`Paso 1`, línea 490):** En `$2Q = \displaystyle\int_0^R \beta {r'}^2(4\pi {r'}^2\,dr') = \dfrac{4\pi\beta R^5}{5}$` se omite la primitiva $\left[\frac{{r'}^5}{5}\right]_0^R$ (aunque el `Repaso exprés` 2 en línea 37 sí la muestra).
4. **`u02-s2` (`details.deriv`, línea 86):** La justificación de Gauss para una superficie cerrada arbitraria se apoya en el conteo cualitativo de líneas de campo (*"cualquier otra superficie cerrada que rodee a $q$ es cortada por exactamente las mismas líneas"*) en lugar del ángulo sólido $d\Omega$; es adecuada al nivel del curso, pero conviene tenerlo presente.

---

## 3. Símbolos usados antes de su definición o sin unidades SI

1. **`Repaso exprés` 1 (líneas 27–30):** Se introducen $dQ$, $dV$, $dA$, $dL$, $dq$, $d\ell$ sin declarar explícitamente las unidades SI de volumen ($V$ en $\text{m}^3$), área ($A$ en $\text{m}^2$), longitud ($L, \ell$ en $\text{m}$) ni carga total ($Q$ en $\text{C}$), aunque se infieren de $\text{C/m}^3$, $\text{C/m}^2$ y $\text{C/m}$.
2. **`Repaso exprés` 3 (línea 47):** Aparecen `R_{\text{ext}}`, `q_{\text{ext}}` y `R_{\text{tierra}}` sin definición explícita ni unidades ($\text{m}$, $\text{C}$) en ese párrafo.
3. **`u02-s7` (líneas 216–221):**
   - Línea 216: `$\vec r_\perp$` se define como *"el vector perpendicular desde el eje hasta el punto"*, sin indicar unidad SI ($\text{m}$).
   - Línea 218 (`.note`): `$\rho_Q$` se introduce sin indicar unidad SI ($\text{C/m}^3$).
   - Línea 221: `$\nabla\cdot\vec E$` se presenta sin indicar unidad SI ($\text{N/(C·m)} = \text{V/m}^2$).
4. **`u02-formulas` (líneas 591–601):** La columna *"Significado y unidades SI"* omite las unidades SI de varios símbolos en sus filas respectivas: $E$ ($\text{N/C}$) y $A, d\vec A$ ($\text{m}^2$) en línea 591; $d\vec A$ ($\text{m}^2$) en línea 593; $R, r$ ($\text{m}$) en línea 595; $r, R$ ($\text{m}$) y $\rho$ ($\text{C/m}^3$) en línea 596; $z, a$ ($\text{m}$) y $\rho$ ($\text{C/m}^3$) en línea 597; $q_{\text{int}}, Q_{\text{enc}}, q_{\text{ext}}, Q_{\text{cond}}$ ($\text{C}$), $\sigma$ ($\text{C/m}^2$) y $E_{\text{sup}}$ ($\text{N/C}$) en línea 598; $V_{\text{cond}}$ ($\text{V}$) y $q_{\text{ext}}, q_{\text{int}}, Q_{\text{enc}}$ ($\text{C}$) en línea 599; $\rho$ ($\text{C/m}^3$) y $\vec a_\perp$ ($\text{m}$) en línea 600; $\nabla\cdot\vec E$ ($\text{V/m}^2$) y $\rho$ ($\text{C/m}^3$) en línea 601.
5. **`u02-x1` (línea 332 vs 337):** El enunciado define `$\beta$ constante en $\text{C/m}^6$` sin indicar su signo, pero `Antes de calcular` (línea 337) supone `(para $\beta \gt 0$)`.

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

- **No se encontraron referencias colgantes externas.** Todas las menciones a fuentes (`Examen 2011-1 P9`, `Ayudantía 04 P1`, `Pauta_Ex_FIS1533_2025_1.md`, etc.) funcionan exclusivamente como trazabilidad o notas de erratas de pauta (conforme a SPEC §1 y §6), no como dependencias para resolver los problemas.
- En línea 69 (`u02-s1`), *"ver sección siguiente"* apunta a `u02-s2` dentro de la misma unidad.
- En `u02-p3` (línea 482), *"Se cierra el interruptor $S$ conectando ambos conductores con un cable"* nombra a $S$ (presente en la figura), pero explica explícitamente su efecto en el texto, por lo que no depende de la figura.

---

## 5. Prerrequisitos usados pero no cubiertos por los recuadros `Repaso exprés`

1. **Justificación de $\vec E = \vec 0$ entre dos cascarones conectados por un cable (`Repaso exprés` 3, línea 46):** El recuadro afirma directamente *"Si no hay cargas libres en el espacio que los separa, $\vec E = \vec 0$ entre ellos y las cargas enfrentadas se neutralizan"*, pero no muestra por qué para cascarones concéntricos (si $V(a_2) = V(b_1)$, entonces $-\int_{a_2}^{b_1} E_r\,dr = 0$, y como $E_r = \frac{Q_{\text{enc}}}{4\pi\varepsilon_0 r^2}$ no cambia de signo, necesariamente $Q_{\text{enc}} = 0 \implies \vec E = \vec 0$).
2. **Vectores unitarios cartesianos ($\hat\imath, \hat\jmath, \hat k$) y vectores posición relativos ($\vec r - \vec r_c$):** Usados en `u02-s1`, `u02-s5`, `u02-s7`, `u02-x2`, `u02-x3` y `u02-p4`. Se asumen conocidos de álgebra vectorial previa (el `Repaso exprés` 1 solo usa $\hat r_i$).
3. **Divergencia y teorema de la divergencia:** Usados en `u02-s7`, `u02-e2`, `u02-p1`, `u02-p5` y el quiz Q7. No están en un `Repaso exprés`, aunque `u02-s7` (líneas 220–221) enuncia el teorema y entrega las fórmulas en cartesianas, esféricas y cilíndricas.

---

## 6. Violaciones a `SPEC-PEDAGOGICO.md` §3, §5 y §9

| Regla SPEC | Ubicación | Descripción exacta |
|---|---|---|
| **§9.4** (`li.final` contiene todo lo pedido) | `u02-p3`, línea 494 | La parte d) pide *"las nuevas cargas y densidades en cada superficie y el nuevo campo entre $a_2$ y $b_1$"*, pero `li.final` dice `Con $S$ cerrado: $\sigma_{a_2} = \sigma_{b_1} = 0$, $\vec E(a_2 \lt r \lt b_1) = \vec 0$, y $\sigma_{a_1}, \sigma_{b_2}$ no cambian`, omitiendo las nuevas cargas ($q'_{a_1} = -2Q$, $q'_{a_2} = q'_{b_1} = 0$, $q'_{b_2} = 3Q$). |
| **§3.6 y §9.8** (Verificación: dimensiones + límite) | `u02-e4`, línea 318 | `li.check` verifica signo y equivalencia con la pauta, pero **falta análisis dimensional** de $V(R_1)$ y **falta un límite** (p. ej. $R_2 \to \infty$). |
| **§3.6 y §9.8** | `u02-x1`, línea 358 | `li.check` verifica continuidad, saltos y unidades, pero **falta un límite físico** (p. ej. $r \gg R$ o $q_{\text{neta}} = -Q$). |
| **§3.6 y §9.8** | `u02-p2`, línea 473 | `li.check` verifica continuidad y el caso $b = 2a$, pero **falta análisis dimensional**. |
| **§3.6 y §9.8** | `u02-p3`, línea 495 | `li.check` verifica continuidad, saltos e invariancia exterior, pero **faltan análisis dimensional y límite**. |
| **§9.2** (Unidades SI en primera aparición y tablas) | `u02-s7` (líneas 216–221), `u02-formulas` (líneas 591–601) | Faltan unidades SI en $\vec r_\perp$, $\rho_Q$, $\nabla\cdot\vec E$ y en varios símbolos de la tabla de fórmulas (ver §3 arriba). |
| **§9.5** (Sin símbolos sobrecargados) | `u02-x1`, líneas 341 vs. 351 | En `Paso 1` usa $r$ como variable muda de integración ($\int_0^R (-3\beta r^3)r^2\,dr$), mientras que en `Paso 4` cambia a $r'$ ($\int_0^r {r'}^5\,dr'$) porque $r$ es el radio de la gaussiana. |
| **§9.9** (Todos los pasos algebraicos) | `u02-e4` (líneas 314, 316), `u02-p5` (línea 537) | Se omiten las primitivas evaluadas al integrar (ver §2 arriba). |

*Nota sobre §5 y §9.9 HTML:* Las convenciones de notación (§5: $k = \frac{1}{4\pi\varepsilon_0}$ y equivalencia $k_e$, $\Delta V = V_b - V_a = -\int_a^b \vec E\cdot d\vec\ell$) se cumplen correctamente, y no hay signos `<` ni `>` sin escapar (`\lt`/`\gt`) dentro de fórmulas matemáticas.

---

## 7. Los 5 arreglos más valiosos (ordenados por impacto)

1. **Completar `li.final` y `li.check` en `u02-p3` (líneas 494–495) [SPEC §9.4, §3.6, §9.8]:**
   - *Ubicación:* `unidades/u02-gauss.html#L494-L495` (`u02-p3`).
   - *Texto propuesto para `li.final` (línea 494):*
     > `Con $S$ cerrado: $q'_{a_1} = -2Q$, $q'_{a_2} = q'_{b_1} = 0$, $q'_{b_2} = 3Q$; $\sigma_{a_2} = \sigma_{b_1} = 0$, $\vec E(a_2 \lt r \lt b_1) = \vec 0$, y $\sigma_{a_1}, \sigma_{b_2}$ no cambian.`
   - *Texto propuesto para `li.check` (línea 495, agregar al final):*
     > `Unidades: $[\beta] = \text{C/m}^5$, $[Q/(\varepsilon_0 r^2)] = \text{N/C}$. Límite $b_1, b_2 \to \infty$ (sin cascarón externo): desaparecen $b_1, b_2$ y para $r \gt a_2$ queda $\vec E = \frac{2Q}{4\pi\varepsilon_0 r^2}\hat r = \frac{Q}{2\pi\varepsilon_0 r^2}\hat r$.`

2. **Completar primitivas evaluadas y verificación en `u02-e4` (líneas 314, 316 y 318) y `u02-p5` (línea 537) [SPEC §9.9, §3.6, §9.8]:**
   - *Ubicación:* `unidades/u02-gauss.html#L314-L318` (`u02-e4`) y `#L537` (`u02-p5`).
   - *Texto propuesto en `u02-e4` (línea 314):*
     > `$V(R_3) = -\displaystyle\int_\infty^{R_3} \dfrac{q_3}{4\pi\varepsilon_0 r^2}\,dr = \dfrac{q_3}{4\pi\varepsilon_0}\left[\dfrac{1}{r}\right]_\infty^{R_3} = \dfrac{q_3}{4\pi\varepsilon_0 R_3}$`
   - *Texto propuesto en `u02-e4` (línea 316):*
     > `$V(R_1) - V(R_2) = -\displaystyle\int_{R_2}^{R_1} \dfrac{Q}{4\pi\varepsilon_0 r^2}\,dr = \dfrac{Q}{4\pi\varepsilon_0}\left[\dfrac{1}{r}\right]_{R_2}^{R_1} = \dfrac{Q}{4\pi\varepsilon_0}\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$`
   - *Texto propuesto en `u02-e4` (`li.check`, línea 318, agregar al final):*
     > `Unidades: $[Q/(\varepsilon_0 R_1)] = \text{N·m/C} = \text{V}$. Límite $R_2 \to \infty$: $V(R_1) \to \frac{Q}{4\pi\varepsilon_0 R_1}$, el potencial de una esfera conductora aislada.`
   - *Texto propuesto en `u02-p5` (línea 537):*
     > `$Q = \displaystyle\int_0^\infty \rho(z)\,A\,dz = \varepsilon_0 A\left[-a e^{-\alpha z} - b e^{-\beta z}\right]_0^\infty = \varepsilon_0 A(a + b)$`

3. **Agregar las verificaciones faltantes en `u02-p2` (línea 473) y `u02-x1` (línea 358) [SPEC §3.6, §9.8]:**
   - *Ubicación:* `unidades/u02-gauss.html#L473` (`u02-p2`) y `#L358` (`u02-x1`).
   - *Texto propuesto para `u02-p2` (`li.check`, línea 473, agregar al final):*
     > `Unidades: $[\rho_0 a/\varepsilon_0] = (\text{C/m}^3)(\text{m})/(\text{C}^2/\text{N·m}^2) = \text{N/C}$.`
   - *Texto propuesto para `u02-x1` (`li.check`, línea 358, agregar al final):*
     > `Límite: si $q_{\text{neta}} = +2\beta\pi R^6 = -Q$ (cascarón neutralizando exactamente a la esfera), entonces $\vec E_4 = \vec 0$ para todo $r \gt 3R$.`

4. **Añadir unidades SI faltantes en `u02-s7` (líneas 216–221) y en la tabla `u02-formulas` (líneas 591–601) [SPEC §1, §9.2]:**
   - *Ubicación:* `unidades/u02-gauss.html#L216-L221` y `#L591-L601`.
   - *Texto propuesto en `u02-s7`:*
     - Línea 216: `donde $\vec r_\perp$ ($\text{m}$) es el vector perpendicular desde el eje hasta el punto`
     - Línea 218 (`.note`): `con otro material uniforme de densidad $\rho_Q$ ($\text{C/m}^3$)`
     - Línea 221 (`.note`): `($\nabla\cdot\vec E$ tiene unidades SI de $\text{N/(C·m)} = \text{V/m}^2$)`
   - *Texto propuesto en `u02-formulas`:* completar las unidades SI en la segunda columna para cada símbolo introducido en la fila (p. ej. línea 591: `$E$ ($\text{N/C}$), $A$ ($\text{m}^2$)`; línea 595: `$R, r$ ($\text{m}$)`; línea 598: `$q_{\text{int}}, Q_{\text{enc}}, q_{\text{ext}}, Q_{\text{cond}}$ ($\text{C}$), $\sigma$ ($\text{C/m}^2$), $E_{\text{sup}}$ ($\text{N/C}$)`).

5. **Justificar en `Repaso exprés` 3 (línea 46) por qué $\vec E = \vec 0$ entre cascarones conectados y unificar variable muda $r'$ en `u02-x1` (línea 341) [SPEC §1, §9.5]:**
   - *Ubicación:* `unidades/u02-gauss.html#L46` y `#L341`.
   - *Texto propuesto en línea 46:*
     > `<b>Conectar dos conductores con un cable:</b> los une en un solo conductor equipotencial ($V_1 = V_2$). Si no hay cargas libres en el espacio que los separa (en simetría esférica o cilíndrica, $-\int_{R_1}^{R_2} E_r\,dr = 0$ con $E_r \propto Q_{\text{enc}}$ exige $Q_{\text{enc}} = 0$), entonces $\vec E = \vec 0$ entre ellos y las cargas enfrentadas se neutralizan.`
   - *Texto propuesto en línea 341 (`u02-x1`, Paso 1):* cambiar la variable muda `r` por `r'` (`$\int_0^R (-3\beta {r'}^3){r'}^2\,dr'$`) para mantener consistencia con `Paso 4` (línea 351).
