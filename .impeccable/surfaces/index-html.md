---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["dist/guia-examen.html"]
---

## Scope

The whole study guide (`index.html`, `dist/guia-examen.html`): units, exam map, mock exams, simulators. Visitor mode: Read. Audience: the author and classmates, long desktop sessions with paper beside them; phone secondary.

## Shape brief (confirmed 2026-11-23)

- Formulas: grouped by family, validity next to each formula.
- Figures: legible SVG text; sticky beside the steps on wide screens.
- Steps: "Antes de calcular" as a visible pause; what/why distinct; step progress.
- Quiz: options as a vertical list; feedback next to the chosen option.
- Mock exam: the bar never covers content; exam mode hides the index.
- Index: readable per-unit progress; "where you left off".
- Out of scope: content, physics, notation, the figure engine (only its type size). E stays blue, B copper.

## Direction contract

THESIS: The guide is a rail network. Each course block is a line with its own colour, each unit a station, and the reader always knows which platform they stand on. Refuses the generic docs shell (rounded cards, blue buttons, mono eyebrows).

OWN-WORLD: White ground, near-black ink, black departure-board bands for the index head, unit openers and problem heads. Line colours only in the frame: A Electrostatics amber, B Circuits green, C Magnetism magenta, D Induction and AC violet, E mock exams grey, R map black. Atkinson Hyperlegible Next for text, Atkinson Hyperlegible Mono for numbers and labels. Square corners, 2 px ink rules, no shadows. Colour carries meaning only (raise from Datamatics). State is a mark, not a hue: mastered is a filled stop, current a thick ring, "where you left off" a flag (raise from the cutting bench). Exam problems and original exercises differ in type, solid citation vs hairline (raise from provenance ribbon).

STORY: The reader finds their station, reads at a fixed 68-character measure, tries each problem before revealing steps, and checks progress along the line.

FIRST VIEWPORT: Left, the index as a vertical line diagram grouped by block, current station ringed, progress per unit in tabular figures. Top of the column, a black band with the unit badge in its line colour and the title, an 8 px line-colour rule under it. Below, the reading column at 68ch; extra width goes to margins and figures, never to text (raise from the ice press).

FORM: Rail timetable and station wayfinding, candidate 5 of 7 on the ordered list. seed:ba90d5aac0462838

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Open decisions

- Signature interaction for "where you left off" (flag placement and restore).
- Component variants (step list, quiz option, formula row, mock-exam bar) to be chosen with the user.
