# Material de cierre 2026-2 (I2 escaneada + Ay26–28)

Objetivo: integrar la I2 2026-2 y las ayudantías 26–28 en el análisis del examen y en las unidades, como material de base (sin marcas de "nuevo"). Rama: `main`. Entrega: commit solo con confirmación del usuario. Runner: compuertas G1–G4 (`SPEC-PEDAGOGICO.md`).

## Specs

- S1 (usuario, literal): "Acabo de agregar ayudantias nuevas de este semestre y el escaneo de lo que preguntaron en la I2, quizas con este material cambia el analisis de lo que esperariamos en el examen, no lo sé, pero integralo como si siempre hubieramos tenido este material, no quiero leer algo sobre de que agregue recien esto o con este cambio, etc."
- S2 (supuesto): fuentes = `Electro/pruebas-anteriores/I2/I2 2026-2 (enunciado escaneado).pdf` (13-11-2026, sin pauta), `Ayudantias/Enunciados/Ay26–28`, `Ayudantias/Soluciones/Ay26, Ay28`.
- S3 (supuesto): la I2 entra como arquetipos (U6-X4, U7-X4, U8-X4) con puntaje del enunciado; de Ay27–28 entran como práctica los temas sin cobertura (disco de Faraday, espira que se expande con B(t), toroide L y U, filtro pasa-altos).
- S4 (supuesto): el análisis (banco, mapa de fuentes, R01, "Qué pregunta el examen") se reescribe en tiempo presente, sin lenguaje de cambio.

## Tasks

| ID | S# | Ruta | Estado |
|---|---|---|---|
| T1 | S3 | inline | hecho: U6-X4, U7-X4, U8-X4 + 3 figuras |
| T2 | S3 | inline | hecho: U9-P6, U9-P7, U10-P5, U11-P5 + 4 figuras |
| T3 | S1,S4 | inline | hecho: banco §5, mapa-fuentes, R01, exam-maps U1/U2/U4/U6–U11 |
| T4 | S1 | verificador independiente | hecho: G1 PASS, G2 0 errores MathJax, G3 7/7 PASS |

## Log

- L1 (2026-11-24): pedido original en S1.
- L2: la I2 2026-2 evaluó Clases 08–12 (RC, Lorentz/espectrómetro, Biot-Savart + Ampère). Faraday, inductancia y CA (Ay21–24, 26–28) no se evaluaron en interrogaciones: solo entran en el examen.
- L3: G3 (verificador independiente, SymPy) 7/7 PASS; se aplicaron 5 ajustes de redacción (salto de la lámina en U8-X4, signo de Lenz con ω≠0 en U9-P6, definición de k̂ y j, frase del factor 0,6 en U6-X4). render_check de páginas completas agota el tiempo de captura; G2 se corrió con un script de scratch sin captura completa (0 errores MathJax y de página). ui_check y nav_check sobre dist: 0 FAIL.
- L4: pendiente: commit, con confirmación del usuario.
