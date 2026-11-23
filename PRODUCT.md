# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- Primary: the author, a FIS1533 (Electricity and Magnetism, PUC Chile) student preparing the cumulative final exam.
- Also: classmates who receive the public link. They did not build the guide, so it must explain itself without the author present.
- Main situation: long study sessions at a desktop or laptop, with paper on the side to work problems by hand. Phone use is secondary (quick lookups), but it must still work.

## Product Purpose

An interactive study guide for the FIS1533 final exam. Each of the 11 units can be studied on its own: theory, worked examples, real past-exam problems with their marking scheme, typical mistakes, practice, a self-check quiz and a formula card. It also has an exam map (formula sheet and notation), two timed mock exams with self-grading, interactive RL, RLC and phasor simulators, and a calculator for the grade needed on the exam.

Success: a student who only has the guide can understand each concept from zero, follow every derivation without gaps, solve the exam archetypes with the method taught, and check their own result.

## Positioning

Built from the course's own material and exam bank: 123 past-exam problems grouped into 12 archetypes with their frequency per unit, each archetype citing its source exam. Notation is unified across semesters, with the equivalents declared. Every final result is independently re-derived before a unit counts as done.

## Operating Context

- Solving on paper while reading: the guide asks before calculating, reveals hints and steps one at a time, and ends each problem with a boxed result and a check (dimensions, limits).
- Self-assessment loop: quiz answers, revealed steps and mock-exam progress persist across reloads in the browser.
- Mock exams run under a timer, with a marking scheme to grade yourself.

## Capabilities and Constraints

- Static site: `index.html` (with `css/`, `js/`) and a single-file `dist/guia-examen.html`; works from `file://` and on GitHub Pages. Built with `scripts/build.py` from `unidades/`.
- One unit mounted at a time from `<template>` elements; MathJax from a CDN, typeset lazily per section (needs an internet connection).
- Figures are SVG generated only by the Python engine (`scripts/svg_primitives.py`), with a fixed semantic palette: current and E in blue, B, F and mu in copper, wires in ink, dimensions in grey. Any visual direction must keep that meaning.
- Light and dark themes.
- Content in neutral Spanish; code identifiers in English.
- Pedagogical contract and quality gates G1 to G4: `SPEC-PEDAGOGICO.md`.

## Evidence on Hand

- 11 units, 2 mock exams, the final review page and simulators in `unidades/`.
- Exam bank and source map in `mapa/`.
- Generated figures in `figuras/svg/`.
- No testimonials, usage numbers or grades obtained with the guide; do not invent them.

## Product Principles

1. Self-sufficient: every unit stands alone; no dangling references.
2. Reasoning before results: intuition and the why of each step come before the answer.
3. Faithful to the exam: archetypes cite their source; nothing is passed off as an exam problem when it is not.
4. Built for long sessions: reading comfort and finding your place again outrank novelty.
5. Clear to someone who did not build it.

## Accessibility & Inclusion

Text contrast at least 4.5:1 in both themes, type that scales with the user's font size, touch targets of at least 44 px on phones, no information carried by color alone (figures label their vectors).
