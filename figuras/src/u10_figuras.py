"""U10 Inductance and RL, LC, RLC circuits figures.
Generate with: python3 scripts/build_figures.py u10
"""

import math
from svg_primitives import FieldGeometryDiagram, arrow, field_cross, field_dot


def _sub_label(d, x: float, y: float, base: str, sub: str, cls: str = "s", anchor: str = "middle", post: str = ""):
    """Draw a serif/body label with a clean tspan subscript (avoids Unicode tofu for letters)."""
    post_span = f'<tspan dy="-3.5">{post}</tspan>' if post else ""
    d.raw(
        f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}">'
        f'{base}<tspan class="sb" dy="3.5">{sub}</tspan>{post_span}</text>',
        layer="labels",
    )


def inductancia_mutua():
    d = FieldGeometryDiagram(460, 230, "Dos bobinas coaxiales acopladas por flujo magnético mutuo")
    # Coil 1 (left)
    x1, cy = 115, 115
    for dx in (-24, -8, 8, 24):
        d.raw(f'<ellipse class="w nofill" cx="{x1 + dx}" cy="{cy}" rx="12" ry="46"/>', layer="wires")
    d.line((x1 - 36, cy + 46), (x1 - 36, cy + 72), cls="w")
    d.line((x1 + 24, cy + 46), (x1 + 24, cy + 72), cls="w")
    d.current_arrow((x1 - 36, cy + 70), (x1 - 36, cy + 52), text="", cls="a")
    _sub_label(d, x1 - 46, cy + 68, "i", "1", cls="sa", anchor="end")
    d.text(x1 - 6, cy - 62, "Bobina 1 (N₁ vueltas)", cls="t", anchor="middle")

    # Coil 2 (right)
    x2 = 335
    for dx in (-18, 0, 18):
        d.raw(f'<ellipse class="w nofill" cx="{x2 + dx}" cy="{cy}" rx="10" ry="38"/>', layer="wires")
    d.line((x2 - 28, cy + 38), (x2 - 28, cy + 68), cls="w")
    d.line((x2 + 18, cy + 38), (x2 + 18, cy + 68), cls="w")
    d.text(x2 - 5, cy - 52, "Bobina 2 (N₂ vueltas)", cls="t", anchor="middle")

    # B-field lines from coil 1 passing through coil 2
    d.current_arrow((68, cy), (402, cy), cls="c")
    for dy, bend in ((-22, -32), (22, 32)):
        d.raw(
            f'<path class="c nofill" d="M {x1 - 35} {cy + dy} C {x1 + 40} {cy + dy}, '
            f'{x2 - 60} {cy + bend}, {x2 + 50} {cy + bend}"/>',
            layer="bg",
        )
        d.raw(arrow(x2 + 34, cy + bend, x2 + 52, cy + bend, line_cls="c", head_cls="cf"), layer="overlay")
    # Outer returning field loop (subtle, below bottom of coil 1 or lower profile above)
    d.raw(
        f'<path class="cd nofill" d="M {x1 + 24} {cy - 44} C {x1 + 52} {cy - 60}, '
        f'{x1 - 52} {cy - 60}, {x1 - 28} {cy - 44}"/>',
        layer="bg",
    )
    d.text(225, cy - 10, "B⃗₁", cls="sc")
    _sub_label(d, 268, cy + 54, "Φ", "21", cls="sc")
    d.text(350, cy + 88, "ε₂ = −M di₁/dt", cls="ta", anchor="middle")
    return d


