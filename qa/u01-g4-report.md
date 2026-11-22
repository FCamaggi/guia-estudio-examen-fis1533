# Reporte G4 — Autosuficiencia: U1 (`unidades/u01-campo-electrico.html`)

Revisión simulando a un estudiante de segundo año de ingeniería que **solo** dispone de `unidades/u01-campo-electrico.html` (sin clases, sin otras unidades, sin calculadora ni formulario), contrastada con `SPEC-PEDAGOGICO.md` (§1, §2, §3, §5 y §9).

---

## 1. Resolubilidad de arquetipos y problemas de práctica

| Ítem (`id`) | ¿Resoluble solo con la unidad? | Qué paso bloquea o dificulta y por qué |
|---|---|---|
| **Arquetipo 1 (`u01-x1`)** — 8 cargas en un cubo (Examen 2026-1 · P1A) | **Sí (con ambigüedad menor en d)** | **a)** Resoluble con simetría por pares (`#u01-mapa` L26) y Coulomb (`#u01-s2` L64). **b)** Resoluble con $r = \frac{\sqrt{3}}{2}a$ (`#u01-mapa` L25) y $V = \sum kq_i/r_i$, $W_{\text{ext}} = q(V_f - V_i)$ (`#u01-mapa` L41); $\sqrt{3}$ se cancela a mano. **c)** Resoluble por superposición ($\vec E_{\text{7 cargas}} = -\vec E_8$). **d)** Resoluble con Gauss (`#u01-mapa` L43–44), **pero hay una ambigüedad en el enunciado**: d) remite a «la configuración original de cargas [inciso a)]», donde no se definió el símbolo $Q$ para las cargas de los vértices ($Q_i = \sqrt{3}\,\mu\text{C}$ recién aparece en b)) ni se aclara si la carga de prueba $q$ del inciso a) permanece en $O$ (la propia solución debe añadir una *Nota de pauta* en L273). Además, d-i se deja simbólico en $Q/\varepsilon_0$ sin indicar si debe evaluarse numéricamente (dividir por $\varepsilon_0 = 8{,}854\times 10^{-12}$ a mano sería engorroso). |
| **Arquetipo 2 (`u01-x2`)** — Anillo $+Q$ y carga con resorte (Examen 2024-1 · P3) | **Sí** | **a)** Derivado paso a paso en `#u01-s4` (L108–109). **b)** Resoluble con $\vec F = q\vec E$ (`#u01-s3` L72) y $F_{\text{elást}} = -k_0 z$ (`#u01-mapa` L45). **c)** Resoluble con MAS (`#u01-mapa` L45) y $(z^2+R_0^2)^{3/2} \approx R_0^3$. *Detalle menor:* c) pide «frecuencia» y `Repaso exprés` solo define frecuencia angular $\omega$ (L45), no $f = \omega/(2\pi)$ (que aparece recién en `li.final` L309). |
| **Práctica 1 (`u01-p1`)** — Triángulo equilátero | **Sí** | Resoluble con ley de Coulomb (`#u01-s2` L64) y geometría básica ($h = L\sqrt{3}/2$, baricentro a $\frac{2}{3}h = L/\sqrt{3}$, $\sin 60^\circ = \sqrt{3}/2$). Resultado simbólico exacto sin calculadora. |
| **Práctica 2 (`u01-p2`)** — Péndulo electrostático | **Sí** | Resoluble con Coulomb (`#u01-s2` L64) y equilibrio estático ($\sum\vec F = \vec 0$). *Detalle:* `Datos` (L356) usa $g$ sin haberla mencionado en `stmt` (L355) ni dar su unidad SI. |
| **Práctica 3 (`u01-p3`)** — Electrón y protón entre placas | **Sí (aritmética pesada a mano en b y c)** | **a)** $t = 1{,}25\times 10^{-8}\ \text{s}$, $a_e = 6{,}40\times 10^{13}\ \text{m/s}^2$, $E = 364{,}4\ \text{N/C}$ son limpiamente calculables a mano. **b)** Calcular $m_p/m_e = 1{,}67\times 10^{-27}/(9{,}11\times 10^{-31}) \approx 1833$ y $5{,}00\times 10^{-3}/1833 \approx 2{,}73\,\mu\text{m}$ sin calculadora exige divisiones largas con 3 cifras significativas. **c)** $\sqrt{1{,}60^2+0{,}80^2} = \sqrt{3{,}20} = 0{,}80\sqrt{5} \approx 1{,}79$ requiere estimar $\sqrt{5}$ a mano si no se deja en forma radical. |
| **Práctica 4 (`u01-p4`)** — Alambre en horquilla | **Sí** | Resoluble con `#u01-s4` (L96) y las dos integrales de sustitución simple y trigonométrica dadas en `#u01-mapa` (L30, L33), más parametrización estándar del cuarto de circunferencia. |
| **Práctica 5 (`u01-p5`)** — Disco con $\sigma(r)$ no uniforme | **Sí** | Resoluble con `#u01-s4` (L109, L111) y las integrales de $r\,dr$ y $r^3\,dr$ explícitamente resueltas en `#u01-mapa` (L30–31). |

