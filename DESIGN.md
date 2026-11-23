---
name: "FIS1533 Study Guide (Andén)"
description: "Rail-timetable and station-wayfinding visual system for the FIS1533 Electricity and Magnetism exam study guide."
colors:
  paper: "#ffffff"
  paper-dark: "#0f1113"
  surface: "#ffffff"
  surface-dark: "#0f1113"
  ink: "#121417"
  ink-dark: "#eceef0"
  muted: "#555b63"
  muted-dark: "#a2a8b0"
  line: "#d9dcdf"
  line-dark: "#2c3035"
  accent: "#1f4fd1"
  accent-dark: "#8aa8ff"
  accent-soft: "#eef2fc"
  accent-soft-dark: "#18203a"
  copper: "#9e5416"
  copper-dark: "#e2a26b"
  copper-soft: "#f8efe6"
  copper-soft-dark: "#2a2119"
  ok: "#17784c"
  ok-dark: "#5fcf98"
  ok-soft: "#e6f4ec"
  ok-soft-dark: "#12271d"
  bad: "#b23b2a"
  bad-dark: "#f08a7a"
  bad-soft: "#fbeae7"
  bad-soft-dark: "#321a17"
  band: "#121417"
  band-dark: "#000000"
  band-ink: "#ffffff"
  l0: "#121417"
  l0-dark: "#eceef0"
  lA: "#d99a00"
  lA-dark: "#f2b81d"
  lB: "#28803a"
  lB-dark: "#51cf66"
  lC: "#c2255c"
  lC-dark: "#f06595"
  lD: "#6741d9"
  lD-dark: "#9775fa"
  lE: "#6b7178"
  lE-dark: "#a2a8b0"
  line-ink: "#ffffff"
  line-ink-dark: "#0f1113"
  lA-ink: "#121417"
  predict-highlight: "#ffd43b"
  sim-time-low: "#ff8776"
  sim-nota-ok: "#69db9e"
  toc-scrim: "rgba(8, 14, 22, 0.45)"
typography:
  display:
    fontFamily: '"Atkinson Hyperlegible Next", "Helvetica Neue", Arial, sans-serif'
    fontSize: "clamp(2rem, 4.5vw, 2.75rem)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.015em"
  headline:
    fontFamily: '"Atkinson Hyperlegible Next", "Helvetica Neue", Arial, sans-serif'
    fontSize: "1.625rem"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  title:
    fontFamily: '"Atkinson Hyperlegible Next", "Helvetica Neue", Arial, sans-serif'
    fontSize: "1.125rem"
    fontWeight: 700
    letterSpacing: "normal"
  body:
    fontFamily: '"Atkinson Hyperlegible Next", "Helvetica Neue", Arial, sans-serif'
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.62
    letterSpacing: "normal"
  label:
    fontFamily: '"Atkinson Hyperlegible Mono", ui-monospace, Menlo, monospace'
    fontSize: "0.75rem"
    fontWeight: 600
    letterSpacing: "0.05em"
rounded:
  none: "0px"
  stop: "50%"
spacing:
  measure: "68ch"
  rail-width: "280px"
  container-max: "1180px"
  xs: "6px"
  sm: "12px"
  md: "18px"
  lg: "28px"
  xl: "40px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "7px 14px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "7px 14px"
  button-master:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
  button-master-pressed:
    backgroundColor: "{colors.ok-soft}"
    textColor: "{colors.ok}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
  input-search:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "7px 10px"
    width: "100%"
  unit-opener:
    backgroundColor: "{colors.band}"
    textColor: "{colors.band-ink}"
    rounded: "{rounded.none}"
    padding: "28px clamp(16px, 5vw, 64px) 22px"
  problem-ticket:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  problem-head:
    backgroundColor: "{colors.band}"
    textColor: "{colors.band-ink}"
    rounded: "{rounded.none}"
    padding: "10px 16px"
  quiz-option:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "10px 8px 10px 52px"
    height: "46px"
  sim-bar:
    backgroundColor: "{colors.band}"
    textColor: "{colors.band-ink}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
  topbar:
    backgroundColor: "{colors.band}"
    textColor: "{colors.band-ink}"
    rounded: "{rounded.none}"
    padding: "0 12px"
    height: "52px"
  callout-key:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
  callout-trap:
    backgroundColor: "{colors.bad-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
