# Reporte G4 — Autosuficiencia de U4 (`unidades/u04-capacitancia.html`)

Revisión según `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5, §9) simulando a un estudiante de segundo año de ingeniería que dispone **únicamente** de esta unidad (sin clases, sin otras unidades, sin calculadora ni formulario).

---

## 1. Simulacro de resolución: arquetipos y problemas de práctica

**Cobertura "pequeña escala" ($\vec E, \vec D, \vec P$, cargas libres y ligadas) y "gran escala" ($C_{\text{eq}}$):**
La unidad entrena bien ambos niveles en placas paralelas en paralelo (`#u04-x1`, `#u04-p5`) y en serie (`#u04-e2`), en esférico en serie (`#u04-e3`) y en cilíndrico homogéneo (`#u04-x2`). Como brecha menor, en esférico en paralelo (`#u04-p2`) el enunciado no pide explícitamente $\vec D$, $\vec P$ ni el reparto de carga libre $\sigma_{\text{libre}}$ (aunque Paso 2 y Paso 3 los calculan), y en cilíndrico en serie (`#u04-p3`) solo se piden magnitudes a gran escala ($C, Q_+, U$), sin pedir $\vec P$ ni $\sigma_b$.

| ID | Problema | ¿Resoluble solo con U4? | Paso que bloquea o genera fricción y por qué |
|---|---|---|---|
| `#u04-x1` | Arquetipo 1 · Tres placas paralelas (`2025-2 P1`) | **Sí** | Ninguno. Asociación en paralelo clara en `#u04-s2`/`#u04-s6`; $\sigma_1 = \varepsilon_1 V_{ab}/d$ y $\sigma_b = \vec P_1\cdot\hat n$ con $\hat n$ saliente del dieléctrico están cubiertos en `#u04-s4` y `#u04-s6`. |
| `#u04-x2` | Arquetipo 2 · Cable coaxial (`2018-2 P2`) | **Sí** | Ninguno. Gauss para $\vec D$ cilíndrico, $\vec E = \vec 0$ en conductores, $\vec P = (\varepsilon-\varepsilon_0)\vec E$, $\sigma_b = \vec P\cdot\hat n$ y $C/L$ están cubiertos en `Repaso exprés`, `#u04-s4` y `#u04-s5`. |
| `#u04-p1` | Práctica 1 · Red mixta de 3 geometrías en vacío | **Sí** | Ninguno para resolverlo (solo fricción menor al comparar con `li.final`, que deja $E_i$ y $|\Delta V_i|=Q/C_i$ fuera de la caja). |
| `#u04-p2` | Práctica 2 · Esférico mitad inferior con $\kappa$ | **Sí (con fricción menor)** | En Paso 1 usa "ángulo sólido ($2\pi$ sr)" (no definido en `Repaso exprés`, aunque evitable usando área hemisférica $2\pi r^2$). En Paso 2 usa continuidad tangencial $E_{1\parallel}=E_{2\parallel}$, que en `#u04-s6` se enuncia sin derivación. |
| `#u04-p3` | Práctica 3 · Coaxial con dos mantos en serie | **Sí** | Ninguno. Gauss para $\vec D$, $\int dr/r$ y asociación en serie están completamente cubiertos. |
| `#u04-p4` | Práctica 4 · Esfera conductora con cáscara dieléctrica | **Sí (con fricción menor)** | En parte b) pide $V(r_0)$ con $V(\infty)=0$, pero el `Repaso exprés` de $\Delta V$ solo muestra límites finitos $0\lt a\lt b$ y no ejemplifica el potencial absoluto tomando $V(\infty)=0$. |
| `#u04-p5` | Práctica 5 · Fuerza sobre bloque dieléctrico | **Sí (con fricción de justificación)** | Resoluble usando $F_x = -dU/dx$ de `#u04-s3`, pero esa fórmula aparece sin derivación en `#u04-s3`, por lo que el estudiante debe aplicarla por fe. |

---

## 2. Saltos en derivaciones

1. **`#u04-s3` (líneas 99 y 117) — Fuerza $F_x = -dU/dx|_Q$ y $F_x = +dU/dx|_V$ sin derivar:**
   - Se afirma `$F_x = -\dfrac{dU}{dx}$` en `.note` (línea 99) y `$F_x = +dU/dx|_{V}$` en `.why` (línea 117) sin deducirlas mediante trabajo virtual ($dW_{\text{mec}} + dU = 0$ a carga fija; $dW_{\text{bat}} = V\,dQ = dU + F_x\,dx$ a voltaje fijo).
