# Estructura oficial del examen 2026-2 + recomendaciones del chat

Objetivo: rehacer el análisis de qué entra y cómo estudiar con la estructura oficial del examen (`Electro/2026-2/Informacion-examen.md`) y las recomendaciones del chat del curso, priorizando a Carlos (ex-ayudante), con créditos. Rama: `main`. Entrega: commit solo con confirmación del usuario. Runner: compuertas G1–G2 (`SPEC-PEDAGOGICO.md`), `ui_check`, `nav_check`.

## Specs

- S1 (usuario, literal): "Electro/2026-2/Informacion-examen.md tiene la info de lo que entraria en el examen (es todo practicamente) pero sabemos como va a ser estructurado ... creo que en base a esto hay que hacer todo el analisis de nuevo de sobre que va a entrar probablemente, como estudiarlo, etc."
- S2 (usuario, literal): "tengo el chat de wsp de lo que han hablado y recomendado este año, veamos los que sean factibles, Carlos es un ayudante destacado en electro asi que me guiaria mas por lo que dice el, pero si usamos algo de esto que este claramente marcado y con los respectivos creditos"
- S3 (usuario, literal): "si ves recursos que podrian servir y no tengo aqui dimelo para ver si los puedo integrar"
- S4 (hecho, Informacion-examen.md): 1-12-2026 08:20, 150 min, 4 preguntas y se responden 3; P3 y P4 obligatorias; P1 (I1) o P2 (I2) a elección para quien rindió todo; justificativo I1 → P1, I2 → P2; desarrollo; sin calculadora; preguntas sobre el enunciado solo la primera hora y media. Temario: todo el curso hasta CA e impedancia, sin ondas EM.
- S5 (hecho verificado): en el examen 2026-1, P1A = I1 2026-1 P1 casi literal (+ inciso de flujo) y P1B = I2 2026-1 P1 casi literal (+ inciso de energía con dieléctrico). P2 = espira que entra a zona con B; P3 = RL/LC conmutado.
- S6 (usuario, respuesta): Carlos = el remitente que publica las predicciones (chat L1041-1047, L2898-2903, L2721). Crédito sin teléfono ni publicidad.
- S7 (supuesto, marcado como inferencia en la guía): P3 y P4 salen de la materia no evaluada (U9–U11): Faraday-Lenz y RL/RLC en tiempo y en frecuencia.

## Tasks

| ID | S# | Ruta | Estado |
|---|---|---|---|
| T1 | S1,S4,S5,S7 | inline | hecho: §4 estructura oficial; §5.3 precedente 2026-1; §5.4 predicción; §5.5 Carlos; §5.6 Ay18/19 |
| T2 | S1,S2,S4-S7 | inline | hecho: key, exam-map, tabla de prioridad por pregunta, #r01-carlos, timer 40 min, plan 25–30 nov |
| T3 | S4 | inline | hecho |
| T4 | S1 | inline | hecho: build 15/15; check_unit U9–U11 PASS (R01: mismos 7 errores que la base); MathJax 0 errores, 0 enlaces rotos; ui_check y nav_check 0 FAIL |

## Log

- L1 (2026-11-25): pedido original en S1–S3.
- L2: Carlos no aparece por nombre en el chat; el usuario confirmó el remitente (S6). Las Ay18/Ay19 de repaso I2 (`Electro/material-apoyo/repasos-otras-secciones/`, sección del Prof. Claudio Arenas, ayudantes Tomás Silva y Elías Pérez) son práctica para P2.
- L3: recursos del chat que no están en el repo: Examen_De_Prueba.pdf + pauta (L1039, L1089), documento de tips de Carlos (L2721), sus drives (L1863, L2679), Examen.zip (L837).
- L4: pendiente: commit, con confirmación del usuario. Sin cambios en simulacros (siguen en formato 2026-1; el plan explica cómo usarlos como 2026-2).