---

# Design System: FIS1533 Study Guide (Andén)

## Overview

**Creative North Star: "Andén — Rail Timetable and Station Wayfinding"**

The visual system models the FIS1533 Electricity and Magnetism study guide as a rail transit network ("Andén"): each course block is a colour-coded line, each unit is a station along that line, and high-contrast black departure-board bands anchor the index head, unit openers, and problem tickets. Designed for long desktop study sessions with paper beside the screen—and secondary mobile lookups—it prioritizes high legibility, fixed reading geometry, and unmistakable positional wayfinding over decorative chrome (inferred).

Rather than a generic documentation shell with rounded cards, uniform blue action buttons, and floating shadows, the interface stays completely flat on a stark white (or near-black dark mode) canvas ruled by 1 px hairlines and 2 px ink dividers (inferred). Line colours appear strictly inside structural navigation and ticket framing, leaving the reading column neutral and preserving blue and copper exclusively for physics vector semantics and pedagogical signals.

**Key Characteristics:**
- High-contrast black departure-board bands (`--band` / `--band-ink`) for the index head, unit openers, problem heads, mobile top bar, and mock-exam timer bar.
- Per-block transit line colours (`--l0`, `--lA`–`--lE`) confined strictly to the frame (index diagram, unit opener badge and 8 px rule, problem tag).
- Semantic physics colour pairing: `--accent` (blue) for electric fields, current, and key ideas; `--copper` for magnetic fields, forces, magnetic moments, and exam maps.
- Square corners (`0px` radius), 1 px–2 px ink rules, and zero box shadows across all containers and controls.
- Fixed `68ch` reading measure with excess horizontal space allocated to two-column problem grids, equation grids, and sticky SVG figures.

## Colors

The palette pairs neutral ink-on-paper surfaces with two physics-semantic accents, binary validation colours, black departure-board bands, and six transit-line identifiers, all defined with explicit light and dark themes in `css/main.css` (inferred).

### Primary
- **Electric Blue (`--accent` / `--accent-dark`):** `{colors.accent}` in light, `{colors.accent-dark}` in dark. Used in SVG figures for electric field $\vec E$ vectors and currents, and in UI for links, focus outlines, derivation toggles, "what I do" (`.do`) step labels, interactive slider readouts, and `.key` callout headings. Paired with `--accent-soft` (`{colors.accent-soft}` light / `{colors.accent-soft-dark}` dark) for `.key` callout backgrounds, figure field fills, and `::selection` tinting (`24%` mix).

### Secondary
- **Magnetic Copper (`--copper` / `--copper-dark`):** `{colors.copper}` in light, `{colors.copper-dark}` in dark. Reserved in SVG figures for magnetic field $\vec B$, force $\vec F$, and magnetic moment $\vec\mu$, and in UI for `.exam-map` callouts, `.why` rationale headings, dual-notation table row headers (`table.duo tbody th`), and `.eq.key` labels. Paired with `--copper-soft` (`{colors.copper-soft}` light / `{colors.copper-soft-dark}` dark) for `.exam-map` and `.eq.key` backgrounds (border mixed at `55%` `--copper`).