def alambre_espira_m():
    d = FieldGeometryDiagram(460, 250, "Alambre infinito sobre el eje x y espira rectangular coplanar")
    ox, oy = 65, 200
    # Axes
    d.axes_2d((ox, oy), x_len=340, y_len=160, x_label="x", y_label="y", neg_x=30, neg_y=20)
    # Wire along x axis
    d.line((30, oy), (405, oy), cls="wk")
    d.current_arrow((115, oy - 12), (185, oy - 12), text="I₁", cls="a", label_side="top", offset=8)
    # Rectangular loop in first quadrant: x from 140 to 300, y from 140 (h) to 65 (h+b)
    x0, x1, y_bot, y_top = 140, 300, 140, 65
    d.field_region(x0 + 25, y_top + 18, x1 - 20, y_bot - 15, step=38, direction="out")
    d.wire((x0, y_bot), (x0, y_top), (x1, y_top), (x1, y_bot), (x0, y_bot))
    # Clockwise current I2
    d.current_arrow((x0 + 60, y_top - 10), (x0 + 110, y_top - 10), text="I₂", cls="a", label_side="top", offset=6)
    d.current_arrow((x1 + 10, y_top + 20), (x1 + 10, y_bot - 20), cls="a")
    # Dimensions
    d.dimension((x0, y_bot + 16), (x1, y_bot + 16), text="a", label_side="bottom", label_offset=10)
    d.dimension((x1 + 26, y_bot), (x1 + 26, y_top), text="b", label_side="right", label_offset=8)
    d.dimension((x0 - 22, oy), (x0 - 22, y_bot), text="h", label_side="left", label_offset=8)
    d.text(425, 36, "B⃗₁ ⊙ (y > 0)", cls="sc", anchor="end")
    return d


def inductor_convencion():
    d = FieldGeometryDiagram(460, 276, "Convención de caída de potencial Vab en resistor e inductor")
    rows = [
        ("a) Resistor", "resistor", 42, "Vab = iR > 0", "+", "−", False),
        ("b) Inductor, di/dt = 0", "inductor", 104, "Vab = 0", "", "", False),
        ("c) Inductor, di/dt > 0", "inductor", 170, "Vab = L di/dt > 0", "+", "−", True),
        ("d) Inductor, di/dt < 0", "inductor", 238, "Vab = L di/dt < 0", "−", "+", True),
    ]
    for title, kind, y, eq_txt, s_left, s_right, show_emf in rows:
        d.text(16, y + 4, title, cls="t", anchor="start")
        pa, pb = (178, y), (312, y)
        d.node(f"a{y}", pa[0], pa[1], text="a", label_dir="top", offset=10)
        d.node(f"b{y}", pb[0], pb[1], text="b", label_dir="top", offset=10)
        if kind == "resistor":
            d.resistor(pa, pb, text="R", label_side="top", offset=16)
        else:
            d.inductor(pa, pb, turns=4, r_coil=6.5, text="L", label_side="top", offset=16)
        d.current_arrow((142, y), (168, y), text="i", cls="a", label_side="top", offset=8)
        if s_left:
            d.text(192, y + 22, s_left, cls="tb")
            d.text(298, y + 22, s_right, cls="tb")
        if show_emf:
            # Induced emf arrow cleanly below inductor between + and -
            if s_left == "+":
                d.current_arrow((265, y + 19), (225, y + 19), cls="c")
            else:
                d.current_arrow((225, y + 19), (265, y + 19), cls="c")
        d.text(335, y + 4, eq_txt, cls="tb", anchor="start")
    return d


def toroide_energia():
    d = FieldGeometryDiagram(460, 250, "Toroide de sección A y radio medio r con campo magnético confinado")
    cx, cy = 155, 128
    d.toroid_2d((cx, cy), r_in=54, r_out=98, turns=16, amperian_radii=[76])
    d.radius_dim((cx, cy), deg=-30, r=76, text="r")
    d.text(cx + 58, cy - 30, "B⃗", cls="sc")
    d.text(290, 62, "N espiras, corriente I", cls="t", anchor="start")
    d.text(290, 90, "Sección transversal: A", cls="t", anchor="start")
    d.text(290, 118, "Volumen: 2πrA", cls="t", anchor="start")
    d.text(290, 152, "B = μ₀NI / (2πr)", cls="sc", anchor="start")
    d.text(290, 182, "u = B² / (2μ₀)", cls="sa", anchor="start")
    d.text(290, 210, "fuera del toroide: B = 0", cls="t", anchor="start")
    return d