2. **`#u04-s4` (línea 125) — $\sigma_b = \vec P\cdot\hat n$ y $\rho_b = -\nabla\cdot\vec P$ sin derivar:**
   - Las dos relaciones fundamentales de carga ligada se presentan en la caja `.eq.key` sin deducción previa (por ejemplo, desde un cilindro elemental de dipolos para $\sigma_b = \vec P\cdot\hat n$ y conservación de carga ligada total para $\rho_b = -\nabla\cdot\vec P$). La `details.deriv` (líneas 127–134) asume ambas fórmulas ya dadas.
3. **`#u04-s4` (línea 134) — Salto a $\rho_b = -\frac{\varepsilon_0(\kappa-1)}{\varepsilon}\rho_{\text{libre}}$ antes de definir $\vec D$:**
   - Escribe `$\rho_b = -\nabla\cdot\vec P = -\frac{\varepsilon_0(\kappa-1)}{\varepsilon}\rho_{\text{libre}} = 0$ donde no hay carga libre` sin mostrar el paso intermedio $\nabla\cdot\vec P = \frac{\varepsilon_0(\kappa-1)}{\varepsilon}\nabla\cdot\vec D$ ni haber introducido todavía $\nabla\cdot\vec D = \rho_{\text{libre}}$ (que recién aparece en `#u04-s5`).
4. **`#u04-s6` (línea 168) — Condiciones de borde $D_{1\perp} = D_{2\perp}$ y $E_{1\parallel} = E_{2\parallel}$ sin derivar:**
   - La `.note` declara la continuidad normal de $\vec D$ y tangencial de $\vec E$ sin mostrar el pastillero gaussiano ($\oint\vec D\cdot d\vec A = 0$) ni el lazo rectangular ($\oint\vec E\cdot d\vec\ell = 0$).
5. **`#u04-s3` (línea 106) — Generalización de $u_E = \frac{1}{2}\varepsilon_0 E^2$ a campos arbitrarios y dieléctricos:**
   - Se deduce solo para placas paralelas en vacío y se afirma `vale para cualquier campo en el vacío (y $u_E = \tfrac12\varepsilon E^2 = \tfrac12\vec D\cdot\vec E$ en un dieléctrico lineal)` sin argumento adicional.

---

## 3. Símbolos usados antes de definirse o sin unidades SI

1. **`#u04-s4` (línea 125) — $\vec p$, $n$ y $dV$:**
   - En `$\vec P = \frac{d\vec p}{dV} = n\vec p$`, ni $\vec p$ (momento dipolar eléctrico, $\text{C}\cdot\text{m}$), ni $n$ (densidad numérica de dipolos, $\text{m}^{-3}$), ni $dV$ (elemento de volumen, $\text{m}^3$) se definen ni llevan unidades SI.
2. **`#u04-s3` (línea 99) — $dV$, $F_x$ y $x$:**
   - `$dV$` (volumen, $\text{m}^3$), `$F_x$` (fuerza, $\text{N}$) y `$x$` (coordenada, $\text{m}$) aparecen sin unidades SI declaradas. Además `$q$`, `$v(q)$` (línea 97) y `$dW$` (línea 98) no explicitan sus unidades SI en su primera aparición.
3. **`#u04-s4` (línea 134) — Constante $A$ sin definir ni unidades:**
   - En `para $\vec P = \frac{A}{r^2}\hat r$`, el símbolo $A$ no se define ni lleva unidades ($\text{C}$), y sobrecarga el símbolo de área $A$.
4. **`#u04-mapa` `Repaso exprés 2` (línea 32) — $ds$:**
   - Usa `$|\Delta V| = \int_+^- E\,ds$` sin definir $ds$ (en la línea anterior usó $d\vec\ell$).
5. **Enunciados de problemas simbólicos (`SPEC §9.2`):**
   - `#u04-e3` (línea 229), `#u04-x1` (línea 263), `#u04-x2` (línea 286), `#u04-p1` (línea 323), `#u04-p2` (línea 345), `#u04-p3` (línea 370: $R, L$), `#u04-p4` (línea 392) y `#u04-p5` (línea 415) no indican unidades SI para sus parámetros simbólicos (p. ej., radios en m, carga en C, área en $\text{m}^2$, permitividad en F/m).

---

## 4. Referencias colgantes