---

## 2. Saltos de derivación

1. **`#u01-s4` (L110, derivación del anillo):** «Derivando respecto a $z$ e igualando a cero: $E_z$ es máximo en $|z| = R/\sqrt{2}$.» Se omite por completo el cálculo de la derivada $\frac{d}{dz}\left[z(z^2+R^2)^{-3/2}\right] = \frac{R^2 - 2z^2}{(z^2+R^2)^{5/2}} = 0$.
2. **`#u01-s4` (L112, derivación del disco):** Pasa de $\dfrac{\sigma z}{2\varepsilon_0}\left[-\dfrac{1}{\sqrt{z^2+r^2}}\right]_0^R$ directamente a $\dfrac{\sigma}{2\varepsilon_0}\left(1 - \dfrac{z}{\sqrt{z^2+R^2}}\right)$, saltando la evaluación intermedia $z\left(\frac{1}{z} - \frac{1}{\sqrt{z^2+R^2}}\right)$ (válida para $z > 0$).
3. **`#u01-s4` (L113, límite lejano del disco):** En $\dfrac{\sigma}{2\varepsilon_0}\dfrac{R^2}{2z^2} = \dfrac{k(\sigma\pi R^2)}{z^2}$, omite mostrar $\frac{1}{4\varepsilon_0} = \frac{\pi}{4\pi\varepsilon_0} = k\pi$.
4. **`#u01-s5` (L127, energía potencial del dipolo):** Escribe $\tau = pE\sin\phi$ y luego $U(\phi) = \int_{\pi/2}^\phi \tau\,d\phi' = \int_{\pi/2}^\phi pE\sin\phi'\,d\phi' = -pE\cos\phi$, sin distinguir explícitamente entre el torque eléctrico restaurador (que tiende a disminuir $\phi$, $-\tau\hat\phi$) y el torque del agente externo necesario para girar de $\pi/2$ a $\phi$ ($+\tau$).
5. **`#u01-p5` (L435–437, disco no uniforme):** Salta de las dos integrales evaluadas por separado directamente al resultado agrupado $\vec E(z) = 2\pi k\sigma_0\left\{1 + \frac{2z^2}{R^2} - \frac{z}{\sqrt{z^2+R^2}}\left(2 + \frac{2z^2}{R^2}\right)\right\}\hat z$ sin mostrar la línea intermedia al multiplicar por $z$ y $-z/R^2$ y factorizar $\frac{z}{\sqrt{z^2+R^2}}$.

---

## 3. Símbolos usados antes de su definición o sin unidades SI

