# Reporte G4 (Autosuficiencia) — U8: Fuentes de campo magnético

- **Archivo revisado:** `unidades/u08-fuentes-campo.html`
- **Contrato de referencia:** `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5 y §9)
- **Perfil simulado:** estudiante de 2.º año de ingeniería con **solo** esta unidad (sin clases, sin otras unidades, sin calculadora ni formulario).

---

## 1. Resolubilidad por arquetipo de examen y problema de práctica

| ID | Título | ¿Resoluble solo con la unidad? | Qué bloquea (si aplica) y por qué |
|---|---|---|---|
| `u08-x1` | Dos semicircunferencias concéntricas y momento dipolar (2024-2 P2) | **Sí** | Sin bloqueos conceptuales. La regla 1 de `u08-s3` justifica los tramos rectos colineales con $P$; `u08-s3` da $B_{\text{arco}} = \mu_0 I\phi/(4\pi R)$ y $\vec\mu = NIA\,\hat n$. *(Menor: `li.final` está completo, pero en Paso 1 aparece $\hat\imath$ sin haber sido declarado como $\hat x$.)* |
| `u08-x2` | Cable coaxial con $\vec J_1$ no uniforme y gráfico de $\|B(r)\|$ (2024-1 P1) | **Sí** | Sin bloqueos para resolver. El `Repaso exprés` de integrales en polares incluye exactamente el ejemplo $\vec J = \alpha r\,\hat z$ y `u08-s5` explica el procedimiento en 4 regiones. *(Incumple §9.2 y §9.4: faltan unidades SI de $\alpha, \beta$ en el enunciado y `li.final` omite la parte c del gráfico.)* |
| `u08-x3` | Cable coaxial de tres regiones con corrientes uniformes (2025-1 P3) | **Sí** | Sin bloqueos para resolver; la estrategia de Ampère (`u08-s4`) y `u08-s5` cubren las 3 regiones. *(Incumple §9.4: `li.final` omite el resumen/valores clave del gráfico pedido en b.)* |
| `u08-p1` | Sector circular con dos arcos concéntricos | **Sí** | Sin bloqueos. Cálculo a mano limpio con $\mu_0 = 4\pi\times10^{-7}\ \text{T·m/A}$. |
| `u08-p2` | Fuerza neta de un alambre infinito sobre una espira coplanar | **Sí** | Sin bloqueos; aunque la orientación cambia respecto al `Repaso exprés` (eje $z$ hacia arriba y $\hat x$ saliendo), la regla $\hat z\times\hat y = -\hat x$ está en el repaso (`u08-mapa`). |
| `u08-p3` | Toroide ideal: campo en tres regiones | **Sí** | Sin bloqueos. `u08-s6` cubre toroide y solenoide, y los números se calculan a mano sin calculadora. |
| `u08-p4` | Lámina gruesa infinita y cilindro no uniforme: anulación de $\vec B$ | **Parcial (fricción)** | La teoría (`u08-s6`) solo deriva una lámina **delgada** con densidad superficial $K$, no una lámina **gruesa** de espesor $b$ con densidad volumétrica $\vec J_s$ (la equivalencia $K = j_s b$ solo aparece en el pie de figura de `u08-p4`). Además, usa $\vec J_s$ como densidad volumétrica ($\text{A/m}^2$) cuando `u08-s6` declaró $J_s$ como densidad superficial ($\text{A/m}$). |
| `u08-p5` | Cilindro infinito con cavidad cilíndrica descentrada | **No (bloqueado sin pista)** | **Bloqueo en el planteo:** ni la teoría (`u08-s5`) ni los `Repaso exprés` enseñan la forma vectorial $\vec B(\vec r) = \frac{1}{2}\mu_0(\vec J\times\vec r)$ ni el principio de superposición $+\vec J / -\vec J$ para modelar cavidades. Sin abrir `li.hint` o el pie de figura, un estudiante que solo conoce $B(r) = \frac{\mu_0 I r}{2\pi R^2}\hat\theta$ queda atascado sumando dos sistemas polares con orígenes distintos $O$ y $O'$. |

---

## 2. Saltos en derivaciones

1. **`u08-s1` (línea 50, de carga a corriente):** `"la carga móvil $dq$ con velocidad de arrastre $\vec v_d$ cumple $dq\,\vec v_d = (dq/dt)\,d\vec\ell = I\,d\vec\ell$."` No se muestra el paso intermedio $\vec v_d = d\vec\ell/dt$ que justifica mover el diferencial $dt$ de $d\vec\ell$ hacia $dq$.
2. **`u08-s5` (línea 121, simetría del cilindro infinito):** `"así que $\vec B = B(r)\,\hat\theta$ (descartando componente radial por $\nabla\cdot\vec B = 0$)." ` Se descarta $B_r$, pero no se justifica por qué no existe componente axial $B_z(r)\,\hat z$ (que también cumple $\nabla\cdot\vec B = 0$ y requiere argumentar con Biot-Savart $d\vec\ell\times\hat r \perp \hat z$ o con un lazo amperiano axial).
3. **`u08-s6` (línea 149, lámina infinita):** `"Un rectángulo amperiano de ancho $L$ paralelo a $\vec B$ que cruza la lámina da $\oint\vec B\cdot d\vec\ell = 2BL = \mu_0 KL$."` Falta explicitar por qué los dos lados perpendiculares a la lámina aportan $0$ ($\vec B\perp d\vec\ell$) y por qué los dos lados paralelos tienen igual magnitud $B$ (simetría de reflexión respecto al plano).
4. **`u08-p5` (línea 452, Paso 1):** `"Como $\hat z\times\hat r = \hat\theta$, se escribe en forma vectorial independiente de los ejes como $\vec B(\vec r) = \frac{1}{2}\mu_0 (\vec J\times\vec r)$."` Se introduce esta identidad vectorial por primera vez dentro de un ejercicio de práctica (sin haberla deducido en `u08-s5`), y se usa $\vec r$ (vector posición 3D o 2D respecto al eje) y $\hat r$ sin aclarar que aquí $\hat r$ no es el vector unitario de Biot-Savart sino $\hat\rho$.

---

## 3. Símbolos usados antes de definirse o sin unidades SI

- **`u08-s1` (línea 49):** aparece $\varepsilon_0$ en `$\varepsilon_0\mu_0 = 1/c^2$` sin definir qué es $\varepsilon_0$ ni sus unidades SI ($\text{C}^2/(\text{N·m}^2)$ o $\text{F/m}$); tampoco se dice explícitamente que $c$ es la rapidez de la luz en el vacío.
- **`u08-x1` Paso 1 (línea 271):** aparece `$\hat\imath$` (`"son colineales con $\hat\imath$"`) sin haberse definido nunca en la unidad (toda la unidad usa $\hat x, \hat y, \hat z$, y el enunciado de `u08-x1` usa $\hat x, \hat y, \hat k$).
- **`u08-mapa` `Repaso exprés` (líneas 30 y 33):** $d\vec A$ aparece sin indicar unidades SI ($\text{m}^2$); en el mini ejemplo (línea 33), el radio $a$ aparece sin unidades ($\text{m}$).
- **`u08-s2` (línea 71):** el largo $L$ del tramo de alambre paralelo se usa antes de indicar unidades (`m`).
- **`u08-s5` (líneas 128 y 131):** en `$\vec J(r) = \alpha r^n\,\hat z$`, $\alpha$ se introduce sin unidades SI ($\text{A/m}^{n+2}$); los radios $a, b, c$ del coaxial se usan sin indicar `(m)`.
- **`u08-s6` (líneas 145 y 148):** $\ell$ (largo del solenoide), $L$ (lado del lazo amperiano) y $b, c$ (radios del toroide) no declaran unidades SI `(m)` en su primera aparición.
- **Enunciados simbólicos sin unidades SI explícitas (viola §9.2):**
  - `u08-x2` (línea 289): no declara unidades de $\alpha$ ($\text{A/m}^3$), $\beta$ ($\text{A/m}^2$), $a, b, c$ ($\text{m}$) ni $I_0$ ($\text{A}$).
  - `u08-p4` (línea 423): no declara unidades de $j_s, j_0$ ($\text{A/m}^2$) ni de $b, R$ ($\text{m}$).
  - `u08-p5` (línea 444): no declara unidades de $J_0$ ($\text{A/m}^2$) ni de $R, a, d$ ($\text{m}$).
  - También faltan unidades en los enunciados simbólicos de `u08-e2`, `u08-e3`, `u08-e4` ($R, I_1, I_2, a, b, c$), `u08-x1`, `u08-x3` y `u08-p2`.

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

**No se detectaron referencias colgantes.** Todas las menciones a evaluaciones externas (`Examen 2024-2 P2`, `Examen 2024-1 P1`, `Examen 2025-1 P3`, `Ayudantía 20 P3`, `Control 3 2026-1`, `Examen 2015-2 P15`) cumplen funciones de trazabilidad (`.src`) o de registro de erratas corregidas según §1 y §6. Los enunciados de `u08-x1` y `u08-p1` describen la geometría completa en texto sin depender de la figura.

---

## 5. Prerrequisitos usados pero no cubiertos por los recuadros `Repaso exprés`

1. **Identidad $\hat z\times\vec r_\perp = r\hat\theta$ (o $\vec B = \frac{1}{2}\mu_0\vec J\times\vec r$) y método de superposición para cavidades:** usados en `u08-p5` (líneas 452–454), ausentes tanto en los `Repaso exprés` como en `u08-s5`.
2. **Evaluación de $\hat\theta$ en ejes cuando el plano de rotación no es el $xy$ estándar:** el primer `Repaso exprés` (línea 24) solo ilustra $(\hat\rho, \hat\theta, \hat z)$ en el plano $xy$ con $\hat z$ saliendo de la hoja; en `u08-e4` (línea 245) y `u08-p2` (línea 386) se requiere evaluar $\hat\theta = -\hat x$ en el plano $yz$ con $\hat z$ hacia arriba y $\hat x$ saliendo (se puede deducir de $\hat z\times\hat\rho = \hat\theta$, pero conviene mostrar un ejemplo breve).
3. **Relación entre lámina gruesa de densidad volumétrica $\vec J$ y lámina delgada $K = Jb$:** usada en `u08-p4` (línea 432), no cubierta en `u08-s6` ni en `Repaso exprés`.

---

## 6. Violaciones a `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§9.4 (`li.final` debe contener todo lo que pide el enunciado):**
  - `u08-x2` (`li.final`, línea 304): "Piden" incluye `gráfico |B(r)|` (parte c, 2 pts.), pero `li.final` solo recuadra $\alpha, \beta$ y $\vec B(r)$; omite el gráfico/comportamiento por región y los valores $B(a) = \mu_0 I_0/(2\pi a)$ y $B(b) = \mu_0 I_0/(2\pi b)$.
  - `u08-x3` (`li.final`, línea 329): "Piden" incluye `gráfico |B(r)|` (parte b, 1 pto.), pero `li.final` solo recuadra $\vec B(r)$; omite la descripción del gráfico y su máximo $B(a) = \mu_0 I_0/(2\pi a)$.
