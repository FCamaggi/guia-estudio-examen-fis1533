"""S1 Mock exam 1 figures. Generate with: python3 scripts/build_figures.py s01"""

import math
from svg_primitives import FieldGeometryDiagram


def _sub_label(d, x, y, base, sub, cls="s", anchor="middle"):
    """Serif label with a tspan subscript (no '_' in SVG text)."""
    d.raw(
        f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}">'
        f'{base}<tspan class="sb" dy="3.5">{sub}</tspan></text>',
        layer="labels",
    )


def p1a_esfera():
    d = FieldGeometryDiagram(520, 260, "Esfera no conductora de radio R con densidad no uniforme dentro de un cascarón conductor de radios 2R y 4R")
    cx, cy = 140, 130
    r1, r2, r4 = 27, 54, 108
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": r4, "r_in": r2, "fill": "soft", "stroke": "w", "hollow_center": True},
            {"r_out": r2, "fill": "paperf", "stroke": "w"},
            {"r_out": r1, "fill": "csoft", "stroke": "w"},
        ],
    )
    p1 = d._polar_svg(cx, cy, r1, -140)
    d.line((cx, cy), p1, cls="m")
    d.text(p1[0] - 4, p1[1] - 2, "R", cls="s", anchor="end")
    p2 = d._polar_svg(cx, cy, r2, -40)
    d.line((cx, cy), p2, cls="m")
    d.text(p2[0] + 6, p2[1] - 2, "2R", cls="s", anchor="start")
    p4 = d._polar_svg(cx, cy, r4, 20)
    d.line((cx, cy), p4, cls="m")
    d.text(p4[0] + 6, p4[1] + 2, "4R", cls="s", anchor="start")
    pc = d._polar_svg(cx, cy, 81, 125)
    _sub_label(d, pc[0], pc[1] + 5, "Q", "c")
    x0 = 292
    d.text(x0, 60, "r < R: ρ(r) = ρ₀(1 − r/R)", cls="tc", anchor="start")
    d.text(x0, 92, "R < r < 2R: vacío", cls="t", anchor="start")
    d.text(x0, 124, "2R < r < 4R: conductor", cls="ta", anchor="start")
    d.text(x0 + 16, 144, "carga neta", cls="t", anchor="start")
    _sub_label(d, x0 + 80, 144, "Q", "c", anchor="start")
    d.text(x0, 176, "r > 4R: vacío", cls="t", anchor="start")
    d.text(x0, 208, "V(∞) = 0", cls="t", anchor="start")
    return d


def _half_annulus(cx, cy, ri, ro, upper=True):
    """SVG path of a half annulus (upper: y < cy in SVG coordinates)."""
    s = 0 if upper else 1
    return (
        f"M {cx - ro:g} {cy:g} A {ro:g} {ro:g} 0 0 {1 - s} {cx + ro:g} {cy:g} "
        f"L {cx + ri:g} {cy:g} A {ri:g} {ri:g} 0 0 {s} {cx - ri:g} {cy:g} Z"
    )


def p1b_coaxial():
    d = FieldGeometryDiagram(520, 260, "Sección de un capacitor cilíndrico con la mitad superior llena de dieléctrico κ₁ y la inferior de κ₂")
    cx, cy = 140, 130
    a, b, t = 30, 96, 8
    d.raw(f'<circle class="inkf nostroke" cx="{cx}" cy="{cy}" r="{b + t}"/>', layer="bg")
    d.raw(f'<path class="soft w" d="{_half_annulus(cx, cy, a, b, True)}"/>', layer="bg")
    d.raw(f'<path class="csoft w" d="{_half_annulus(cx, cy, a, b, False)}"/>', layer="bg")
    d.raw(f'<circle class="paperf w" cx="{cx}" cy="{cy}" r="{a}"/>', layer="bg")
    d.text(cx - 6, cy + 5, "+Q", cls="tc", anchor="end")
    pk1 = d._polar_svg(cx, cy, 64, 110)
    pk2 = d._polar_svg(cx, cy, 64, 250)
    _sub_label(d, pk1[0], pk1[1] + 5, "κ", "1", cls="sa")
    _sub_label(d, pk2[0], pk2[1] + 5, "κ", "2", cls="sc")
    pa = d._polar_svg(cx, cy, a, 35)
    d.line((cx, cy), pa, cls="m")
    d.text(pa[0] + 4, pa[1] - 4, "a", cls="s", anchor="start")
    pb = d._polar_svg(cx, cy, b, -30)
    d.line((cx, cy), pb, cls="m")
    d.text(pb[0] - 12, pb[1] + 4, "b", cls="s", anchor="end")
    x0 = 285
    d.text(x0, 56, "r < a: conductor interno (+Q)", cls="t", anchor="start")
    d.text(x0, 88, "a < r < b, arriba: dieléctrico", cls="ta", anchor="start")
    _sub_label(d, x0 + 172, 88, "κ", "1", cls="sa", anchor="start")
    d.text(x0, 120, "a < r < b, abajo: dieléctrico", cls="tc", anchor="start")
    _sub_label(d, x0 + 172, 120, "κ", "2", cls="sc", anchor="start")
    d.text(x0, 152, "r = b: conductor externo (−Q)", cls="t", anchor="start")
    d.text(x0, 184, "largo L ≫ b", cls="t", anchor="start")
    d.text(x0, 216, "interfaz: plano horizontal", cls="t", anchor="start")
    return d