def circuito_rl():
    d = FieldGeometryDiagram(460, 248, "Circuito RL con interruptor de dos posiciones para carga y descarga")
    # Left branch: battery
    d.node("top_l", 75, 45, draw_dot=False)
    d.node("bot_l", 75, 185, draw_dot=False)
    d.battery("top_l", "bot_l", text="ε", positive_at="p1", label_side="left", offset=22)
    # SPDT switch at top between left/mid
    d.node("sw_a", 155, 45, text="a", label_dir="top", offset=10)
    d.node("sw_b", 155, 185, text="b", label_dir="left", offset=12)
    d.node("sw_p", 205, 45, draw_dot=True)
    d.wire("top_l", "sw_a")
    d.wire("bot_l", "sw_b")
    d.switch_spdt("sw_p", "sw_a", "sw_b", text="S", label_offset=(-14, -18))
    # Middle-right loop: R on top, L on right
    d.node("tr", 390, 45, draw_dot=False)
    d.node("br", 390, 185, draw_dot=False)
    d.node("bm", 205, 185, draw_dot=True)
    d.wire("sw_b", "bm", "br")
    d.resistor("sw_p", "tr", text="R", label_side="top", offset=20)
    d.inductor("tr", "br", turns=4, r_coil=7, text="L", label_side="right", offset=22)
    d.current_arrow((225, 25), (270, 25), text="i(t)", cls="a", label_side="top", offset=6)
    d.text(230, 232, "a: fuente conectada (crecimiento)   |   b: sin fuente (decaimiento)", cls="t", anchor="middle")
    return d


def rl_curvas():
    d = FieldGeometryDiagram(490, 225, "Curvas de crecimiento y decaimiento de corriente en un circuito RL")
    pts_up = [(t / 20, 1 - math.exp(-t / 20)) for t in range(0, 101)]
    pts_dn = [(t / 20, math.exp(-t / 20)) for t in range(0, 101)]
    d.function_plot(
        72, 35, 150, 130, (0, 5), (0, 1.1), [pts_up],
        v_lines=[(1, "τ")], h_lines=[(1, "I∞"), (1 - math.exp(-1), "0,63 I∞")],
        x_label="t", y_label="i(t)", cls="a",
    )
    d.text(147, 198, "Crecimiento: I∞(1 − exp(−t/τ))", cls="ta")
    d.function_plot(
        304, 35, 150, 130, (0, 5), (0, 1.1), [pts_dn],
        v_lines=[(1, "τ")], h_lines=[(1, "I₀"), (math.exp(-1), "0,37 I₀")],
        x_label="t", y_label="i(t)", cls="c",
    )
    d.text(379, 198, "Decaimiento: I₀ exp(−t/τ)", cls="tc")
    return d


def circuito_lc():
    d = FieldGeometryDiagram(470, 230, "Circuito LC ideal y oscilación armónica de carga y corriente")
    # Left: LC schematic
    d.node("tl", 45, 50, draw_dot=False)
    d.node("tr", 165, 50, draw_dot=False)
    d.node("br", 165, 175, draw_dot=False)
    d.node("bl", 45, 175, draw_dot=False)
    d.capacitor("tl", "bl", text="C", label_side="left", offset=20)
    d.inductor("tr", "br", turns=4, r_coil=7, text="L", label_side="right", offset=20)
    d.wire("bl", "br")
    # Switch on top
    d.node("s1", 85, 50, draw_dot=True)
    d.node("s2", 125, 50, draw_dot=True)
    d.wire("tl", "s1")
    d.wire("s2", "tr")
    d.switch_spdt("s1", "s2", text="S", label_offset=(20, -14))
    d.text(65, 92, "+q", cls="tc")
    d.text(65, 140, "−q", cls="ta")
    d.current_arrow((125, 36), (155, 36), text="i", cls="a", label_side="top", offset=6)
    d.text(105, 206, "ω₀ = 1/√(LC)", cls="tb")

    # Right: plot of q(t)/Qmax and i(t)/Imax
    pts_q = [(x / 40, math.cos(2 * math.pi * (x / 40))) for x in range(0, 61)]
    pts_i = [(x / 40, -math.sin(2 * math.pi * (x / 40))) for x in range(0, 61)]
    d.function_plot(
        245, 35, 195, 130, (0, 1.5), (-1.2, 1.2), [pts_q],
        v_lines=[(0.25, "T/4"), (0.5, "T/2"), (1.0, "T")],
        h_lines=[(0, "0")],
        x_label="t", y_label="q, i", cls="a",
    )
    # Draw i(t) curve in copper
    x0, x1 = 0.0, 1.5
    y0, y1 = -1.2, 1.2
    px = lambda vx: 245 + (vx - x0) / (x1 - x0) * 195
    py = lambda vy: 35 + 130 - (vy - y0) / (y1 - y0) * 130
    ipts = " ".join(f"{px(vx):.1f},{py(vy):.1f}" for vx, vy in pts_i)
    d.raw(f'<polyline class="cd" points="{ipts}"/>', layer="overlay")
    d.text(285, 22, "q(t) azul", cls="ta", anchor="start")
    d.text(365, 22, "i(t) cobre", cls="tc", anchor="start")
    return d


