# Reporte G4 (Autosuficiencia) — Unidad 11: Corriente alterna y ondas EM

**Archivo revisado:** `unidades/u11-ca-ondas.html`  
**Contrato:** `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5 y §9)  
**Perfil simulado:** Estudiante de 2.º año de ingeniería con **solo** esta unidad (sin clases, sin otras unidades, sin calculadora, sin formulario).

---

## 1. Evaluabilidad de arquetipos y práctica + suficiencia de profundidad (SPEC §2 y §3)

### 1.1 Resolución desde la unidad sola (sin abrir pasos)

| Ítem | ID | ¿Resoluble solo con U11? | Qué bloquea y por qué |
|---|---|---|---|
| Arquetipo 1 (Examen 2025-1 P5) | `u11-x1` | **Sí** (salvedad menor) | Las reglas de serie (`u11-s1`, `u11-s2`), fasores ($\hat I = \hat V/Z_{\text{eq}}$) y resonancia ($\operatorname{Im} Z_{\text{eq}} = 0$) están cubiertas. Salvedad menor: el enunciado (línea 213) remite a la figura para la referencia de $\hat V_L$ sin explicitar en texto la polaridad respecto al sentido de $\hat I$ (SPEC §9.6). |
| Arquetipo 2 (Examen 2025-2 P3) | `u11-x2` | **Sí** (ambigüedad en c) | Asociación en paralelo (`u11-s2`), módulo de cociente (`Repaso exprés`, línea 28) y $\langle P\rangle$ (`u11-s3`) están cubiertos. Sin embargo, la parte c) pregunta *"potencia que se disipa en el circuito durante un período"* (línea 235): el estudiante puede dudar entre potencia media $\langle P\rangle$ o energía total en un ciclo $E_T = \langle P\rangle T$ (ambigüedad reconocida en el Paso 3, línea 245, pero ausente en `li.final`). |
| Arquetipo 3 (Examen 2025-1 P6) | `u11-x3` | **Parcialmente** (bloqueo en demostración) | **Bloqueo en la demostración de $\vec k\times\vec E = \omega\vec B$ (2,5 pts.):** ni `Repaso exprés` ni `u11-s4` definen el operador rotor $\nabla\times\vec E$ en coordenadas cartesianas, por lo que el estudiante sin formulario no tiene cómo justificar el paso *"el determinante del rotor da $\nabla\times\vec E = -j\vec k\times\vec E$"* (línea 264). Las partes a) y b) ($\vec B$, $\vec S$, $P$) sí son resolubles con `u11-s4` y `u11-s5`. |
| Práctica 1 | `u11-p1` | **Sí** | Todos los pasos ($Z$, $I_{\text{rms}}$, $\cos\varphi$, $\langle P\rangle$, compensación a $\cos\varphi=1$) están en `u11-s1`–`u11-s3` y los números forman un triángulo 3-4-5 ($40$-$30$-$50$) calculable a mano. |
| Práctica 2 (base 2024-2 P3) | `u11-p2` | **Sí** | La EDO de malla (`u11-s2` Paso 1), la suma de impedancias en serie (`u11-s1`) y $\operatorname{Im} Z_{\text{eq}} = 0$ (`u11-s2`) bastan para resolver las tres partes. |
| Práctica 3 | `u11-p3` | **Sí** | Producto cruz dextrógiro (`Repaso exprés`, línea 35), $\vec B = \frac{1}{c}(\hat k\times\vec E)$ (`u11-s4`) y $\vec S, I$ (`u11-s5`) permiten resolverlo a mano usando la terna $3/5, 4/5$. |
| Práctica 4 | `u11-p4` | **Sí** (con conocimiento trigonométrico externo) | La unidad advierte en `u11-s5` (línea 133) que al superponer ondas se suman primero $\vec E$ y $\vec B$. Sin embargo, en a) se requiere $\cos A\cos B = \frac12[\cos(A-B)+\cos(A+B)]$ y $\cos(\pi/3) = 1/2$, que no figuran en `Repaso exprés`. |

### 1.2 Juicio de profundidad frente a SPEC §2 y §3

Para cubrir **dos temas extensos** (Circuitos CA + Ondas EM), la unidad es **funcional para los arquetipos actuales del banco, pero delgada en fundamentos operativos**:

1. **En Circuitos CA (`u11-s1`–`u11-s3`):**
   - Falta enunciar la validez de las **leyes de Kirchhoff en forma fasorial** ($\sum \hat V_k = 0$, $\sum \hat I_k = 0$) y mostrar cómo calcular el voltaje o la corriente en una **rama individual** de una red mixta (divisor de voltaje/corriente).
   - La **antirresonancia** ($I_0 = 0$) aparece por primera vez en `u11-e3` sin haber sido introducida en `u11-s2`.
   - No se explica cómo proceder si la fuente viene con $\sin(\omega t)$ o con una fase inicial $\phi_V \neq 0$ (todos los ejemplos usan $V_0\cos(\omega t)$).
2. **En Ondas EM (`u11-s4`–`u11-s5`):**
   - Falta definir $\nabla\times$ y $\nabla^2$ en coordenadas cartesianas para que la derivación de la ecuación de onda y $\vec k\times\vec E = \omega\vec B$ sea autocontenida.
   - El objetivo 6 de `u11-mapa` (línea 14) promete *"identificar su polarización"*, pero la teoría solo cubre polarización lineal (no menciona polarización circular/elíptica ni luz no polarizada).
   - En `u11-s4` (línea 116) se menciona de paso la propagación en medios ($v = c/n$), sin definir $n$, $\varepsilon$ ni $\mu$.
   - Solo hay **1 ejemplo resuelto** (`u11-e2`) y **1 arquetipo** (`u11-x3`) de ondas EM frente a 2 ejemplos y 2 arquetipos de CA (en parte reflejo del banco reciente, pero un ejemplo adicional de ondas, p. ej. con incidencia oblicua sobre un receptor como se menciona en `u11-s5` línea 131, equilibraría la práctica).

---

## 2. Saltos de derivación

1. **`u11-s1`, Paso 1 (línea 49):** En $q(t) = \int i(t)\,dt = \operatorname{Re}\!\left\{\frac{\hat I}{j\omega}\,e^{j\omega t}\right\}$ se omite sin explicar por qué la constante de integración es nula (régimen estacionario sinusoidal sin componente DC).
2. **`u11-s2`, Paso 2 (línea 75):** Se pasa de $j\omega V_0 = (-\omega^2 L + j\omega R + 1/C)\hat I$ a $V_0 = \left[R + j\left(\omega L - \frac{1}{\omega C}\right)\right]\hat I$ sin mostrar la división por $j\omega$ ni la simplificación $-\omega^2 L / (j\omega) = +j\omega L$ (usando $1/j = -j$).
3. **`u11-s3`, Paso 1 y 3 (líneas 91 y 95):**
   - Línea 91: usa $\cos(\omega t - \varphi) = \cos\omega t\cos\varphi + \sin\omega t\sin\varphi$ sin haberla incluido en `Repaso exprés`.
   - Línea 95: afirma *"para un circuito serie, $V_0\cos\varphi = I_0 R$"* sin mostrar el paso previo ($\cos\varphi = R/|Z|$ e $I_0 = V_0/|Z|$).
4. **`u11-s4`, Paso 1 y 2 (líneas 107–112):**
   - Línea 107: intercambia $\nabla\times$ y $\partial/\partial t$ sin comentarlo y no define el laplaciano vectorial $\nabla^2\vec E$.
   - Línea 108: compara con $\nabla^2 f = \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$ asumiendo que el estudiante recuerda la ecuación de onda clásica.
   - Línea 109 y 112: pasa directamente a $\nabla\times \leftrightarrow j\vec k\times$ (y en `u11-x3` línea 264 a *"el determinante del rotor da $\nabla\times\vec E = -j\vec k\times\vec E$"*) sin escribir explícitamente al menos una componente del rotor para demostrarlo.
5. **`u11-s5`, introducción y Paso 2 (líneas 123 y 128):**
   - Línea 123: introduce $u = \frac12(\varepsilon_0 E^2 + B^2/\mu_0)$ y $\vec S = \frac{1}{\mu_0}(\vec E\times\vec B)$ sin derivarlos ni mencionar el teorema de Poynting.
   - Línea 128: usa la identidad $\hat n\times(\hat k\times\hat n) = \hat k$ (regla BAC-CAB para $\hat n\perp\hat k$) sin justificarla ni tenerla en `Repaso exprés`.

---

## 3. Símbolos usados antes de definirse o sin unidades SI

| Ubicación (id y línea) | Símbolo(s) | Problema detectado |
|---|---|---|
| `u11-mapa` (línea 7, Idea central) | $j, \omega, Z_R, R, Z_L, L, Z_C, C, \vec E, \vec B, c, \mu_0, \varepsilon_0, \vec S$ | Aparecen en el resumen inicial antes de definirse en la teoría y sin unidades SI. |
| `u11-mapa`, `Repaso exprés` 1 (línea 23) | $\theta$ | Argumento complejo usado sin unidad SI ($\text{rad}$). |
| `u11-mapa`, `Repaso exprés` 2 (línea 33) | $T$, $\omega$, $\delta$ | $T$ y $\omega$ sin unidades SI ($\text{s}$, $\text{rad/s}$); $\delta$ sin definir ni unidad ($\text{rad}$). |
| `u11-s1` (líneas 44, 46, 49, 51) | $v(t)$, $t$, $\phi_V$, $\phi_I$, $q(t)$, $\phi$, $V_{R0}$, $V_{L0}$, $V_{C0}$ | $t$ ($\text{s}$) y $q(t)$ ($\text{C}$) sin definir ni unidades; $\phi_V, \phi_I, \phi$ ($\text{rad}$) sin unidades; $V_{R0}, V_{L0}, V_{C0}$ ($\text{V}$) usados sin definición explícita. |
| `u11-s2` (líneas 68, 70) | $I_0$, $\varphi$ | Primera aparición de $I_0$ ($\text{A}$) y $\varphi$ ($\text{rad}$) en la sección sin unidades SI explícitas. |
| `u11-s3` (líneas 87, 89) | $p(t)$, $\varphi$ | $p(t)$ sin unidad SI ($\text{W}$); $\varphi$ sin unidad ($\text{rad}$). |
| `u11-s4` (líneas 104, 108, 116) | $\vec r$, $\delta$, $f$, $\varepsilon$, $\mu$, $n$ | $\vec r$ ($\text{m}$) y $\delta$ ($\text{rad}$) no aparecen definidos en `.note` (línea 104); $f$ en $\nabla^2 f$ (línea 108) sin definir; $\varepsilon$, $\mu$ y $n$ (línea 116) sin definir ni unidades SI. |
| `u11-s5` (líneas 126, 131) | $u_E$, $u_B$, $\theta$ | $u_E, u_B$ ($\text{J/m}^3$) sin unidad explícita; $\theta$ ($\text{rad}$) sin unidad. |
| Enunciados simbólicos (`u11-e3` l.186, `u11-x1` l.213, `u11-x2` l.235, `u11-x3` l.256, `u11-p2` l.313, `u11-p3` l.334, `u11-p4` l.355) | $R, L, C, C_1, C_2, V_0, U_0, \omega, E_0, k, k_z, \mu_0, a$ | Según SPEC §9.2, los enunciados de problemas simbólicos deben indicar las unidades SI de sus símbolos (ninguno de los 7 enunciados simbólicos lo hace). |

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

No hay referencias prohibidas del tipo *"ver clase X"* o *"como vimos en la unidad Y"* para omitir resultados; las menciones a `Ayudantía 24`, `Examen 2024-2 P3` o `Tema 5 Ondas EM` cumplen función de trazabilidad (`.src`, SPEC §6). Sin embargo, existen **dependencias implícitas**:

1. **`u11-x1` (línea 213):** *"como se observa en la figura (en la rama derecha hay una sola inductancia $L$, sobre la cual se indica la referencia de voltaje $\hat V_L$)"* — El signo de $\hat V_L$ depende de la polaridad dibujada en la figura `u11-arq1-2025-1-p5`, no descrita en el texto.
2. **`u11-s2` (línea 72):** *"Por la regla de mallas de Kirchhoff en el sentido de $i(t)$"* — Aplica la ley de mallas sin haberla enunciado en la unidad.
3. **`u11-s4` (línea 108):** *"Comparando con la ecuación de onda $\nabla^2 f = \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$"* — Supone conocida la forma general de la ecuación de onda sin mostrarla previamente.
4. **`u11-s5` (línea 123):** Da por conocidas las fórmulas de densidad de energía $u_E = \frac12\varepsilon_0 E^2$ y $u_B = \frac{B^2}{2\mu_0}$ de unidades previas.

---

## 5. Prerrequisitos usados pero no cubiertos por los recuadros `Repaso exprés`

Los dos recuadros `details.prereq` de `u11-mapa` (líneas 21–39) cubren complejos/Euler, promedios de $\cos$ y $\cos^2$, producto cruz unitario, doble rotor y ecuaciones de Maxwell en el vacío. Quedan **sin cubrir**:

1. **Definición cartesiana del rotor ($\nabla\times\vec A$) y del laplaciano ($\nabla^2$):** indispensable para `u11-s4` Paso 2 y `u11-x3` Paso 1 (2,5 pts.).
2. **Identidad del triple producto vectorial (BAC-CAB):** $\vec A\times(\vec B\times\vec C) = \vec B(\vec A\cdot\vec C) - \vec C(\vec A\cdot\vec B)$, usada en `u11-s5` (línea 128).
3. **Identidades trigonométricas:** $\cos(A - B) = \cos A\cos B + \sin A\sin B$ (usada en `u11-s3` línea 91), $\cos A\cos B = \frac12[\cos(A-B) + \cos(A+B)]$ y valor exacto $\cos(\pi/3) = 1/2$ (usados en `u11-p4` línea 364).
4. **Regla de mallas de Kirchhoff y ecuaciones constitutivas de $R, L, C$ ($v_R = iR$, $v_L = L\,di/dt$, $v_C = q/C$):** usadas en `u11-s1`, `u11-s2` y `u11-p2`.
5. **Ecuación de onda clásica** ($\nabla^2 f = \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$) y **densidades de energía** ($u_E = \frac12\varepsilon_0 E^2$, $u_B = \frac{B^2}{2\mu_0}$).

---

## 6. Violaciones de `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§3.6 y §9.8 (Verificación con análisis dimensional + límite en cada problema):**
  - `u11-e1` (línea 156): verifica potencia y $\omega \gt \omega_0$, pero **falta análisis dimensional**.
  - `u11-p1` (línea 304): verifica $I_{\text{rms}}^2 R$ y unidades, pero **falta un límite o caso conocido**.
  - `u11-p3` (línea 346): verifica límite $\hat n = \hat x$, pero **falta análisis dimensional**.
  - `u11-p4` (línea 367): verifica límite de onda estacionaria, pero **falta análisis dimensional**.