- **§5 y §9.5 (Sin símbolos sobrecargados / convenciones únicas):**
  - `u08-x2` (`li.hint`, línea 296): escribe `En polares, $d\vec s = r\,dr\,d\theta\,\hat z$` usando $d\vec s$ para el elemento de **área** ($d\vec A$), mientras que §5 reserva $d\vec s$ como equivalente del elemento de **línea** $d\vec\ell$.
  - `u08-p4` vs `u08-s6`: `u08-s6` (línea 149) declara que $J_s$ denota corriente **superficial** ($\text{A/m}$, equivalente a $K$), pero `u08-p4` (línea 423) define $\vec J_s = j_s\,\hat z$ como densidad **volumétrica** ($\text{A/m}^2$).
  - `u08-p5` (línea 452): usa $\hat r$ como vector unitario radial cilíndrico ($\hat z\times\hat r = \hat\theta$), colisionando con $\hat r$ de Biot-Savart (`u08-s1`) y con $\hat\rho$ del `Repaso exprés` (línea 25).
  - `u08-x1` y `u08-x3` vs resto de la unidad: mezclan $\hat k$ (e $\hat\imath$ en `u08-x1` Paso 1) con $\hat x, \hat y, \hat z$ sin declarar la equivalencia en los enunciados.
- **§9.2 (Unidades SI en primera aparición y enunciados simbólicos):** detallado en la sección 3.
- **§9.1 (Cálculos a mano) y §9.9 (HTML `\lt`, `\gt`):** **Cumplidos.** Todos los problemas numéricos (`u08-e1`, `u08-p1`, `u08-p3`) se calculan a mano con exactitud y todas las desigualdades en fórmulas usan `\lt` y `\gt`.
- **§3 (Formato de problema guiado) y §9.6 (Desglose de puntaje):** **Cumplidos.** Todos los problemas tienen enunciado, `Datos`/`Piden`, figura, `Antes de calcular`, `li.hint`, pasos `Qué hago`/`Por qué`, `li.final`, `li.check`, y los puntajes de `u08-x1` (4+2=6), `u08-x2` (2+2+2=6, +0,5 bonus) y `u08-x3` (5+1=6) suman exactamente el total.

