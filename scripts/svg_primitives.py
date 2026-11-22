#!/usr/bin/env python3
"""Declarative Python DSL and reusable SVG primitives for all FIS1533 physics diagrams (I1, I2, I3, Examen)."""

import math
from html import escape

STANDALONE_STYLE = """<style>
  :root {
    --surface: #ffffff; --ink: #142030; --muted: #566273; --line: #d8dee7;
    --accent: #1f4fd1; --accent-soft: #e7edfc; --copper: #a85a18; --copper-soft: #f8eee4;
    --font-body: "Source Sans 3", "Segoe UI", Roboto, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --surface: #151c26; --ink: #e5eaf1; --muted: #9aa6b6; --line: #29323f;
      --accent: #84a6ff; --accent-soft: #1b2640; --copper: #e2a26b; --copper-soft: #2a2119;
    }
  }
  svg { background: var(--surface); font-family: var(--font-body); }
  .w { stroke: var(--ink); stroke-width: 1.8; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .wk { stroke: var(--ink); stroke-width: 3.2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .m { stroke: var(--muted); stroke-width: 1.2; fill: none; }
  .md { stroke: var(--muted); stroke-width: 1.3; stroke-dasharray: 4 4; fill: none; }
  .a { stroke: var(--accent); stroke-width: 2.2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .ad { stroke: var(--accent); stroke-width: 1.6; stroke-dasharray: 5 4; fill: none; }
  .c { stroke: var(--copper); stroke-width: 2.2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
  .cd { stroke: var(--copper); stroke-width: 1.4; stroke-dasharray: 4 3; fill: none; }
  .fld { stroke: var(--muted); stroke-width: 1.3; opacity: .38; }
  .fldl { stroke: var(--muted); stroke-width: 1.4; opacity: .6; fill: none; }
  .af { fill: var(--accent); } .cf { fill: var(--copper); } .wf, .inkf, .wkf { fill: var(--ink); }
  .mf, .mdf { fill: var(--muted); } .fldlf { fill: var(--muted); opacity: .6; }
  .adf { fill: var(--accent); } .cdf { fill: var(--copper); }
  .soft { fill: var(--accent-soft); } .csoft { fill: var(--copper-soft); } .paperf { fill: var(--surface); }
  .nostroke { stroke: none; } .nofill { fill: none; }
  .s, .sa, .sc { font: italic 17px "Times New Roman", "STIX Two Text", serif; fill: var(--ink); }
  .sa { fill: var(--accent); } .sc { fill: var(--copper); }
  .t { font: 12.5px var(--font-body); fill: var(--muted); }
  .tb { font: 600 14px var(--font-body); fill: var(--ink); }
  .tc { font: 600 13px var(--font-body); fill: var(--copper); }
  .ta { font: 600 13px var(--font-body); fill: var(--accent); }
  .tw { font: 700 13px var(--font-body); fill: var(--surface); }
  .gl-ink, .gl-acc, .gl-cop, .gl-mut, .gl-srf { fill: none; stroke-width: 1.2; stroke-linecap: round; }
  .gl-ink { stroke: var(--ink); } .gl-acc { stroke: var(--accent); } .gl-cop { stroke: var(--copper); }
  .gl-mut { stroke: var(--muted); } .gl-srf { stroke: var(--surface); }
  .glf-ink { fill: var(--ink); } .glf-acc { fill: var(--accent); } .glf-cop { fill: var(--copper); }
  .glf-mut { fill: var(--muted); } .glf-srf { fill: var(--surface); }
  .sb { font-size: 72%; }
</style>"""


def wire(points: list[tuple[float, float]], cls: str = "w") -> str:
    pts = " ".join(f"{x:g},{y:g}" for x, y in points)
    return f'<polyline class="{cls}" points="{pts}"/>'


def node(x: float, y: float, r: float = 3.6, cls: str = "inkf") -> str:
    return f'<circle class="{cls}" cx="{x:g}" cy="{y:g}" r="{r:g}"/>'


def resistor(x: float, y: float, length: float = 110, angle: float = 0, zigzag_span: float = 44, amp: float = 8) -> str:
    """Standard 6-peak IEEE zigzag resistor centered along `length`."""
    mid = length / 2.0
    span = min(zigzag_span, max(24.0, length * 0.65))
    z0 = mid - span / 2.0
    step = span / 6.0
    pts = [(0.0, 0.0), (round(z0, 1), 0.0)]
    for i in range(6):
        px = z0 + (i + 0.5) * step
        py = amp if i % 2 == 0 else -amp
        pts.append((round(px, 1), py))
    pts.extend([(round(z0 + span, 1), 0.0), (round(length, 1), 0.0)])
    pts_s = " ".join(f"{px:g},{py:g}" for px, py in pts)
    return f'<g transform="translate({x:g},{y:g}) rotate({angle:g})"><polyline class="w" points="{pts_s}"/></g>'


def battery(x: float, y: float, length: float = 60, angle: float = 0, positive_first: bool = True) -> str:
    """DC fem source: long thin plate (.w, +-15) and short thick plate (.wk, +-8)."""
    mid = length / 2.0
    x1, x2 = mid - 4.0, mid + 4.0
    c1, h1 = ("w", 15) if positive_first else ("wk", 8)
    c2, h2 = ("wk", 8) if positive_first else ("w", 15)
    return (
        f'<g transform="translate({x:g},{y:g}) rotate({angle:g})">'
        f'<line class="w" x1="0" y1="0" x2="{x1:g}" y2="0"/>'
        f'<line class="w" x1="{x2:g}" y1="0" x2="{length:g}" y2="0"/>'
        f'<line class="{c1}" x1="{x1:g}" y1="-{h1}" x2="{x1:g}" y2="{h1}"/>'
        f'<line class="{c2}" x1="{x2:g}" y1="-{h2}" x2="{x2:g}" y2="{h2}"/>'
        "</g>"
    )


def capacitor(x: float, y: float, length: float = 60, angle: float = 0, gap: float = 10, half_h: float = 14) -> str:
    """Parallel-plate capacitor centered along `length`."""
    mid = length / 2.0
    x1, x2 = mid - gap / 2.0, mid + gap / 2.0
    return (
        f'<g transform="translate({x:g},{y:g}) rotate({angle:g})">'
        f'<line class="w" x1="0" y1="0" x2="{x1:g}" y2="0"/>'
        f'<line class="w" x1="{x2:g}" y1="0" x2="{length:g}" y2="0"/>'
        f'<line class="w" x1="{x1:g}" y1="-{half_h:g}" x2="{x1:g}" y2="{half_h:g}"/>'
        f'<line class="w" x1="{x2:g}" y1="-{half_h:g}" x2="{x2:g}" y2="{half_h:g}"/>'
        "</g>"
    )


def inductor(x: float, y: float, length: float = 90, angle: float = 0, turns: int = 4, r_coil: float = 7.0) -> str:
    """Standard N-loop semicircular inductor centered along `length`."""
    span = turns * 2.0 * r_coil
    z0 = (length - span) / 2.0
    arcs = "".join(
        f" A {r_coil:g} {r_coil:g} 0 0 1 {z0 + (i + 1) * 2 * r_coil:g} 0"
        for i in range(turns)
    )
    return (
        f'<g transform="translate({x:g},{y:g}) rotate({angle:g})">'
        f'<line class="w" x1="0" y1="0" x2="{z0:g}" y2="0"/>'
        f'<path class="w" d="M {z0:g} 0{arcs}"/>'
        f'<line class="w" x1="{z0 + span:g}" y1="0" x2="{length:g}" y2="0"/>'
        "</g>"
    )


def ac_source(x: float, y: float, length: float = 60, angle: float = 0, r: float = 14.0) -> str:
    """AC sinusoidal source centered along `length`."""
    mid = length / 2.0
    x_l, x_r = mid - r, mid + r
    s_w = r * 0.55
    s_h = r * 0.48
    return (
        f'<g transform="translate({x:g},{y:g}) rotate({angle:g})">'
        f'<line class="w" x1="0" y1="0" x2="{x_l:g}" y2="0"/>'
        f'<line class="w" x1="{x_r:g}" y1="0" x2="{length:g}" y2="0"/>'
        f'<circle class="w paperf" cx="{mid:g}" cy="0" r="{r:g}"/>'
        f'<path class="w" d="M {mid - s_w:g} 0 Q {mid - s_w/2:g} {-s_h:g} {mid:g} 0 T {mid + s_w:g} 0"/>'
        "</g>"
    )