- **§9.4 (`li.final` debe contener todo lo pedido en el enunciado):**
  - **`u11-p4` (línea 366):** El enunciado y `Piden` solicitan *"los campos totales $\vec E$ y $\vec B$"*, pero `li.final` solo reporta $\langle\vec S\rangle$ e $I$ (omite $\vec E$ y $\vec B$).
  - **`u11-e3` (línea 198):** La parte c) pregunta *"qué ocurre a la frecuencia en que se anula la corriente"*, y `li.final` solo da $\omega_{\text{anti}}$ sin la respuesta cualitativa (impedancia infinita / cancelación de corrientes en el nodo).
- **§5 (Notación $j$ y amplitud vs. rms):**
  - **Cumple:** usa $j$, fasores $\hat V, \hat I$, $Z_L = j\omega L$, $Z_C = 1/(j\omega C)$, declara $i$ y $A\angle\phi$ como equivalencias, distingue $V_0, I_0$ de $V_{\text{rms}}, I_{\text{rms}}$, y usa ambos factores ($1/2$ vs. sin $1/2$) en $\langle P\rangle$.
- **§9.5 (Sin símbolos sobrecargados):**
  - **$f$ sobrecargado en `u11-s4` (línea 108):** en la misma línea, $f$ es función de onda ($\nabla^2 f = \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$) y frecuencia ($\lambda f = c$).
  - **$I$ para corriente vs. intensidad:** `u11-x2` (línea 235) y `u11-p2` (línea 313) usan $I(t)$ para corriente, mientras `u11-s5`–`u11-p4` usan $I$ para intensidad de onda (aunque `u11-s5` línea 123 lo advierte).
  - **$\phi$ vs. $\varphi$:** el desfase entre $v$ e $i$ se llama $\phi$ en `u11-s1` (línea 51) y `u11-s3` (línea 95), pero $\varphi$ en `u11-s2`, `u11-s3` (línea 89) y los problemas.