### Tertiary
- **Transit Line Colours (`--l0`, `--lA`–`--lE`, `--line-ink`):** Assigned via `--line-c` per unit block:
  - **Block 0 · Antes de estudiar (`r01`, `--l0`):** `{colors.l0}` light / `{colors.l0-dark}` dark (Ink Line). `#r01 .unit-num` adds a `1px` border at `40%` `--band-ink`.
  - **Block A · Electrostática (`u01`–`u04`, `--lA`):** `{colors.lA}` light / `{colors.lA-dark}` dark (Amber Line). Overrides `--line-ink` to `{colors.lA-ink}` (`#121417`) in both themes for readable contrast against amber.
  - **Block B · Circuitos (`u05`–`u06`, `--lB`):** `{colors.lB}` light / `{colors.lB-dark}` dark (Green Line).
  - **Block C · Magnetismo (`u07`–`u08`, `--lC`):** `{colors.lC}` light / `{colors.lC-dark}` dark (Magenta Line).
  - **Block D · Inducción y CA (`u09`–`u11`, `--lD`):** `{colors.lD}` light / `{colors.lD-dark}` dark (Violet Line).
  - **Block E · Simulacros y simuladores (`s01`, `s02`, `t01`, `--lE`):** `{colors.lE}` light / `{colors.lE-dark}` dark (Slate Line).
  - **Line Label Ink (`--line-ink`):** `{colors.line-ink}` light / `{colors.line-ink-dark}` dark default text inside `.unit-num` and `.tag` badges (overridden to `{colors.lA-ink}` on amber Block A).
- **Validation & Diagnostic Tones:**
  - **Mastered / Correct (`--ok` / `--ok-soft`):** `{colors.ok}` / `{colors.ok-soft}` light; `{colors.ok-dark}` / `{colors.ok-soft-dark}` dark. Used for mastered `.master[aria-pressed="true"]` buttons, `.final` problem answer boxes, `.try` quick-check blocks, `.mini` summaries, and `.right` quiz options/feedback.
  - **Trap / Error (`--bad` / `--bad-soft`):** `{colors.bad}` / `{colors.bad-soft}` light; `{colors.bad-dark}` / `{colors.bad-soft-dark}` dark. Used for `.trap` warning callouts (`30%` `--bad` border), `.wrong` quiz options/feedback, `.confirming` destructive reset buttons, and `.fig-missing` placeholders.
- **Hardcoded Exceptions (Non-Tokenized CSS Values):**
  - **Prediction Highlighter (`.predict b`):** `{colors.predict-highlight}` background with `#121417` text in both themes for the "Antes de calcular:" pause badge.
  - **Mock Exam Status Accents (`.sim-time.low`, `.sim-nota.ok`):** `{colors.sim-time-low}` when `<= 10` minutes remain and `{colors.sim-nota-ok}` for passing grades (`>= 4.0`) over the dark `--band` bar.
  - **Mobile Drawer Scrim (`.toc-scrim`):** `{colors.toc-scrim}` backdrop behind the off-canvas mobile index.

### Neutral
- **Paper & Surface (`--paper`, `--surface`):** `{colors.paper}` light / `{colors.paper-dark}` dark. `--paper` is the page ground; `--surface` is the container canvas for cards, tables, simulators, and the index sidebar (identical in hex, semantically split between page and component grounds).
- **Primary Ink (`--ink`):** `{colors.ink}` light / `{colors.ink-dark}` dark. Body text, headings, structural `2px` rules, and resting primary button fills.
- **Muted Ink (`--muted`):** `{colors.muted}` light / `{colors.muted-dark}` dark. Lead paragraphs, captions, `.note` text, labels, inactive segmented buttons, and scrollbar thumbs (`50%` mix).
- **Hairline Divider (`--line`):** `{colors.line}` light / `{colors.line-dark}` dark. `1px` borders on sections, table rows, problem `.given` rows, `.reveal` step dividers, and figures.
- **Departure-Board Band (`--band` / `--band-ink`):** `{colors.band}` light / `{colors.band-dark}` dark, always paired with `{colors.band-ink}` (`#ffffff`) for header text. Secondary band metadata (`.toc-progress`, `.unit-weight`, `.src`, `.diff`, `.sim-nota`) uses `color-mix(in srgb, var(--band-ink) 72%–75%, transparent)`.

