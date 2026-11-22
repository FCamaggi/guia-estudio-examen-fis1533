"""U7 Magnetic force figures. Generate with: python3 scripts/build_figures.py u07"""

import math
from svg_primitives import FieldGeometryDiagram, arrow


def _vec_sub(d, x, y, base, sub, cls="sc", anchor="start"):
    """Draw a vector label with a clean lowered subscript (no '_' in SVG)."""
    tcls = {"sc": "tc", "sa": "ta", "s": "t"}.get(cls, "t")
    if anchor == "start":
        d.text(x, y, base + "\u20d7", cls=cls, anchor="start")
        d.text(x + 12, y + 4, sub, cls=tcls, anchor="start")
    else:
        d.text(x, y, base + "\u20d7", cls=cls, anchor="middle")
        d.text(x + 7, y + 4, sub, cls=tcls, anchor="start")


def _vc_label(d, x, y, rel, cls="ta", anchor="start"):
    """Draw 'v < vc', 'v = vc', 'v > vc' with lowered 'c' subscript (no '_')."""
    txt = f"v {rel} v"
    d.text(x, y, txt, cls=cls, anchor=anchor)
    dx = 29 if anchor == "start" else 4
    d.text(x + dx, y + 3, "c", cls=cls, anchor="start")


def lorentz_mano():
    d = FieldGeometryDiagram(460, 250, "Fuerza magnética sobre cargas positiva y negativa y convención de campo")
    ox, oy = 130, 142
    d.raw(
        f'<polygon class="soft nostroke" opacity="0.45" '
        f'points="{ox-75},{oy+26} {ox+95},{oy+26} {ox+130},{oy-18} {ox-40},{oy-18}"/>',
        layer="bg",
    )
    d.point_charge((ox, oy), sign="+", r=8, text="+q", label_dir="left")
    d.current_arrow((ox + 8, oy), (ox + 100, oy), text="v⃗", cls="a", label_side="bottom", offset=16)
    b_tip = d._polar_svg(ox, oy, 84, 36)
    d.current_arrow((ox, oy), b_tip, text="B⃗", cls="c", label_side="top", offset=10)
    d.angle_arc((ox, oy), 0, 36, r=36, text="θ")
    d.current_arrow((ox, oy - 8), (ox, oy - 98), text="F⃗ (+q)", cls="c", label_side="left", offset=10)
    d.current_arrow((ox, oy + 8), (ox, oy + 68), cls="a")
    d.text(ox + 10, oy + 64, "F⃗ (−q)", cls="sa", anchor="start")
    d.text(140, 236, "F⃗ = q (v⃗ × B⃗)  perpendicular al plano", cls="t")

    d.raw('<rect class="paperf m" x="288" y="28" width="154" height="175" rx="8"/>', layer="bg")
    d.text(365, 50, "Convención 3D", cls="tb")
    d.wire_z((326, 95), direction="in", cls="c", r=12)
    d.text(350, 93, "B⃗ ⊗", cls="sc", anchor="start")
    d.text(350, 110, "entra a la hoja", cls="t", anchor="start")
    d.wire_z((326, 158), direction="out", cls="c", r=12)
    d.text(350, 156, "B⃗ ⊙", cls="sc", anchor="start")
    d.text(350, 173, "sale de la hoja", cls="t", anchor="start")
    return d