| Ubicación | Símbolo(s) | Problema |
|---|---|---|
| `#u01-mapa` (L18) | $R_0$, $z$ | Aparecen en «($z\ll R_0$)» en el resumen inicial antes de definirse en `#u01-x2`. |
| `#u01-mapa` (L26, L34, L42, L44, L45) | $r', \phi$ (L26); $r, dr, a, \theta, \phi$ (L34); $\varphi, \vec E$ (L42); $a$ (L44); $t$ (L45) | En los recuadros `Repaso exprés` faltan las unidades SI explícitas en esas apariciones (`m`, `rad`, `N/C`, `s`). |
| `#u01-s1` (L54) | $E_g \gt 4{,}0\ \text{eV}$ | Unidad no SI (`eV`) sin definir ni dar su equivalencia en joule ($1\ \text{eV} = 1{,}602\times 10^{-19}\ \text{J}$). |
| `#u01-s4` tabla (L91–93) | $L$, $A$, $V$, $Q$ | La tabla da unidades SI para $\lambda, \sigma, \rho$, pero no indica unidades SI para $L$ ($\text{m}$), $A$ ($\text{m}^2$), $V$ ($\text{m}^3$) ni $Q$ ($\text{C}$). |
| `#u01-s4` (L99, L102, L108) | $a$ (L99), $x, y$ (L102), $z$ (L108) | Coordenadas o distancias introducidas sin explicitar `(en m)`. |
| `#u01-s5` `.note` (L122) | $\phi$, $x$, $z$ | $\phi$ (ángulo entre $\vec p$ y $\vec E$) y las distancias $x, z$ del campo lejano no declaran unidades (`rad`, `m`). |
| `#u01-s6` `.note` (L136) | $v_0$, $t$, $\Delta y$ | Faltan sus unidades SI (`m/s`, `s`, `m`) en `.note`. |
| `#u01-x1` (L254, L258) | $q$ (L254), $R$ (L258) | $q$ aparece en a) sin unidad (`C`, recién en b) toma $1\,\mu\text{C}$); $R$ en d) sin unidad explícita (`m`). |
| `#u01-p2` (L355–356) | $g$, $\theta$ | $g$ aparece en `Datos` (L356) sin estar en `stmt` (L355) y sin unidad SI (`m/s²`); $\theta$ sin unidad (`rad` o grados). |
| `#u01-formulas` (L499–503) | $x, R, z, Q, \sigma, \phi$ | Algunas filas no repiten las unidades de símbolos que ya aparecieron en la teoría (en la tabla resumen, L499–503). |

---

## 4. Referencias colgantes necesarias para seguir el razonamiento

- **No hay referencias colgantes externas** (no se remite a clases, ayudantías ni otras unidades como dependencia; las etiquetas `.src` como `Examen 2026-1 · P1A` o `(Ayudantía 01 2026-2, Problema 2.)` son citas de trazabilidad permitidas por `SPEC-PEDAGOGICO.md` §1 y §6).
- **Referencia interna ambigua en `#u01-x1` (L258):** «Para la configuración original de cargas [inciso a)]...» remite al inciso a), donde las cargas de los vértices no tenían símbolo $Q$ ni valor numérico (solo «son iguales») y había una carga de prueba $q$ en el centro. La solución en L273 y L275 usa el símbolo $Q$ (definido en b)) y excluye $q$ (aclarándolo en una *Nota de pauta*).

---

## 5. Prerrequisitos usados pero no cubiertos por los recuadros `Repaso exprés`

1. **Producto cruz y producto punto ($\vec p\times\vec E$, $\vec p\cdot\vec E$):** usados en `#u01-s5` (L122, L127) y `#u01-e3` (L206). `SPEC-PEDAGOGICO.md` §1 menciona explícitamente el producto cruz como ejemplo de herramienta que conviene tener en `Repaso exprés`.
2. **Integral logarítmica $\int du/u = \ln u$ y series de $(1-\epsilon)^{-1}$ y $\ln(1-\epsilon)$:** usadas en `#u01-e4` (L231 en el paso de integración y L239 en `li.check`).
3. **Teorema trabajo–energía cinética ($W = \Delta K$):** usado en las verificaciones de `#u01-e2` (L188) y `#u01-p3` (L389).
4. **Frecuencia ordinaria $f = \omega/(2\pi)$:** citada en `#u01-x2` (`li.final`, L309), mientras que `Repaso exprés` 3 (L45) solo define $\omega$.

---

## 6. Violaciones de `SPEC-PEDAGOGICO.md` §3, §5 y §9

- **§3 (Formato de problema guiado):**
  - En `#u01-p2` (L355–356), `Datos` incluye `$g$` aunque `stmt` no lo menciona ni da su unidad; en `#u01-p3` (L376), `Datos` omite $e, m_e, m_p$ que sí están en `stmt`.
  - En `#u01-x1` (L259), `Datos` fija $Q_i = Q = \sqrt{3}\,\mu\text{C}$, pero en a) $Q$ no existe y en d) la respuesta queda simbólica en $Q$.