---

## 7. Las 5 correcciones más valiosas (ordenadas por impacto)

### 1. Enseñar $\vec B(\vec r) = \frac{1}{2}\mu_0(\vec J\times\vec r_\perp)$ y la superposición de cavidades en `u08-s5` (y corregir $\hat r \to \hat\rho$ en `u08-p5`)
- **Ubicación:** `unidades/u08-fuentes-campo.html`, al final de la derivación en `u08-s5` (después de la línea 125) y en `u08-p5` Paso 1 (línea 452).
- **Por qué:** Desbloquea `u08-p5` para un estudiante que trabaja sin abrir la pista, elimina el salto de derivación y quita la sobrecarga de $\hat r$.
- **Texto propuesto (al final de `details.deriv` en `u08-s5`):**
```html
    <p><b>Forma vectorial (útil para cavidades por superposición):</b> como $I/(\pi R^2) = J_0$ (con $\vec J = J_0\,\hat z$) y $\hat z\times\hat\rho = \hat\theta$, si $\vec r_\perp$ es el vector desde el eje del cilindro al punto interior, se cumple</p>
    $$\vec B(\vec r_\perp) = \frac{1}{2}\mu_0\,(\vec J\times\vec r_\perp)$$
    <p>Si un cilindro tiene un hueco cilíndrico paralelo descentrado, por superposición equivale a un cilindro macizo con $+\vec J$ más un cilindro menor en la posición del hueco con $-\vec J$.</p>
```
  Y en `u08-p5` línea 452 reemplazar `Como $\hat z\times\hat r = \hat\theta$` por `Como $\hat z\times\hat\rho = \hat\theta$ (con $\vec r_\perp$ medido perpendicularmente desde el eje del cilindro)`.