- **§9.1 (Cálculo a mano) y §9.9 (`\lt`/`\gt` en HTML):**
  - **Cumple:** usa triángulos 3-4-5 y potencias de 10; usa `\lt` y `\gt` dentro de fórmulas en toda la unidad.

---

## 7. Las 5 mejoras más valiosas (ordenadas por impacto)

### 1. Completar `Repaso exprés` con $\nabla\times$, BAC-CAB y trigonometría + detallar el rotor en `#u11-s4`
- **Ubicación:** `#u11-mapa` (`Repaso exprés` 2, líneas 34–35) y `#u11-s4` (Paso 2, línea 112).
- **Por qué:** Desbloquea la demostración de 2,5 pts. de `#u11-x3` (2025-1 P6) y elimina los saltos algebraicos en `#u11-s4`, `#u11-s5` y `#u11-p4`.
- **Texto propuesto (para `#u11-mapa`, tras línea 35):**
  > `<p><b>Identidades vectoriales y trigonométricas útiles:</b> triple producto $\vec A\times(\vec B\times\vec C) = \vec B(\vec A\cdot\vec C) - \vec C(\vec A\cdot\vec B)$. Rotor en cartesianas: $(\nabla\times\vec E)_x = \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}$ (y permutaciones cíclicas $x\to y\to z$). Suma de ángulos: $\cos(A\pm B) = \cos A\cos B \mp \sin A\sin B$, y $\cos A\cos B = \frac12[\cos(A-B)+\cos(A+B)]$.</p>`