def lineas_gauss():
    d = FieldGeometryDiagram(460, 235, "Líneas cerradas de campo magnético de un imán y superficie cerrada de Gauss")
    mx, my, mw, mh = 145, 92, 160, 48
    d.raw(f'<rect class="csoft w" x="{mx}" y="{my}" width="{mw/2}" height="{mh}"/>', layer="wires")
    d.raw(f'<rect class="soft w" x="{mx+mw/2}" y="{my}" width="{mw/2}" height="{mh}"/>', layer="wires")
    d.text(mx + mw * 0.25, my + 29, "N", cls="tc")
    d.text(mx + mw * 0.75, my + 29, "S", cls="ta")

    # Internal lines S -> N near top and bottom of magnet bar (avoiding N / S letters)
    for dy in (-14, 14):
        yc = my + mh / 2 + dy
        d.raw(arrow(mx + mw - 12, yc, mx + 12, yc, line_cls="cd", head_cls="cf", head_len=6, head_w=3), layer="overlay")

    for sign in (-1, 1):
        y_edge = my + mh / 2 + sign * 14
        y_peak = my + mh / 2 + sign * 76
        path = (
            f"M {mx},{y_edge} C {mx-65},{y_edge} {mx-65},{y_peak} {mx+mw/2},{y_peak} "
            f"C {mx+mw+65},{y_peak} {mx+mw+65},{y_edge} {mx+mw},{y_edge}"
        )
        d.raw(f'<path class="c nofill" d="{path}"/>', layer="bg")
        d.raw(arrow(mx + mw / 2 - 12, y_peak, mx + mw / 2 + 14, y_peak, line_cls="c", head_cls="cf", head_len=6, head_w=3.2), layer="overlay")

    for sign in (-1, 1):
        y_edge = my + mh / 2 + sign * 7
        y_peak = my + mh / 2 + sign * 48
        path = (
            f"M {mx},{y_edge} C {mx-32},{y_edge} {mx-32},{y_peak} {mx+mw/2},{y_peak} "
            f"C {mx+mw+32},{y_peak} {mx+mw+32},{y_edge} {mx+mw},{y_edge}"
        )
        d.raw(f'<path class="c nofill" d="{path}"/>', layer="bg")

    d.raw('<ellipse class="ad nofill" cx="155" cy="116" rx="68" ry="64"/>', layer="overlay")
    d.text(84, 56, "S (cerrada)", cls="ta", anchor="end")
    d.text(392, 42, "B⃗", cls="sc")
    d.text(230, 218, "Toda línea que entra a S también sale: ∮ B⃗ · dA = 0", cls="t")
    return d


def orbita_helice():
    d = FieldGeometryDiagram(480, 240, "Movimiento circular y helicoidal de una carga en campo magnético uniforme")
    d.field_region(20, 36, 220, 206, step=34, direction="in")
    d.text(216, 24, "B⃗ ⊗", cls="sc", anchor="end")
    cx, cy, r = 115, 118, 56
    d.raw(f'<circle class="ad nofill" cx="{cx}" cy="{cy}" r="{r}"/>', layer="bg")
    d.node("_c", cx, cy, draw_dot=True)
    d.radius_dim((cx, cy), -40, r, text="R")
    px, py = cx, cy + r
    d.point_charge((px, py), sign="+", r=7, text="+q", label_dir="bottom")
    d.current_arrow((px + 7, py), (px + 48, py), text="v⃗", cls="a", label_side="bottom", offset=14)
    d.current_arrow((px, py - 7), (px, py - 42), text="F⃗", cls="c", label_side="left", offset=10)
    d.arc_wire((cx, cy), r, -15, 30, cls="ad", current_dir="ccw", current_cls="a", arrow_offset_r=0, arrow_span_deg=35)
    d.text(115, 228, "Circular (v⃗ ⊥ B⃗): giro antihorario (+q)", cls="t")

    hx0 = 268
    d.current_arrow((hx0, 128), (464, 128), cls="c")
    d.text(464, 118, "B⃗", cls="sc", anchor="end")
    pts = []
    steps = 120
    for i in range(steps + 1):
        t = i / steps * 2.3 * 2 * math.pi
        px_h = hx0 + 22 + (i / steps) * 160
        py_h = 128 - 40 * math.sin(t)
        pts.append((round(px_h, 1), round(py_h, 1)))
    d.wire(*pts, cls="a")
    sx, sy = pts[0]
    d.point_charge((sx, sy), sign="+", r=6)
    d.current_arrow((sx, sy), (sx + 32, sy - 38), cls="a")
    d.text(sx + 20, sy - 44, "v⃗", cls="sa", anchor="start")
    d.current_arrow((sx, sy), (sx + 32, sy), cls="m")
    d.text(sx + 24, sy + 16, "v∥", cls="s")
    d.current_arrow((sx, sy), (sx, sy - 38), cls="m")
    d.text(sx - 8, sy - 20, "v⊥", cls="s", anchor="end")
    x_c1 = hx0 + 22 + (0.25 / 2.3) * 160
    x_c2 = hx0 + 22 + (1.25 / 2.3) * 160
    d.dimension((x_c1, 66), (x_c2, 66), text="p = v∥ T", label_side="top", label_offset=10)
    d.text(366, 228, "Helicoidal (v∥ ≠ 0): avance p por vuelta", cls="t")
    return d