### Named Rules
**The Meaning-Only Colour Rule.** Colour carries meaning only—never decoration. Per-block line colours (`--l0`, `--lA`–`--lE`) live exclusively in the frame (TOC line diagram, unit opener badge and 8 px rule, problem `.tag`), while `--accent` (blue: $\vec E$, $I$) and `--copper` (copper: $\vec B$, $\vec F$, $\vec\mu$) keep their physical meaning inside figures and derivations.

## Typography

**Display Font:** `"Atkinson Hyperlegible Next"` (with `"Helvetica Neue", Arial, sans-serif` fallback)
**Body Font:** `"Atkinson Hyperlegible Next"` (with `"Helvetica Neue", Arial, sans-serif` fallback)
**Label/Mono Font:** `"Atkinson Hyperlegible Mono"` (with `ui-monospace, Menlo, monospace` fallback)

**Character:** Built around the Atkinson Hyperlegible family (loaded via Google Fonts in `scripts/build.py`: `Next` weights 400, 600, 700, 800 and `Mono` weights 400, 600) to distinguish visually similar glyphs (`1`/`I`/`l`, `0`/`O`, minus signs) during dense equation reading and long problem-solving sessions (inferred). Numeric counters, timers, progress ratios, and coordinates use `font-variant-numeric: tabular-nums`.

### Hierarchy
- **Display (`800`, `clamp(2rem, 4.5vw, 2.75rem)`, `1.08` line-height, `-0.015em` tracking):** Page-level `h1` with `text-wrap: balance`. Unit opener `h1` scales at `clamp(1.75rem, 4vw, 2.375rem)` with `1.1` line-height and `-0.01em` tracking; `.unit-num` badge sits at `800`, `1.25rem`.
- **Headline (`800`, `1.625rem`, `1.15` line-height, `-0.01em` tracking):** Section headings (`.sec h2`) paired with `2px solid var(--ink)` `.sec-head` top rules.
- **Title (`700`, `1.125rem`):** Subsection headings (`.sec h3`), simulator titles (`.sim-title`), and TOC course header (`.toc-course` at `800`). Problem titles (`.ptitle`) use `700`, `1.0625rem`; `.lead` uses `1.1875rem` in `--muted`.
- **Body (`400`, `1.0625rem`, `1.62` line-height):** Primary prose and list copy, constrained to `max-width: 68ch`. Supporting prose (`.small`, `.tbl-wrap` cells at `0.9688rem`, `.note` at `0.875rem`, TOC links at `0.9062rem` / `1.35` line-height) steps down cleanly.
- **Label (`600`–`700` Mono, `0.75rem`–`0.8125rem`, `0.04em`–`0.05em` tracking, uppercase where tagged):** Station tags (`.tag`), given-data labels (`.gl`), step labels (`.rl` at `0.8125rem`), difficulty/source metadata (`.src`, `.diff`), quiz option badges (`.opts button::before` at `700`, `0.875rem`), and mock-exam timers (`.sim-time` at `700`, `1.5rem`, `tabular-nums`). Note: CSS declares `font-weight: 700` on `.opts button::before`, `.sb-sub`, `.sim-time`, and `.sim-pts` even though `scripts/build.py` loads `Atkinson Hyperlegible Mono` weights `400` and `600` (synthesized or fallback-rendered at 700).
- **SVG Figure Math Labels (`.fig .s`, `.fig .t`):** Variable symbols inside inline SVG diagrams use italic `17px "Times New Roman", "STIX Two Text", serif`, paired with `Atkinson Hyperlegible Next` labels at `12.5px` (`.t`), `13px` (`.ta`, `.tc`, `.tw`), `14px` (`.tb`), and `72%` subscripts (`.sb`).

### Named Rules
**The Fixed-Measure Rule.** Reading prose, lists, callouts, and figure captions never exceed `68ch` (`max-width: 68ch`). Extra viewport width expands outer margins, two-column problem grids, equation grids, and sticky figures—never the character measure of body text.

