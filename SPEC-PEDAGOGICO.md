# Contrato pedagógico — Guía de estudio Examen FIS1533 (2026-2)

> Este documento define **qué debe contener cada unidad** y **cómo se verifica**. Todo escritor (humano, Claude o agy) lo lee completo antes de escribir. La guía de I2 (`../guia-estudio-i2/`) es solo referencia visual y técnica, no plantilla de contenido.

## 1. Principio rector: autosuficiencia

Cada unidad se puede estudiar **sola**, sin abrir clases, ayudantías ni otras unidades. Un estudiante que solo tiene la unidad debe poder:

1. entender cada concepto desde cero (qué es, por qué existe, cómo se ve);
2. seguir cada derivación sin saltos ("es fácil ver que" está prohibido);
3. resolver los arquetipos de examen de la unidad (ver `mapa/banco-examenes.md` §3) con el método enseñado;
4. verificar su propio resultado (dimensiones, límites, signos).

Consecuencias obligatorias:

- **Prerrequisitos embebidos:** si la unidad usa una herramienta previa (producto cruz, integral en coordenadas cilíndricas, ley de Ampère dentro de Faraday, ecuación diferencial de primer orden), incluye un recuadro `Repaso exprés` con lo mínimo para usarla, aunque se repita en otra unidad.
- **Sin referencias colgantes:** nunca "ver clase 12" ni "como vimos antes" sin repetir el resultado. Se cita la fuente (`.src`) como trazabilidad, no como dependencia.
- **Cada símbolo se define** la primera vez que aparece en la unidad, con unidades SI.

## 2. Estructura obligatoria de una unidad

| # | Bloque | Contenido | Mínimo |
|---|---|---|---|
| 1 | **Mapa de la unidad** | Idea central en 2 líneas; qué pregunta el examen (frecuencia y arquetipos del banco); "Al terminar deberías poder" (4–7 verbos evaluables); prerrequisitos. | 1 |
| 2 | **Teoría por subtemas** | Para cada subtema: problema físico que motiva → intuición (figura) → enunciado formal → derivación completa → interpretación y límites → "cuándo se usa / cuándo NO". | 1 por subtema del programa |
| 3 | **Figuras** | Toda situación geométrica o circuito lleva figura generada con el motor (`scripts/svg_primitives.py`). Ver §4. | ≥1 por subtema |
| 4 | **Ejemplos resueltos** | Dificultad graduada (1→3). Formato de problema guiado (§3). | ≥3 por unidad |
| 5 | **Arquetipos de examen** | Problemas reales de exámenes anteriores (citados) resueltos completos, con puntaje por parte como en la pauta. | ≥2 por unidad (si el banco los tiene) |
| 6 | **Errores típicos** | Cajas `.trap`: confusión concreta, por qué está mal, cómo detectarla. | ≥3 |
| 7 | **Práctica** | Ejercicios con solución completa colapsable (no solo el resultado). | ≥4 |
| 8 | **Autoevaluación conceptual** | Quiz de selección múltiple con retroalimentación por alternativa. | ≥5 preguntas |
| 9 | **Tarjeta de fórmulas** | Cada fórmula con significado de cada símbolo, condiciones de validez y unidades. | 1 |

## 3. Formato de problema guiado

1. Enunciado completo + `Datos` / `Piden` + figura.
2. `Antes de calcular`: pregunta de intuición (signo, orden de magnitud, qué pasa en un límite).
3. Pista inicial colapsable.
4. Pasos `Paso N · Título` con **Qué hago** y **Por qué** (la ley o el argumento físico que lo justifica).
5. Resultado final recuadrado, con unidades y dirección si es vector.
6. Verificación: análisis dimensional + al menos un límite o caso conocido.

## 4. Figuras