- **Texto propuesto (para `#u11-s4`, línea 112):**
  > `Por ejemplo, la componente $x$ del rotor es $\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} = j(k_y E_z - k_z E_y) = (j\vec k\times\vec E)_x$, luego $\nabla\times\vec E = j\vec k\times\vec E$.`

### 2. Completar `li.final` en Práctica 4 (`#u11-p4`) y Ejemplo 3 (`#u11-e3`) según SPEC §9.4
- **Ubicación:** `#u11-p4` (`li.final`, línea 366) y `#u11-e3` (`li.final`, línea 198).
- **Por qué:** `#u11-p4` pide $\vec E$ y $\vec B$ totales pero los omite en la caja final; `#u11-e3` pide qué ocurre en $\omega_{\text{anti}}$ pero solo da la fórmula.
- **Texto propuesto (`#u11-p4`, línea 366):**
  > `$$\boxed{\text{Mismo sentido: }\vec E = E_0[\cos u + 2\cos(u+\tfrac{\pi}{3})]\,\hat y,\ \vec B = \frac{E_0}{c}[\cos u + 2\cos(u+\tfrac{\pi}{3})]\,\hat z,\ \langle\vec S\rangle = \frac{7}{2}c\varepsilon_0 E_0^2\,\hat x,\ I = \frac{7}{2}c\varepsilon_0 E_0^2}$$ $$\boxed{\text{Opuestos: }\langle\vec S\rangle = -\frac{3}{2}c\varepsilon_0 E_0^2\,\hat x,\ I = \frac{3}{2}c\varepsilon_0 E_0^2}$$` (indicando $u = kx - \omega t$).