### 2. Completar `li.final` en `u08-x2` y `u08-x3` con el resultado de la parte del gráfico
- **Ubicación:** `unidades/u08-fuentes-campo.html`, `u08-x2` línea 304 y `u08-x3` línea 329.
- **Por qué:** Cumple `SPEC-PEDAGOGICO.md` §9.4 (`li.final` debe incluir todo lo pedido en el enunciado).
- **Texto propuesto para `u08-x2` (línea 304, añadiendo la línea del gráfico dentro de `li.final`):**
```html
      <li class="final">$$\boxed{\alpha = \frac{3I_0}{2\pi a^3},\qquad \beta = \frac{I_0}{\pi(c^2-b^2)}}$$ $$\boxed{\vec B(r) = \begin{cases}\dfrac{\mu_0 I_0 r^2}{2\pi a^3}\,\hat\theta & (r \lt a)\\[1ex] \dfrac{\mu_0 I_0}{2\pi r}\,\hat\theta & (a \le r \le b)\\[1ex] \dfrac{\mu_0 I_0}{2\pi r}\dfrac{c^2-r^2}{c^2-b^2}\,\hat\theta & (b \lt r \le c)\\[1ex] \vec 0 & (r \gt c)\end{cases}}$$<p><b>Gráfico $|\vec B(r)|$:</b> continuo en todo $r\ge 0$; sube $\propto r^2$ hasta $B(a) = \dfrac{\mu_0 I_0}{2\pi a}$, decae $\propto 1/r$ hasta $B(b) = \dfrac{\mu_0 I_0}{2\pi b}$, cae a $0$ en $r=c$ y es $0$ para $r\gt c$.</p></li>
```
- **Texto propuesto para `u08-x3` (línea 329, añadiendo la línea del gráfico dentro de `li.final`):**
```html
      <li class="final">$$\boxed{\vec B(r) = \begin{cases}\dfrac{\mu_0 I_0 r}{2\pi a^2}\,\hat\theta & (r \lt a)\\[1ex] \dfrac{\mu_0 I_0}{2\pi r}\,\dfrac{b^2-r^2}{b^2-a^2}\,\hat\theta & (a \lt r \lt b)\\[1ex] \vec 0 & (r \gt b)\end{cases}}$$<p><b>Gráfico $|\vec B(r)|$:</b> continuo; crece linealmente en $r\lt a$ hasta el máximo $B(a) = \dfrac{\mu_0 I_0}{2\pi a}$, decrece hasta $0$ en $r=b$ y vale $0$ para $r\gt b$.</p></li>
```