- Se generan **solo** con el motor Python (`scripts/svg_primitives.py`); fuente en `figuras/src/uNN_*.py`, salida en `figuras/svg/`.
- Paleta semántica fija: corriente y $\vec E$ en azul (`.a`), $\vec B$, $\vec F$ y $\vec\mu$ en cobre (`.c`), cables en tinta (`.w`), cotas en gris (`.m`, `.md`).
- Texto dentro del SVG: variables en itálica serif (`.s`); **nada de caracteres combinantes** (`⃗`) ni glifos frágiles (`⊗`, `⊙`) como texto: las flechas de vector y los símbolos de campo se dibujan como geometría.
- Cada figura se aprueba con `scripts/render_check.mjs` en modo claro **y** oscuro, inspeccionando el PNG (sin tofu, sin solapamientos, etiquetas legibles).

## 5. Convenciones de notación (únicas en toda la guía)

| Tema | Convención de la guía | Equivalencias que se declaran al estudiante |
|---|---|---|
| Constante de Coulomb | $k = \dfrac{1}{4\pi\varepsilon_0}$ | $k_e$ |
| Constante dieléctrica | $\kappa$ | $K$ (2026-2), $\varepsilon_r$ |
| Diferencia de potencial | $\Delta V = V_b - V_a = -\int_a^b \vec E\cdot d\vec\ell$; $V_{ab} = V_a - V_b$ | — |
| Elemento de línea | $d\vec\ell$ | $d\vec s$, $d\vec l$ |
| Momento dipolar magnético | $\vec\mu = N I A\,\hat n$ | $\vec m$ (Cádiz) |
| Unidad imaginaria (CA) | $j$, fasores $\hat V,\ \hat I$; impedancias $Z_L = j\omega L$, $Z_C = \dfrac{1}{j\omega C}$ | $i$, notación polar $A\angle\phi$ |
| Amplitud vs. eficaz | Amplitud $V_0, I_0$ por defecto; eficaz siempre con subíndice: $V_{\text{rms}} = V_0/\sqrt2$ | $\langle P\rangle = \tfrac12 V_0 I_0\cos\phi = V_{\text{rms}} I_{\text{rms}}\cos\phi$ |
| Ley de Faraday | $\varepsilon = -\dfrac{d\Phi_B}{dt}$, normal $\hat n$ por regla de la mano derecha respecto al sentido de recorrido | — |

## 6. Fuentes y fidelidad

- Prioridad: `Electro/2026-2/` (Clases, Ayudantías, Pautas) → pautas de otros semestres → `fuentes/` (transcripciones de esta guía) → bibliografía. Ver `mapa/mapa-fuentes.md`.
- Erratas conocidas de las fuentes (`Electro/2026-2/docs/analisis-completitud.md`) se corrigen y se anota la corrección.
- No se inventan problemas "de examen": un arquetipo cita su examen de origen. Los ejercicios originales se marcan como tales.

## 7. Compuertas de calidad (en orden)

| Compuerta | Qué verifica | Herramienta |
|---|---|---|
| G1 Estructura | Los 9 bloques presentes; `$`/`$$` balanceados; figuras referenciadas existen; cada problema con final y verificación; ids únicos. | `scripts/check_unit.py` |
| G2 Render | 0 errores MathJax, 0 imágenes rotas; figuras revisadas en claro y oscuro. | `scripts/render_check.mjs` |
| G3 Física | Un verificador independiente (modelo distinto al escritor) recalcula cada resultado final; los numéricos y simbólicos no triviales se comprueban con SymPy. | subagente verificador + `qa/` |
| G4 Autosuficiencia | Revisor que simula a un estudiante con solo la unidad: ¿puede resolver los arquetipos? Lista de saltos, símbolos sin definir y referencias colgantes. | subagente revisor |

Una unidad se marca terminada solo con G1–G4 observadas.

## 8. Flujo de autoría (comandos)