- **Texto propuesto (`#u11-e3`, línea 198):** agregar tras $\omega_{\text{anti}}$:
  > `\text{ (antirresonancia: }|Z_{\text{eq}}|\to\infty\text{, corrientes de ramas iguales y opuestas se cancelan en el nodo)}`

### 3. Hacer autosuficiente el enunciado de `#u11-x1` y aclarar `#u11-x2` parte c)
- **Ubicación:** `#u11-x1` (línea 213) y `#u11-x2` (líneas 235 y 246).
- **Por qué:** Cumple SPEC §9.6 (no depender de la figura para la polaridad de $\hat V_L$) y elimina la ambigüedad entre potencia media y energía por período en `#u11-x2`.
- **Texto propuesto (`#u11-x1`, línea 213):** reemplazar el paréntesis por:
  > `(en la rama derecha hay una sola inductancia $L$, con $\hat V_L$ medido en el sentido de la corriente $\hat I$, es decir, signo $+$ en el terminal de entrada de $\hat I$)`
- **Texto propuesto (`#u11-x2`, línea 246, en `li.final`):** añadir entre paréntesis:
  > `\text{ (energía por período: }E_T = \langle P\rangle T = \frac{2\pi U_0^2\sqrt{LC}}{R}\text{)}`

### 4. Incorporar análisis dimensional y límites faltantes en las verificaciones (`li.check`)
- **Ubicación:** `#u11-e1` (línea 156), `#u11-p1` (línea 304), `#u11-p3` (línea 346) y `#u11-p4` (línea 367).
- **Por qué:** Exigido explícitamente por SPEC §3.6 y §9.8 en cada problema.
- **Texto propuesto (para `#u11-e1`, línea 156):** agregar:
  > `Unidades: $[\omega_0] = 1/\sqrt{\text{H}\cdot\text{F}} = \text{rad/s}$ y $[V_0 I_0] = \text{V}\cdot\text{A} = \text{W}$.`