def rlc_regimenes():
    d = FieldGeometryDiagram(470, 235, "Circuito RLC serie libre y sus tres regímenes de amortiguamiento")
    # Left: series RLC loop
    d.node("tl", 40, 48, draw_dot=False)
    d.node("tr", 170, 48, draw_dot=False)
    d.node("br", 170, 175, draw_dot=False)
    d.node("bl", 40, 175, draw_dot=False)
    d.capacitor("tl", "bl", text="C", label_side="left", offset=20)
    d.resistor("tl", "tr", text="R", label_side="top", offset=18)
    d.inductor("tr", "br", turns=4, r_coil=7, text="L", label_side="right", offset=20)
    d.wire("bl", "br")
    d.text(105, 115, "q(0) = Q₀", cls="s")
    d.text(105, 136, "i(0) = 0", cls="s")

    # Right: 3 damping curves
    pts_sub = [(t / 25, math.exp(-0.55 * (t / 25)) * math.cos(4.2 * (t / 25))) for t in range(0, 126)]
    pts_crit = [(t / 25, (1 + 2.2 * (t / 25)) * math.exp(-2.2 * (t / 25))) for t in range(0, 126)]
    pts_sob = [(t / 25, 1.35 * math.exp(-0.95 * (t / 25)) - 0.35 * math.exp(-3.6 * (t / 25))) for t in range(0, 126)]
    d.function_plot(
        245, 35, 195, 135, (0, 5), (-0.75, 1.15), [pts_sub],
        h_lines=[(0, "0"), (1, "Q₀")], x_label="t", y_label="q(t)", cls="a",
    )
    x0, x1, y0, y1 = 0.0, 5.0, -0.75, 1.15
    px = lambda vx: 245 + (vx - x0) / (x1 - x0) * 195
    py = lambda vy: 35 + 135 - (vy - y0) / (y1 - y0) * 135
    cpts = " ".join(f"{px(vx):.1f},{py(vy):.1f}" for vx, vy in pts_crit)
    spts = " ".join(f"{px(vx):.1f},{py(vy):.1f}" for vx, vy in pts_sob)
    d.raw(f'<polyline class="c" points="{cpts}"/>', layer="overlay")
    d.raw(f'<polyline class="md" points="{spts}"/>', layer="overlay")
    d.text(255, 200, "azul: subamortiguado", cls="ta", anchor="start")
    d.text(255, 216, "cobre: crítico   |   gris: sobreamortiguado", cls="t", anchor="start")
    return d


def solenoides_concentricos():
    d = FieldGeometryDiagram(460, 230, "Dos solenoides concéntricos de radios r1 < r2 y longitud l")
    cx, cy = 140, 118
    # Concentric circles view (cross-section)
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 82, "fill": "paperf", "stroke": "wk", "r_label": "r₂", "r_deg": -25},
            {"r_out": 46, "fill": "soft", "stroke": "w", "r_label": "r₁", "r_deg": 40},
        ],
    )
    # Put B dots inside r1
    for dx, dy in ((0, -22), (-20, 10), (20, 10)):
        d.raw(field_dot(cx + dx, cy + dy, r_outer=4.5, r_inner=1.5, line_cls="c", fill_cls="cf"), layer="overlay")
    d.text(cx + 68, cy - 66, "N₂", cls="tb")
    d.text(cx - 28, cy - 16, "N₁", cls="ta")
    d.text(275, 68, "largo ℓ ≫ r₂", cls="t", anchor="start")
    d.text(275, 96, "Solo hay B₁ dentro de r₁:", cls="t", anchor="start")
    d.text(275, 118, "B₁ = μ₀ N₁ I₁ / ℓ", cls="sc", anchor="start")
    d.text(275, 146, "Área con flujo en cada", cls="t", anchor="start")
    d.text(275, 164, "espira de N₂: A₁ = π r₁²", cls="ta", anchor="start")
    return d


