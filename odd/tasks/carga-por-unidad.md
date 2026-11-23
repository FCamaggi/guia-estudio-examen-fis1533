# Feature: load one unit at a time (carga-por-unidad)

Objective: make the guide load fast and work on mobile by mounting only the open unit. Branch: main (local commits only with user confirmation). Delivery: ask-on-risk. Test runner: none (manual + `node scripts/render_check.mjs` + headless timing).

## Specs

Quoted from the design agreed in the 2026-11-22 session (see L1).

- S1 Build: "cada unidad va dentro de un <template> en el mismo HTML. Así sigue funcionando sin servidor (file://) y en GitHub Pages. MathJax deja de tipografiar todo al cargar."
- S2 Navigation:
  - S2a "Solo se monta la unidad abierta, y sus fórmulas se tipografían por sección al acercarte."
  - S2b "Las unidades ya abiertas quedan guardadas en memoria, así no se pierden el cronómetro, el quiz ni los pasos revelados."
  - S2c "Los links profundos (#u10-x1) abren la unidad y saltan ahí."
  - S2d "Al recargar o ir atrás vuelves a donde estabas; al hacer clic en una unidad del índice empiezas desde arriba."
  - S2e "Al final de cada unidad, botones de anterior y siguiente."
- S3 JS modules: "Hay que cambiarlos para que se inicien cada vez que se monta una unidad: quiz, pasos de los problemas, simulacro, simuladores y calculadora de nota."
- S4 TOC: "solo la unidad activa queda desplegada, con un buscador de secciones (porque Ctrl+F solo buscará en la unidad abierta) y el progreso calculado con los totales que genera el build."
- S5 UI/UX with impeccable, keeping the "cuaderno de laboratorio" style: "el botón "dominado" pasa a la misma línea del título de la sección"; "las cajas destacadas pierden el borde izquierdo grueso"; "selección de texto y scrollbars con los colores de la paleta"; "en móvil, el índice pasa a un panel lateral que se abre con un botón y se corrige el desborde."
- S6 QA: "capturas en PC y móvil, en claro y oscuro, el detector de impeccable, y una auditoría independiente delegada a agy al final."

Baseline measured before the change: 44 s to ready, ~640k DOM nodes, 18,640 formulas typeset at load; horizontal overflow on mobile; TOC shows 158 sections expanded.

## Tasks

| ID | Specs | Route | Status | Evidence |
|---|---|---|---|---|
| T0 | (prior session) remove 8-day plan and dates | inline | done, uncommitted | build 15/15 |
| T1 | S1 | inline | done, uncommitted | build 15/15; templates + #guide-data; MathJax `startup.typeset: false` |
| T2 | S2a–S2e | inline | done, uncommitted | `scripts/nav_check.cjs` 13/13 PASS on index.html and dist |
| T3 | S3 | inline | done, uncommitted | quiz, steps, simulacro (timer keeps running hidden), simulators, nota via `Guide.onMount` |
| T4 | S4 | inline | pending | |
| T5 | S5 | inline | pending | |
| T6 | S6 | inline + agy audit | pending | |

T1–T3 are one coupled change (build output, router and module init contract); they land together.

## Log

- L1 (2026-11-22, user-approved design, carried over verbatim in the 2026-11-23 handoff): "Pendiente: el diseño que elegiste, una unidad a la vez: 1. Build … 6. QA … En la próxima sesión arranco por los puntos 1 a 3, que son la base de todo lo demás."
- L2 (2026-11-23): session resumed; starting T1–T3 inline (coupled, no writer reason).
- L3 (2026-11-23): T1–T3 implemented. Measured after (headless Chromium, file://): ready in 2.2–3.7 s (was 44 s), 2.6k DOM nodes at start (was ~640k), 29 formulas typeset at start. Programmatic jumps use instant scroll because main.css sets `scroll-behavior: smooth`; a 4 s "pin" keeps a jump target in place while math above it typesets. `render_check.mjs` now forces a full typeset before capturing. Pre-existing (base commit too): `render_check.mjs` times out on the full-page capture of the u10 preview. Risk: item 6 (only the ad-hoc `nav_check.cjs` guards navigation); independent check is the agy audit planned in T6. Next: T4 TOC search + T5 UI.