- **No se detectaron referencias colgantes externas** necesarias para seguir el razonamiento (no hay "ver clase X" ni "ver unidad Y"). Las menciones a `2026-2`, `2025-2`, `Pauta I1 2026-1`, `Ayudantía 09`, etc. son citas de trazabilidad (`.src`) permitidas por `SPEC §1`.
- Las referencias internas a figuras (`#u04-s4` línea 128 "el bloque de la figura") y a secciones posteriores (`#u04-s4` línea 136 "como veremos en el Ejemplo 2") van acompañadas de la descripción explícita necesaria, por lo que no bloquean la lectura.

---

## 5. Prerrequisitos usados pero no cubiertos por `Repaso exprés`

1. **Divergencia en coordenadas esféricas y teorema de la divergencia:**
   - `#u04-s4` (línea 134) y `#u04-quiz` Q7 (línea 471) usan `$\nabla\cdot\vec P = \frac{1}{r^2}\frac{d}{dr}(r^2 P_r)$`, y `#u04-s5` (línea 150) aplica el teorema de la divergencia para pasar de $\nabla\cdot\vec D = \rho_{\text{libre}}$ a $\oint\vec D\cdot d\vec A = Q_{\text{libre, enc}}$. Ninguno está en `Repaso exprés`.
2. **Potencial absoluto con referencia en el infinito ($V(\infty) = 0$):**
   - `#u04-p4` (línea 401) calcula `$V(r_0) = -\int_\infty^{r_0} \vec E\cdot d\vec r$`. `Repaso exprés 2` solo trata $\Delta V = V_b - V_a$ entre radios finitos $0 \lt a \lt b$.
3. **Conservatividad del campo electrostático ($\oint\vec E\cdot d\vec\ell = 0$):**
   - Implícita en la continuidad tangencial `$E_{1\parallel} = E_{2\parallel}$` usada en `#u04-s6` (línea 168) y `#u04-p2` (línea 356).
4. **Ángulo sólido (sr):**
   - `#u04-p2` Paso 1 (línea 353) menciona `ángulo sólido ($2\pi$ sr)` sin estar en `Repaso exprés`.

---

## 6. Violaciones a `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§3.5 y §9.4 (`li.final` contiene todo lo pedido y recuadrado):**
  - `#u04-e3` (línea 248): en `li.final` aparece `$C = \left(\frac{1}{C_1}+\frac{1}{C_2}\right)^{-1}$`, pero $C_1$ y $C_2$ no fueron definidos en el enunciado ni en `li.final` (debería figurar la expresión explícita en $a, b, c, \varepsilon_1, \varepsilon_2$).
  - `#u04-p1` (línea 335): `li.final` deja `$E_1, E_2, E_3$` y `$|\Delta V_i| = Q/C_i$` fuera del `\boxed{...}` y sin las expresiones explícitas de $|\Delta V_i|$ pedidas en la parte a).
- **§3.6 y §9.8 (Verificación: dimensiones + límite):**
  - `#u04-p2` (línea 361), `#u04-p3` (línea 383) y `#u04-p4` (línea 406) verifican límites y neutralidad de carga ligada, pero omiten el análisis dimensional explícito (a diferencia de `#u04-x1`, `#u04-x2`, `#u04-p1`, `#u04-p5`).
- **§9.2 (Unidades SI en primera aparición y enunciados simbólicos):**
  - Faltan unidades SI en `#u04-s3` ($dV, F_x, x$), `#u04-s4` ($\vec p, n, dV, A$) y en los enunciados simbólicos (`#u04-e3`, `#u04-x1`, `#u04-x2`, `#u04-p1`–`#u04-p5`).
- **§9.5 (Sin símbolos sobrecargados):**
  - `$dV$` (volumen en `#u04-s3` línea 99 y `#u04-s4` línea 125) sobrecarga `$V$` (potencial/voltaje).
  - `$A$` (constante en `$\vec P = \frac{A}{r^2}\hat r$`, `#u04-s4` línea 134) sobrecarga `$A$` (área).
- **§5 (Convenciones de notación):**
  - Cumplidas ($\kappa \equiv K \equiv \varepsilon_r$, $\Delta V = V_b - V_a$, $d\vec\ell$). Solo detalles menores: `ds` en línea 32 y `d\vec r` en `#u04-p4` línea 401.
- **§9.1 (Números a mano) y §9.9 (`\lt`/`\gt` en fórmulas):**
  - Cumplidos en toda la unidad.
- **§9.6 (Arquetipos autosuficientes y suma exacta de puntajes):**
  - Cumplido en `#u04-x1` (2+2+2 = 6 pts) y `#u04-x2` (2+1,5+1,5+1 = 6 pts), con enunciados claros sin depender de la figura. En `#u04-p5` (línea 415), la frase `$x \le \text{posición} \le a$` es algo forzada (mejor redactarla en palabras).