def cable_coaxial():
    d = FieldGeometryDiagram(460, 230, "Sección transversal de un cable coaxial con corrientes opuestas +I y -I")
    cx, cy = 145, 118
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 84, "fill": "soft", "stroke": "wk", "r_label": "b", "r_deg": -35},
            {"r_out": 30, "fill": "csoft", "stroke": "wk", "r_label": "a", "r_deg": 45},
        ],
        gaussian_radii=[{"r": 58, "cls": "cd", "label": "r", "deg": 135}],
    )
    d.raw(field_dot(cx, cy, r_outer=5, r_inner=1.8, line_cls="a", fill_cls="af"), layer="overlay")
    d.text(cx - 66, cy - 72, "−I (⊗)", cls="ta", anchor="end")
    d.text(cx, cy + 16, "+I", cls="tc")
    d.text(275, 72, "Región a < r < b:", cls="tb", anchor="start")
    d.text(275, 98, "B(r) = μ₀ I / (2πr)", cls="sc", anchor="start")
    d.text(275, 130, "Para r < a y r > b:", cls="t", anchor="start")
    _sub_label(d, 275, 152, "B = 0  (I", "enc", cls="t", anchor="start", post=" = 0)")
    d.text(275, 184, "Toda la energía magnética", cls="t", anchor="start")
    d.text(275, 202, "está entre r = a y r = b", cls="t", anchor="start")
    return d


def rl_dos_mallas():
    d = FieldGeometryDiagram(450, 220, "Circuito RL de dos mallas con interruptor y resistencias R1 y R2")
    d.node("tl", 55, 50, draw_dot=False)
    d.node("bl", 55, 175, draw_dot=False)
    d.node("tm", 230, 50, draw_dot=True)
    d.node("bm", 230, 175, draw_dot=True)
    d.node("tr", 375, 50, draw_dot=False)
    d.node("br", 375, 175, draw_dot=False)
    d.battery("tl", "bl", text="ε", positive_at="p1", label_side="left", offset=22)
    d.node("s1", 95, 50, draw_dot=True)
    d.node("s2", 130, 50, draw_dot=True)
    d.wire("tl", "s1")
    d.switch_spdt("s1", "s2", text="S", label_offset=(18, -14))
    d.resistor("s2", "tm", text="R₁", label_side="top", offset=18)
    d.wire("bl", "bm")
    d.resistor("tm", "bm", text="R₂", label_side="left", offset=18)
    d.wire("tm", "tr")
    d.wire("bm", "br")
    d.inductor("tr", "br", turns=4, r_coil=7, text="L", label_side="right", offset=20)
    d.current_arrow((290, 34), (335, 34), cls="a")
    _sub_label(d, 312, 22, "i", "L", cls="sa")
    return d


