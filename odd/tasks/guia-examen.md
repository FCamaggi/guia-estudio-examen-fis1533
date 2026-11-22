# Guía de estudio Examen FIS1533 (2026-2)

Objetivo: guía interactiva HTML que cubre las 11 unidades del programa, cada una autosuficiente, con figuras del motor propio, para el examen del 01-12-2026 08:20. Rama: `main` local (git init sin commits; commits solo con confirmación del usuario). Estrategia de entrega: ask-on-risk. Runner: sin tests unitarios; compuertas G1–G4 de `SPEC-PEDAGOGICO.md`.

## Specs

- S1 (usuario, literal): "Quiero usar todo el contenido que tenemos para hacer una guia de estudio pero para el examen, este semestre (2026-2) aun no terminamos todo el contenido, pero tengo de otros semestres para poder completar"
- S2 (usuario, literal): "no te guies de la guia de estudio de la I2, solo esta como referencia"
- S3 (usuario, literal): "quiero que cada contendo sea autosuficiente, es decir que todo material tenga lo suficiente para entender y realizarlo"
- S4 (usuario, literal): "tenemos una forma de crear figuras, usala"
- S5 (usuario, literal): "finalmente el objetivo es tener todo el contenido necesario para estudiar toda la materia para el examen"
- S6 (usuario, literal): "no te sesgues completamente con este prompt, quiero que usemos el potencial completo del harness para esta tarea, asi que comencemos con el setup o init necesario para cnseguir el mejor producto posible en terminos pedagogicos y de calidad de producto"
- S7 (supuesto): alcance = las 11 unidades del programa 2026-2 (`Electro/2026-2/Programa_FIS1533-4_2026_2.pdf`); el examen es acumulativo con peso fuerte en U7–U11 (banco: 4 exámenes recientes → U7 5, U8 4, U9 5, U10 3, U11 4 de 17 problemas).
- S8 (supuesto): formato = HTML con MathJax, módulos JS reutilizados de la guía I2 (problemas guiados, progreso, quiz, simulacro), más un build autónomo offline.
- S9 (supuesto): idioma del contenido = español neutro.

## Unidades (orden de producción por peso en examen)

| Unidad | Tema | Fuente principal | Brecha |
|---|---|---|---|
| U9 | Inducción: Faraday, Lenz, fem de movimiento, $\vec E$ inducido, Maxwell | Clase 13, Ay21–22, pautas Ex 2024-2/2025-2/2026-1 | Maxwell y corriente de desplazamiento: Clase 12 (Ampère-Maxwell) |
| U10 | Inductancia: mutua, propia, energía, RL, LC, RLC | Clase 14, Ay23, pauta Ex 2026-1 P3 | RLC: requiere T3 (Tema4 2025-2) |
| U11 | Corriente alterna y ondas EM | Ay24, pauta Ex 2025-2 P3, Ex 2024-2 P3 | Teoría CA y ondas EM ausentes en 2026-2: requiere T3 |
| U8 | Biot-Savart, Ampère, conductores paralelos | Clases 11–12, Ay18–20 | Coaxial: Ay20 P1 |
| U7 | Fuerza magnética, Lorentz, torque, dipolo | Clase 10, Ay16–17 | — |
| U6 | Circuitos DC, Kirchhoff, RC, medidores | Clase 09, Ay14–15 | Medidores: Resumen 2025-2 §9.2 |
| U5 | Corriente, resistencia, fem, potencia | Clases 08–09, Ay12 | — |
| U4 | Capacitancia y dieléctricos | Clases 06–07, Ay08–11, Ay13 | — |
| U3 | Potencial eléctrico | Clase 05, Ay06 | Equipotenciales: Ay06 |
| U2 | Gauss y conductores | Clases 03–04, Ay04–05, Ay07 | — |
| U1 | Carga, Coulomb, campo, dipolos | Clases 02–03, Ay01–03 | — |

## Tasks