def p2_espira():
    d = FieldGeometryDiagram(480, 260, "Alambre infinito con corriente hacia arriba y espira cuadrada coplanar que se acerca al alambre")
    d.field_region(100, 30, 460, 240, step=30, direction="in")
    xw = 60
    d.line((xw, 15), (xw, 245), cls="wk")
    d.current_arrow((44, 170), (44, 110), text="I", cls="a", label_side="left", offset=8)
    x0, x1, y0, y1 = 190, 310, 75, 195
    d.wire((x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0))
    d.dimension((xw, 222), (x0, 222), text="x", label_side="bottom", label_offset=10)
    d.dimension((x0, 222), (x1, 222), text="a", label_side="bottom", label_offset=10)
    d.dimension((x1 + 14, y0), (x1 + 14, y1), text="a", label_side="right", label_offset=8)
    d.current_arrow((180, 55), (120, 55), text="v⃗", cls="a", label_side="top", offset=8)
    d.text(455, 22, "B⃗ ⊗ (lado derecho)", cls="sc", anchor="end")
    d.text(250, 140, "R, m", cls="s")
    return d


def p3_rlc():
    d = FieldGeometryDiagram(600, 240, "Dos circuitos RLC en serie: a la izquierda sin fuente y con interruptor; a la derecha con fuente sinusoidal")
    # (a) natural circuit with switch
    d.node("al", 50, 60, draw_dot=False)
    d.node("ar", 250, 60, draw_dot=False)
    d.node("abr", 250, 180, draw_dot=False)
    d.node("abl", 50, 180, draw_dot=False)
    d.capacitor("al", "abl", text="C", label_side="left", offset=20)
    d.resistor((130, 60), "ar", text="R", label_side="top", offset=18)
    d.inductor("ar", "abr", turns=4, r_coil=7, text="L", label_side="right", offset=20)
    d.wire("abr", "abl")
    d.node("s1", 70, 60, draw_dot=True)
    d.node("s2", 110, 60, draw_dot=True)
    d.wire("al", "s1")
    d.wire("s2", (130, 60))
    d.switch_spdt("s1", (104, 38), text="S", label_offset=(14, -30))
    d.text(72, 105, "+q", cls="tc", anchor="start")
    d.text(72, 150, "−q", cls="ta", anchor="start")
    d.current_arrow((170, 196), (120, 196), text="i", cls="a", label_side="bottom", offset=14)
    d.text(150, 232, "(a) sin fuente", cls="t")
    # (b) driven circuit
    d.node("bl", 360, 180, draw_dot=False)
    d.node("tl", 360, 60, draw_dot=False)
    d.node("tm", 460, 60, draw_dot=False)
    d.node("tr", 560, 60, draw_dot=False)
    d.node("br", 560, 180, draw_dot=False)
    d.ac_source("bl", "tl", text="", label_side="left")
    d.resistor("tl", "tm", text="R", label_side="top", offset=18)
    d.inductor("tm", "tr", turns=4, r_coil=7, text="L", label_side="top", offset=18)
    d.capacitor("tr", "br", text="C", label_side="right", offset=20)
    d.wire("br", "bl")
    d.text(405, 112, "V(t)", cls="s", anchor="start")
    d.text(405, 132, "= V₀ cos ωt", cls="t", anchor="start")
    d.current_arrow((430, 196), (500, 196), text="i(t)", cls="a", label_side="bottom", offset=14)
    d.text(460, 232, "(b) con fuente", cls="t")
    return d


def figures():
    return {
        "s01-p1a-esfera": p1a_esfera(),
        "s01-p1b-coaxial": p1b_coaxial(),
        "s01-p2-espira": p2_espira(),
        "s01-p3-rlc": p3_rlc(),
    }