## Layout

The desktop shell (`.layout`) uses a two-column CSS Grid: a sticky `{spacing.rail-width}` (`280px`, `100vh`) vertical index rail on the left and a fluid reading column (`minmax(0, 1fr)`) on the right. `main` caps at `{spacing.container-max}` (`1180px`) with `40px clamp(16px, 5vw, 64px) 80px` padding. When `.no-toc` is active (mock-exam or fragment preview mode), the layout collapses to a single centered column (`max-width: 1180px; margin: 0 auto`) so the index never distracts or obstructs the timer bar.

Multi-part content expands horizontally into structured grids rather than widening prose:
- **Problem Grid (`.prob-grid`):** `minmax(0, 1fr) minmax(0, 1fr)` with `16px` gap; the statement and `.given` data sit on the left while `.fig` sticks on the right (`position: sticky; top: 12px`).
- **Equation Grid (`.eqgrid`):** `repeat(auto-fit, minmax(300px, 1fr))` with `10px` gap.
- **Simulator Grid (`.sim-controls` / `.sim-read`):** `110px 1fr` label-slider pairs and `repeat(auto-fit, minmax(130px, 1fr))` monospace telemetry readouts.

**Responsive Breakpoints & Print:**
- **`<= 900px`:** `.layout` becomes single-column; `.topbar` (`52px`) becomes sticky; `.toc` moves off-canvas (`position: fixed`, `min(86vw, 340px)`, `100dvh`) with `.toc-scrim`; `.unit-head` top negative margin adjusts to `-20px`; `.sim-bar` pins at `top: 52px` below the top bar; `scroll-padding-top` increases to `64px` (`232px` when `.simulacro` is present); interactive controls enforce `min-height: 44px` touch targets; `.sim-controls` stacks to `1fr`.
- **`<= 760px`:** `.prob-grid` collapses to `1fr`, `.prob-grid .fig` unsticks (`position: static`), and `.src` aligns left.
- **`<= 640px`:** `.reveal li` step rows collapse from `9rem minmax(0, 1fr)` to `1fr`.
- **`@media print`:** Hides `.toc`, `.master`, `.ctrl`, `.quiz-bar`, `.sim-bar`, and `.score-box`; switches `.layout` to `display: block`; forces all `.reveal > li`, `.try-ans`, `.q .fb`, and `<details>` open.

## Elevation & Depth

The system is **strictly flat**—zero box shadows exist anywhere in `css/main.css` or `css/guia.css` (`box-shadow: none` is explicitly asserted even on the open mobile drawer). Depth and visual separation are established entirely through contrast polarity (`--band` dark bands against `--paper` light ground), border weight hierarchy (`1px` `--line` hairlines vs. `2px` `--ink` structural rules vs. `8px` `--line-c` unit opener dividers), and low-saturation semantic surface tints (`--accent-soft`, `--copper-soft`, `--ok-soft`, `--bad-soft`). The sole layered overlay is the mobile off-canvas drawer paired with `.toc-scrim` (`rgba(8, 14, 22, 0.45)`).

### Named Rules
**The Square-Ink-No-Shadow Rule.** Surfaces stay flat at rest and in motion: zero box shadows, zero blur elevation, and `0px` corner radii across every interactive and structural element. Hierarchy comes from ink rule weight (`1px` vs. `2px` vs. `8px`) and `--band` contrast polarity.

## Shapes