1. Copiar `unidades/_plantilla.html` a `unidades/uNN-slug.html` (nombre según `unidades/manifest.json`) y reemplazar `u00` por el id de la unidad. Todos los `id` llevan el prefijo de la unidad.
2. Figuras: `figuras/src/uNN_figuras.py` con `figures() -> {"uNN-nombre": diagrama}`; generar con `python3 scripts/build_figures.py uNN`.
3. G1: `python3 scripts/check_unit.py unidades/uNN-slug.html` (debe dar PASS).
4. G2: `python3 scripts/build.py --preview unidades/uNN-slug.html` y `node scripts/render_check.mjs qa/preview/uNN-slug.html` (0 errores) + `node scripts/render_check.mjs figuras/svg/uNN-*.svg [--dark]` e inspección de los PNG.
5. Build completo: `python3 scripts/build.py` → `index.html` y `dist/guia-examen.html`.

Vocabulario de componentes (definido en la plantilla): secciones `section.sec[data-block=mapa|teoria|ejemplos|arquetipos|errores|practica|quiz|formulas][data-title]`; problemas `.prob[data-kind=ejemplo|arquetipo|practica][data-diff]` con `ol.reveal` (`li.hint`, pasos, `li.final`, `li.check`) y `div.ctrl`; `.trap`; `details.prereq`; `details.deriv`; `.quiz > .q[data-correct]` con `.opts button[data-o]` y `.fb[data-o]`; `figure.fig[data-fig]`.

## 9. Lecciones del piloto U9 (obligatorias)

La unidad modelo es `unidades/u09-induccion.html` (aprobada por el usuario el 2026-11-22). Imita su profundidad, su tono (tú, español neutro) y su forma de explicar. Estas reglas salen de lo que G3 y G4 encontraron en ella:

1. **Examen sin calculadora ni formulario.** Los datos numéricos se eligen para calcularse a mano (potencias de 10, fracciones simples, $\sin 30^\circ$, $e^{-1}\approx 0{,}37$); se privilegian resultados simbólicos. La tarjeta de fórmulas es lo que el estudiante debe memorizar.
2. **Unidades SI en la primera aparición de cada símbolo**, también en repasos exprés, tablas (p. ej. $\rho$, $\vec J$) y enunciados de problemas simbólicos (p. ej. "$\alpha$ en T/m").
3. **Forma general antes que la particular.** Si una fórmula de la unidad solo vale en un caso (campo uniforme, tramo recto), el repaso o la teoría da también la forma diferencial que necesitan los arquetipos (p. ej. $d\vec F = I\,d\vec\ell\times\vec B$).
4. **`li.final` contiene todo lo que pide el enunciado**: cada magnitud de "Piden", con dirección o sentido, y las respuestas cualitativas (p. ej. "máxima con el plano paralelo a $\vec B$").
5. **Sin símbolos sobrecargados**: coordenada vs. número fijo, $y$ vs. $\hat y$, $R$ radio vs. resistencia. Si la fuente original lo hace, se aclara en el enunciado o se renombra.
6. **Arquetipos autosuficientes**: el enunciado da, sin depender de la figura, los sentidos de corrientes y la posición relativa. El puntaje por paso suma exactamente el total de cada parte de la pauta; si la pauta no lo detalla, se indica el puntaje por parte. Las erratas de la pauta oficial se corrigen y se anotan.
7. **Signos con coordenadas**: se escribe el resultado en función de la componente con signo ($v_z = dz/dt$) y se reemplaza al final; el sentido obtenido se contrasta con el argumento físico (Lenz, energía).
8. **Verificación física en cada problema**: dimensiones + un límite, y balance de energía cuando aplique.
9. **HTML**: dentro de fórmulas usa `\lt` y `\gt` (nunca `<` seguido de letra). Cada derivación pasa por todos los pasos algebraicos (planteo de la integral, primitiva evaluada, separación de variables).
10. **Figuras**: etiquetas de vectores solo en clases serif (`s`, `sa`, `sc`); en el SVG no hay subíndices con `_` (usa `₀`–`₉` o renombra); se inspecciona el PNG buscando solapes de texto con líneas o símbolos de campo.
