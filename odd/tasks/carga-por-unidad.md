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
- S5 UI/UX, rewritten from the impeccable battery (L6) and the user's answers (L7). Scope: "Todo (P0 a P2)".
  - S5a [P0] Mobile: no horizontal overflow at 375/390 px; compact top bar with the TOC in an off-canvas panel; mock-exam bar must not collide; touch targets >= 44 px.
  - S5b [P1] Derivations: "Cerradas + abrir todas": closed by default, one per-unit button to open them all, choice remembered.
  - S5c [P1] Study loop: quiz answers and revealed steps survive reload; per-question retry; mock-exam reset asks for confirmation and the pauta can be cleared.
  - S5d [P1] Accessibility: copper labels and placeholders >= 4.5:1; no h2->h4 skips; type scales with the user's font size (rem); no labels under 12 px; unit change announced.
  - S5e [P2] Hierarchy: "dominado" on the section title line and only on "Solo estudio U1–U11" (theory, examples, archetypes, traps, practice, quiz, formulas: 132 sections); labelled quiz feedback; "Rediseñar el código": keep each callout color's meaning without the thick left stripe and without nested frames inside problems; callout line length capped; active TOC unit scrolled into view; dead CSS/JS removed.
- S6 QA: "capturas en PC y móvil, en claro y oscuro, el detector de impeccable, y una auditoría independiente delegada a agy al final."

Baseline measured before the change: 44 s to ready, ~640k DOM nodes, 18,640 formulas typeset at load; horizontal overflow on mobile; TOC shows 158 sections expanded.

## Tasks

| ID | Specs | Route | Status | Evidence |
|---|---|---|---|---|
| T0 | (prior session) remove 8-day plan and dates | inline | done, 86c03d9 | build 15/15 |
| T1 | S1 | inline | done, 8f45fda | build 15/15; templates + #guide-data; MathJax `startup.typeset: false` |
| T2 | S2a–S2e | inline | done, 8f45fda | `scripts/nav_check.cjs` 13/13 PASS on index.html and dist |
| T3 | S3 | inline | done, 8f45fda | quiz, steps, simulacro (timer keeps running hidden), simulators, nota via `Guide.onMount` |
| T4 | S4 | inline | done (commit after 8f45fda) | search RED on 8f45fda dist (no #toc-q), GREEN: nav_check 18/18 on index.html and dist |
| T5 | S5a–S5e | inline | done, uncommitted | ui_check RED on 822dfed (overflow 709/775/423 px, no top bar); GREEN 42/42 + nav_check 18/18 on index and dist; detector 330 -> 11 (11 known false positives); check_unit 11/11 before and after | critique 22/40, audit 11/20 |
| T6 | S6 | inline + agy audit | pending | |

T1–T3 are one coupled change (build output, router and module init contract); they land together.

## Log

- L1 (2026-11-22, user-approved design, carried over verbatim in the 2026-11-23 handoff): "Pendiente: el diseño que elegiste, una unidad a la vez: 1. Build … 6. QA … En la próxima sesión arranco por los puntos 1 a 3, que son la base de todo lo demás."
- L2 (2026-11-23): session resumed; starting T1–T3 inline (coupled, no writer reason).
- L3 (2026-11-23): T1–T3 implemented. Measured after (headless Chromium, file://): ready in 2.2–3.7 s (was 44 s), 2.6k DOM nodes at start (was ~640k), 29 formulas typeset at start. Programmatic jumps use instant scroll because main.css sets `scroll-behavior: smooth`; a 4 s "pin" keeps a jump target in place while math above it typesets. `render_check.mjs` now forces a full typeset before capturing. Pre-existing (base commit too): `render_check.mjs` times out on the full-page capture of the u10 preview. Risk: item 6 (only the ad-hoc `nav_check.cjs` guards navigation); independent check is the agy audit planned in T6. Next: T4 TOC search + T5 UI.
- L4 (2026-11-23, user, verbatim): "dale y push a main, ademas continua con el punto 4, pero el punto 5 no lo continues porque tengo un desacuerdo, yo correria la bateria completa de impeccable (y otros de diseño) no asumiria el tema como correcto, dale continua hasta antes del punto 5, haz commit y push". T0 and T1–T3 committed and pushed (86c03d9, 8f45fda). S5 is on hold: its listed UI items are not accepted as the plan; the user wants the full impeccable battery (and other design skills) to decide the design instead of assuming the current direction is right.
- L5 (2026-11-23): T4 done. TOC search filters section titles of every unit (case- and accent-insensitive); a unit-title hit lists all its sections; Enter opens the first result, Escape clears; "Sin resultados" when nothing matches. Collapse and build-total progress were already in 8f45fda. Next: T5 stays on hold until the user runs the design review (L4); T6 QA depends on T5.
- L6 (2026-11-23, user: "dale, corre todo"): ran the impeccable battery as two isolated agy assessments (A design review d13a206b445f, B detector + technical audit c174c5ab58f5), both read-only and accepted. Critique 22/40, audit 11/20. Parent spot-checked: mobile scrollWidth 709/775 px at 390 px, TOC 310/530 px tall, copper/copper-soft 4.43:1, 54/59 derivations open, mock-exam reset unguarded. Priority: P0 mobile; P1 open derivations, study-loop persistence + reset guard, a11y (contrast, h2->h4, rem, tiny text); P2 hierarchy/progress. Prior S5 list: "dominado" inline confirmed, mobile TOC confirmed, thick left border debatable, palette selection/scrollbars dropped (no evidence). Reports: qa/preview/_impeccable/report-A.md, report-B.md (gitignored); snapshot .impeccable/critique/2026-11-23T12-10-52Z__index-html.md. S5 must be rewritten from the user's scope choice.
- L7 (2026-11-23, user answers, verbatim option labels): scope "Todo (P0 a P2)"; derivations "Cerradas + abrir todas (Recomendado)"; dominado "Solo estudio U1–U11 (Recomendado)"; left border "Rediseñar el código (Recomendado)". S5 rewritten accordingly. Route: inline (shared CSS makes units non-disjoint; agy auto mode would lock parent edits).
- L8 (2026-11-23): T5 implemented inline. Mobile: `.layout` uses minmax(0,1fr), top bar + off-canvas index (Escape, scrim, focus return, inert main), bare tables wrapped in `.tbl-scroll`, wide display math scrolls, 44 px targets. Derivations closed in sources (55 `open` removed) + per-unit open-all button remembered in localStorage `fis1533-deriv-open`. Study loop: quiz answers in state.quizAns, per-question retry, labelled feedback, score bar on top; revealed steps in `fis1533-examen-steps`; mock-exam reset and new "Limpiar pauta" need a second click when there is something to lose. A11y: copper #9e5416 (>= 4.8:1 on all its backgrounds), themed placeholders, exam-map h4 -> h3, font sizes in rem with a 12 px floor (SVG figure text stays px), live region announces unit changes. Hierarchy: "dominado" in `.sec-head` on 132 study sections (`study` list in #guide-data), callouts without the side stripe (1 px tinted border, block headline), no nested frames inside problems, 72-76ch caps, sticky TOC header, active unit scrolled into view, drawn check marks instead of unicode glyphs, themed selection/scrollbars/caret (impeccable craft floor). Removed unused js/02–05, js/app.js, css/mathjax-svg.css. Bug caught in visual review: `.eq.key` inherited the `.key` width cap and clipped equations; fixed and pinned in ui_check.