def switch_spdt(px: float, py: float, ax: float, ay: float, bx: float | None = None, by: float | None = None) -> str:
    """Switch pivot at (px, py) closed to A (ax, ay) and optionally open position B (bx, by)."""
    parts = [
        node(px, py),
        node(ax, ay),
        f'<line class="w" x1="{px:g}" y1="{py:g}" x2="{ax:g}" y2="{ay:g}"/>',
    ]
    if bx is not None and by is not None:
        parts.append(node(bx, by))
        parts.append(f'<line class="md" x1="{px:g}" y1="{py:g}" x2="{bx:g}" y2="{by:g}"/>')
    return "".join(parts)


def arrow(x1: float, y1: float, x2: float, y2: float, line_cls: str = "a", head_cls: str = "af", head_len: float = 8.0, head_w: float = 4.0) -> str:
    """Vector arrow from (x1, y1) to (x2, y2) with triangular polygon tip."""
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    if dist < 1e-6:
        return ""
    ux, uy = dx / dist, dy / dist
    nx, ny = -uy, ux
    bx, by = x2 - head_len * ux, y2 - head_len * uy
    p1 = (bx + head_w * nx, by + head_w * ny)
    p2 = (bx - head_w * nx, by - head_w * ny)
    return (
        f'<line class="{line_cls}" x1="{x1:g}" y1="{y1:g}" x2="{bx:.1f}" y2="{by:.1f}"/>'
        f'<polygon class="{head_cls}" points="{x2:g},{y2:g} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"/>'
    )


def field_cross(cx: float, cy: float, half: float = 4.0, cls: str = "fld") -> str:
    return (
        f'<line class="{cls}" x1="{cx-half:g}" y1="{cy-half:g}" x2="{cx+half:g}" y2="{cy+half:g}"/>'
        f'<line class="{cls}" x1="{cx-half:g}" y1="{cy+half:g}" x2="{cx+half:g}" y2="{cy-half:g}"/>'
    )


def field_dot(cx: float, cy: float, r_outer: float = 5.0, r_inner: float = 1.6, line_cls: str = "fld", fill_cls: str = "mf") -> str:
    return (
        f'<circle class="{line_cls} nofill" cx="{cx:g}" cy="{cy:g}" r="{r_outer:g}"/>'
        f'<circle class="{fill_cls}" cx="{cx:g}" cy="{cy:g}" r="{r_inner:g}"/>'
    )


def field_grid(x0: float, y0: float, x1: float, y1: float, step: float = 40.0, kind: str = "in") -> str:
    """Uniform magnetic field grid: kind='in' (x) or 'out' (dot)."""
    items = []
    y = y0
    while y <= y1 + 1e-6:
        x = x0
        while x <= x1 + 1e-6:
            items.append(field_cross(x, y) if kind == "in" else field_dot(x, y))
            x += step
        y += step
    return "".join(items)


def wire_symbol_z(cx: float, cy: float, direction: str = "out", cls: str = "a", fill_cls: str = "af", r: float = 10.0) -> str:
    """Current wire perpendicular to page: out (dot) or in (cross)."""
    if direction == "out":
        return (
            f'<circle class="{cls} nofill" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>'
            f'<circle class="{fill_cls}" cx="{cx:g}" cy="{cy:g}" r="{r*0.24:g}"/>'
        )
    d = r * 0.55
    return (
        f'<circle class="{cls} nofill" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>'
        f'<line class="{cls}" x1="{cx-d:g}" y1="{cy-d:g}" x2="{cx+d:g}" y2="{cy+d:g}"/>'
        f'<line class="{cls}" x1="{cx-d:g}" y1="{cy+d:g}" x2="{cx+d:g}" y2="{cy-d:g}"/>'
    )


NBSP = "\u00a0"
VEC_MARK = "\u20d7"  # combining right arrow above: rendered as drawn geometry
FIELD_GLYPHS = {"\u2297": "in", "\u2299": "out"}  # ⊗ / ⊙: rendered as drawn geometry

# font size (px) and glyph color family per text class
_TEXT_METRICS = {
    "s": (17.0, "ink"), "sa": (17.0, "acc"), "sc": (17.0, "cop"),
    "t": (12.5, "mut"), "tb": (14.0, "ink"), "tc": (13.0, "cop"),
    "ta": (13.0, "acc"), "tw": (13.0, "srf"),
}
_NARROW = set("ijlI.,:;'|!·()[] ")


def _char_w(ch: str, fs: float) -> float:
    if ch in FIELD_GLYPHS:
        return 0.95 * fs
    if ch == " ":
        return 0.28 * fs
    if ch in _NARROW:
        return 0.32 * fs
    if ch in "mwMWμ":
        return 0.72 * fs
    return 0.52 * fs


def _field_symbol(cx: float, cy: float, r: float, kind: str, fam: str) -> str:
    out = f'<circle class="gl-{fam}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>'
    if kind == "out":
        out += f'<circle class="glf-{fam}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r * 0.28:.1f}"/>'
    else:
        d = r * 0.7071
        out += (
            f'<line class="gl-{fam}" x1="{cx - d:.1f}" y1="{cy - d:.1f}" x2="{cx + d:.1f}" y2="{cy + d:.1f}"/>'
            f'<line class="gl-{fam}" x1="{cx - d:.1f}" y1="{cy + d:.1f}" x2="{cx + d:.1f}" y2="{cy - d:.1f}"/>'
        )
    return out


def _over_arrow(x0: float, x1: float, y: float, fam: str) -> str:
    head = 3.4
    return (
        f'<line class="gl-{fam}" x1="{x0:.1f}" y1="{y:.1f}" x2="{x1 - 1.5:.1f}" y2="{y:.1f}"/>'
        f'<polygon class="glf-{fam}" points="{x1:.1f},{y:.1f} {x1 - head * 1.6:.1f},{y - head * 0.75:.1f} '
        f'{x1 - head * 1.6:.1f},{y + head * 0.75:.1f}"/>'
    )


def label(x: float, y: float, text: str, cls: str = "s", anchor: str = "middle") -> str:
    """Text label. Vector marks (U+20D7) and field glyphs (⊗, ⊙) are drawn as geometry
    because their font rendering is unreliable (missing glyphs, misplaced combining arrows)."""
    if VEC_MARK not in text and not any(g in text for g in FIELD_GLYPHS):
        return f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}">{escape(text)}</text>'
    fs, fam = _TEXT_METRICS.get(cls, (14.0, "ink"))
    italic = cls in ("s", "sa", "sc")
    # tokens: (char, has_vector_mark)
    tokens: list[tuple[str, bool]] = []
    for ch in text:
        if ch == VEC_MARK and tokens:
            tokens[-1] = (tokens[-1][0], True)
        elif ch != VEC_MARK:
            tokens.append((ch, False))
    total = sum(_char_w(c, fs) for c, _ in tokens)
    cx = {"start": x, "end": x - total}.get(anchor, x - total / 2.0)
    parts: list[str] = []
    run, run_x = "", cx
    for ch, vec in tokens:
        w = _char_w(ch, fs)
        if ch in FIELD_GLYPHS or vec:
            if run:
                parts.append(f'<text class="{cls}" x="{run_x:.1f}" y="{y:g}" text-anchor="start">{escape(run.replace(" ", NBSP))}</text>')
                run = ""
            if ch in FIELD_GLYPHS:
                parts.append(_field_symbol(cx + w / 2.0, y - 0.33 * fs, 0.36 * fs, FIELD_GLYPHS[ch], fam))
            else:
                parts.append(f'<text class="{cls}" x="{cx + w / 2.0:.1f}" y="{y:g}" text-anchor="middle">{escape(ch)}</text>')
                lean = 0.1 * fs if italic else 0.0
                rise = 0.86 * fs if italic else 1.05 * fs
                parts.append(_over_arrow(cx + 0.08 * w + lean, cx + 0.98 * w + lean, y - rise, fam))
            cx += w
            run_x = cx
        else:
            if not run:
                run_x = cx
            run += ch
            cx += w
    if run:
        parts.append(f'<text class="{cls}" x="{run_x:.1f}" y="{y:g}" text-anchor="start">{escape(run.replace(" ", NBSP))}</text>')
    return "<g>" + "".join(parts) + "</g>"


def wrap_svg_figure(
    elements: list[str],
    width: int,
    height: int,
    aria_label: str,
    caption: str = "",
    standalone: bool = False,
) -> str:
    max_w = round(width * 1.35)
    style_block = f"\n{STANDALONE_STYLE}\n" if standalone else ""
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'style="max-width:{max_w}px" role="img" aria-label="{escape(aria_label)}">'
        f"{style_block}{''.join(elements)}</svg>"
    )
    if standalone:
        return svg
    cap_html = f"<figcaption>{caption}</figcaption>" if caption else ""
    return f'<figure class="fig">{svg}{cap_html}</figure>'


# =====================================================================
# High-Level Declarative DSL (Option A): CircuitDiagram & FieldGeometryDiagram
# =====================================================================

