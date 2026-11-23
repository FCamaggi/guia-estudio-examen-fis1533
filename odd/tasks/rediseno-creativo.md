# Feature: creative design pass with impeccable (rediseno-creativo)

Objective: run the creative half of impeccable that the audit-only pass skipped, pick a visual direction with the user from real screenshots, then re-critique against the 22/40 baseline. Branch: main (commits only with user confirmation). Delivery: ask-on-risk. Test runner: `node scripts/ui_check.cjs`, `node scripts/nav_check.cjs`, `python3 scripts/check_unit.py`, impeccable detector.

## Specs

- S1 "init conmigo para PRODUCT.md" (interview with the user, then write PRODUCT.md).
- S2 "shape de las partes (fórmulas, figuras, paso a paso, quiz, simulacro, índice)".
- S3 "2 o 3 direcciones visuales con capturas reales para elegir el tema". "El estilo "cuaderno de laboratorio" no está fijo."
- S4 "variantes de componentes".
- S5 "al final, critique de nuevo para comparar con el 22/40".
- S6 "Después va el punto 6 (QA + auditoría con agy)" (T6 of odd/tasks/carga-por-unidad.md).

## Tasks

| ID | Specs | Route | Status | Evidence |
|---|---|---|---|---|
| T1 | S1 | inline | done | PRODUCT.md written from 2 interview answers (L3) |
| T2 | S2 | inline | done | brief confirmed by user (L4) |
| T3 | S3 | inline | done | decision page: user chose "Andén" (L5); contract in .impeccable/surfaces/index-html.md |
| T3b | S3 | delegated (agy hydrogen-high, run bb487aa1e18f, context backstop) | done, uncommitted | ui_check 42/42 index+dist; nav_check 18/18 index+dist after check fix (L6); screenshots reviewed |
| T4 | S4 | inline (live mode, needs user in browser) | pending | |
| T5 | S5 | agy assessment (independent, as the 22/40 baseline) | pending | |
| T6 | S6 | inline + agy audit | pending | |

## Log

- L1 (2026-11-23, user, verbatim): "Sigamos con la guía del examen (guia-estudio-examen). Los puntos 1 a 5 están en main (7ac7e4d). Ahora quiero la parte creativa de impeccable que faltó: init conmigo para PRODUCT.md, shape de las partes (fórmulas, figuras, paso a paso, quiz, simulacro, índice), 2 o 3 direcciones visuales con capturas reales para elegir el tema, variantes de componentes y, al final, critique de nuevo para comparar con el 22/40. El estilo "cuaderno de laboratorio" no está fijo. Después va el punto 6 (QA + auditoría con agy)."
- L2 (2026-11-23): impeccable context: no PRODUCT.md, no DESIGN.md, incumbent visual system present; init required before shape/new-work. Baseline: critique 22/40, audit 11/20 (carga-por-unidad L6), after-T5 code at 7ac7e4d.
- L3 (2026-11-23, user answers, verbatim option labels): users "Yo y compañeros"; usage "PC, sesiones largas". PRODUCT.md written (platform web; principles: self-sufficient, reasoning before results, faithful to the exam, built for long sessions, clear to someone who did not build it). No image generation available, so buildPath not asked (code-first is the only path).
- L4 (2026-11-23): shape from screenshots of the current build (scratchpad shots, 1440x900, light/dark). Findings: mock-exam sticky bar covers the "Enunciados" heading; mock-exam figure labels ~7 px; at 1440 px the column uses ~800 px. Brief (mode Read), confirmed by the user ("Confirmo"): formulas grouped by family with validity next to each formula; figures with legible SVG text and sticky beside the steps; steps with "Antes de calcular" as a pause, what/why distinct, step progress; quiz options as a vertical list, feedback next to the chosen option; mock exam bar never covers content, exam mode without the TOC; TOC with readable per-unit progress and "where you left off". Out of scope: content, physics, notation, figure engine (only its type size). Keep E blue, B copper.
- L5 (2026-11-23): concept-seed (direction, read) seed:ba90d5aac0462838 assigned candidate 5 of 7 (rail timetable / station wayfinding). Three directions prototyped as CSS overrides injected into the real index.html (scratchpad proto/anden.css, aparato.css, canon.css) and captured at 1440x900 light/dark; contact sheets in .impeccable/mocks/decision/. Six catalog challengers declined; four raises kept on Andén (state as marks, citation typography, fixed measure, colour only for meaning). User chose on the decision page: {"optionId":"assigned"} = "Andén". Direction contract written to the surface brief. Correction: web fonts ARE loaded (scripts/build.py FONTS link in both builds); an earlier truncated grep suggested otherwise and the canon card text repeated that error. Build path: code-led (Read surface, no image generation).
- L6 (2026-11-23): Andén folded into css/main.css + css/guia.css by agy (Atkinson Hyperlegible Next/Mono via build.py FONTS; line colours by data-unit; state marks on the index line; 68ch measure; vertical lettered quiz options; sticky problem figure; html:has(.simulacro) scroll-padding so the mock-exam bar no longer covers "Enunciados"). Parent checks: git HEAD unchanged (7ac7e4d), no protected paths in diff, ui_check 42/42. nav_check "reload restores u09 position" failed 5000 -> 5094: probe showed the same block at the same viewport top (133 -> 132 px); scrollY differs because content above is not re-typeset after reload. Assertion changed to compare the visible block (text + top) instead of scrollY; 18/18 on index and dist. RDD assess: high (process_boundary signal on scripts/build.py; the change there is only the font URL). Native review START blocked on the untracked-selection JSON format (invalid_request x5, schema undocumented); deferred to a committed-only assess after the user confirms the commit. Still open from the shape brief: formulas grouped by family (needs unit markup), quiz feedback next to the chosen option, exam mode hides the index, "where you left off" flag, mock-exam figure labels ~10 px (figure engine).