| ID | Specs | Entrega | Ruta | Estado |
|---|---|---|---|---|
| T0 | S1–S6 | Setup: scaffold, `mapa/banco-examenes.md`, `mapa/mapa-fuentes.md`, `SPEC-PEDAGOGICO.md`, `CLAUDE.md`, `scripts/render_check.mjs` | inline + 2 exploradores agy (plan) | hecho |
| T1 | S4 | Motor de figuras: flechas de vector y ⊙/⊗ dibujados como geometría; etiquetas de vectores en itálica serif. Primitivas nuevas (onda EM 3D, espira en $\vec B(t)$) se agregan dentro de la unidad que las necesite | inline | hecho (glifos); primitivas → T5 |
| T2 | S3, S8 | Build: `scripts/build.py` (+`--preview`), `scripts/build_figures.py`, `scripts/check_unit.py` (G1), `js/guia.js`, `css/guia.css`, `unidades/manifest.json`, `unidades/_plantilla.html` | inline | hecho |
| T3 | S1 | Transcribir a Markdown+LaTeX los PDFs 2025-2 sin ecuaciones (Tema4 RLC 23 p, Tema5 CA 35 p, Tema5 Ondas EM 54+26 p) → `../Electro/2025-2/Clases/markdown-latex/` | agy hydrogen-high ×3 en paralelo (route 7c98b6873dc2) | hecho |
| T4 | S3–S5 | Unidad piloto U9 completa con G1–G4; revisión del usuario antes de escalar | inline (escritura) + agy hydrogen-high G3/G4 (routes 70eac4b60697, 3db173511091) | hecho; aprobada por el usuario (L14) |
| T5 | S3–S5 | U10, U11 (dependen de T3) | 4 escritores agy hydrogen-high en paralelo con T6 (routes 47f2713175bc, 1317e8a0947e; motivo: unidades independientes + reparto de cuota); G3 Claude Sonnet; G4 agy; 1 tanda de corrección (resume) | hecho: G1–G4 observadas |
| T6 | S3–S5 | U8, U7 | agy hydrogen-high en paralelo con T5 (routes 9093489fc9df, 9caf104c9ca3); G3 Claude Sonnet; G4 agy; 1 tanda de corrección | hecho: G1–G4 observadas |
| T7 | S3–S5 | U6, U5, U4 | 6 escritores agy hydrogen-high en paralelo con T8, arquetipos asignados (routes 77edd71dd72e, 6ba975c85cdd, f68328ccf2a8); G3 Claude Sonnet; G4 agy; 1 tanda de corrección | hecho: G1–G4 observadas |
| T8 | S3–S5 | U3, U2, U1 | agy hydrogen-high en paralelo con T7 (routes 88ddd3ccf8ff, c65524a88ee5, fb80357ff2ce); G3 Claude Sonnet; G4 agy; 1 tanda de corrección | hecho: G1–G4 observadas |
| T9 | S5 | Transversal: formulario global, hoja de memoria, tabla de notación, índice arquetipo → sección | inline | pendiente |
| T10 | S5, S6 | 2 simulacros formato reciente (3–4 problemas × 6 pts, 150 min) con pauta y rúbrica | escritor + verificador | pendiente |
| T11 | S6 | Simuladores interactivos RL/RLC transitorio y fasores CA | escritor | pendiente |
| T12 | S5 | QA final y build `dist/` | inline + verificador | pendiente |

## Log