- **Texto propuesto (para `#u11-p3`, línea 346):** agregar:
  > `Unidades: $[c\varepsilon_0 E_0^2] = (\text{m/s})\cdot(\text{C}^2/(\text{N}\cdot\text{m}^2))\cdot(\text{V/m})^2 = \text{W/m}^2$.`

### 5. Añadir unidades SI en primeras apariciones/enunciados simbólicos y evitar sobrecarga de $f$
- **Ubicación:** `#u11-s4` (líneas 104 y 108) y enunciados simbólicos (`#u11-e3`, `#u11-x1`–`#u11-x3`, `#u11-p2`–`#u11-p4`).
- **Por qué:** Cumple SPEC §1, §9.2 y §9.5.
- **Texto propuesto (`#u11-s4`, línea 108):** cambiar $\nabla^2 f = \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$ por:
  > `Comparando con la ecuación de onda para una perturbación escalar $\psi(\vec r, t)$: $\nabla^2\psi = \frac{1}{v^2}\frac{\partial^2\psi}{\partial t^2}$ (con $v$ en $\text{m/s}$)`
- **Texto propuesto (`#u11-s4`, línea 104, `.note`):** añadir:
  > `$\vec r$: vector posición ($\text{m}$); $t$: tiempo ($\text{s}$); $\delta$: fase inicial ($\text{rad}$).`
- **Texto propuesto (enunciados simbólicos, p. ej. `#u11-x1` línea 213):**
  > `...dos resistencias $R$ ($\Omega$), dos inductancias $L$ ($\text{H}$) y una capacitancia $C$ ($\text{F}$)... $V(t) = V_0\cos(\omega t)$ ($V_0$ en $\text{V}$, $\omega$ en $\text{rad/s}$)...` (aplicar análogo en `#u11-e3`, `#u11-x2`, `#u11-x3`, `#u11-p2`, `#u11-p3`, `#u11-p4`).