- **§5 (Convenciones de notación):**
  - Cumple con $k = \frac{1}{4\pi\varepsilon_0}$ (y declara $k_e$, $K$), $\Delta V = V_b - V_a$ y $d\vec\ell$. *Detalle menor:* `#u01-x2` (L295–297) usa $ds$ en $dq = \lambda\,ds$ sin recordar la equivalencia $d\ell \leftrightarrow ds$.
- **§9.1 (Sin calculadora, números calculables a mano):**
  - `#u01-p3` b) y c) (L386–387) requieren $16700/9{,}11 \approx 1833$, $5{,}00/1833 \approx 2{,}73$ y $\sqrt{3{,}20} \approx 1{,}79$, poco amigables sin calculadora frente a `#u01-e2` o `#u01-x1`.
- **§9.2 (Unidades SI en primera aparición):**
  - Faltan en `#u01-s4` tabla ($L, A, V$), `#u01-s6` `.note` ($v_0, t, \Delta y$), `#u01-p2` ($g, \theta$), `#u01-s1` ($E_g$ en `eV` sin equivalencia SI) y en varios símbolos de `Repaso exprés`.
- **§9.4 (`li.final` contiene todo lo pedido):**
  - **Cumplido** en los 11 problemas (`u01-e1`–`e4`, `u01-x1`–`x2`, `u01-p1`–`p5`).
- **§9.5 (Sin símbolos sobrecargados):**
  - **$r$ sobrecargado:** en `#u01-s4` L108 es distancia al punto $P$ ($\sqrt{z^2+R^2}$), y en `#u01-s4` L111 / `#u01-p5` L431 pasa a ser el radio variable del anillo elemental ($r\in[0,R]$).
  - **$R$ sobrecargado:** en `#u01-mapa` L23 es $|\vec r - \vec r\,'|$; en `#u01-x1` L258 designa el radio de la esfera $S_1$ y además el radio basal del cilindro $S_3$ en la misma oración.
  - **$V$ sobrecargado:** potencial eléctrico (V) en `#u01-mapa` L41 y volumen ($\text{m}^3$) en `#u01-s4` L93.
  - **$k$ vs $\hat k$:** en `#u01-x1` (L253–255) coexisten $\hat k$ (unitario en $z$) y $k$ (constante de Coulomb).
- **§9.6 (Arquetipos autosuficientes sin figura y suma de puntaje exacta):**
  - Todos los enunciados son autosuficientes sin la figura. Los puntajes por paso en `#u01-x1` (1 + 1 + 2 + 2 = 6 pts.) y `#u01-x2` (3 + 2 + 1 = 6 pts.) suman **exactamente** el total de cada parte.
- **§9.9 (HTML `\lt`/`\gt` y pasos algebraicos completos):**
  - `\lt` y `\gt` se usan correctamente en todo el archivo. Faltan los pasos algebraicos indicados en la Sección 2.

---

## 7. Las 5 mejoras más valiosas (priorizadas)

1. **Resolver la ambigüedad de $Q$ y $q$ en `#u01-x1` inciso d) (L254, L258)**
   - **Por qué:** Un estudiante que resuelve d) no sabe si la carga de prueba $q$ sigue en el centro ni por qué aparece $Q$ en `li.final` si a) no la definió.
   - **Texto propuesto (español):**
     - En L254 (inciso a): `Determine la fuerza eléctrica sobre una carga $q$ situada en el centro del cubo en el caso en que todas las cargas de los vértices son iguales a una carga $Q$ ($\text{C}$).`
     - En L258 (inciso d): `Para la configuración original de cargas iguales $Q$ en los vértices [inciso a), sin la carga de prueba $q$ en el centro], considere tres superficies cerradas...`