- L1 (2026-11-22, usuario, literal): "Quiero usar todo el contenido que tenemos para hacer una guia de estudio pero para el examen, este semestre (2026-2) aun no terminamos todo el contenido, pero tengo de otros semestres para poder completar, no te guies de la guia de estudio de la I2, solo esta como referencia, quiero que cada contendo sea autosuficiente, es decir que todo material tenga lo suficiente para entender y realizarlo, tenemos una forma de crear figuras, usala, finalmente el objetivo es tener todo el contenido necesario para estudiar toda la materia para el examen, no te sesgues completamente con este prompt, quiero que usemos el potencial completo del harness para esta tarea, asi que comencemos con el setup o init necesario para cnseguir el mejor producto posible en terminos pedagogicos y de calidad de producto"
- L2: Banco de exámenes (agy plan, route b6cee93f67a0): 14 exámenes únicos, 123 problemas, 12 arquetipos. Formato reciente: 3–6 problemas de desarrollo × 6 pts, 120–150 min, sin calculadora ni formulario en la mayoría. 2026-1 introdujo P1A (I1) / P1B (I2) a elección.
- L3: Mapa de fuentes (agy plan, route e4ebcc9b9d84). Brechas: teoría CA y ondas EM ausentes en 2026-2; medidores; coaxial. Spot check confirmado: los `.md` de 2025-2 Tema4/Tema5 tienen 0 ecuaciones (`pdftotext_cleaned`) → T3.
- L4: QA visual operativa (`render_check.mjs`, Chromium de Playwright). Primera corrida detectó tofu en `⃗` y `⊗` del motor (fuente sin glifos) → T1.
- L5: T1 hecho: `label()` dibuja flechas de vector y ⊙/⊗; verificado en claro y oscuro (`qa/render/glyph_test*.png`).
- L6: T2 hecho. Prueba de humo: plantilla PASS en G1; prueba negativa detecta li.check faltante, `$` desbalanceado, `\sumR` y "como vimos"; preview con 92 fórmulas MathJax, pasos y quiz interactivos verificados con Playwright.
- L7: T3 hecho. 3 archivos en `Electro/2025-2/Clases/markdown-latex/` (330 + 442 + 554 líneas, `$`/`$$` balanceados, 44 figuras descritas). Spot checks: potencia media y resonancia CA correctas (curvas coherentes con $V_0=100$ V); intensidad $I=\tfrac12 c\varepsilon_0E_0^2$ correcta. Las "erratas" anotadas en CA son tipográficas. agy no tocó otros archivos.
- L8: Hallazgo lateral: la guía I2 tiene `$\sumR_i$` en sec-27 (error MathJax); no se corrige (fuera de alcance).
- L9 (2026-11-22, usuario, literal): "no hay calculadora ni formulario, por eso es importante \"pautear\" (hacer repetitivamente ejercicios) por eso tengo tanto material de ejercicios y pruebas pasadas etc" / "ademas no se nada de como va a ser el examen" / predicción de Carlos Saez (ayudante): "A) circuitos RL o RLC ... b) Faraday Lenz con un espira cuadrada y algún cable con I cte o J variable, calcular campo, luego flujo, fem, sentido i inducida, Fuerza y velocidad ... c) capacitor de placas paralelas/esfericas o cilindricas, rellno con dielectricos ..." / "esto es solo una prediccion ... demosle creditos si lo vas a poner, pero no creo que sea necesario o sea el foco" / "deberiamos de seguir con el plan, pero no complicarnos con informacion que te respondi ahora, es solo contextual"
- L10: Decisión: sin calculadora → los numéricos de la guía usan valores que se resuelven a mano (fracciones, potencias de 10, $\ln 2$ dejado simbólico) y se privilegian resultados simbólicos. La predicción es contexto; no cambia el plan ni el orden.
- L11: T4 escrita: `unidades/u09-induccion.html` (6 subtemas de teoría, 4 ejemplos, 4 arquetipos 2026-1 P2 / 2024-1 P2 / 2025-2 P2 / 2024-2 P4, 7 trampas, 5 prácticas, quiz de 7, tarjeta de 15 fórmulas) y `figuras/src/u09_figuras.py` (13 figuras, render claro/oscuro revisado).
- L12: G1 PASS (0/0). G2: 0 errores MathJax en claro y oscuro; PNG inspeccionados. G3 (agy, SymPy 1.12): 0 errores de física, 10 detalles menores → `qa/u09-g3-report.md`. G4 (agy): un bloqueo real (fuerza sobre lados con $B(z)$ no uniforme en x3, sin $d\vec F = I\,d\vec\ell\times\vec B$) y huecos de autosuficiencia (Gauss/mallas sin repaso, unidades SI, símbolos de la tabla de Maxwell, notación $z$ y $y$ sobrecargada) → `qa/u09-g4-report.md`. Una tanda de corrección (42 cambios de texto, sin cambiar resultados); G1/G2 re-ejecutadas: PASS. agy no modificó nada fuera de `qa/` (hash del árbol antes/después).
- L13: Hallazgo de proceso: agy en modo `plan` no puede ejecutar comandos (deniega "command"); para G3/G4 se usa modo auto con alcance "solo escribe qa/<informe>.md" y verificación por hash.
- L14 (2026-11-22, usuario, literal): "Me parece bien, sigamos" (aprueba U9 y su extensión).
- L15: `SPEC-PEDAGOGICO.md` §9 con las 10 lecciones del piloto. T5+T6 lanzadas juntas (4 escritores agy hydrogen-high): U7 508, U8 529, U10 547, U11 478 líneas; 54+1 figuras inspeccionadas en hojas de contacto. Alcance de edición verificado por hash (sin cambios fuera de sus superficies).
- L16: G3 con Claude Sonnet (el router siempre devuelve Gemini y §7 exige otro modelo que el escritor): 0 errores de física en las 4 unidades. G4 (agy hydrogen-medium): bloqueos U7 x2c (pedía $M$), U10 x2b (fuerza sin repaso de producto cruz), U8 p5 (cavidad sin $\vec B = \tfrac12\mu_0\vec J\times\vec r_\perp$), U11 x3 (rotor cartesiano) y U11 delgada. Una tanda de corrección por unidad (resume de la misma sesión); G1/G2 re-ejecutadas: PASS; bloqueos verificados por mí. Informes en `qa/u0{7,8}-g4-report.md`, `qa/u1{0,1}-g4-report.md`.
- L17: Hallazgo: escritores en paralelo eligieron el mismo problema (Examen 2024-2 P1 en U7 y U10). Se resolvió dejando en U7 solo las partes a) y b). Para T7/T8, el prompt asigna los arquetipos explícitamente.
- L18: T7+T8: 6 escritores agy en paralelo con arquetipos asignados por unidad (U1 2026-1 P1A, 2024-1 P3; U2 2025-1 P1, 2021-2 Ej 2, 2022-2 P11; U3 2018-2 P1, 2022-2 P7; U4 2025-2 P1, 2018-2 P2; U5 I2 2012-1 P2, I2 2014-1 P4; U6 2026-1 P1B, 2021-2 Ej 1, 2022-2 P5). Sin duplicados. Alcance verificado por hash.
- L19: Incidentes: (a) el seguimiento MCP de U6 se cortó a los ~30 min sin respuesta (idle timeout), pero el proceso agy siguió y terminó la unidad sin generar figuras ni chequeos; las figuras se generaron después y se pulieron con un agy aparte (route edda9dd729fd). (b) Presión de memoria (3,9 GB): render_check en oscuro excedió los 30 s en páginas largas y el sistema cerró un servidor local en `localhost:8765`. Por eso G2 final se corrió en secuencia.
- L20: G3 (Claude Sonnet, independiente del escritor Gemini): U1–U5 0 errores; U6 1 error (afirmación de límite en `u06-e2` li.check: $I_3 = 0$ requiere $\varepsilon_2 = 28/3$ V, no 8 V). G4 (agy): bloqueos en U3 p1 (laplaciano sin definir) y U6 e3/p1/p3/p4 (enunciados que dependían de la figura), más `li.final` incompletos y unidades SI. Una tanda de corrección por unidad; la de U6 se contrastó con `figuras/src/u06_figuras.py` como fuente de verdad de la topología.
- L21: Cierre T7/T8: G1 PASS en las 11 unidades; G2 0 errores en claro y oscuro en las 11 (U1 claro requirió reintento por timeout de captura); build completo `index.html` + `dist/guia-examen.html` con 11/11 unidades.
- Siguiente paso: T9 (formulario transversal, hoja de memoria, tabla de notación, índice arquetipo → sección), T10 (2 simulacros con pauta), T11 (simuladores RL/RLC y fasores), T12 (QA final).
