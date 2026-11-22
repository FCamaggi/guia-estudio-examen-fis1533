# Reporte G4 — Autosuficiencia de U5 (`unidades/u05-corriente.html`)

Revisión simulando a un estudiante de segundo año de ingeniería que dispone **únicamente** de `unidades/u05-corriente.html` (sin clases, sin otras unidades, sin calculadora ni formulario), contrastada contra `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5 y §9).

---

## 1. Resolubilidad de arquetipos y problemas de práctica (solo con la unidad)

| ID | Título | ¿Resoluble solo con U5? | Paso que bloquea / observación |
|---|---|---|---|
| `u05-x1` | Cable coaxial con dos capas de distinta conductividad (`I2 2012-1 · P2`) | **Sí** | Todas las partes (a–d) se resuelven con `u05-s3` (Caso 2: cilindro hueco, serie), `u05-s2` (continuidad e interfaz $\sigma_q = \varepsilon_0 J_n \frac{\sigma_1-\sigma_2}{\sigma_1\sigma_2}$), `u05-s1` ($I = \int \vec J\cdot d\vec A$) y `Repaso exprés` ($A(r) = 2\pi r L$). En Paso 4 (línea 231) la sustitución de $E_2(b) = J(b)/\sigma_2$ es compacta pero verificable. |
| `u05-x2` | Cascarones esféricos concéntricos con material óhmico (`I2 2014-1 · P4`) | **Sí** | a) Ley de Gauss y $4\pi r^2$ están en los `Repaso exprés` (líneas 33 y 38). b) $V_0 = \int_a^b \vec E\cdot d\vec\ell$ e $\int dx/x^2$ están en `Repaso exprés` (líneas 31 y 37). c) $\vec J = \sigma\vec E$ en `u05-s2`. d) $I = \oint \vec J\cdot d\vec A$ en `u05-s1` y $R = V_0/I$ en `u05-s2`. |
| `u05-p1` | Conductividad de un alambre desde mediciones de voltaje y corriente | **Sí** | Usa $R = \Delta V/I = L/(\sigma A)$, $E = \Delta V/L$ (`u05-s2`) y $P = I\,\Delta V$ (`u05-s5`). Números exactos a mano ($R = \frac{2}{3}\,\Omega$, $\sigma = 1{,}5\times 10^6\ (\Omega\cdot\text{m})^{-1}$, $E = 2{,}0\ \text{V/m}$, $P = 6{,}0\ \text{W}$). |
| `u05-p2` | Resistencia de un cono truncado | **Sí** | Parte a) coincide con `u05-s3` Caso 1 y la sustitución lineal del `Repaso exprés` (línea 32). Parte b) pide dejar $\pi$ explícito y simplifica a mano a $20/\pi\,\Omega$. |
| `u05-p3` | Comparación de arreglos con dos conos sólidos idénticos | **Sí** (con ruido de notación) | Usa $R_{\text{cono}} = L/(\pi\sigma ab)$ (`u05-s3` Caso 1) y reglas de serie/paralelo (`u05-s3`). **Bloqueo menor de lectura:** el enunciado sobrecarga $a$ y $b$ (radios de los conos y nombres de los terminales). |
| `u05-p4` | Esferas concéntricas óhmicas: potencia Joule y casos límite | **Sí** | Usa $\vec J = \frac{I}{4\pi r^2}\hat r$, $\vec E = \rho\vec J$, $V = \int_a^b E\,dr$, $P = V^2/R$, $p = J^2\rho$ (`u05-s5`) y límite $b\to\infty$ (`u05-s3`, línea 104). |

**Conclusión de resolubilidad:** Los 2 arquetipos y los 4 problemas de práctica son **100 % resolubles** usando únicamente el contenido de `u05-corriente.html`, sin calculadora ni formulario.

---

## 2. Saltos en derivaciones

1. **`u05-x1`, Paso 4 (línea 231) — Compresión algebraica en $E_2(b)$:**
   - Texto exacto: `"E_2(b) = \frac{J(b)}{\sigma_2}. Aplicando la ley de Gauss en la interfaz..."` seguido inmediatamente de `"\left(1 - \frac{\sigma_2}{\sigma_1}\right)E_2(b) = \frac{\sigma_1 - \sigma_2}{\sigma_1}\cdot\frac{\sigma_1\,V_0}{\left[\sigma_2\ln(b/a) + \sigma_1\ln(c/b)\right]b}"`.
   - Por qué puede trabar al estudiante: omite el paso intermedio donde se sustituye $J(b) = \frac{\sigma_1\sigma_2 V_0}{[\sigma_2\ln(b/a)+\sigma_1\ln(c/b)]b}$ y se cancela $\sigma_2$.
2. **`u05-s2`, Ecuación de continuidad (línea 72) y Paso 3 de interfaz (línea 80):**
   - La equivalencia `"\oint_S \vec J\cdot d\vec A = -\frac{dQ_{\text{enc}}}{dt} \Longleftrightarrow \nabla\cdot\vec J + \frac{\partial\rho_q}{\partial t} = 0"` se presenta sin mencionar el teorema de la divergencia, y en la línea 80 `"la continuidad exige J_{1n} = J_{2n} = J_n"` no menciona explícitamente la cajita gaussiana aplicada a $\vec J$ (aunque sí se explica para $\vec E$ en el `Repaso exprés` de la línea 38).

---

## 3. Símbolos usados antes de su definición o sin unidades SI

1. **`u05-mapa`, `Repaso exprés: rebanar un cuerpo...` (líneas 29–33):**
   - `G = 1/R` (`"conductancias G = 1/R"`) aparece sin unidades SI (`\text{S} = \Omega^{-1}`) y tampoco se define $R$ ($\Omega$) en ese recuadro.
   - Los parámetros geométricos $a, b, h, x, s, R_0, L, r$ ($\text{m}$) y $dA, A(r)$ ($\text{m}^2$) no declaran unidades SI en el recuadro.
2. **`u05-mapa`, `Repaso exprés: potencial, ley de Gauss...` (líneas 37–40):**
   - `"\Delta V = V(b) - V(a)"` y `"V_{ab} = V(a) - V(b)"` no declaran su unidad SI ($\text{V}$).
   - `"Q_{\text{enc}}"` (línea 38) no declara su unidad ($\text{C}$), y `"\varepsilon_1"`, `"\varepsilon_2"`, `"\sigma_{q,\text{libre}}"` (línea 40) tampoco explicitan unidades.
3. **`u05-s1` (líneas 52–54 y 61):**
   - En la intuición (línea 53), `"q\vec E"` usa $q$ antes de definirlo en la línea 55.
   - En la derivación no uniforme (línea 61), `"\vec J(s) = J_0(s/R_0)\,\hat z"` usa $J_0$ sin unidad ($\text{A/m}^2$) y $\hat z$ sin definirlo explícitamente como versor axial.
4. **`u05-s2` (líneas 71, 73 y 76):**
   - El pie de figura (`figcaption`, línea 71) usa $A_1, A_2, J_1, J_2, T, T_0, \alpha$ antes de definir $T_0$ y $\alpha$ en la línea 73.
   - En la línea 73, `"\rho_0"` omite repetir `(\Omega\cdot\text{m})`.
5. **Enunciados simbólicos sin unidades SI explícitas (SPEC §9.2):**
   - `u05-x1` (línea 220): $a, b, c, L$ ($\text{m}$), $\sigma_1, \sigma_2$ ($(\Omega\cdot\text{m})^{-1}$), $V_0$ ($\text{V}$), $\varepsilon_0$ ($\text{C}^2/(\text{N}\cdot\text{m}^2)$) sin unidades en el enunciado/Datos (a diferencia de `u05-e3`, que sí las incluye).
   - `u05-x2` (línea 242): $a, b, \sigma, V_0, \pm Q, \varepsilon_0$ sin unidades en el enunciado/Datos.
   - `u05-p3` (línea 320) y `u05-p4` (línea 341): $L, a, b, \sigma, \rho, V, \Delta t$ sin unidades en el enunciado/Datos.
6. **Versor radial $\hat r$:** usado en `u05-x1` (línea 230), `u05-x2` (línea 250) y `u05-p4` (línea 349) sin definición explícita previa en la sección de teoría.

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

No se encontraron referencias colgantes que impidan seguir el razonamiento ni resolver los problemas. Todas las citas a pruebas (`I2 2012-1 · P2`, `I2 2014-1 · P4`, etc.) son de trazabilidad (`.src`), y las menciones a `U6` y `U8` (línea 18) son solo mapa de ruta.

*Nota menor:* en `u05-x2`, `li.check` (línea 255) menciona `"la relación universal RC = \varepsilon_0/\sigma"` sin haber definido capacitancia $C$ en esta unidad; al ser un comentario adicional de verificación y no parte de la resolución, no bloquea el problema.

---

## 5. Prerrequisitos usados pero no cubiertos por los recuadros `Repaso exprés`

1. **Divergencia y teorema de la divergencia:** `u05-s2` (línea 72) pasa de $\oint_S \vec J\cdot d\vec A = -dQ_{\text{enc}}/dt$ a $\nabla\cdot\vec J + \partial\rho_q/\partial t = 0$. Aunque los problemas de U5 solo usan la forma integral, el operador $\nabla\cdot$ aparece en la tarjeta de fórmulas (`u05-formulas`, línea 407) sin recuadro `Repaso exprés`.
2. **Forma diferencial radial $E_r = -dV/dr$:** `u05-p4` (línea 341) pide `"Integrando E = -dV/dr, obtén la resistencia R"`. El `Repaso exprés` (línea 37) da la forma integral $\Delta V = -\int_a^b \vec E\cdot d\vec\ell$, pero no escribe explícitamente $E_r = -dV/dr$ (aunque la integral resultante $\int_a^b E\,dr$ es idéntica).

---

## 6. Violaciones a `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§9.5 (Sin símbolos sobrecargados) — Violación en `u05-p3` (línea 320):**
  - Texto exacto: `"cada uno de largo L, radio menor a, radio mayor b (a \lt b) y conductividad uniforme \sigma, se conectan entre los terminales a y b en tres configuraciones"`.
  - Se usa $a$ y $b$ simultáneamente para los **radios** de los conos y para los **terminales** del circuito.