def espectrometro():
    d = FieldGeometryDiagram(480, 260, "Selector de velocidades y espectrómetro de masas")
    d.velocity_selector_spectrometer(60, 130, plate_len=130, plate_gap=70, chamber_w=175, r_orbit=62, q_sign="+")
    d.text(125, 194, "E⃗", cls="sc")
    d.text(448, 36, "B⃗₀ ⊗", cls="sc", anchor="end")
    d.text(46, 114, "B⃗ ⊗", cls="sc", anchor="start")
    d.text(125, 248, "Selector: v = E/B", cls="t")
    d.text(310, 248, "Cámara: d = 2R = 2mv/(|q|B₀)", cls="t")
    return d


def conductor_curvo():
    d = FieldGeometryDiagram(470, 235, "Fuerza sobre un alambre curvo y sobre una espira cerrada en campo uniforme")
    d.field_region(24, 42, 446, 196, step=38, direction="in")
    d.text(446, 24, "B⃗ ⊗ (uniforme)", cls="sc", anchor="end")

    pa, pb = (48, 168), (185, 72)
    d.raw(f'<path class="wk" d="M {pa[0]},{pa[1]} C 65,72 130,178 {pb[0]},{pb[1]}"/>', layer="wires")
    d.node("a", pa[0], pa[1], text="a", label_dir="bottom")
    d.node("b", pb[0], pb[1], text="b", label_dir="top")
    d.current_arrow((92, 118), (118, 123), text="dℓ⃗", cls="a", label_side="top", offset=10)
    d.current_arrow(pa, pb, cls="c")
    d.text(134, 136, "L⃗'", cls="sc")
    d.text(118, 222, "Abierto: F⃗ = I L⃗' × B⃗", cls="t")

    d.raw(
        '<path class="wk" d="M 285,124 C 285,62 385,58 405,110 C 425,162 320,186 285,124 Z"/>',
        layer="wires",
    )
    d.current_arrow((328, 72), (362, 74), text="I", cls="a", label_side="top", offset=10)
    d.text(348, 126, "∮ dℓ⃗ = 0", cls="s")
    d.text(350, 222, "Cerrado: F⃗ = 0  (puede haber torque)", cls="t")
    return d


