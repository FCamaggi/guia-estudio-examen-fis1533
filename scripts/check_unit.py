#!/usr/bin/env python3
"""Gate G1 (structure) for one or more unit fragments. See SPEC-PEDAGOGICO.md §2 and §7.

Usage: python3 scripts/check_unit.py unidades/u09-induccion.html [...]
Exit code 1 if any ERROR is found. WARN lines do not fail the gate.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
FIG_DIR = BASE / "figuras" / "svg"

MIN = {"ejemplo": 3, "arquetipo": 2, "practica": 4, "trap": 3, "quiz_q": 5}
DANGLING = re.compile(r"como vimos|ver (la )?clase|visto antes|es f[aá]cil ver|trivialmente", re.I)
# A macro glued to the next letters becomes an undefined control sequence (e.g. "\sumR_i").
TEX_GLUE = re.compile(r"\\(sum|int|oint|iint|cdot|times|frac|vec|hat|sqrt|Delta|mu|varepsilon)([A-Za-z]+)")
TEX_OK = {"cdots", "cdotp", "iiint", "intop", "ointop", "intercal", "sumop"}


class Node:
    def __init__(self, tag: str, attrs: dict[str, str], parent: "Node | None"):
        self.tag, self.attrs, self.parent = tag, attrs, parent
        self.children: list[Node] = []

    @property
    def classes(self) -> set[str]:
        return set(self.attrs.get("class", "").split())

    def iter(self):
        yield self
        for c in self.children:
            yield from c.iter()

    def find_all(self, pred):
        return [n for n in self.iter() if pred(n)]


VOID = {"br", "img", "hr", "meta", "link", "input", "source", "wbr"}


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {}, None)
        self.cur = self.root
        self.ids: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if "id" in a:
            self.ids.append(a["id"])
        n = Node(tag, a, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if "id" in a:
            self.ids.append(a["id"])
        self.cur.children.append(Node(tag, a, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent


def has_cls(c: str):
    return lambda n: c in n.classes


def check(path: Path) -> tuple[list[str], list[str]]:
    errs, warns = [], []
    src = path.read_text(encoding="utf-8")
    tb = TreeBuilder()
    tb.feed(src)
    root = tb.root

    units = root.find_all(lambda n: n.tag == "section" and "unit" in n.classes)
    if len(units) != 1:
        errs.append(f"expected exactly 1 <section class=\"unit\">, found {len(units)}")
        return errs, warns
    unit = units[0]
    uid = unit.attrs.get("id", "")
    for a in ("id", "data-num", "data-title"):
        if not unit.attrs.get(a):
            errs.append(f"unit missing attribute {a}")

    dup = [i for i, c in Counter(tb.ids).items() if c > 1]
    if dup:
        errs.append(f"duplicate ids: {', '.join(dup)}")
    bad_ids = [i for i in tb.ids if uid and not i.startswith(uid)]
    if bad_ids:
        warns.append(f"ids not prefixed with '{uid}': {', '.join(bad_ids[:8])}")

    secs = root.find_all(lambda n: n.tag == "section" and "sec" in n.classes)
    blocks = Counter(s.attrs.get("data-block", "") for s in secs)
    for s in secs:
        if not s.attrs.get("data-title"):
            errs.append(f"section {s.attrs.get('id')} missing data-title")
    for b in ("mapa", "teoria", "formulas"):
        if blocks[b] < 1:
            errs.append(f"missing section data-block=\"{b}\"")
    for s in secs:
        if s.attrs.get("data-block") == "teoria" and not s.find_all(lambda n: n.tag == "figure"):
            errs.append(f"theory section {s.attrs.get('id')} has no figure")

    mapa = [s for s in secs if s.attrs.get("data-block") == "mapa"]
    if mapa:
        for c in ("key", "goals", "exam-map"):
            if not mapa[0].find_all(has_cls(c)):
                errs.append(f"mapa section missing .{c}")

    probs = root.find_all(has_cls("prob"))
    kinds = Counter(p.attrs.get("data-kind", "?") for p in probs)
    for k in ("ejemplo", "arquetipo", "practica"):
        if kinds[k] < MIN[k]:
            msg = f"{k}: {kinds[k]} < {MIN[k]}"
            (warns if k == "arquetipo" and unit.attrs.get("data-waive-arquetipo") else errs).append(msg)
    for p in probs:
        pid = p.attrs.get("id", "?")
        if p.attrs.get("data-kind") not in ("ejemplo", "arquetipo", "practica"):
            errs.append(f"prob {pid}: data-kind must be ejemplo|arquetipo|practica")
        lis = p.find_all(lambda n: n.tag == "li")
        if not any("final" in li.classes for li in lis):
            errs.append(f"prob {pid}: no li.final")
        if not any("check" in li.classes for li in lis):
            errs.append(f"prob {pid}: no li.check")
        if not p.find_all(has_cls("ctrl")):
            errs.append(f"prob {pid}: no .ctrl")
        if p.attrs.get("data-kind") == "arquetipo" and not p.find_all(has_cls("src")):
            errs.append(f"prob {pid}: arquetipo without .src citation")

    if len(root.find_all(has_cls("trap"))) < MIN["trap"]:
        errs.append(f"traps < {MIN['trap']}")
    qs = root.find_all(lambda n: "q" in n.classes and n.parent and any("quiz" in a.classes for a in _ancestors(n)))
    if len(qs) < MIN["quiz_q"]:
        errs.append(f"quiz questions: {len(qs)} < {MIN['quiz_q']}")
    for q in qs:
        opts = [b.attrs.get("data-o") for b in q.find_all(lambda n: n.tag == "button")]
        if q.attrs.get("data-correct") not in opts:
            errs.append(f"quiz question with data-correct not among options ({q.attrs.get('data-correct')})")
        if len(q.find_all(has_cls("fb"))) < len(opts):
            warns.append("quiz question without feedback for every option")

    for f in root.find_all(lambda n: n.tag == "figure"):
        name = f.attrs.get("data-fig")
        if not name:
            errs.append("figure without data-fig (figures must come from the engine)")
        elif not (FIG_DIR / f"{name}.svg").exists():
            errs.append(f"figure file missing: figuras/svg/{name}.svg")

    text = re.sub(r"<[^>]+>", " ", src)
    no_esc = text.replace("\\$", "")
    if no_esc.count("$$") % 2:
        errs.append("unbalanced $$")
    if no_esc.replace("$$", "").count("$") % 2:
        errs.append("unbalanced $")
    for m in TEX_GLUE.finditer(src):
        if m.group(1) + m.group(2) not in TEX_OK:
            errs.append(f"TeX macro glued to letters: {m.group(0)!r}")
    for m in DANGLING.finditer(text):
        warns.append(f"possible dangling reference: '{m.group(0)}'")
    if "\u20d7" in src:
        warns.append("combining arrow U+20D7 in HTML text; use $\\vec{}$")
    return errs, warns


def _ancestors(n: Node):
    p = n.parent
    while p is not None:
        yield p
        p = p.parent


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    failed = False
    for a in argv:
        errs, warns = check(Path(a))
        print(f"== {a}: {'FAIL' if errs else 'PASS'} ({len(errs)} errors, {len(warns)} warnings)")
        for e in errs:
            print(f"  ERROR {e}")
        for w in warns:
            print(f"  WARN  {w}")
        failed |= bool(errs)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