### 3. Incluir la lámina gruesa en `u08-s6` y renombrar $\vec J_s \to \vec J_{\text{lám}}$ en `u08-p4`
- **Ubicación:** `unidades/u08-fuentes-campo.html`, `u08-s6` línea 149 y `u08-p4` líneas 423–433.
- **Por qué:** Elimina la dependencia no enseñada en `u08-p4` y resuelve la colisión de $J_s$ (corriente superficial en `u08-s6` vs. volumétrica en `u08-p4`).
- **Texto propuesto (al final del punto 3 en `u08-s6`, línea 149):**
```html
    <p>Si la lámina tiene <b>grosor $b$</b> (en $\text{m}$) con densidad volumétrica uniforme $\vec J$ (en $\text{A/m}^2$), un rectángulo amperiano que encierra todo el grosor $b$ encierra corriente $I_{\text{enc}} = JbL$, equivalente a $K = Jb$: fuera de la lámina $B = \dfrac{\mu_0 Jb}{2}$.</p>
```
  Y en `u08-p4` (líneas 423–433), reemplazar $\vec J_s = j_s\,\hat z$ y $\vec B_s$ por $\vec J_{\text{lám}} = j_{\text{lám}}\,\hat z$ y $\vec B_{\text{lám}}$.

### 4. Corregir $d\vec s \to d\vec A$ en `u08-x2` y $\hat\imath \to \hat x$ en `u08-x1`
- **Ubicación:** `unidades/u08-fuentes-campo.html`, `u08-x2` línea 296 y `u08-x1` línea 271.
- **Por qué:** Evita violar la convención §5 ($d\vec s$ es elemento de línea, no de área) y elimina el símbolo no definido $\hat\imath$.
- **Texto propuesto:**
  - En `u08-x2` línea 296: cambiar `En polares, $d\vec s = r\,dr\,d\theta\,\hat z$.` por `En polares, $d\vec A = r\,dr\,d\theta\,\hat z$.`
  - En `u08-x1` línea 271: cambiar `colineales con $\hat\imath$` por `colineales con $\hat x$ (o $\hat\imath$)`.

### 5. Declarar unidades SI faltantes en enunciados simbólicos y primeras apariciones
- **Ubicación:** `unidades/u08-fuentes-campo.html`, especialmente `u08-s1` línea 49 ($\varepsilon_0$), `u08-x2` línea 289 ($\alpha, \beta, a, b, c, I_0$), `u08-p4` línea 423 ($j_s, j_0, b, R$) y `u08-p5` línea 444 ($J_0, R, a, d$).
- **Por qué:** Cumple `SPEC-PEDAGOGICO.md` §1 y §9.2.
- **Texto propuesto (ejemplos concretos):**
  - En `u08-s1` línea 49: añadir `donde $\varepsilon_0 \approx 8{,}85\times10^{-12}\ \text{C}^2/(\text{N·m}^2)$ es la permitividad del vacío y $c \approx 3{,}00\times10^8\ \text{m/s}$ es la rapidez de la luz.`
  - En `u08-x2` línea 289: `radios $a \lt b \lt c$ (en $\text{m}$)... $\vec J_1 = \alpha r\,\hat z$ ($\alpha$ constante en $\text{A/m}^3$)... $\vec J_2 = -\beta\,\hat z$ ($\beta \gt 0$ en $\text{A/m}^2$)... corriente total de igual magnitud $I_0 \gt 0$ (en $\text{A}$)`
  - En `u08-p4` línea 423: `grosor $b$ ($\text{m}$)... $\vec J_{\text{lám}} = j_{\text{lám}}\,\hat z$ ($j_{\text{lám}} \gt 0$ en $\text{A/m}^2$)... radio $R$ ($\text{m}$)... $j_0$ (en $\text{A/m}^2$)`
  - En `u08-p5` línea 444: `radio $R$ ($\text{m}$)... radio $a$ ($\text{m}$)... $d$ ($\text{m}$)... $\vec J = J_0\,\hat z$ ($J_0 \gt 0$ en $\text{A/m}^2$)`