def torque_espira():
    d = FieldGeometryDiagram(440, 240, "Vista lateral de una espira inclinada en campo magnético uniforme y torque resultante")
    cx, cy = 195, 114
    length = 124
    tilt = 32  # angle with vertical; angle between mu (normal) and B (vertical down) is phi = 90 - tilt = 58
    d.line((cx, cy - 76), (cx, cy + 78), cls="md")
    p_top = d._polar_svg(cx, cy, length / 2.0, 90 - tilt)
    p_bot = d._polar_svg(cx, cy, length / 2.0, 270 - tilt)
    d.line(p_top, p_bot, cls="wk")
    d.wire_z(p_top, direction="in", cls="a", r=7)
    d.wire_z(p_bot, direction="out", cls="a", r=7)
    # Normal mu perpendicular to loop, pointing down-right at -tilt deg
    mu_end = d._polar_svg(cx, cy, 56, -tilt)
    d.current_arrow((cx, cy), mu_end, text="μ⃗", cls="c", label_side="top", offset=10)
    # Angle phi between B (downward 270 deg) and mu (-tilt = 328 deg)
    d.angle_arc((cx, cy), 270, 360 - tilt, r=32, text="φ")
    # Forces on top and bottom wires: I out x B down = right; I in x B down = left
    d.current_arrow(p_bot, (p_bot[0] + 46, p_bot[1]), text="F⃗", cls="a", label_side="bottom", offset=14)
    d.current_arrow(p_top, (p_top[0] - 46, p_top[1]), text="−F⃗", cls="a", label_side="top", offset=10)
    d.text(p_top[0] - 46, p_top[1] + 22, "brazo (b/2) sen φ", cls="t", anchor="end")
    # Uniform B vertical downward on right
    d.current_arrow((335, 62), (335, 158), text="B⃗", cls="c", label_side="right", offset=10)
    d.text(220, 224, "Par de fuerzas: τ = μB sen φ  (φ ángulo entre μ⃗ y B⃗)", cls="t")
    return d


def alambre_espira():
    d = FieldGeometryDiagram(470, 265, "Alambre infinito con corriente I₁ y espira rectangular coplanar con corriente I₂")
    wy = 205
    d.line((25, wy), (445, wy), cls="wk")
    d.current_arrow((50, wy - 14), (120, wy - 14), text="I₁", cls="a", label_side="top", offset=8)
    d.text(36, wy + 18, "y = 0", cls="t", anchor="start")

    d.field_region(40, 48, 435, wy - 30, step=44, direction="out")
    _vec_sub(d, 404, 26, "B", "1", cls="sc", anchor="start")
    d.text(434, 24, "⊙", cls="sc", anchor="start")

    x0, x1 = 155, 315
    ybot, ytop = wy - 56, wy - 146
    d.wire((x0, ytop), (x1, ytop), (x1, ybot), (x0, ybot), (x0, ytop))
    d.current_arrow((215, ytop), (255, ytop), text="I₂", cls="a", label_side="top", offset=8)
    d.current_arrow((x1, (ytop + ybot) / 2 - 14), (x1, (ytop + ybot) / 2 + 16), cls="a")
    d.current_arrow((255, ybot), (215, ybot), cls="a")
    d.current_arrow((x0, (ytop + ybot) / 2 + 16), (x0, (ytop + ybot) / 2 - 14), cls="a")

    d.current_arrow((235, ybot), (235, ybot - 34), cls="c")
    _vec_sub(d, 244, ybot - 22, "F", "inf", cls="sc", anchor="start")
    d.current_arrow((235, ytop), (235, ytop + 22), cls="c")
    _vec_sub(d, 244, ytop + 22, "F", "sup", cls="sc", anchor="start")

    d.current_arrow((x0, (ytop + ybot) / 2), (x0 - 26, (ytop + ybot) / 2), cls="m")
    d.current_arrow((x1, (ytop + ybot) / 2), (x1 + 26, (ytop + ybot) / 2), cls="m")

    d.dimension((x0, wy + 18), (x1, wy + 18), text="a", label_side="bottom", label_offset=10)
    d.dimension((x1 + 42, wy), (x1 + 42, ybot), text="h", label_side="right", label_offset=8)
    d.dimension((x1 + 42, ybot), (x1 + 42, ytop), text="b", label_side="right", label_offset=8)
    return d