def ex_2026_1_p3():
    d = FieldGeometryDiagram(460, 230, "Circuito de dos mallas del Examen 2026-1 P3 con inductancia compartida L y condensador C")
    # Nodes a, b (left), c, d (center), e, f (right)
    d.node("a", 65, 55, text="a", label_dir="top", offset=10, draw_dot=False)
    d.node("b", 65, 180, text="b", label_dir="bottom", offset=10, draw_dot=False)
    d.node("c", 230, 55, text="c", label_dir="top", offset=12)
    d.node("d", 230, 180, text="d", label_dir="bottom", offset=12)
    d.node("e", 390, 55, text="e", label_dir="top", offset=10, draw_dot=False)
    d.node("f", 390, 180, text="f", label_dir="bottom", offset=10, draw_dot=False)

    d.battery("a", "b", text="E", positive_at="p1", label_side="left", offset=22)
    # Top left: S1
    d.node("s1a", 125, 55, draw_dot=True)
    d.node("s1b", 165, 55, draw_dot=True)
    d.wire("a", "s1a")
    d.wire("s1b", "c")
    d.switch_spdt("s1a", "s1b", text="S₁", label_offset=(20, -14))
    d.resistor("b", "d", text="R", label_side="bottom", offset=20)
    # Center: L
    d.inductor("c", "d", turns=4, r_coil=7, text="L", label_side="left", offset=18)
    # Top right: S2
    d.node("s2a", 290, 55, draw_dot=True)
    d.node("s2b", 330, 55, draw_dot=True)
    d.wire("c", "s2a")
    d.wire("s2b", "e")
    d.switch_spdt("s2a", "s2b", text="S₂", label_offset=(20, -14))
    d.wire("d", "f")
    d.capacitor("e", "f", text="C", label_side="right", offset=18)

    # Current arrows as in pauta: iR right on top-left, iL down in center, iC up on right
    d.current_arrow((175, 39), (210, 39), cls="a")
    _sub_label(d, 192, 27, "i", "R", cls="sa")
    d.current_arrow((250, 92), (250, 138), cls="a")
    _sub_label(d, 266, 120, "i", "L", cls="sa", anchor="start")
    d.current_arrow((368, 138), (368, 92), cls="a")
    _sub_label(d, 354, 120, "i", "C", cls="sa", anchor="end")
    return d


def ex_2021_2_ej4():
    d = FieldGeometryDiagram(460, 240, "Dos alambres infinitos con corrientes opuestas y espira cuadrada coplanar")
    ox, oy = 55, 195
    d.axes_2d((ox, oy), x_len=365, y_len=165, x_label="x", y_label="", neg_x=25, neg_y=20)
    d.text(ox - 16, 26, "y", cls="s")
    # Wire 1 at x = ox (x=0)
    d.line((ox, 20), (ox, 205), cls="wk")
    d.current_arrow((ox - 16, 135), (ox - 16, 75), text="I(t)", cls="a", label_side="left", offset=8)
    # Wire 2 at x = 165 (x=L)
    xw2 = 165
    d.line((xw2, 20), (xw2, 205), cls="wk")
    d.current_arrow((xw2 - 16, 75), (xw2 - 16, 135), text="I(t)", cls="a", label_side="left", offset=8)
    # Square loop from x = xw2 + d = 235 to 335, y from oy (0) to oy - 100 (a)
    xl0, xl1, yt = 235, 335, oy - 100
    d.field_region(xl0 + 18, yt + 18, xl1 - 15, oy - 15, step=35, direction="out")
    d.wire((xl0, oy), (xl0, yt), (xl1, yt), (xl1, oy), (xl0, oy))
    # Dimensions
    d.dimension((ox, 218), (xw2, 218), text="D", label_side="bottom", label_offset=10)
    d.dimension((xw2, 218), (xl0, 218), text="d", label_side="bottom", label_offset=10)
    d.dimension((xl0, 218), (xl1, 218), text="a", label_side="bottom", label_offset=10)
    d.dimension((xl1 + 14, oy), (xl1 + 14, yt), text="a", label_side="right", label_offset=8)
    d.text(355, 45, "z saliendo (⊙)", cls="t", anchor="start")
    return d


def figures():
    return {
        "u10-inductancia-mutua": inductancia_mutua(),
        "u10-alambre-espira-m": alambre_espira_m(),
        "u10-inductor-convencion": inductor_convencion(),
        "u10-toroide-energia": toroide_energia(),
        "u10-circuito-rl": circuito_rl(),
        "u10-rl-curvas": rl_curvas(),
        "u10-circuito-lc": circuito_lc(),
        "u10-rlc-regimenes": rlc_regimenes(),
        "u10-solenoides-concentricos": solenoides_concentricos(),
        "u10-cable-coaxial": cable_coaxial(),
        "u10-rl-dos-mallas": rl_dos_mallas(),
        "u10-ex-2026-1-p3": ex_2026_1_p3(),
        "u10-ex-2021-2-ej4": ex_2021_2_ej4(),
    }