PointRef = str | tuple[float, float]


class CircuitDiagram:
    """Declarative circuit & schematic builder with named nodes and auto-oriented components."""

    def __init__(self, width: int, height: int, aria_label: str, caption: str = ""):
        self.width = width
        self.height = height
        self.aria_label = aria_label
        self.caption = caption
        self.nodes: dict[str, tuple[float, float]] = {}
        self.layers: dict[str, list[str]] = {"bg": [], "wires": [], "overlay": [], "labels": []}

    def _pt(self, ref: PointRef) -> tuple[float, float]:
        if isinstance(ref, str):
            if ref not in self.nodes:
                raise KeyError(f"Unknown node name: {ref!r}")
            return self.nodes[ref]
        return float(ref[0]), float(ref[1])

    def _place_side_label(
        self,
        p1: tuple[float, float],
        p2: tuple[float, float],
        text: str,
        side: str = "auto",
        offset: float = 22.0,
        cls: str = "s",
    ) -> None:
        if not text:
            return
        mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        if abs(dx) >= abs(dy):
            nx, ny = (0.0, -1.0) if side in ("auto", "top", "up") else (0.0, 1.0)
            anchor = "middle"
            dy_baseline = 5.0 if ny > 0 else 0.0
            lx, ly = mx + nx * offset, my + ny * offset + dy_baseline
        else:
            nx, ny = (1.0, 0.0) if side in ("auto", "right") else (-1.0, 0.0)
            anchor = "start" if nx > 0 else "end"
            lx, ly = mx + nx * offset, my + ny * offset + 5.0
        self.layers["labels"].append(label(round(lx, 1), round(ly, 1), text, cls=cls, anchor=anchor))

    def _span_geom(self, p1: PointRef, p2: PointRef) -> tuple[tuple[float, float], tuple[float, float], float, float]:
        c1, c2 = self._pt(p1), self._pt(p2)
        dx, dy = c2[0] - c1[0], c2[1] - c1[1]
        return c1, c2, math.hypot(dx, dy), math.degrees(math.atan2(dy, dx))

    def node(
        self,
        name: str,
        x: float,
        y: float,
        text: str | None = None,
        label_dir: str = "left",
        offset: float = 14.0,
        draw_dot: bool = True,
        cls: str = "s",
    ) -> "CircuitDiagram":
        self.nodes[name] = (float(x), float(y))
        if draw_dot:
            self.layers["overlay"].append(node(x, y))
        if text:
            dx, dy, anchor = {
                "left": (-offset, 5.0, "end"),
                "right": (offset, 5.0, "start"),
                "top": (0.0, -offset, "middle"),
                "bottom": (0.0, offset + 12.0, "middle"),
            }[label_dir]
            self.layers["labels"].append(label(x + dx, y + dy, text, cls=cls, anchor=anchor))
        return self

    def terminal_open(
        self,
        name: str,
        x: float,
        y: float,
        text: str = "",
        label_dir: str = "left",
        offset: float = 14.0,
    ) -> "CircuitDiagram":
        self.nodes[name] = (float(x), float(y))
        self.layers["overlay"].append(f'<circle class="w paperf" cx="{x:g}" cy="{y:g}" r="4"/>')
        if text:
            dx, dy, anchor = {
                "left": (-offset, 5.0, "end"),
                "right": (offset, 5.0, "start"),
                "top": (0.0, -offset, "middle"),
                "bottom": (0.0, offset + 12.0, "middle"),
            }[label_dir]
            self.layers["labels"].append(label(x + dx, y + dy, text, cls="s", anchor=anchor))
        return self

    def ground(self, pos: PointRef, stem: float = 12.0) -> "CircuitDiagram":
        x, y = self._pt(pos)
        yg = y + stem
        self.layers["wires"].append(
            f'<line class="w" x1="{x:g}" y1="{y:g}" x2="{x:g}" y2="{yg:g}"/>'
            f'<line class="w" x1="{x-11:g}" y1="{yg:g}" x2="{x+11:g}" y2="{yg:g}"/>'
            f'<line class="w" x1="{x-7:g}" y1="{yg+4:g}" x2="{x+7:g}" y2="{yg+4:g}"/>'
            f'<line class="w" x1="{x-3:g}" y1="{yg+8:g}" x2="{x+3:g}" y2="{yg+8:g}"/>'
        )
        return self

    def wire(self, *pts: PointRef, cls: str = "w") -> "CircuitDiagram":
        coords = [self._pt(p) for p in pts]
        self.layers["wires"].append(wire(coords, cls=cls))
        return self

    def line(self, p1: PointRef, p2: PointRef, cls: str = "m") -> "CircuitDiagram":
        c1, c2 = self._pt(p1), self._pt(p2)
        self.layers["wires"].append(
            f'<line class="{cls}" x1="{c1[0]:g}" y1="{c1[1]:g}" x2="{c2[0]:g}" y2="{c2[1]:g}"/>'
        )
        return self

    def resistor(self, p1: PointRef, p2: PointRef, text: str = "", label_side: str = "auto", offset: float = 22.0, cls: str = "s") -> "CircuitDiagram":
        c1, c2, length, angle = self._span_geom(p1, p2)
        self.layers["wires"].append(resistor(c1[0], c1[1], length=length, angle=angle))
        self._place_side_label(c1, c2, text, side=label_side, offset=offset, cls=cls)
        return self

    def inductor(self, p1: PointRef, p2: PointRef, turns: int = 4, r_coil: float = 7.0, text: str = "", label_side: str = "auto", offset: float = 22.0, cls: str = "s") -> "CircuitDiagram":
        c1, c2, length, angle = self._span_geom(p1, p2)
        self.layers["wires"].append(inductor(c1[0], c1[1], length=length, angle=angle, turns=turns, r_coil=r_coil))
        self._place_side_label(c1, c2, text, side=label_side, offset=offset, cls=cls)
        return self

    def ac_source(self, p1: PointRef, p2: PointRef, r: float = 14.0, text: str = "V(t)", label_side: str = "auto", offset: float = 24.0, cls: str = "s") -> "CircuitDiagram":
        c1, c2, length, angle = self._span_geom(p1, p2)
        self.layers["wires"].append(ac_source(c1[0], c1[1], length=length, angle=angle, r=r))
        self._place_side_label(c1, c2, text, side=label_side, offset=offset, cls=cls)
        return self

    def meter(self, p1: PointRef, p2: PointRef, symbol: str = "V", r: float = 13.0, text: str = "", label_side: str = "auto", offset: float = 22.0) -> "CircuitDiagram":
        c1, c2, length, angle = self._span_geom(p1, p2)
        mx, my = (c1[0] + c2[0]) / 2.0, (c1[1] + c2[1]) / 2.0
        mid = length / 2.0
        self.layers["wires"].append(
            f'<g transform="translate({c1[0]:g},{c1[1]:g}) rotate({angle:g})">'
            f'<line class="w" x1="0" y1="0" x2="{mid-r:g}" y2="0"/>'
            f'<line class="w" x1="{mid+r:g}" y1="0" x2="{length:g}" y2="0"/>'
            f"</g>"
            f'<circle class="w paperf" cx="{mx:g}" cy="{my:g}" r="{r:g}"/>'
        )
        self.layers["labels"].append(label(mx, my + 5, symbol, cls="tb"))
        if text:
            self._place_side_label(c1, c2, text, side=label_side, offset=offset)
        return self

    def battery(
        self,
        p1: PointRef,
        p2: PointRef,
        text: str = "",
        positive_at: str = "p1",
        show_polarity: bool = True,
        label_side: str = "auto",
        offset: float = 24.0,
        cls: str = "s",
    ) -> "CircuitDiagram":
        c1, c2, length, angle = self._span_geom(p1, p2)
        dx, dy = c2[0] - c1[0], c2[1] - c1[1]
        pos_first = positive_at == "p1"
        self.layers["wires"].append(battery(c1[0], c1[1], length=length, angle=angle, positive_first=pos_first))
        self._place_side_label(c1, c2, text, side=label_side, offset=offset, cls=cls)
        if show_polarity and length >= 30:
            ux, uy = dx / length, dy / length
            if abs(dx) >= abs(dy):
                nx, ny = (0.0, 1.0) if label_side in ("auto", "top", "up") else (0.0, -1.0)
            else:
                nx, ny = (-1.0, 0.0) if label_side in ("auto", "right") else (1.0, 0.0)
            mid_x, mid_y = (c1[0] + c2[0]) / 2.0, (c1[1] + c2[1]) / 2.0
            s_pos = "+" if pos_first else "−"
            s_neg = "−" if pos_first else "+"
            p_left = (mid_x - 13 * ux + 24 * nx, mid_y - 13 * uy + 24 * ny + 4)
            p_right = (mid_x + 13 * ux + 24 * nx, mid_y + 13 * uy + 24 * ny + 4)
            self.layers["labels"].append(label(round(p_left[0], 1), round(p_left[1], 1), s_pos, cls="tb"))
            self.layers["labels"].append(label(round(p_right[0], 1), round(p_right[1], 1), s_neg, cls="tb"))
        return self

    def real_battery(
        self,
        p1: PointRef,
        p2: PointRef,
        emf_text: str = "ε",
        r_text: str = "r",
        positive_at: str = "p1",
        label_side: str = "auto",
    ) -> "CircuitDiagram":
        """Real battery (emf + internal resistance) inside a dashed bounding box."""
        c1, c2, length, _ = self._span_geom(p1, p2)
        dx, dy = c2[0] - c1[0], c2[1] - c1[1]
        ux, uy = dx / (length or 1.0), dy / (length or 1.0)
        mid = (c1[0] + 0.42 * dx, c1[1] + 0.42 * dy)
        # Dashed box around [0.12*L .. 0.88*L]
        b0 = (c1[0] + 0.1 * dx, c1[1] + 0.1 * dy)
        b1 = (c1[0] + 0.9 * dx, c1[1] + 0.9 * dy)
        rx0, ry0 = min(b0[0], b1[0]) - 22, min(b0[1], b1[1]) - 22
        rw = max(abs(b1[0] - b0[0]), 0) + 44
        rh = max(abs(b1[1] - b0[1]), 0) + 44
        self.layers["bg"].append(f'<rect class="csoft md" x="{rx0:.1f}" y="{ry0:.1f}" width="{rw:.1f}" height="{rh:.1f}" rx="8"/>')
        self.battery(c1, mid, text=emf_text, positive_at=positive_at, show_polarity=False, label_side=label_side, offset=24)
        self.resistor(mid, c2, text=r_text, label_side=label_side, offset=24)
        return self

    def capacitor(self, p1: PointRef, p2: PointRef, text: str = "", label_side: str = "auto", offset: float = 22.0, cls: str = "s") -> "CircuitDiagram":
        c1, c2, length, angle = self._span_geom(p1, p2)
        self.layers["wires"].append(capacitor(c1[0], c1[1], length=length, angle=angle))
        self._place_side_label(c1, c2, text, side=label_side, offset=offset, cls=cls)
        return self

    def _draw_element(self, kind: str, pa: PointRef, pb: PointRef, lbl: str, side: str, offset: float, turns: int = 4, positive_at: str = "p1") -> None:
        if kind == "resistor":
            self.resistor(pa, pb, text=lbl, label_side=side, offset=offset)
        elif kind == "capacitor":
            self.capacitor(pa, pb, text=lbl, label_side=side, offset=offset)
        elif kind == "inductor":
            self.inductor(pa, pb, text=lbl, label_side=side, offset=offset, turns=turns)
        elif kind == "battery":
            self.battery(pa, pb, text=lbl, label_side=side, offset=offset, positive_at=positive_at)
        elif kind == "ac_source":
            self.ac_source(pa, pb, text=lbl, label_side=side, offset=offset)
        else:
            self.wire(pa, pb)

    def parallel_group(
        self,
        p_start: PointRef,
        p_end: PointRef,
        branches: list[dict],
        lead: float = 25.0,
        draw_nodes: bool = True,
    ) -> "CircuitDiagram":
        """Auto-layout parallel branches between horizontal points p_start and p_end."""
        x0, y0 = self._pt(p_start)
        x1, y1 = self._pt(p_end)
        if abs(y0 - y1) > 1e-3:
            raise ValueError("parallel_group expects horizontal alignment between p_start and p_end")
        xb0, xb1 = x0 + lead, x1 - lead
        self.wire((x0, y0), (xb0, y0))
        self.wire((xb1, y0), (x1, y0))
        if draw_nodes:
            self.layers["overlay"].append(node(xb0, y0))
            self.layers["overlay"].append(node(xb1, y0))
        for br in branches:
            dy = float(br.get("dy", 0.0))
            yb = y0 + dy
            inset = float(br.get("inset", 10.0))
            self.wire((xb0, y0), (xb0, yb), (xb0 + inset, yb))
            self.wire((xb1 - inset, yb), (xb1, yb), (xb1, y0))
            side = br.get("label_side", "top" if dy <= 0 else "bottom")
            off = float(br.get("offset", 18.0 if side == "top" else 24.0))
            self._draw_element(
                br.get("kind", "resistor"),
                (xb0 + inset, yb),
                (xb1 - inset, yb),
                br.get("label", ""),
                side,
                off,
                turns=int(br.get("turns", 4)),
                positive_at=br.get("positive_at", "p1"),
            )
        return self

    def wheatstone_bridge(
        self,
        top: tuple[float, float],
        right: tuple[float, float],
        bottom: tuple[float, float],
        left: tuple[float, float],
        arms: list[dict],
        center_arm: dict | None = None,
        node_labels: tuple[str, str, str, str] = ("a", "b", "c", "d"),
    ) -> "CircuitDiagram":
        """Diamond Wheatstone bridge with 4 outer arms and optional center bridge branch."""
        pts = [top, right, bottom, left]
        pairs = [(top, right), (right, bottom), (bottom, left), (left, top)]
        default_sides = ["top", "right", "bottom", "left"]
        for i, ((pa, pb), arm) in enumerate(zip(pairs, arms)):
            self._draw_element(
                arm.get("kind", "resistor"),
                pa,
                pb,
                arm.get("label", ""),
                arm.get("label_side", default_sides[i]),
                float(arm.get("offset", 20.0)),
                turns=int(arm.get("turns", 4)),
                positive_at=arm.get("positive_at", "p1"),
            )
        if center_arm:
            self._draw_element(
                center_arm.get("kind", "capacitor"),
                left,
                right,
                center_arm.get("label", ""),
                center_arm.get("label_side", "top"),
                float(center_arm.get("offset", 20.0)),
                turns=int(center_arm.get("turns", 4)),
                positive_at=center_arm.get("positive_at", "p1"),
            )
        dirs = ["top", "right", "bottom", "left"]
        for name, (nx, ny), ldir in zip(node_labels, pts, dirs):
            self.node(name, nx, ny, text=name, label_dir=ldir)
        return self

    def switch_spdt(
        self,
        pivot: PointRef,
        target_closed: PointRef,
        target_open: PointRef | None = None,
        text: str = "S",
        label_offset: tuple[float, float] = (0.0, -20.0),
        draw_terminal_dots: bool = False,
        shorten_px: float = 4.0,
    ) -> "CircuitDiagram":
        cp = self._pt(pivot)
        ca = self._pt(target_closed)
        cb = self._pt(target_open) if target_open is not None else None

        def _short(p0, p1):
            dx, dy = p1[0] - p0[0], p1[1] - p0[1]
            dist = math.hypot(dx, dy) or 1.0
            return p1 if dist <= shorten_px else (p1[0] - shorten_px * dx / dist, p1[1] - shorten_px * dy / dist)

        ca_end = _short(cp, ca)
        self.layers["overlay"].append(f'<line class="w" x1="{cp[0]:g}" y1="{cp[1]:g}" x2="{ca_end[0]:.1f}" y2="{ca_end[1]:.1f}"/>')
        if cb is not None:
            cb_end = _short(cp, cb)
            self.layers["overlay"].append(f'<line class="md" x1="{cp[0]:g}" y1="{cp[1]:g}" x2="{cb_end[0]:.1f}" y2="{cb_end[1]:.1f}"/>')
        if draw_terminal_dots:
            for pt in ([cp, ca] + ([cb] if cb is not None else [])):
                self.layers["overlay"].append(node(pt[0], pt[1]))
        if text:
            self.layers["labels"].append(label(cp[0] + label_offset[0], cp[1] + label_offset[1], text))
        return self

    def current_arrow(self, p1: PointRef, p2: PointRef, text: str = "", cls: str = "a", label_side: str = "auto", offset: float = 16.0) -> "CircuitDiagram":
        c1, c2 = self._pt(p1), self._pt(p2)
        hcls = {"a": "af", "c": "cf", "m": "mf", "w": "inkf"}.get(cls, "af")
        tcls = {"a": "sa", "c": "sc", "m": "t", "w": "s"}.get(cls, "sa")
        self.layers["overlay"].append(arrow(c1[0], c1[1], c2[0], c2[1], line_cls=cls, head_cls=hcls))
        self._place_side_label(c1, c2, text, side=label_side, offset=offset, cls=tcls)
        return self

    def text(self, x: float, y: float, txt: str, cls: str = "t", anchor: str = "middle") -> "CircuitDiagram":
        self.layers["labels"].append(label(x, y, txt, cls=cls, anchor=anchor))
        return self

    def raw(self, svg_snippet: str, layer: str = "overlay") -> "CircuitDiagram":
        self.layers[layer].append(svg_snippet)
        return self

    def render(self, standalone: bool = True) -> str:
        elements = self.layers["bg"] + self.layers["wires"] + self.layers["overlay"] + self.layers["labels"]
        return wrap_svg_figure(
            elements,
            width=self.width,
            height=self.height,
            aria_label=self.aria_label,
            caption=self.caption,
            standalone=standalone,
        )