def ejemplo_lorentz():
    d = FieldGeometryDiagram(440, 230, "Protón con velocidad v⃗ en el eje x y campo magnético B⃗ a 30° en el plano xy")
    ox, oy = 140, 145
    d.axes_2d((ox, oy), x_len=190, y_len=115, x_label="x", y_label="y", neg_x=45, neg_y=40)
    d.point_charge((ox, oy), sign="+", r=7)
    d.text(ox - 12, oy + 22, "+e", cls="s", anchor="end")
    d.current_arrow((ox + 8, oy), (ox + 128, oy), text="v⃗", cls="a", label_side="bottom", offset=16)
    b_tip = d._polar_svg(ox, oy, 115, 30)
    d.current_arrow((ox, oy), b_tip, text="B⃗", cls="c", label_side="top", offset=10)
    d.angle_arc((ox, oy), 0, 30, r=52, text="30°")
    d.wire_z((ox - 42, oy - 48), direction="out", text="F⃗ (+ẑ)", cls="c", r=9)
    d.text(355, 70, "ẑ sale de la hoja", cls="t")
    return d


def semicirculo():
    d = FieldGeometryDiagram(440, 240, "Espira semicircular cerrada en un campo magnético uniforme hacia +y")
    cx, cy, r = 210, 160, 84
    d.axes_2d((cx, cy), x_len=150, y_len=128, x_label="x", y_label="y", neg_x=140, neg_y=35)
    d.line((cx - r, cy), (cx + r, cy), cls="wk")
    d.current_arrow((cx - 35, cy), (cx + 35, cy), text="I", cls="a", label_side="bottom", offset=14)
    d.arc_wire((cx, cy), r, 0, 180, cls="wk", current_dir="ccw", current_cls="a", current_label="I", arrow_offset_r=12)
    d.radius_dim((cx, cy), 135, r, text="R")
    for bx in (70, 355):
        d.current_arrow((bx, 190), (bx, 60), text="B⃗", cls="c", label_side="right", offset=10)
    d.wire_z((cx + 16, cy + 28), direction="out", cls="c", r=8)
    _vec_sub(d, cx + 30, cy + 32, "F", "1", cls="sc", anchor="start")
    d.text(cx + 50, cy + 32, "(+ẑ)", cls="sc", anchor="start")
    d.wire_z((cx + 42, cy - r - 30), direction="in", cls="a", r=8)
    _vec_sub(d, cx + 56, cy - r - 26, "F", "2", cls="sa", anchor="start")
    d.text(cx + 76, cy - r - 26, "(−ẑ)", cls="sa", anchor="start")
    return d


def espira_pivotada():
    d = FieldGeometryDiagram(440, 255, "Espira cuadrada pivotada en el eje AA' en equilibrio bajo gravedad y campo vertical")
    ox, oy = 185, 52
    L = 138
    theta = 28
    d.line((ox, oy), (ox, oy + L + 35), cls="md")
    d.axes_2d((55, 206), x_len=48, y_len=48, x_label="x (î)", y_label="y (ĵ)")
    d.wire_z((55, 206), direction="out", cls="w", r=5)
    d.text(44, 228, "ẑ ⊙", cls="s", anchor="end")

    bot = d._polar_svg(ox, oy, L, 270 + theta)
    mid = ((ox + bot[0]) / 2, (oy + bot[1]) / 2)
    p_mu = (ox + 0.68 * (bot[0] - ox), oy + 0.68 * (bot[1] - oy))
    d.line((ox, oy), bot, cls="wk")
    d.wire_z((ox, oy), direction="in", cls="a", r=7)
    d.text(ox - 12, oy + 4, "AA' (⊗)", cls="ta", anchor="end")
    d.wire_z(bot, direction="out", cls="a", r=7)
    d.text(bot[0] - 12, bot[1] + 20, "lado inf. (⊙)", cls="ta", anchor="end")
    d.angle_arc((ox, oy), 270, 270 + theta, r=42, text="θ")

    d.current_arrow(mid, (mid[0], mid[1] + 54), cls="m")
    d.text(mid[0], mid[1] + 68, "Mg", cls="t", anchor="middle")
    d.current_arrow(bot, (bot[0] + 64, bot[1]), cls="c")
    _vec_sub(d, bot[0] + 18, bot[1] + 20, "F", "inf", cls="sc", anchor="start")
    mu_end = d._polar_svg(p_mu[0], p_mu[1], 44, 180 + theta)
    d.current_arrow(p_mu, mu_end, cls="c")
    d.text(mu_end[0] - 8, mu_end[1] + 2, "μ⃗", cls="sc", anchor="end")

    d.current_arrow((360, 58), (360, 152), text="B⃗", cls="c", label_side="right", offset=10)
    d.current_arrow((405, 58), (405, 128), text="g⃗", cls="m", label_side="right", offset=8)
    return d