---

## 7. Las 5 mejoras más valiosas (priorizadas)

1. **`#u04-s4` (líneas 125 y 134) — Definir $\vec p, n$, eliminar sobrecarga de $dV$ y $A$, y derivar $\sigma_b$ y $\rho_b$:**
   - *Por qué importa:* Es el único punto donde aparecen símbolos completamente indefinidos y sobrecargados en el núcleo conceptual de dieléctricos.
   - *Texto propuesto (reemplazo de `.note` en línea 125 y adición breve en `details.deriv`):*
     - En `.eq.key` (línea 125): cambiar `dV` por `d\tau` (o `d\text{Vol}`): `$$\vec P = \frac{d\vec p}{d\tau} = n\vec p, ...$$` y en `.note`: `$\vec p$: momento dipolar eléctrico de una molécula ($\text{C}\cdot\text{m}$); $n$: densidad numérica de dipolos ($\text{m}^{-3}$); $d\tau$: elemento de volumen ($\text{m}^3$); $\vec P$: vector polarización ($\text{C/m}^2$)...`
     - En línea 134: reemplazar `$A$` por `$k_0$` (`$\vec P = \frac{k_0}{r^2}\hat r$`, con `$k_0$` constante en $\text{C}$), y reemplazar la frase de `$\rho_b$` antes de `#u04-s5` por: `si $\vec P$ es radial con dependencia $1/r^2$ (como ocurre alrededor de una carga libre puntual o esfera conductora), en coordenadas esféricas $\nabla\cdot\vec P = \frac{1}{r^2}\frac{d}{dr}(r^2\cdot\frac{k_0}{r^2}) = 0$, así que $\rho_b = 0$ en todo el volumen del dieléctrico.`
     - Agregar en `details.deriv` (antes de Paso 1): `<b>Paso 0 · Origen de $\sigma_b = \vec P\cdot\hat n$:</b> en un cilindro pequeño de área $dA$ y espesor $\ell$ paralelo a $\vec P$, los dipolos alineados equivalen a cargas $\pm\sigma_b\,dA$ separadas una distancia $\ell$, con momento dipolar neto $P\,(dA\,\ell) = (\sigma_b\,dA)\,\ell \implies \sigma_b = P$ (y $\vec P\cdot\hat n$ si la cara tiene normal $\hat n$).`

2. **`#u04-mapa` (después de línea 36) — Añadir `Repaso exprés: divergencia, potencial en $\infty$ y condiciones de borde`:**
   - *Por qué importa:* Cubre todos los prerrequisitos faltantes usados en `#u04-s4`, `#u04-s5`, `#u04-s6`, `#u04-p4` y `#u04-quiz` Q7.
   - *Texto propuesto (nuevo `<details class="prereq">` tras línea 36):*
     ```html
     <details class="prereq"><summary>Repaso exprés: divergencia, potencial desde $\infty$ y continuidad en interfaces</summary>
       <ul>
         <li><b>Teorema de la divergencia y divergencia radial:</b> $\displaystyle\int_{\text{Vol}}(\nabla\cdot\vec F)\,d\tau = \oint_S \vec F\cdot d\vec A$ (para todo campo vectorial $\vec F$ y volumen cerrado por $S$). En simetría esférica $\vec F = F_r(r)\hat r$, $\nabla\cdot\vec F = \dfrac{1}{r^2}\dfrac{d}{dr}(r^2 F_r)$; en cilíndrica $\vec F = F_r(r)\hat r$, $\nabla\cdot\vec F = \dfrac{1}{r}\dfrac{d}{dr}(r F_r)$.</li>
         <li><b>Potencial absoluto con referencia en el infinito ($V(\infty) = 0$):</b> tomando $a \to \infty$ y $b = r$ en $\Delta V = V_b - V_a = -\int_a^b \vec E\cdot d\vec\ell$, resulta $V(r) = -\displaystyle\int_\infty^r \vec E\cdot d\vec\ell = \int_r^\infty \vec E\cdot d\vec\ell$.</li>
         <li><b>Condiciones de borde entre dos medios (sin carga libre en la interfaz):</b> aplicando Gauss en un cilindro "pastillero" chato que cruza la interfaz se obtiene $D_{1\perp} = D_{2\perp}$; aplicando $\oint \vec E\cdot d\vec\ell = 0$ en un lazo rectangular chato paralelo a la interfaz se obtiene $E_{1\parallel} = E_{2\parallel}$.</li>
       </ul>
     </details>
     ```