- **§9.5 (Consistencia de coordenadas) — Violación en `u05-e3` (líneas 194, 204 y 205):**
  - En el enunciado (línea 194), la parte a) usa eje $\hat z$ (`"\vec J(s) = J_0(1 - s^2/R_0^2)\hat z"`), mientras la parte b) usa coordenada axial $x$ (`"T(0) = T_0 hasta T(L) = 2T_0"`, `"\vec E(x) en función de x (0 \le x \le L)"`), pero en Paso 3 (línea 204) y `li.final` (línea 205) el campo $\vec E(x)$ lleva versor `"\hat z"` en lugar de $\hat x$ (o usar $z$ como coordenada).
- **§5 (Convención de $\Delta V$ vs. $V_{ab}$) — Violación en `u05-s2` (línea 76):**
  - Texto exacto: `"sometido a una diferencia de potencial \Delta V = V_a - V_b \gt 0"`.
  - En §5 (y en el `Repaso exprés` de la línea 37), $\Delta V = V_b - V_a$ y $V_{ab} = V_a - V_b$.
- **§3.6 (Verificación física en cada problema):**
  - `u05-e1` (línea 164) y `u05-p1` (línea 290) verifican consistencia y/o unidades, pero no incluyen un límite físico explícito.
  - `u05-p3` (línea 332) verifica la razón $R_{\text{I}}/R_{\text{III}} = 4$, pero no incluye análisis dimensional explícito.