Every structural container, card, callout, table, input, canvas, focus ring, and button uses sharp `0px` corners (`border-radius: 0`). Border treatment encodes container authority:
- **`2px solid var(--ink)`:** Primary structural boundaries (`.toc` right edge, `.toc-block`, `.sec-head` top rule, `.prob` ticket, `.sim` frame, `.predict` divider, `.formulas` header, `.unit-pager` top rule).
- **`1px solid var(--ink)`:** Interactive controls and inputs (`.master`, `.ctrl button`, `.b-try`, `.deriv-all`, `.quiz-bar button`, `.seg`, `.toc-search input`, `.nota-calc`, `.unit-pager a`).
- **`1px solid var(--line)`:** Passive internal divisions (`.sec` bottom rule, `.eq`, `.tbl-wrap`, `.fig`, `.given > div`, `.reveal li`, `.opts button` top divider, `.deriv` left rule).
- **`1px dashed` (`--line`, `--muted`, `--ink`):** Meta, prerequisite, and self-grading boxes (`.goals`, `.prereq`, `.why`, `.score-box`); `2px dashed var(--bad)` for `.fig-missing`.
- **Circular Exception (`border-radius: 50%`):** Restricted solely to the transit station stops on the index rail (`.toc-unit::after`, `10px` resting / `16px` open) and the unpressed dot on `.master::before` (`0.8em`).

## Components

### Index Line Diagram (`.toc`) & Off-Canvas Drawer
Vertical transit map anchoring course progress and navigation.
- **Header (`.toc-head`):** Sticky `--band` / `--band-ink` block (`18px 20px 16px`), `800`-weight `.toc-course`, tabular mono `.toc-progress`, and `4px` `.bar` progress track (`--band-ink` fill at `25%` track opacity, `.3s` width transition).
- **Line & Station Marks (`.toc-unit`):** Left padding `26px` with a continuous `4px` vertical rail (`::before`, `var(--line-c)`). Station stops (`::after`) encode state geometrically:
  - *Default:* `10px × 10px` circle filled with `--surface` and `2px solid var(--line-c)`.
  - *Current / Open (`.open` or `:has(a.active)`):* `16px × 16px` thick ring (`border-width: 4px`, `left: 0`, `top: 10px`).
  - *Mastered (`:has(a.done)`):* `background: var(--line-c)` filled stop.
- **Links & Progress:** Active link gets `font-weight: 700` and a `2px` `--line-c` bottom gradient underline; `.up` shows per-unit tabular progress; pending units render at `opacity: 0.6`.
- **Mobile Drawer (`<= 900px`):** `min(86vw, 340px)`, `100dvh`, slides from `-100%` via `transform .28s cubic-bezier(.16, 1, .3, 1)` over `.toc-scrim` with `44px` minimum link height.

### Top Bar (`.topbar`, Mobile `<= 900px`)
Compact sticky station header replacing the sidebar on narrow screens.
- **Style:** `52px` height, `--band` background, `--band-ink` text, `2px solid var(--ink)` bottom border.
- **Contents:** `.toc-toggle` button (`44px` min-height, `1px` border at `45%` `--band-ink`), single-line ellipsis-truncated `.topbar-unit`, and tabular mono `.topbar-prog`.

### Search Input (`.toc-search input`)
Live accent-insensitive section filter across all unmounted unit templates.
- **Style:** `100%` width, `7px 10px` padding (`44px` min-height on `<= 900px`), `0.875rem` body font, `--surface` background, `--ink` text, `1px solid var(--ink)` border, `0px` radius.
- **Focus:** `2px solid var(--accent)` outline with `1px` offset; `caret-color: var(--accent)`.

### Unit Opener Band (`.unit-head`)
Full-bleed station arrival banner at the top of each unit.
- **Structure:** Bleeds across `main` horizontal padding (`margin: -40px calc(-1 * clamp(16px, 5vw, 64px)) 0`, `-20px` top on mobile) on `--band` ground with an `8px solid var(--line-c)` bottom border.
- **Badge & Title:** `.unit-num` (`6px 12px`, `800` `1.25rem`) in `--line-c` / `--line-ink`, `h1` in `--band-ink`, and `.unit-weight` in `600` `0.8125rem` mono (`75%` `--band-ink`).