3. **`#u04-s3` (líneas 99 y 117) — Derivar $F_x = -dU/dx$ por trabajo virtual, unificar $d\tau$ y agregar unidades SI:**
   - *Por qué importa:* Justifica directamente el método de `#u04-p5` (Práctica 5) y elimina la sobrecarga de $dV$ y la falta de unidades de $F_x, x$.
   - *Texto propuesto:* En línea 99, cambiar `$dV$` por `$d\tau$` ($\text{m}^3$), y agregar unidades: `$F_x$ es la componente $x$ de la fuerza (N) al variar la coordenada $x$ (m)`. En `details.deriv` (tras línea 115), añadir: `<b>4. Fuerza por trabajo virtual ($Q$ fija):</b> si una pieza móvil se desplaza $dx$ bajo la fuerza eléctrica $F_x$, el campo realiza trabajo mecánico $dW_{\text{mec}} = F_x\,dx$ a costa de la energía almacenada ($dW_{\text{mec}} = -dU$ porque el sistema está aislado), de donde $F_x = -\dfrac{dU}{dx}\Big|_Q$. (Si permanece conectado a una batería a $V$ constante, la batería aporta $V\,dQ = dU + F_x\,dx$, resultando $F_x = +\dfrac{dU}{dx}\Big|_V$.)`

4. **`#u04-e3` (línea 248) y `#u04-p1` (línea 335) — Completar `li.final` con todo lo pedido y recuadrado:**
   - *Por qué importa:* Cumple `SPEC §3.5` y `§9.4` para que el estudiante verifique su respuesta final de un vistazo sin símbolos externos al enunciado.
   - *Texto propuesto:*
     - En `#u04-e3` (línea 248), reemplazar `C = \left(\frac{1}{C_1}+\frac{1}{C_2}\right)^{-1}` por:
       `C = \frac{4\pi}{\dfrac{1}{\varepsilon_1}\left(\dfrac{1}{a}-\dfrac{1}{b}\right)+\dfrac{1}{\varepsilon_2}\left(\dfrac{1}{b}-\dfrac{1}{c}\right)} = \left(\frac{1}{C_1}+\frac{1}{C_2}\right)^{-1}`
     - En `#u04-p1` (línea 335), incluir todo en `\boxed{...}` con expresiones explícitas:
       `$$\boxed{E_1 = \frac{Q}{\varepsilon_0 A_1},\quad E_2(r) = \frac{Q}{2\pi\varepsilon_0 L r},\quad E_3(r) = \frac{Q}{4\pi\varepsilon_0 r^2}}$$ $$\boxed{|\Delta V_1| = \frac{Qd}{\varepsilon_0 A_1},\quad |\Delta V_2| = \frac{Q}{2\pi\varepsilon_0 L}\ln\!\left(\frac{R_2}{R_1}\right),\quad |\Delta V_3| = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{R_1}-\frac{1}{R_2}\right)}$$ $$\boxed{C_1 = \frac{\varepsilon_0 A_1}{d},\quad C_2 = \frac{2\pi\varepsilon_0 L}{\ln(R_2/R_1)},\quad C_3 = \frac{4\pi\varepsilon_0 R_1 R_2}{R_2 - R_1},\quad C_{AB} = \frac{C_1(C_2+C_3)}{C_1+C_2+C_3}}$$`

5. **`#u04-p2` (línea 353), `#u04-p5` (línea 415) y enunciados simbólicos — Eliminar "ángulo sólido", mejorar redacción sin figura y explicitar unidades SI:**
   - *Por qué importa:* Evita vocabulario innecesario no cubierto (`sr`) en `#u04-p2`, limpia la redacción de `#u04-p5` sin depender de la figura y cumple `SPEC §9.2` en enunciados simbólicos.
   - *Texto propuesto:*
     - En `#u04-p2` (línea 353): cambiar `cada hemisferio ocupa la mitad del ángulo sólido ($2\pi$ sr)` por `cada hemisferio abarca la mitad del área esférica ($2\pi r^2$)`.
     - En `#u04-p5` (línea 415): cambiar `ocupa la región $x \le \text{posición} \le a$` por `ocupa la región comprendida entre la coordenada $x$ y el borde derecho $a$`.
     - En los enunciados simbólicos (`#u04-e3`, `#u04-x1`, `#u04-x2`, `#u04-p1`–`#u04-p5`): añadir una cláusula breve al final de `.stmt` o en `Datos`, p. ej. `(todas las longitudes en m, áreas en $\text{m}^2$, cargas en C, voltajes en V y permitividades en F/m)`.