def ex_2025_1_p2():
    d = FieldGeometryDiagram(450, 240, "Partículas que describen una semicircunferencia antihoraria en campo B saliente")
    d.field_region(125, 44, 420, 206, step=34, direction="out")
    d.line((110, 24), (110, 214), cls="wk")
    d.text(416, 24, "B⃗ ⊙", cls="sc", anchor="end")
    r = 58
    cy = 118
    d.point_charge((72, cy + r), sign="-", r=6, text="q", label_dir="bottom")
    d.current_arrow((35, cy + r), (110, cy + r), text="v⃗", cls="a", label_side="top", offset=10)
    d.arc_wire((110, cy), r, -90, 90, cls="ad", current_dir="ccw", current_cls="a", arrow_offset_r=0, arrow_span_deg=45)
    d.node("_hit", 110, cy - r, draw_dot=True)
    d.radius_dim((110, cy), 35, r, text="r")
    d.dimension((88, cy + r), (88, cy - r), text="d = 2r", label_side="left", label_offset=8)
    d.text(280, 226, "Trayectoria antihoraria con B⃗ ⊙ ⇒ q < 0", cls="t")
    return d


def ex_2018_2_p3():
    d = FieldGeometryDiagram(460, 235, "Selector de velocidades con placas horizontales separadas una distancia d")
    px, py, plen, gap = 115, 65, 225, 100
    d.raw(f'<rect class="csoft w" x="{px}" y="{py-8}" width="{plen}" height="8"/>', layer="wires")
    d.raw(f'<rect class="soft w" x="{px}" y="{py+gap}" width="{plen}" height="8"/>', layer="wires")
    d.text(px + plen / 2, py - 14, "+σ  (+ + + + +)", cls="tc")
    d.text(px + plen / 2, py + gap + 22, "−σ  (− − − − −)", cls="ta")
    d.field_region(px + 15, py + 14, px + plen - 15, py + gap - 14, step=38, direction="in")
    d.text(px + plen + 28, py + 24, "B⃗ (ŷ ⊗)", cls="sc", anchor="start")
    for ex in (px + 65, px + 165):
        d.current_arrow((ex, py + 10), (ex, py + gap - 10), cls="c")
    d.text(px + 146, py + gap * 0.42, "E⃗ (−ẑ)", cls="sc", anchor="end")
    ymid = py + gap / 2
    d.point_charge((42, ymid), sign="+", r=7, text="+q, m", label_dir="bottom")
    d.current_arrow((50, ymid), (112, ymid), text="v⃗₀", cls="a", label_side="top", offset=10)
    d.line((112, ymid), (px + plen + 10, ymid), cls="ad")
    d.dimension((px + plen + 14, py), (px + plen + 14, py + gap), text="d", label_side="right", label_offset=8)
    d.axes_2d((405, 195), x_len=36, y_len=36, x_label="x", y_label="z")
    return d


