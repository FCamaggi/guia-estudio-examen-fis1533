# guia-estudio-examen — Guía de estudio Examen FIS1533 (2026-2)

Examen: **01-12-2026 08:20**. Acumulativo, peso fuerte en U7–U11.

## Leer primero

1. `odd/tasks/guia-examen.md` — specs literales del usuario, tareas y log (fuente de verdad del avance).
2. `SPEC-PEDAGOGICO.md` — contrato de cada unidad (autosuficiencia, 9 bloques, convenciones, compuertas G1–G4).
3. `mapa/banco-examenes.md` — qué pregunta el examen (123 problemas, 12 arquetipos, frecuencia por unidad).
4. `mapa/mapa-fuentes.md` — mejor fuente por subtema, brechas, notación entre semestres, archivos a evitar.

## Estructura

| Ruta | Rol |
|---|---|
| `unidades/` | Una carpeta o fragmento por unidad (U1–U11) |
| `figuras/src/` → `figuras/svg/` | Scripts Python que generan cada figura con `scripts/svg_primitives.py` |
| `fuentes/` | Transcripciones Markdown+LaTeX de fuentes sin ecuaciones (2025-2 Tema4/5) |
| `css/`, `js/` | Estilos y módulos interactivos (copiados de `../guia-estudio-i2/`) |
| `scripts/render_check.mjs` | QA visual: `node scripts/render_check.mjs <svg/html...> [--dark]` → PNG en `qa/render/` + errores MathJax |
| `qa/` | Salidas de verificación (no se edita a mano) |

## Reglas

- Fuentes del curso en `../Electro/` son **solo lectura**. Nunca escanear `../Electro/2026-2/scratch/`.
- Contenido en español neutro; identificadores y código en inglés.
- Toda figura sale del motor y pasa `render_check.mjs` en claro y oscuro con inspección del PNG.
- Cada resultado final de un problema pasa por verificación independiente (G3) antes de marcar la unidad.
- Commits solo con confirmación del usuario.