2. **Completar los saltos de derivación en `#u01-s4` (L110 y L112)**
   - **Por qué:** Cumple §1 y §9.9 al evitar saltos en la obtención del máximo del anillo y en la evaluación del disco.
   - **Texto propuesto (español):**
     - En L110: `Derivando respecto a $z$ e igualando a cero: $\dfrac{dE_z}{dz} = kQ\dfrac{(z^2+R^2)^{3/2} - 3z^2(z^2+R^2)^{1/2}}{(z^2+R^2)^3} = kQ\dfrac{R^2 - 2z^2}{(z^2+R^2)^{5/2}} = 0$, luego $E_z$ es máximo en $|z| = R/\sqrt{2}$.`
     - En L112 (antes del resultado final): `...$= \dfrac{\sigma z}{2\varepsilon_0}\left(\dfrac{1}{z} - \dfrac{1}{\sqrt{z^2+R^2}}\right) = \dfrac{\sigma}{2\varepsilon_0}\left(1 - \dfrac{z}{\sqrt{z^2+R^2}}\right)$ (para $z \gt 0$).`

3. **Dejar `#u01-p3` b) y c) calculables a mano según §9.1 (L386–388)**
   - **Por qué:** Evita exigir divisiones largas ($16700/9{,}11$ y $5/1833$) y raíces irracionales ($\sqrt{3{,}20}$) a un estudiante sin calculadora.
   - **Texto propuesto (español):**
     - En L386: `...con $m_p/m_e \approx 1833$ (a mano: $1{,}67\times 10^{-27}/(9{,}11\times 10^{-31}) \approx 1830$), $|\Delta y_p| = \Delta y_e\dfrac{m_e}{m_p} \approx \dfrac{5{,}00\ \text{mm}}{1833} \approx 2{,}73\,\mu\text{m}$...`
     - En L387: `...$v = 10^6\sqrt{1{,}60^2 + 0{,}80^2} = 0{,}80\sqrt{5}\times 10^6\ \text{m/s} \approx 1{,}79\times 10^6\ \text{m/s}$ (usando $\sqrt{5}\approx 2{,}24$).`

4. **Mostrar el paso intermedio de agrupación algebraica en `#u01-p5` (L436–437)**
   - **Por qué:** Permite seguir la combinación de las dos integrales del disco no uniforme sin perderse en el álgebra.
   - **Texto propuesto (español):**
     - En L436–437: `Reemplazando ambas en $E_z(z)$:`
       $$E_z(z) = 2\pi k\sigma_0\left[z\left(\frac{1}{z} - \frac{1}{\sqrt{z^2+R^2}}\right) - \frac{z}{R^2}\left(\frac{R^2+2z^2}{\sqrt{z^2+R^2}} - 2z\right)\right]$$
       `Agrupando los términos con $\dfrac{z}{\sqrt{z^2+R^2}}$ ($1 + \frac{R^2+2z^2}{R^2} = 2 + \frac{2z^2}{R^2}$):`

5. **Completar unidades SI en primeras apariciones y corregir `Datos` en `#u01-s4`, `#u01-s6`, `#u01-s1` y `#u01-p2` (L54, L91–93, L136, L355–356)**
   - **Por qué:** Cumple §1 y §9.2 de manera uniforme en toda la unidad.
   - **Texto propuesto (español):**
     - En `#u01-s1` (L54): `(brecha energética $E_g \gt 4{,}0\ \text{eV}$, con $1\ \text{eV} = 1{,}602\times 10^{-19}\ \text{J}$; en semiconductores $E_g \le 4{,}0\ \text{eV}$).`
     - En `#u01-s4` tabla (L91–93): `Línea de largo $L$ ($\text{m}$)`, `Superficie de área $A$ ($\text{m}^2$)`, `Volumen $V_{\text{vol}}$ ($\text{m}^3$)` (evita además sobrecargar $V$ con potencial eléctrico).
     - En `#u01-s6` `.note` (L136): `...$L$ ($\text{m}$), el tiempo de tránsito es $t = L/v_0$ ($\text{s}$, con $v_0$ en $\text{m/s}$) y la deflexión transversal es $\Delta y = \dfrac{qEL^2}{2mv_0^2}$ ($\text{m}$)...`
     - En `#u01-p2` (L355–356): añadir en `stmt`: `bajo gravedad $g$ ($\text{m/s}^2$)` y en `Datos` especificar `$\theta$ ($\text{rad}$), $g$ ($\text{m/s}^2$)`.
