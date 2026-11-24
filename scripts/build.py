#!/usr/bin/env python3
"""Assemble the exam study guide.

Reads unidades/manifest.json, includes every unit fragment that exists, inlines
figures referenced as <figure class="fig" data-fig="NAME"> from figuras/svg/NAME.svg,
injects "dominado" buttons per section and generates the TOC.

Outputs:
  index.html               dev build (links css/ and js/)
  dist/guia-examen.html    single-file build (css, js and figures inlined; MathJax via CDN)

Each unit is emitted inside <template id="tpl-UNIT">; js/00-guide.js mounts one unit at a
time and typesets its formulas section by section. A JSON block (#guide-data) carries the
unit order, section titles and an id -> unit map so deep links can open the right unit.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
UNITS_DIR = BASE / "unidades"
FIG_DIR = BASE / "figuras" / "svg"
CSS = ["css/main.css", "css/guia.css"]
JS = ["js/00-guide.js", "js/01-problemas-guiados.js", "js/guia.js", "js/06-simulacro.js", "js/07-simuladores.js", "js/08-nota-necesaria.js", "js/09-prompt-ia.js"]
TITLE = "Guía de estudio · Examen FIS1533"

MATHJAX = """<script>
window.MathJax = {
  tex: { inlineMath: [["$", "$"]], displayMath: [["$$", "$$"]], processEscapes: true,
         macros: { dd: "\\\\mathrm{d}", ui: ["\\\\hat{\\\\mathbf{#1}}", 1] } },
  svg: { fontCache: "global" },
  startup: { typeset: false }
};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>"""

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;600;700;800'
    '&family=Atkinson+Hyperlegible+Mono:wght@400;600&display=swap">'
)

FIG_RE = re.compile(r'<figure class="fig([^"]*)" data-fig="([\w-]+)"([^>]*)>')
SEC_RE = re.compile(r'<section class="sec([^"]*)" id="([\w-]+)"([^>]*)>')
STYLE_RE = re.compile(r"<style>.*?</style>", re.S)
ID_RE = re.compile(r'\bid="([\w-]+)"')


def load_manifest() -> list[dict]:
    return json.loads((UNITS_DIR / "manifest.json").read_text(encoding="utf-8"))


def inline_figures(fragment: str, errors: list[str]) -> str:
    def repl(m: re.Match) -> str:
        name = m.group(2)
        path = FIG_DIR / f"{name}.svg"
        if not path.exists():
            errors.append(f"missing figure: {name}")
            return m.group(0) + f'<div class="fig-missing">Figura pendiente: {html.escape(name)}</div>'
        svg = STYLE_RE.sub("", path.read_text(encoding="utf-8"))
        return m.group(0) + svg

    return FIG_RE.sub(repl, fragment)


STUDY_UNIT_RE = re.compile(r"u\d\d$")
SEC_H2_RE = re.compile(r'(<section class="sec[^"]*" id="([\w-]+)"([^>]*)>)\s*<h2>(.*?)</h2>', re.S)


def is_study(unit_id: str, attrs: str) -> bool:
    """Progress counts only study sections of U1-U11 (not the unit map, R, S or T)."""
    return bool(STUDY_UNIT_RE.match(unit_id)) and 'data-block="mapa"' not in attrs


def inject_masters(fragment: str, unit_id: str) -> str:
    """Put a "dominado" toggle on the title line of every study section."""

    def repl(m: re.Match) -> str:
        sec_id, attrs, title = m.group(2), m.group(3), m.group(4)
        if not is_study(unit_id, attrs):
            return m.group(0)
        btn = (
            f'<button type="button" class="master" data-sec="{sec_id}" data-unit="{unit_id}" '
            f'aria-pressed="false">Marcar como dominado</button>'
        )
        return f'{m.group(1)}\n  <div class="sec-head"><h2>{title}</h2>{btn}</div>'

    return SEC_H2_RE.sub(repl, fragment)


TABLE_RE = re.compile(r"<table\b.*?</table>", re.S)


def wrap_tables(fragment: str) -> str:
    """Give bare tables a horizontal scroll container so they never widen the page on mobile."""
    out, pos = [], 0
    for m in TABLE_RE.finditer(fragment):
        before = fragment[pos:m.start()]
        out.append(before)
        if (fragment[:m.start()].rstrip().endswith('<div class="tbl-wrap">')):
            out.append(m.group(0))
        else:
            out.append(f'<div class="tbl-scroll">{m.group(0)}</div>')
        pos = m.end()
    out.append(fragment[pos:])
    return "".join(out)


def study_sections(fragment: str, unit_id: str) -> list[str]:
    return [m.group(2) for m in SEC_RE.finditer(fragment) if is_study(unit_id, m.group(3))]


def section_titles(fragment: str) -> list[tuple[str, str]]:
    out = []
    for m in SEC_RE.finditer(fragment):
        t = re.search(r'data-title="([^"]+)"', m.group(3))
        if t:
            out.append((m.group(2), t.group(1)))
    return out


def build_toc(units: list[dict], present: dict[str, str]) -> str:
    rows = [
        '<aside class="toc" id="toc" aria-label="Índice">',
        '<div class="toc-head"><div class="toc-course">FIS1533 · Examen</div>',
        '<div class="toc-progress"><span id="prog-count">0/0</span> secciones dominadas',
        '<div class="bar"><div class="bar-fill" id="prog-bar"></div></div></div>',
        '<div class="toc-search"><input type="search" id="toc-q" placeholder="Buscar sección…" '
        'aria-label="Buscar sección en todas las unidades" aria-controls="toc-nav" autocomplete="off">',
        '<p class="toc-empty" id="toc-empty" hidden>Sin resultados. Se buscan títulos de unidades y secciones; '
        'prueba con otra palabra.</p></div></div>',
        '<nav id="toc-nav" aria-label="Unidades y secciones">',
    ]
    block = None
    for u in units:
        if u.get("block") != block:
            block = u.get("block")
            if block:
                rows.append(f'<div class="toc-block">{html.escape(block)}</div>')
        uid = u["id"]
        if uid in present:
            rows.append(f'<div class="toc-unit" data-unit="{uid}">')
            rows.append(
                f'<a class="toc-u" href="#{uid}" data-unit="{uid}"><span class="n">{html.escape(u["num"])}</span>'
                f'{html.escape(u["title"])} <span class="up" data-unit-progress="{uid}"></span></a>'
            )
            for sid, stitle in section_titles(present[uid]):
                rows.append(f'<a class="sub" href="#{sid}">{html.escape(stitle)}</a>')
            rows.append("</div>")
        else:
            rows.append(
                f'<span class="pending"><span class="n">{html.escape(u["num"])}</span>'
                f'{html.escape(u["title"])} · pendiente</span>'
            )
    rows += ["</nav>", "</aside>"]
    return "\n".join(rows)


def guide_data(units: list[dict], present: dict[str, str]) -> str:
    """JSON consumed by js/00-guide.js: unit order, sections and id -> unit map."""
    data: dict = {"units": [], "ids": {}}
    for u in units:
        uid = u["id"]
        if uid not in present:
            continue
        secs = section_titles(present[uid])
        data["units"].append({"id": uid, "num": u["num"], "title": u["title"], "sections": [s for s, _ in secs],
                              "study": study_sections(present[uid], uid)})
        for i in ID_RE.findall(present[uid]):
            data["ids"].setdefault(i, uid)
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script type="application/json" id="guide-data">{raw}</script>'


TOPBAR = (
    '<header class="topbar">'
    '<button type="button" class="toc-toggle" aria-controls="toc" aria-expanded="false">'
    '<svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false">'
    '<path d="M3 5.5h14M3 10h14M3 14.5h14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
    '<span>Índice</span></button>'
    '<span class="topbar-unit" id="topbar-unit"></span>'
    '<span class="topbar-prog" id="topbar-prog"></span>'
    '</header>'
    '<p class="sr-only" id="sr-status" aria-live="polite"></p>'
)


def page(head_assets: str, toc: str, body: str, tail_assets: str) -> str:
    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="es">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f"<title>{TITLE}</title>",
            FONTS,
            head_assets,
            MATHJAX,
            "</head>",
            "<body>",
            TOPBAR if toc else "",
            '<div class="layout">' if toc else '<div class="layout no-toc">',
            toc,
            '<div class="toc-scrim" hidden></div>' if toc else "",
            '<main id="top">',
            body,
            "</main>",
            "</div>",
            tail_assets,
            "</body>",
            "</html>",
            "",
        ]
    )


def preview(fragment_path: Path) -> int:
    """Build qa/preview/<stem>.html with a single fragment (for gate G2 while authoring)."""
    errors: list[str] = []
    frag = inline_figures(fragment_path.read_text(encoding="utf-8"), errors)
    uid = re.search(r'<section class="unit" id="([\w-]+)"', frag)
    frag = wrap_tables(inject_masters(frag, uid.group(1) if uid else "u00"))
    out_dir = BASE / "qa" / "preview"
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = page(
        "\n".join(f'<link rel="stylesheet" href="../../{c}">' for c in CSS if (BASE / c).exists()),
        "",
        frag,
        "\n".join(f'<script src="../../{j}"></script>' for j in JS if (BASE / j).exists()),
    )
    out = out_dir / f"{fragment_path.stem.lstrip('_')}.html"
    out.write_text(doc, encoding="utf-8")
    print(out.relative_to(BASE))
    for e in errors:
        print(f"ERROR {e}", file=sys.stderr)
    return 1 if errors else 0


def main() -> int:
    if len(sys.argv) == 3 and sys.argv[1] == "--preview":
        return preview(Path(sys.argv[2]).resolve())
    units = load_manifest()
    errors: list[str] = []
    present: dict[str, str] = {}
    for u in units:
        path = UNITS_DIR / u["file"]
        if path.exists():
            present[u["id"]] = path.read_text(encoding="utf-8")

    hero_path = UNITS_DIR / "00-portada.html"
    parts = [hero_path.read_text(encoding="utf-8")] if hero_path.exists() else []
    parts.append('<div id="unit-host" tabindex="-1"></div>')
    for u in units:
        if u["id"] in present:
            frag = wrap_tables(inject_masters(inline_figures(present[u["id"]], errors), u["id"]))
            parts.append(f'<template id="tpl-{u["id"]}" data-unit="{u["id"]}">\n{frag}\n</template>')
    parts.append(guide_data(units, present))
    body = "\n".join(parts)
    toc = build_toc(units, present)

    dev = page(
        "\n".join(f'<link rel="stylesheet" href="{c}">' for c in CSS if (BASE / c).exists()),
        toc,
        body,
        "\n".join(f'<script src="{j}"></script>' for j in JS if (BASE / j).exists()),
    )
    (BASE / "index.html").write_text(dev, encoding="utf-8")

    css_inline = "\n".join((BASE / c).read_text(encoding="utf-8") for c in CSS if (BASE / c).exists())
    js_inline = "\n".join((BASE / j).read_text(encoding="utf-8") for j in JS if (BASE / j).exists())
    single = page(f"<style>\n{css_inline}\n</style>", toc, body, f"<script>\n{js_inline}\n</script>")
    (BASE / "dist").mkdir(exist_ok=True)
    (BASE / "dist" / "guia-examen.html").write_text(single, encoding="utf-8")

    print(f"units included: {len(present)}/{len(units)}")
    for e in errors:
        print(f"ERROR {e}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