### Problem Ticket (`.prob`)
Guided problem-solving container separating statement, intuition pause, step-by-step reveal, and verification.
- **Container & Head:** `2px solid var(--ink)` border on `--surface`; `.prob-head` (`--band`, `10px 16px`) holds the `--line-c`/`--line-ink` `.tag` badge, `.ptitle`, `.diff`, and right-aligned `.src` citation.
- **Statement & Sticky Figure (`.prob-grid`):** Left column holds `.stmt` and hairline-divided `.given` rows (`.gl` uppercase mono key); right column holds `.fig` with `position: sticky; top: 12px` above `760px`.
- **"Antes de calcular" (`.predict`):** Separated by `2px solid var(--ink)` top border (`margin-top: 14px; padding-top: 12px`); bold lead-in highlighted `#121417` on `#ffd43b`.
- **Step Rows (`.reveal`):** Progressive reveal list (`rise .25s ease` animation). Each step row uses `grid-template-columns: 9rem minmax(0, 1fr)` with `18px` column gap (`1fr` below `640px`): `.rl` (`0.8125rem` mono) spans up to 3 rows on the left, while `.do` (`--accent` bold "Qué hago:") and rationale ("Por qué:") sit in column 2.
- **Final Box & Check:** `.final` row switches to a `2px solid var(--ok)` border (`10px 14px` padding) with `--ok` `.rl` label; `.check` row renders `.rl` in `--muted`. `.ctrl` footer holds `.primary` next-step button, secondary "Ver solución completa" / "Ocultar todo" buttons, and right-aligned mono `.count`.

### Quiz Option List (`.quiz`, `.q`, `.opts`)
Vertical self-check question blocks with auto-numbered letter badges and inline per-option feedback.
- **Structure:** `.quiz-bar` summary + reset above `.q` blocks (`2px solid var(--ink)` top border).
- **Options (`.opts button`):** Single-column grid, `1px solid var(--line)` top border, `46px` min-height, `10px 8px 10px 52px` padding. CSS `counter(opt, upper-alpha)` renders a `28px × 28px` square badge (`--ink` fill, `--surface` text, `700` `0.875rem` mono) at `left: 8px; top: 9px`.
- **States:** Hover tints `4%` `--ink`; `.right` applies `--ok-soft` row + `--ok` badge; `.wrong` applies `--bad-soft` row + `--bad` badge. Per-option `.fb` (`--paper`, `1px` `--ok` or `--bad` border) reveals directly beneath with `.q-retry` underlined link button.

### Formula Timetable Table (`.formulas table`, `table`, `.tbl-wrap`)
Timetable-styled formula reference pairing equation, meaning, and validity condition.
- **Style:** `border-top: 2px solid var(--ink)`, header bottom `2px solid var(--ink)` with transparent background in `.formulas` (or `4%` `--ink` in general `.tbl-wrap` tables), `1px solid var(--line)` cell dividers (`10px 12px` padding in `.formulas`, `9px 12px` in `table`), and `4%` `--ink` zebra striping on even rows in `.formulas`. First column scales `1.05em` for math readability; `.tbl-scroll` and `.tbl-wrap` prevent horizontal overflow.

### Mock-Exam Bar & Self-Scoring (`.sim-bar`, `.score-box`)
Non-occluding timed exam bar paired with `.layout.no-toc` mode.
- **Bar (`.sim-bar`):** Sticky (`top: 0` desktop, `top: 52px` mobile), `--band` / `--band-ink`, `2px solid var(--ink)` bottom border, `12px 16px` padding. Displays `1.5rem` tabular mono `.sim-time` (`#ff8776` `.low` under 10 min), `.eb-btns` (primary inverted `--band-ink`/`--band` start button + outlined reset button with `.confirming` `--bad-soft`/`--bad` second-click guard), and `.sim-pts` / `.sim-nota` (`#69db9e` `.ok` when passing).
- **Pauta Checklist (`.score-box`):** `1px dashed var(--ink)` (`1px dashed var(--line)` outside `.simulacro`), `--paper` background, `--ok`-accented checkboxes.