def placa_deflexion():
    d = FieldGeometryDiagram(450, 235, "Electrón deflectado entre dos placas en un campo magnético entrante")
    px, py, plen, gap = 105, 55, 220, 110
    d.line((px, py), (px + plen, py), cls="wk")
    d.line((px, py + gap), (px + plen, py + gap), cls="wk")
    d.field_region(px + 16, py + 16, px + plen - 16, py + gap - 16, step=36, direction="in")
    d.text(px + plen + 30, py + 24, "B⃗ ⊗", cls="sc", anchor="start")
    ymid = py + gap / 2
    d.point_charge((42, ymid), sign="-", r=7, text="e⁻", label_dir="bottom")
    d.current_arrow((50, ymid), (104, ymid), text="v⃗₀", cls="a", label_side="top", offset=10)
    d.raw(f'<path class="ad nofill" d="M {px},{ymid} Q {px + plen*0.55},{ymid + 5} {px + plen},{py + gap}"/>', layer="overlay")
    d.node("_hit", px + plen, py + gap, draw_dot=True)
    d.current_arrow((px + 30, ymid + 4), (px + 30, ymid + 36), text="F⃗", cls="c", label_side="left", offset=8)
    d.dimension((px, py + gap + 18), (px + plen, py + gap + 18), text="ℓ", label_side="bottom", label_offset=10)
    d.dimension((px + plen + 14, py), (px + plen + 14, py + gap), text="d", label_side="right", label_offset=8)
    return d


def barrera_campo():
    d = FieldGeometryDiagram(460, 240, "Tres regímenes de trayectoria al cruzar una zona de campo magnético de ancho L")
    x0, x1, y0, y1 = 140, 290, 25, 200
    d.raw(f'<rect class="soft nostroke" opacity="0.35" x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}"/>', layer="bg")
    d.field_region(x0 + 18, y0 + 16, x1 - 18, y1 - 16, step=36, direction="in")
    d.line((x0, y0), (x0, y1), cls="md")
    d.line((x1, y0), (x1, y1), cls="md")
    d.text(x1 + 10, y0 + 18, "B⃗ ⊗", cls="sc", anchor="start")

    ye = 168
    d.point_charge((50, ye), sign="+", r=7, text="+q", label_dir="bottom")
    d.current_arrow((58, ye), (138, ye), text="v⃗", cls="a", label_side="top", offset=10)
    r1 = 44
    d.arc_wire((x0, ye - r1), r1, -90, 90, cls="c")
    d.current_arrow((x0, ye - 2 * r1), (x0 - 38, ye - 2 * r1), cls="c")
    _vc_label(d, x0 + r1 + 8, ye - r1, "<", cls="tc", anchor="start")
    d.raw(f'<path class="ad nofill" d="M {x0},{ye} A 132 132 0 0 0 {x1},{ye-125}"/>', layer="overlay")
    _vc_label(d, x1 - 54, ye - 116, "=", cls="ta", anchor="start")
    d.raw(f'<path class="a nofill" d="M {x0},{ye} A 230 230 0 0 0 {x1},{ye-54}"/>', layer="overlay")
    d.current_arrow((x1, ye - 54), (x1 + 52, ye - 92), cls="a")
    _vc_label(d, x1 + 56, ye - 92, ">", cls="ta", anchor="start")
    d.dimension((x0, y1 + 14), (x1, y1 + 14), text="L", label_side="bottom", label_offset=10)
    return d


def figures():
    return {
        "u07-lorentz-mano": lorentz_mano(),
        "u07-lineas-gauss": lineas_gauss(),
        "u07-orbita-helice": orbita_helice(),
        "u07-espectrometro": espectrometro(),
        "u07-conductor-curvo": conductor_curvo(),
        "u07-torque-espira": torque_espira(),
        "u07-alambre-espira": alambre_espira(),
        "u07-ejemplo-lorentz": ejemplo_lorentz(),
        "u07-semicirculo": semicirculo(),
        "u07-espira-pivotada": espira_pivotada(),
        "u07-ex-2025-1-p2": ex_2025_1_p2(),
        "u07-ex-2018-2-p3": ex_2018_2_p3(),
        "u07-placa-deflexion": placa_deflexion(),
        "u07-barrera-campo": barrera_campo(),
    }