- **Aspectos conformes:**
  - `li.final` contiene **todo** lo pedido en `Piden` en los 9 problemas (incluyendo direcciones vectoriales, unidades y respuestas cualitativas).
  - Todos los enunciados de arquetipos y práctica son **autosuficientes** sin depender de la figura (polaridades y sentidos de flujo están descritos en texto).
  - Todos los cálculos numéricos (`u05-e1`, `u05-e2`, `u05-p1`, `u05-p2`, quiz) son **calculables a mano** sin calculadora.
  - Los puntajes de `u05-x1` (6,0 pts.) y `u05-x2` (6,0 pts.) suman exactamente por parte.

---

## 7. Las 5 mejoras más valiosas (ordenadas por impacto)

1. **Eliminar la sobrecarga de $a, b$ en `u05-p3` (línea 320, SPEC §9.5)**
   - **Ubicación:** `unidades/u05-corriente.html`, `#u05-p3`, `<p class="stmt">` (línea 320).
   - **Texto actual:** `"...radio menor $a$, radio mayor $b$ ($a \lt b$) y conductividad uniforme $\sigma$, se conectan entre los terminales $a$ y $b$ en tres configuraciones:"`
   - **Texto propuesto:** `"...radio menor $a$, radio mayor $b$ ($a \lt b$) y conductividad uniforme $\sigma$, se conectan entre los terminales $A$ y $B$ en tres configuraciones:"`