### Callouts (`.key`, `.trap`, `.note`, `.exam-map`, `.goals`, `.prereq`, `.deriv`, `.why`, `.mini`)
- **Key Idea (`.key`):** `--accent-soft` background, no border, `12px 16px` padding, block bold `--accent` heading (`.eq.key` variant uses `--copper-soft` with `1px` `55%` `--copper` border).
- **Trap (`.trap`):** `--bad-soft` background, `1px solid` `30%` `--bad` border, `12px 16px` padding, block bold `--bad` heading.
- **Note (`.note`):** `0.875rem` `--muted` prose without container fill.
- **Pedagogical Variants:** `.exam-map` (`--copper-soft` + `1px solid var(--copper)`), `.goals` (`1px dashed var(--line)`), `.prereq` (`1px dashed var(--muted)` `<details>`), `.deriv` (`1px solid var(--line)` left rule `<details>`), `.why` (`1px dashed var(--line)` + `--copper` bold label), `.mini` (`--ok-soft` + `1px solid var(--ok)`).

### Buttons
All buttons share `border-radius: 0`, `font-weight: 600` body font, `1px solid var(--ink)` resting border on `--surface` (except `.primary` filled `--ink`/`--surface`), `--accent` border on hover, and `min-height: 44px` at `<= 900px`.
- **Mastery Toggle (`.master`):** `6px 12px` padding, `0.8125rem`, includes a `0.8em` circular dot (`::before`); `[aria-pressed="true"]` switches to `--ok-soft` / `--ok` with an SVG checkmark mask.
- **Problem & Quiz Actions (`.ctrl button`, `.b-try`, `.deriv-all`, `.quiz-bar button`):** `7px 14px` (`.ctrl`/`.b-try`) or `6px 12px` padding.
- **Segmented Toggle (`.seg button`):** `6px 14px` padding inside `1px solid var(--ink)` frame; `.on` inverts to `--ink` / `--surface`.

### Named Rules
**The Mark-Not-Hue State Rule.** Navigation state in the index line diagram is conveyed by geometric mark rather than hue shifts: unstudied units sit as hollow `10px` stops, the active/open unit expands to a `16px` ring (`4px` stroke), and a mastered unit fills solid in its line colour.

## Do's and Don'ts

### Do:
- **Do** restrict per-block line colours (`--l0`, `--lA`–`--lE`) strictly to the navigation and ticket frame (TOC line diagram, unit opener badge and 8 px rule, problem `.tag`).
- **Do** preserve `--accent` for electric fields/currents and `--copper` for magnetic fields/forces inside every SVG figure and derivation.
- **Do** constrain prose, lists, callouts, and captions to `68ch` (`max-width: 68ch`) and route extra horizontal space to margins, `.prob-grid`, `.eqgrid`, and sticky figures.
- **Do** encode transit index state with geometric marks (hollow stop, thick `16px` ring, filled stop) and tabular monospace counters (`font-variant-numeric: tabular-nums`).
- **Do** keep corners at `0px`, rules at `1px`/`2px`/`8px`, box shadows at `none`, and mobile touch targets at `>= 44px`.

### Don't:
- **Don't** add `border-radius` (other than `50%` on TOC station stops and unpressed `.master` dots) or `box-shadow` to cards, buttons, inputs, tables, or drawers.
- **Don't** reuse `--lA`–`--lE` line colours inside prose, callouts, or physics vector diagrams, or repurpose `--accent`/`--copper` in figures for decorative UI accents.
- **Don't** render the `.toc` sidebar during mock-exam mode (`.layout.no-toc`), or allow `.sim-bar` to overlap content or headings (`scroll-margin-top` must clear both `.topbar` and `.sim-bar`).
- **Don't** widen text paragraphs past `68ch` on large monitors.
- **Don't** place un-contrasted `--line-ink` on Block A amber (`u01`–`u04` must keep `#121417` ink).