class FieldGeometryDiagram(CircuitDiagram):
    """Unified declarative physics diagrammer covering Electrostatics, Magnetostatics, Induction & Plots."""

    @staticmethod
    def _polar_svg(cx: float, cy: float, r: float, deg: float) -> tuple[float, float]:
        rad = math.radians(deg)
        return cx + r * math.cos(rad), cy - r * math.sin(rad)

    # --- Coordinates, Dimensions & Angles ---

    def axes_2d(self, origin: PointRef, x_len: float = 140, y_len: float = 120, x_label: str = "x", y_label: str = "y", neg_x: float = 0, neg_y: float = 0) -> "FieldGeometryDiagram":
        ox, oy = self._pt(origin)
        if neg_x > 0:
            self.line((ox - neg_x, oy), (ox, oy), cls="m")
        if neg_y > 0:
            self.line((ox, oy + neg_y), (ox, oy), cls="m")
        self.layers["overlay"].append(arrow(ox, oy, ox + x_len, oy, line_cls="m", head_cls="mf", head_len=6, head_w=3))
        self.layers["overlay"].append(arrow(ox, oy, ox, oy - y_len, line_cls="m", head_cls="mf", head_len=6, head_w=3))
        self.text(ox + x_len + 10, oy + 5, x_label, cls="s")
        self.text(ox, oy - y_len - 8, y_label, cls="s")
        return self

    def axes_3d(self, origin: PointRef, scale: float = 70, labels: tuple[str, str, str] = ("x", "y", "z")) -> "FieldGeometryDiagram":
        ox, oy = self._pt(origin)
        # x down-left (215 deg), y right (0 deg), z up (90 deg)
        px = self._polar_svg(ox, oy, scale * 0.85, 215)
        py = (ox + scale, oy)
        pz = (ox, oy - scale)
        for pt, lbl, off in [(px, labels[0], (-12, 10)), (py, labels[1], (12, 5)), (pz, labels[2], (0, -10))]:
            self.layers["overlay"].append(arrow(ox, oy, pt[0], pt[1], line_cls="m", head_cls="mf", head_len=6, head_w=3))
            self.text(pt[0] + off[0], pt[1] + off[1], lbl, cls="s")
        return self

    def dimension(self, p1: PointRef, p2: PointRef, text: str = "L", offset: float = 0.0, tick: float = 4.0, label_side: str = "auto", label_offset: float = 12.0) -> "FieldGeometryDiagram":
        c1, c2 = self._pt(p1), self._pt(p2)
        dx, dy = c2[0] - c1[0], c2[1] - c1[1]
        dist = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / dist, dx / dist
        q1 = (c1[0] + nx * offset, c1[1] + ny * offset)
        q2 = (c2[0] + nx * offset, c2[1] + ny * offset)
        self.line(q1, q2, cls="m")
        for q in (q1, q2):
            self.line((q[0] - nx * tick, q[1] - ny * tick), (q[0] + nx * tick, q[1] + ny * tick), cls="m")
        self._place_side_label(q1, q2, text, side=label_side, offset=label_offset, cls="s")
        return self

    def angle_arc(self, vertex: PointRef, deg1: float, deg2: float, r: float = 24.0, text: str = "θ", cls: str = "m") -> "FieldGeometryDiagram":
        vx, vy = self._pt(vertex)
        p1 = self._polar_svg(vx, vy, r, deg1)
        p2 = self._polar_svg(vx, vy, r, deg2)
        delta = deg2 - deg1
        sweep = 0 if delta >= 0 else 1
        large_arc = 1 if abs(delta) > 180.0 else 0
        self.layers["overlay"].append(f'<path class="{cls}" d="M {p1[0]:.1f} {p1[1]:.1f} A {r:g} {r:g} 0 {large_arc} {sweep} {p2[0]:.1f} {p2[1]:.1f}"/>')
        if text:
            lp = self._polar_svg(vx, vy, r + 13.0, (deg1 + deg2) / 2.0)
            self.text(lp[0], lp[1] + 5, text, cls="s")
        return self

    # --- Electrostatics: Charges, Dipoles, Rods, Disks, Concentric Shells, Dielectrics, Cubes ---

    def point_charge(self, pos: PointRef, sign: str = "+", r: float = 9.0, text: str = "", label_dir: str = "top", radial_rays: int = 0, ray_len: float = 34.0) -> "FieldGeometryDiagram":
        cx, cy = self._pt(pos)
        fill_cls = {"+": "csoft", "-": "soft"}.get(sign, "paperf")
        stroke_cls = {"+": "c", "-": "a"}.get(sign, "w")
        if radial_rays > 0:
            for k in range(radial_rays):
                deg = k * (360.0 / radial_rays)
                p_in = self._polar_svg(cx, cy, r + 3, deg)
                p_out = self._polar_svg(cx, cy, r + ray_len, deg)
                if sign == "-":
                    self.layers["bg"].append(arrow(p_out[0], p_out[1], p_in[0], p_in[1], line_cls="a", head_cls="af", head_len=6, head_w=3))
                else:
                    self.layers["bg"].append(arrow(p_in[0], p_in[1], p_out[0], p_out[1], line_cls="c", head_cls="cf", head_len=6, head_w=3))
        self.layers["overlay"].append(f'<circle class="{fill_cls} {stroke_cls}" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>')
        if sign in ("+", "-"):
            sym = "+" if sign == "+" else "−"
            tcls = "tc" if sign == "+" else "ta"
            self.layers["labels"].append(label(cx, cy + 4.5, sym, cls=tcls))
        if text:
            dx, dy, anc = {"top": (0, -(r + 8), "middle"), "bottom": (0, r + 16, "middle"), "left": (-(r + 8), 5, "end"), "right": (r + 8, 5, "start")}[label_dir]
            self.text(cx + dx, cy + dy, text, cls="s", anchor=anc)
        return self

    def dipole(self, p_neg: PointRef, p_pos: PointRef, q_labels: tuple[str, str] = ("−q", "+q"), p_label: str = "p⃗") -> "FieldGeometryDiagram":
        c1, c2 = self._pt(p_neg), self._pt(p_pos)
        self.line(c1, c2, cls="w")
        self.point_charge(c1, sign="-", r=8, text=q_labels[0], label_dir="bottom")
        self.point_charge(c2, sign="+", r=8, text=q_labels[1], label_dir="bottom")
        # p vector pointing from -q to +q slightly above
        dx, dy = c2[0] - c1[0], c2[1] - c1[1]
        dist = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / dist, dx / dist
        if ny > 0:
            nx, ny = -nx, -ny
        self.current_arrow((c1[0] + 16 * nx + 0.2 * dx, c1[1] + 16 * ny + 0.2 * dy), (c1[0] + 16 * nx + 0.8 * dx, c1[1] + 16 * ny + 0.8 * dy), text=p_label, cls="c", offset=12)
        return self

    def pendulum_charges(self, apex: PointRef, length: float = 110.0, angle_deg: float = 20.0, q_left: str = "+q", q_right: str = "+q", show_forces: bool = True) -> "FieldGeometryDiagram":
        ax, ay = self._pt(apex)
        # Hatched ceiling
        self.line((ax - 60, ay), (ax + 60, ay), cls="wk")
        for hx in range(-55, 60, 12):
            self.line((ax + hx, ay), (ax + hx + 6, ay - 7), cls="m")
        self.line((ax, ay), (ax, ay + length * 0.95), cls="md")
        p_l = self._polar_svg(ax, ay, length, 270 - angle_deg)
        p_r = self._polar_svg(ax, ay, length, 270 + angle_deg)
        self.wire((ax, ay), p_l)
        self.wire((ax, ay), p_r)
        self.angle_arc((ax, ay), 270 - angle_deg, 270, r=32, text="θ")
        self.angle_arc((ax, ay), 270, 270 + angle_deg, r=32, text="θ")
        self.point_charge(p_l, sign="+", r=8, text=q_left, label_dir="left")
        self.point_charge(p_r, sign="+", r=8, text=q_right, label_dir="right")
        if show_forces:
            self.current_arrow(p_r, (p_r[0], p_r[1] + 40), text="mg", cls="m", label_side="right", offset=10)
            self.current_arrow(p_r, (p_r[0] + 42, p_r[1]), text="Fe", cls="a", label_side="top", offset=10)
        return self

    def charged_rod(self, p1: PointRef, p2: PointRef, thickness: float = 10.0, text: str = "λ", dq_frac: float | None = None, dq_text: str = "dq", target_P: PointRef | None = None) -> "FieldGeometryDiagram":
        c1, c2, length, angle = self._span_geom(p1, p2)
        self.layers["wires"].append(
            f'<g transform="translate({c1[0]:g},{c1[1]:g}) rotate({angle:g})">'
            f'<rect class="csoft w" x="0" y="{-thickness/2:g}" width="{length:g}" height="{thickness:g}" rx="2"/>'
            "</g>"
        )
        self._place_side_label(c1, c2, text, side="bottom", offset=18, cls="sc")
        if dq_frac is not None:
            dx, dy = c2[0] - c1[0], c2[1] - c1[1]
            qx, qy = c1[0] + dq_frac * dx, c1[1] + dq_frac * dy
            self.layers["overlay"].append(
                f'<g transform="translate({qx:g},{qy:g}) rotate({angle:g})">'
                f'<rect class="soft a" x="-6" y="{-thickness/2:g}" width="12" height="{thickness:g}"/>'
                "</g>"
            )
            self.text(qx, qy + thickness + 12, dq_text, cls="sa")
            if target_P is not None:
                cp = self._pt(target_P)
                self.layers["overlay"].append(arrow(qx, qy, cp[0], cp[1], line_cls="ad", head_cls="af"))
                self.node("_P", cp[0], cp[1], text="P", label_dir="top", offset=10)
        return self

    def ring_or_disk_3d(self, center: PointRef, rx: float = 65.0, ry: float = 24.0, is_disk: bool = False, ring_dr_frac: float | None = None, target_P: PointRef | None = None, text: str = "σ") -> "FieldGeometryDiagram":
        cx, cy = self._pt(center)
        if is_disk:
            self.layers["bg"].append(f'<ellipse class="csoft w" cx="{cx:g}" cy="{cy:g}" rx="{rx:g}" ry="{ry:g}"/>')
            if ring_dr_frac:
                r1, r2 = ring_dr_frac * rx, (ring_dr_frac + 0.14) * rx
                y1, y2 = ring_dr_frac * ry, (ring_dr_frac + 0.14) * ry
                self.layers["wires"].append(f'<ellipse class="soft a" cx="{cx:g}" cy="{cy:g}" rx="{r2:g}" ry="{y2:g}"/>')
                self.layers["wires"].append(f'<ellipse class="csoft w" cx="{cx:g}" cy="{cy:g}" rx="{r1:g}" ry="{y1:g}"/>')
        else:
            self.layers["wires"].append(f'<ellipse class="wk nofill" cx="{cx:g}" cy="{cy:g}" rx="{rx:g}" ry="{ry:g}"/>')
        self.line((cx, cy), (cx + rx, cy), cls="md")
        self.text(cx + rx * 0.5, cy + 14, "R", cls="s")
        self.text(cx - rx - 14, cy + 5, text, cls="sc")
        if target_P is not None:
            px, py = self._pt(target_P)
            self.line((cx, cy + ry + 10), (px, py - 24), cls="md")
            self.node("_P", px, py, text="P", label_dir="right", offset=10)
            self.line((cx - rx, cy), (px, py), cls="ad")
            self.line((cx + rx, cy), (px, py), cls="ad")
            self.current_arrow((px, py), (px, py - 42), text="dE⃗", cls="a", label_side="left", offset=12)
        return self

    def concentric_system(
        self,
        center: PointRef,
        shells: list[dict],
        gaussian_radii: list[dict] | None = None,
        cavities: list[dict] | None = None,
    ) -> "FieldGeometryDiagram":
        """Cross-section of concentric spheres/cylinders with optional dashed Gaussian/Ampère circles and cavities."""
        cx, cy = self._pt(center)
        # Draw shells largest radius first so inner regions sit on top
        for sh in sorted(shells, key=lambda s: -float(s["r_out"])):
            ro = float(sh["r_out"])
            ri = float(sh.get("r_in", 0.0))
            fill = sh.get("fill", "paperf")
            stroke = sh.get("stroke", "w")
            self.layers["bg"].append(f'<circle class="{fill} {stroke}" cx="{cx:g}" cy="{cy:g}" r="{ro:g}"/>')
            if ri > 0 and sh.get("hollow_center", False):
                self.layers["bg"].append(f'<circle class="paperf w" cx="{cx:g}" cy="{cy:g}" r="{ri:g}"/>')
            if sh.get("label"):
                r_mid = (ri + ro) / 2.0 if ri > 0 else ro * 0.55
                deg = float(sh.get("label_deg", 35.0))
                lp = self._polar_svg(cx, cy, r_mid, deg)
                self.text(lp[0], lp[1] + 4, sh["label"], cls=sh.get("label_cls", "s"))
            if sh.get("r_label"):
                deg_r = float(sh.get("r_deg", -35.0))
                rp = self._polar_svg(cx, cy, ro, deg_r)
                self.line((cx, cy), rp, cls="m")
                mp = self._polar_svg(cx, cy, ro * 0.65, deg_r)
                self.text(mp[0] + 6, mp[1] + 12, sh["r_label"], cls="s")
        for g in (gaussian_radii or []):
            gr = float(g["r"])
            cls = g.get("cls", "ad")
            self.layers["overlay"].append(f'<circle class="{cls} nofill" cx="{cx:g}" cy="{cy:g}" r="{gr:g}"/>')
            if g.get("label"):
                lp = self._polar_svg(cx, cy, gr, float(g.get("deg", 135.0)))
                self.text(lp[0] - 8, lp[1] - 4, g["label"], cls="sa" if "a" in cls else "sc")
        for cav in (cavities or []):
            vx, vy = cx + float(cav.get("dx", 0.0)), cy + float(cav.get("dy", 0.0))
            vr = float(cav["r"])
            self.layers["overlay"].append(f'<circle class="paperf w" cx="{vx:g}" cy="{vy:g}" r="{vr:g}"/>')
            if cav.get("q"):
                self.point_charge((vx, vy), sign=cav.get("sign", "+"), r=6, text=cav["q"], label_dir="top")
        self.layers["overlay"].append(node(cx, cy, r=2.6))
        return self

    def dielectric_capacitor(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        blocks: list[dict],
        plate_labels: tuple[str, str] = ("+Q", "−Q"),
    ) -> "FieldGeometryDiagram":
        """Parallel-plate capacitor filled with series/parallel dielectric or ohmic blocks."""
        # Top and bottom thick conducting plates
        self.layers["wires"].append(f'<rect class="inkf nostroke" x="{x:g}" y="{y-6:g}" width="{width:g}" height="6"/>')
        self.layers["wires"].append(f'<rect class="inkf nostroke" x="{x:g}" y="{y+height:g}" width="{width:g}" height="6"/>')
        self.text(x + width / 2.0, y - 14, plate_labels[0], cls="tc")
        self.text(x + width / 2.0, y + height + 22, plate_labels[1], cls="ta")
        for blk in blocks:
            bx = x + float(blk.get("x_frac", 0.0)) * width
            bw = float(blk.get("w_frac", 1.0)) * width
            by = y + float(blk.get("y_frac", 0.0)) * height
            bh = float(blk.get("h_frac", 1.0)) * height
            fill = blk.get("fill", "soft")
            self.layers["bg"].append(f'<rect class="{fill} w" x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}"/>')
            if blk.get("label"):
                self.text(bx + bw / 2.0, by + bh / 2.0 + 5, blk["label"], cls="s")
        return self

    def cube_3d(
        self,
        center: PointRef,
        size: float = 110.0,
        vertex_charges: list[str] | None = None,
        center_charge: str | None = None,
        highlight_face: str | None = None,
        show_axes: bool = True,
    ) -> "FieldGeometryDiagram":
        """Isometric/oblique 3D cube centered at `center` with optional 8 vertex charges & axes."""
        cx, cy = self._pt(center)
        s = size
        ox, oy = s * 0.36, -s * 0.28  # oblique depth vector
        # Front face (FBL, FBR, FTR, FTL) and Back face (BBL, BBR, BTR, BTL)
        fbl = (cx - s / 2, cy + s / 2)
        fbr = (cx + s / 2, cy + s / 2)
        ftr = (cx + s / 2, cy - s / 2)
        ftl = (cx - s / 2, cy - s / 2)
        bbl = (fbl[0] + ox, fbl[1] + oy)
        bbr = (fbr[0] + ox, fbr[1] + oy)
        btr = (ftr[0] + ox, ftr[1] + oy)
        btl = (ftl[0] + ox, ftl[1] + oy)

        if highlight_face == "right":
            pts = f"{fbr[0]},{fbr[1]} {bbr[0]},{bbr[1]} {btr[0]},{btr[1]} {ftr[0]},{ftr[1]}"
            self.layers["bg"].append(f'<polygon class="soft nostroke" points="{pts}"/>')
        elif highlight_face == "top":
            pts = f"{ftl[0]},{ftl[1]} {ftr[0]},{ftr[1]} {btr[0]},{btr[1]} {btl[0]},{btl[1]}"
            self.layers["bg"].append(f'<polygon class="soft nostroke" points="{pts}"/>')

        # Hidden edges
        for pa, pb in [(fbl, bbl), (bbl, bbr), (bbl, btl)]:
            self.line(pa, pb, cls="md")
        # Visible edges
        for pa, pb in [(fbl, fbr), (fbr, ftr), (ftr, ftl), (ftl, fbl), (ftl, btl), (ftr, btr), (fbr, bbr), (btl, btr), (btr, bbr)]:
            self.line(pa, pb, cls="w")

        cube_center = (cx + ox / 2, cy + oy / 2)
        if show_axes:
            self.axes_3d(cube_center, scale=s * 0.85)
        if center_charge:
            self.point_charge(cube_center, sign="+" if "-" not in center_charge else "-", r=7, text=center_charge, label_dir="right")
        if vertex_charges:
            verts = [fbl, fbr, ftr, ftl, bbl, bbr, btr, btl]
            dirs = ["left", "right", "right", "left", "left", "right", "right", "left"]
            for pt, qtxt, ldir in zip(verts, vertex_charges, dirs):
                if qtxt:
                    sgn = "-" if ("-" in qtxt or "−" in qtxt) else "+"
                    self.point_charge(pt, sign=sgn, r=5.5, text=qtxt, label_dir=ldir)
        return self

    # --- Magnetostatics, Induction & Spectrometers ---

    def field_region(self, x0: float, y0: float, x1: float, y1: float, step: float = 40.0, direction: str = "in") -> "FieldGeometryDiagram":
        self.layers["bg"].append(field_grid(x0, y0, x1, y1, step=step, kind=direction))
        return self

    def arc_wire(
        self,
        center: PointRef,
        r: float,
        deg_start: float,
        deg_end: float,
        cls: str = "w",
        current_dir: str | None = None,
        current_cls: str = "a",
        current_label: str = "",
        arrow_span_deg: float = 36.0,
        arrow_offset_r: float = 13.0,
    ) -> "FieldGeometryDiagram":
        cx, cy = self._pt(center)
        p1 = self._polar_svg(cx, cy, r, deg_start)
        p2 = self._polar_svg(cx, cy, r, deg_end)
        delta = deg_end - deg_start
        sweep = 0 if delta >= 0 else 1
        large_arc = 1 if abs(delta) > 180.0 else 0
        self.layers["wires"].append(
            f'<path class="{cls}" d="M {p1[0]:.1f} {p1[1]:.1f} A {r:g} {r:g} 0 {large_arc} {sweep} {p2[0]:.1f} {p2[1]:.1f}"/>'
        )
        if current_dir in ("ccw", "cw"):
            mid_deg = (deg_start + deg_end) / 2.0
            half_span = arrow_span_deg / 2.0
            a0, a1 = (mid_deg - half_span, mid_deg + half_span) if current_dir == "ccw" else (mid_deg + half_span, mid_deg - half_span)
            ra = r + arrow_offset_r
            ap1 = self._polar_svg(cx, cy, ra, a0)
            ap2 = self._polar_svg(cx, cy, ra, a1)
            asweep = 0 if current_dir == "ccw" else 1
            rad2 = math.radians(a1)
            sign = 1.0 if current_dir == "ccw" else -1.0
            ux, uy = -math.sin(rad2) * sign, -math.cos(rad2) * sign
            tip = ap2
            tail = (tip[0] - 8.0 * ux, tip[1] - 8.0 * uy)
            nx, ny = -uy, ux
            p_l, p_r = (tail[0] + 4.0 * nx, tail[1] + 4.0 * ny), (tail[0] - 4.0 * nx, tail[1] - 4.0 * ny)
            hcls = {"a": "af", "c": "cf", "m": "mf"}.get(current_cls, "af")
            self.layers["overlay"].append(
                f'<path class="{current_cls}" d="M {ap1[0]:.1f} {ap1[1]:.1f} A {ra:g} {ra:g} 0 0 {asweep} {tail[0]:.1f} {tail[1]:.1f}"/>'
                f'<polygon class="{hcls}" points="{tip[0]:.1f},{tip[1]:.1f} {p_l[0]:.1f},{p_l[1]:.1f} {p_r[0]:.1f},{p_r[1]:.1f}"/>'
            )
            if current_label:
                lp = self._polar_svg(cx, cy, ra + 14.0, mid_deg)
                self.layers["labels"].append(label(round(lp[0], 1), round(lp[1] + 4, 1), current_label, cls="sa"))
        return self

    def amperian_loop(self, center: PointRef, r: float, label_txt: str = "", ccw: bool = True, cls: str = "c", dashed: bool = False) -> "FieldGeometryDiagram":
        cx, cy = self._pt(center)
        line_cls = f"{cls}d" if dashed else cls
        self.layers["wires"].append(f'<circle class="{line_cls} nofill" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>')
        tx, ty = cx, cy - r
        if ccw:
            self.layers["overlay"].append(arrow(tx + 8, ty, tx - 8, ty, line_cls=cls, head_cls=f"{cls}f"))
        else:
            self.layers["overlay"].append(arrow(tx - 8, ty, tx + 8, ty, line_cls=cls, head_cls=f"{cls}f"))
        if label_txt:
            self.layers["labels"].append(label(cx, cy + r + 18, label_txt, cls=f"t{cls}" if cls in ("a", "c") else "t"))
        return self

    def wire_z(self, pos: PointRef, direction: str = "out", text: str = "", cls: str = "a", r: float = 10.0) -> "FieldGeometryDiagram":
        cx, cy = self._pt(pos)
        fill_cls = {"a": "af", "c": "cf", "w": "inkf"}.get(cls, "af")
        self.layers["overlay"].append(wire_symbol_z(cx, cy, direction=direction, cls=cls, fill_cls=fill_cls, r=r))
        if text:
            self.layers["labels"].append(label(cx, cy + r + 18, text, cls=f"s{cls}" if cls in ("a", "c") else "s"))
        return self

    def radius_dim(self, center: PointRef, deg: float, r: float, text: str = "r", cls: str = "md") -> "FieldGeometryDiagram":
        c = self._pt(center)
        p = self._polar_svg(c[0], c[1], r, deg)
        self.line(c, p, cls=cls)
        self._place_side_label(c, p, text, side="auto", offset=12.0, cls="s")
        return self

    def motional_rail_circuit(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        bar_x: float,
        v_text: str = "v⃗",
        B_dir: str = "in",
        left_elem: str = "resistor",
        left_label: str = "R",
        bar_label: str = "ℓ",
    ) -> "FieldGeometryDiagram":
        """Parallel conducting rails with sliding rod, left-branch element, B-field grid, and velocity vector."""
        self.field_region(x + 25, y - 15, x + width + 20, y + height + 15, step=38, direction=B_dir)
        self.wire((x, y), (x + width, y))
        self.wire((x, y + height), (x + width, y + height))
        self._draw_element(left_elem, (x, y), (x, y + height), left_label, "left", 16)
        # Moving rod
        self.line((bar_x, y - 6), (bar_x, y + height + 6), cls="wk")
        self.node("_t", bar_x, y, draw_dot=True)
        self.node("_b", bar_x, y + height, draw_dot=True)
        self.text(bar_x - 10, y + height / 2 + 5, bar_label, cls="s", anchor="end")
        self.current_arrow((bar_x + 8, y + height / 2), (bar_x + 56, y + height / 2), text=v_text, cls="a", label_side="top", offset=10)
        return self

    def solenoid_2d(self, x: float, y: float, length: float = 280, height: float = 110, turns: int = 8, top_dir: str = "in", show_B: bool = True, amperian_rect: bool = True) -> "FieldGeometryDiagram":
        step = length / (turns + 1)
        bot_dir = "out" if top_dir == "in" else "in"
        for k in range(1, turns + 1):
            wx = x + k * step
            self.wire_z((wx, y), direction=top_dir, r=8)
            self.wire_z((wx, y + height), direction=bot_dir, r=8)
        if show_B:
            for row in (0.3, 0.5, 0.7):
                by = y + row * height
                self.layers["bg"].append(arrow(x + length - 10, by, x + 10, by, line_cls="c", head_cls="cf"))
            self.text(x + length / 2, y + height * 0.5 - 10, "B⃗", cls="sc")
        if amperian_rect:
            rx, rw, ry0, ry1 = x + length * 0.25, length * 0.5, y + height * 0.48, y - 35
            self.layers["overlay"].append(f'<rect class="ad nofill" x="{rx:g}" y="{ry1:g}" width="{rw:g}" height="{ry0 - ry1:g}"/>')
            for pt, lbl, d in [((rx, ry0), "a", "bottom"), ((rx + rw, ry0), "b", "bottom"), ((rx + rw, ry1), "c", "top"), ((rx, ry1), "d", "top")]:
                self.text(pt[0], pt[1] + (14 if d == "bottom" else -6), lbl, cls="ta")
        return self

    def toroid_2d(self, center: PointRef, r_in: float = 55.0, r_out: float = 110.0, turns: int = 16, amperian_radii: list[float] | None = None) -> "FieldGeometryDiagram":
        cx, cy = self._pt(center)
        self.layers["bg"].append(f'<circle class="soft w" cx="{cx:g}" cy="{cy:g}" r="{r_out:g}"/>')
        self.layers["bg"].append(f'<circle class="paperf w" cx="{cx:g}" cy="{cy:g}" r="{r_in:g}"/>')
        for k in range(turns):
            deg = k * (360.0 / turns)
            p_in = self._polar_svg(cx, cy, r_in - 6, deg)
            p_out = self._polar_svg(cx, cy, r_out + 6, deg)
            self.wire_z(p_in, direction="in", r=5)
            self.wire_z(p_out, direction="out", r=5)
        for ar in (amperian_radii or []):
            self.amperian_loop((cx, cy), ar, ccw=True, cls="c", dashed=True)
        return self

    def velocity_selector_spectrometer(self, x: float, y: float, plate_len: float = 130, plate_gap: float = 70, chamber_w: float = 170, r_orbit: float = 58, q_sign: str = "+") -> "FieldGeometryDiagram":
        """Crossed-field velocity selector leading into semicircular deflection chamber."""
        # Plates
        self.layers["wires"].append(f'<rect class="csoft w" x="{x:g}" y="{y-8:g}" width="{plate_len:g}" height="8"/>')
        self.layers["wires"].append(f'<rect class="soft w" x="{x:g}" y="{y+plate_gap:g}" width="{plate_len:g}" height="8"/>')
        self.text(x + plate_len * 0.5, y - 14, "+ + + + +", cls="tc")
        self.text(x + plate_len * 0.5, y + plate_gap + 22, "− − − − −", cls="ta")
        # Vertical slit wall at x + plate_len
        sx = x + plate_len + 14
        ymid = y + plate_gap / 2.0
        self.line((sx, y - 24), (sx, ymid - 8), cls="wk")
        self.line((sx, ymid + 8), (sx, y + plate_gap + 24), cls="wk")
        # B field in selector + chamber
        self.field_region(x + 15, y + 12, sx + chamber_w - 15, y + plate_gap - 12, step=34, direction="in")
        self.field_region(sx + 20, ymid - r_orbit * 2 - 15, sx + chamber_w - 15, y + plate_gap + 15, step=34, direction="in")
        # E arrows inside plates
        for ex in (x + plate_len * 0.3, x + plate_len * 0.7):
            self.layers["overlay"].append(arrow(ex, y + 8, ex, y + plate_gap - 8, line_cls="c", head_cls="cf"))
        # Straight beam + semicircle of radius r_orbit
        self.current_arrow((x - 36, ymid), (sx + 10, ymid), text="v⃗", cls="a", label_side="top", offset=10)
        self.line((x - 10, ymid), (sx, ymid), cls="ad")
        # Semicircle bending right into chamber (270 -> 360 -> 450 deg CCW around center (sx, ymid - r_orbit))
        self.arc_wire((sx, ymid - r_orbit), r=r_orbit, deg_start=270, deg_end=450, cls="ad", current_dir="ccw", current_cls="a")
        self.node("_hit", sx, ymid - 2 * r_orbit, text="detector", label_dir="left", offset=10, cls="t")
        self.radius_dim((sx, ymid - r_orbit), deg=45, r=r_orbit, text="R")
        self.point_charge((x - 36, ymid), sign=q_sign, r=7, text=f"{q_sign}q", label_dir="bottom")
        return self

    def tilted_loop_side_view(self, center: PointRef, length: float = 120.0, angle_deg: float = 28.0, B_dir_deg: float = 270.0, show_forces: bool = True) -> "FieldGeometryDiagram":
        cx, cy = self._pt(center)
        self.line((cx, cy - length * 0.65), (cx, cy + length * 0.65), cls="md")
        p_top = self._polar_svg(cx, cy, length / 2.0, 90 - angle_deg)
        p_bot = self._polar_svg(cx, cy, length / 2.0, 270 - angle_deg)
        self.line(p_top, p_bot, cls="wk")
        self.wire_z(p_top, direction="in", r=7)
        self.wire_z(p_bot, direction="out", r=7)
        self.angle_arc((cx, cy), 90 - angle_deg, 90, r=32, text="θ")
        # Normal mu vector perpendicular to tilted loop
        mu_end = self._polar_svg(cx, cy, 52, -angle_deg)
        self.current_arrow((cx, cy), mu_end, text="μ⃗", cls="c", label_side="top", offset=10)
        if show_forces:
            self.current_arrow(p_bot, (p_bot[0] + 44, p_bot[1]), text="F⃗", cls="a", label_side="bottom", offset=14)
            self.current_arrow(p_top, (p_top[0] - 44, p_top[1]), text="F⃗", cls="a", label_side="top", offset=10)
            # Uniform B lines at edge
            bx = cx + length * 0.75
            self.current_arrow((bx, cy - 45), (bx, cy + 45) if B_dir_deg == 270 else (bx + 60, cy - 45), text="B⃗", cls="c", label_side="right", offset=10)
        return self

    # --- 1D Function Plots & Phasor Diagrams ---

    def function_plot(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        x_domain: tuple[float, float],
        y_domain: tuple[float, float],
        curves: list[list[tuple[float, float]]],
        v_lines: list[tuple[float, str]] | None = None,
        h_lines: list[tuple[float, str]] | None = None,
        x_label: str = "r",
        y_label: str = "E(r)",
        cls: str = "a",
    ) -> "FieldGeometryDiagram":
        """Plot piecewise/continuous curves inside (x, y, width, height) with dashed guides."""
        x0, x1 = x_domain
        y0, y1 = y_domain
        px = lambda vx: x + (vx - x0) / ((x1 - x0) or 1.0) * width
        py = lambda vy: y + height - (vy - y0) / ((y1 - y0) or 1.0) * height

        # Axes
        self.layers["wires"].append(arrow(x, y + height, x + width + 14, y + height, line_cls="w", head_cls="inkf", head_len=6, head_w=3))
        self.layers["wires"].append(arrow(x, y + height, x, y - 14, line_cls="w", head_cls="inkf", head_len=6, head_w=3))
        self.text(x + width + 18, y + height + 5, x_label, cls="s", anchor="start")
        self.text(x - 6, y - 16, y_label, cls="s", anchor="end")

        for vx, lbl in (v_lines or []):
            gx = px(vx)
            self.line((gx, y), (gx, y + height), cls="md")
            if lbl:
                self.text(gx, y + height + 16, lbl, cls="s")
        for vy, lbl in (h_lines or []):
            gy = py(vy)
            self.line((x, gy), (x + width, gy), cls="md")
            if lbl:
                self.text(x - 8, gy + 4, lbl, cls="s", anchor="end")

        for seg in curves:
            pts = [(round(px(vx), 1), round(py(vy), 1)) for vx, vy in seg]
            self.layers["overlay"].append(wire(pts, cls=cls))
        return self

    def phasor_diagram(self, center: PointRef, radius: float = 70.0, phasors: list[dict] | None = None) -> "FieldGeometryDiagram":
        cx, cy = self._pt(center)
        self.axes_2d((cx, cy), x_len=radius + 24, y_len=radius + 24, x_label="Re", y_label="Im", neg_x=radius + 14, neg_y=radius + 14)
        self.layers["bg"].append(f'<circle class="md nofill" cx="{cx:g}" cy="{cy:g}" r="{radius:g}"/>')
        for ph in (phasors or []):
            r = float(ph.get("r", radius * 0.85))
            deg = float(ph.get("deg", 0.0))
            tip = self._polar_svg(cx, cy, r, deg)
            cls = ph.get("cls", "a")
            self.current_arrow((cx, cy), tip, text=ph.get("label", ""), cls=cls, label_side=ph.get("label_side", "auto"), offset=float(ph.get("offset", 12)))
        return self


# Unified alias exposing all 23 physics diagram pieces
PhysicsDiagram = FieldGeometryDiagram