2. **Corregir la inconsistencia entre coordenada $x$ y versor $\hat z$ en `u05-e3` (líneas 194, 201, 203–206, SPEC §9.5)**
   - **Ubicación:** `unidades/u05-corriente.html`, `#u05-e3` (`stmt`, `given`, `hint`, Pasos 2–3, `li.final`).
   - **Texto propuesto (en `stmt`, línea 194):** reemplazar `"en función de $x$ ($0 \le x \le L$)"` por `"en función de $z$ ($0 \le z \le L$)"`, y cambiar $x \to z$ en `hint`, Pasos 2–3 y `li.final` (`\vec E(z) = \dfrac{\rho_0 I_0}{A_0}\left(1 + \alpha T_0\dfrac{z}{L}\right)\hat z`), manteniendo así el eje $\hat z$ de la parte a).

3. **Alinear $\Delta V$ vs. $V_{ab}$ con SPEC §5 en `u05-s2` (línea 76)**
   - **Ubicación:** `unidades/u05-corriente.html`, `#u05-s2`, `<details class="deriv">`, punto 1 (línea 76).
   - **Texto actual:** `"sometido a una diferencia de potencial $\Delta V = V_a - V_b \gt 0$ entre sus extremos."`
   - **Texto propuesto:** `"sometido a una caída de potencial $V_{ab} = V(a) - V(b) \gt 0$ (que aquí abreviaremos $\Delta V \gt 0$) entre sus extremos."`

4. **Agregar unidades SI faltantes en `Repaso exprés` y enunciados simbólicos (líneas 29, 37–38, 220, 242, SPEC §1 y §9.2)**
   - **Ubicación:** `unidades/u05-corriente.html`, `#u05-mapa` (líneas 29, 37–38) y `#u05-x1`, `#u05-x2` (`given`, líneas 221 y 243).
   - **Texto propuesto (línea 29):** `"...se suman sus conductancias $G = 1/R$ ($\text{S} = \Omega^{-1}$):"`
   - **Texto propuesto (línea 37):** `"Diferencia de potencial ($\text{V}$): $\Delta V = V(b) - V(a)..."` y en línea 38 `"donde $Q_{\text{enc}}$ ($\text{C}$) es la carga encerrada..."`
   - **Texto propuesto (línea 221, `given` de `u05-x1`):** `"radios $a \lt b \lt c$ ($\text{m}$), largo $L$ ($\text{m}$), conductividades $\sigma_1$ ($a\lt r\lt b$) y $\sigma_2$ ($b\lt r\lt c$) en $(\Omega\cdot\text{m})^{-1}$, $V_0 = V(a) - V(c) \gt 0$ ($\text{V}$), $\varepsilon_0$ ($\text{C}^2/(\text{N}\cdot\text{m}^2)$)"`

5. **Explicitar el paso de sustitución de $J(b)$ en `u05-x1` Paso 4 y definir $\hat r$ (líneas 99 y 231, SPEC §1.2)**
   - **Ubicación:** `unidades/u05-corriente.html`, `#u05-s3` (línea 99) y `#u05-x1` Paso 4 (línea 231).
   - **Texto propuesto (línea 99):** `"La corriente sale radialmente (dirección $+\hat r$) de $r = a$ hacia $r = b$..."`
   - **Texto propuesto (línea 231):** agregar antes de despejar $\sigma_q$: `"Como $E_2(b) = \dfrac{J(b)}{\sigma_2} = \dfrac{\sigma_1 V_0}{\left[\sigma_2\ln(b/a) + \sigma_1\ln(c/b)\right]b}$, aplicando la ley de Gauss en la interfaz..."`
