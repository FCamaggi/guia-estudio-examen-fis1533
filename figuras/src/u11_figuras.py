"""U11 Alternating current and electromagnetic waves figures.
Generate with: python3 scripts/build_figures.py u11
"""

import math
from svg_primitives import FieldGeometryDiagram, arrow


def _sub_label(d, x: float, y: float, base: str, sub: str, cls: str = "s", anchor: str = "middle"):
    """Draw a serif/body label with a clean tspan subscript (avoids Unicode tofu for letters)."""
    d.raw(
        f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}">'
        f'{base}<tspan class="sb" dy="3.5">{sub}</tspan></text>',
        layer="labels",
    )


def _hat_sub_label(d, x: float, y: float, base: str, sub: str = "", cls: str = "s", anchor: str = "middle"):
    """Draw a phasor symbol with circumflex hat (e.g. V̂, Î) and optional subscript."""
    hat = base + "\u0302"
    if sub:
        _sub_label(d, x, y, hat, sub, cls=cls, anchor=anchor)
    else:
        d.text(x, y, hat, cls=cls, anchor=anchor)


def fasores_rlc():
    d = FieldGeometryDiagram(470, 238, "Diagramas fasoriales de R, L, C individuales y circuito RLC en serie")
    # Left: individual elements relative to I_hat along +Re
    c1 = (112, 118)
    d.axes_2d(c1, x_len=92, y_len=82, x_label="Re", y_label="Im", neg_x=52, neg_y=76)
    d.current_arrow(c1, (c1[0] + 74, c1[1]), text="", cls="a")
    _hat_sub_label(d, c1[0] + 76, c1[1] - 10, "I", cls="sa", anchor="start")
    d.current_arrow((c1[0], c1[1] + 1), (c1[0] + 44, c1[1] + 1), text="", cls="w")
    _hat_sub_label(d, c1[0] + 34, c1[1] + 20, "V", "R", cls="s")
    d.current_arrow(c1, (c1[0], c1[1] - 66), text="", cls="c")
    _hat_sub_label(d, c1[0] - 12, c1[1] - 56, "V", "L", cls="sc", anchor="end")
    d.current_arrow(c1, (c1[0], c1[1] + 46), text="", cls="c")
    _hat_sub_label(d, c1[0] - 12, c1[1] + 44, "V", "C", cls="sc", anchor="end")
    d.text(112, 224, "Elementos: +90° (L), 0° (R), −90° (C)", cls="t")

    # Right: RLC series vector sum (inductive case XL > XC)
    c2 = (322, 118)
    d.axes_2d(c2, x_len=88, y_len=82, x_label="Re", y_label="Im", neg_x=38, neg_y=76)
    vr = 58.0
    vx = 48.0  # VL - VC > 0
    d.current_arrow(c2, (c2[0] + vr, c2[1]), text="", cls="a")
    _hat_sub_label(d, c2[0] + vr * 0.5, c2[1] + 20, "V", "R", cls="sa")
    d.current_arrow((c2[0] + vr, c2[1]), (c2[0] + vr, c2[1] - vx), text="", cls="c")
    _sub_label(d, c2[0] + vr + 8, c2[1] - vx * 0.55 + 4, "V", "L", cls="sc", anchor="start")
    d.text(c2[0] + vr + 24, c2[1] - vx * 0.55 + 4, "−", cls="sc", anchor="start")
    _sub_label(d, c2[0] + vr + 37, c2[1] - vx * 0.55 + 4, "V", "C", cls="sc", anchor="start")
    d.current_arrow(c2, (c2[0] + vr, c2[1] - vx), text="", cls="w")
    _hat_sub_label(d, c2[0] + vr * 0.42, c2[1] - vx * 0.68, "V", cls="s", anchor="end")
    d.angle_arc(c2, 0, math.degrees(math.atan2(vx, vr)), r=28, text="φ")
    d.text(335, 224, "Suma fasorial (caso X_L > X_C)".replace("_L", "L").replace("_C", "C"), cls="t")
    return d


def circuito_rlc():
    d = FieldGeometryDiagram(460, 220, "Circuito RLC en serie alimentado por una fuente sinusoidal")
    d.node("bl", 105, 165, draw_dot=False)
    d.node("tl", 105, 52, draw_dot=False)
    d.node("tm", 235, 52, draw_dot=False)
    d.node("tr", 390, 52, draw_dot=False)
    d.node("br", 390, 165, draw_dot=False)
    d.ac_source("bl", "tl", text="", label_side="left")
    d.text(80, 106, "V(t)", cls="s", anchor="end")
    d.text(80, 124, "V₀ cos ωt", cls="t", anchor="end")
    d.resistor("tl", "tm", text="R", label_side="top", offset=18)
    d.inductor("tm", "tr", turns=4, r_coil=7, text="L", label_side="top", offset=18)
    d.capacitor("tr", "br", text="C", label_side="right", offset=20)
    d.wire("br", "bl")
    d.current_arrow((160, 182), (230, 182), text="i(t)", cls="a", label_side="bottom", offset=16)
    return d


def resonancia():
    d = FieldGeometryDiagram(460, 238, "Curva de resonancia de la amplitud de corriente frente a la frecuencia angular")
    def amp(w, Q):
        return Q / math.sqrt(1.0 + (Q * (w - 1.0 / w)) ** 2)

    pts_sharp = [(0.18 + 2.02 * k / 120, amp(0.18 + 2.02 * k / 120, 4.0) / 4.0) for k in range(121)]
    pts_wide = [(0.18 + 2.02 * k / 120, amp(0.18 + 2.02 * k / 120, 1.4) / 4.0) for k in range(121)]

    x0, y0, w, h = 78, 34, 330, 155
    d.function_plot(
        x0, y0, w, h, (0, 2.3), (0, 1.12), [pts_sharp],
        v_lines=[(1.0, "")],
        h_lines=[(1.0, ""), (0.35, "")],
        x_label="ω", y_label="I₀(ω)", cls="a",
    )
    px = lambda vx: x0 + vx / 2.3 * w
    py = lambda vy: y0 + h - vy / 1.12 * h
    pts_w_svg = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts_wide)
    d.raw(f'<polyline class="c" points="{pts_w_svg}"/>', layer="overlay")

    _sub_label(d, px(1.0) - 18, y0 + h + 18, "ω", "0", cls="s", anchor="end")
    d.text(px(1.0) - 14, y0 + h + 18, "= 1/√(LC)", cls="t", anchor="start")
    _sub_label(d, 70, py(1.0) + 4, "V₀/R", "1", cls="sa", anchor="end")
    _sub_label(d, 70, py(0.35) + 4, "V₀/R", "2", cls="sc", anchor="end")
    _sub_label(d, px(1.26), py(0.76), "R", "1", cls="sa", anchor="start")
    d.text(px(1.26) + 18, py(0.76), "pequeña", cls="ta", anchor="start")
    _sub_label(d, px(1.55), py(0.44), "R", "2", cls="sc", anchor="start")
    d.text(px(1.55) + 18, py(0.44), "> R₁", cls="tc", anchor="start")
    return d


def potencia_ca():
    d = FieldGeometryDiagram(470, 240, "Voltaje, corriente desfasada y potencia instantánea en un ciclo")
    phi = math.pi / 3.0  # 60 deg lag
    xs = [2.0 * math.pi * k / 120.0 for k in range(121)]
    pts_v = [(x, 0.92 * math.cos(x)) for x in xs]
    pts_i = [(x, 0.68 * math.cos(x - phi)) for x in xs]
    pts_p = [(x, 0.92 * 0.68 * math.cos(x) * math.cos(x - phi)) for x in xs]
    p_avg = 0.5 * 0.92 * 0.68 * math.cos(phi)

    x0, y0, w, h = 52, 34, 358, 168
    px = lambda vx: x0 + vx / (2.0 * math.pi) * w
    py = lambda vy: y0 + h - (vy + 1.05) / 2.1 * h
    y_zero = py(0.0)

    # Vertical axis and horizontal zero axis
    d.raw(arrow(x0, y_zero, x0 + w + 14, y_zero, line_cls="w", head_cls="inkf", head_len=6, head_w=3), layer="wires")
    d.raw(arrow(x0, y0 + h, x0, y0 - 14, line_cls="w", head_cls="inkf", head_len=6, head_w=3), layer="wires")
    d.text(x0 + w + 18, y_zero + 4, "ωt", cls="s", anchor="start")

    # Guides for T and <P>
    d.line((px(2.0 * math.pi), y0), (px(2.0 * math.pi), y0 + h), cls="md")
    d.text(px(2.0 * math.pi), y_zero + 18, "T", cls="s")
    d.line((x0, py(p_avg)), (x0 + w, py(p_avg)), cls="md")
    d.text(x0 + w + 8, py(p_avg) + 4, "⟨P⟩", cls="tb", anchor="start")

    # Curves
    d.raw(f'<polyline class="a" points="{" ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts_v)}"/>', layer="overlay")
    d.raw(f'<polyline class="c" points="{" ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts_i)}"/>', layer="overlay")
    d.raw(f'<polyline class="w" points="{" ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts_p)}"/>', layer="overlay")

    # Top legend (clear of curves)
    d.line((90, 16), (112, 16), cls="a")
    d.text(118, 20, "v(t)", cls="sa", anchor="start")
    d.line((185, 16), (207, 16), cls="c")
    d.text(213, 20, "i(t)", cls="sc", anchor="start")
    d.line((280, 16), (302, 16), cls="w")
    d.text(308, 20, "p(t) = v(t)i(t)", cls="s", anchor="start")
    return d


def onda_em():
    d = FieldGeometryDiagram(470, 275, "Onda electromagnética plana linealmente polarizada en el vacío")
    ox, oy = 76, 150
    ux_x, ux_y = 0.0, -1.0
    uy_x, uy_y = -0.72, 0.58
    uz_x, uz_y = 1.0, 0.0

    # 3D right-handed axes
    d.raw(arrow(ox, oy, ox, oy - 115, line_cls="m", head_cls="mf", head_len=6, head_w=3), layer="wires")
    d.raw(arrow(ox, oy, ox + 100 * uy_x, oy + 100 * uy_y, line_cls="m", head_cls="mf", head_len=6, head_w=3), layer="wires")
    d.raw(arrow(ox, oy, ox + 355, oy, line_cls="m", head_cls="mf", head_len=6, head_w=3), layer="wires")
    d.text(ox, oy - 124, "x", cls="s")
    d.text(ox + 100 * uy_x - 10, oy + 100 * uy_y + 10, "y", cls="s")
    d.text(ox + 365, oy + 4, "z", cls="s", anchor="start")

    z_len = 310.0
    lam = 180.0
    amp_e = 72.0
    amp_b = 58.0

    for k in range(1, 25):
        z = k * (z_len / 25.0)
        s = math.sin(2.0 * math.pi * z / lam)
        if abs(s) > 0.16:
            ex = ox + z * uz_x + amp_e * s * ux_x
            ey = oy + z * uz_y + amp_e * s * ux_y
            d.raw(arrow(ox + z, oy, ex, ey, line_cls="a", head_cls="af", head_len=5.5, head_w=2.6), layer="bg")
            bx = ox + z * uz_x + amp_b * s * uy_x
            by = oy + z * uz_y + amp_b * s * uy_y
            d.raw(arrow(ox + z, oy, bx, by, line_cls="c", head_cls="cf", head_len=5.5, head_w=2.6), layer="bg")

    e_pts, b_pts = [], []
    for k in range(0, 141):
        z = z_len * k / 140.0
        s = math.sin(2.0 * math.pi * z / lam)
        e_pts.append(f"{ox + z * uz_x + amp_e * s * ux_x:.1f},{oy + z * uz_y + amp_e * s * ux_y:.1f}")
        b_pts.append(f"{ox + z * uz_x + amp_b * s * uy_x:.1f},{oy + z * uz_y + amp_b * s * uy_y:.1f}")
    d.raw(f'<polyline class="a" points="{" ".join(e_pts)}"/>', layer="overlay")
    d.raw(f'<polyline class="c" points="{" ".join(b_pts)}"/>', layer="overlay")

    z_c1, z_c2 = lam * 0.25, lam * 1.25
    y_dim = oy - amp_e - 22
    d.line((ox + z_c1, oy - amp_e - 4), (ox + z_c1, y_dim - 4), cls="md")
    d.line((ox + z_c2, oy - amp_e - 4), (ox + z_c2, y_dim - 4), cls="md")
    d.dimension((ox + z_c1, y_dim), (ox + z_c2, y_dim), text="λ", label_side="top", label_offset=8)

    d.current_arrow((ox + 260, oy - 96), (ox + 335, oy - 96), text="c, k⃗", cls="w", label_side="top", offset=8)
    d.text(ox + z_c1 - 14, oy - amp_e + 12, "E⃗", cls="sa", anchor="end")
    d.text(ox + z_c1 + amp_b * uy_x - 10, oy + amp_b * uy_y + 16, "B⃗", cls="sc", anchor="end")

    # Bottom summary using serif classes for vectors
    d.text(132, 260, "E⃗", cls="sa")
    d.text(146, 260, "⊥", cls="s")
    d.text(160, 260, "B⃗", cls="sc")
    d.text(174, 260, "⊥", cls="s")
    d.text(188, 260, "k⃗", cls="s")
    d.text(196, 260, ",  en fase,   B₀ = E₀ / c", cls="t", anchor="start")
    return d


def polarizacion():
    d = FieldGeometryDiagram(470, 225, "Polarización lineal y polarización circular en el plano transversal xy")
    # Left: Linear polarization in xy plane (tilted angle theta)
    c1 = (115, 112)
    d.axes_2d(c1, x_len=84, y_len=80, x_label="x", y_label="y", neg_x=70, neg_y=70)
    ang = math.radians(35)
    r_lin = 62.0
    p_pos = (c1[0] + r_lin * math.cos(ang), c1[1] - r_lin * math.sin(ang))
    p_neg = (c1[0] - r_lin * math.cos(ang), c1[1] + r_lin * math.sin(ang))
    d.line(p_neg, p_pos, cls="ad")
    d.current_arrow(c1, p_pos, text="E⃗", cls="a", label_side="top", offset=10)
    d.angle_arc(c1, 0, 35, r=28, text="θ")
    d.text(c1[0], 208, "Lineal: dirección fija n̂", cls="t")

    # Right: Circular polarization (E rotates on circle of radius E0 in xy plane)
    c2 = (348, 112)
    d.axes_2d(c2, x_len=84, y_len=80, x_label="x", y_label="y", neg_x=70, neg_y=70)
    r_circ = 56.0
    d.raw(f'<circle class="ad nofill" cx="{c2[0]:g}" cy="{c2[1]:g}" r="{r_circ:g}"/>', layer="bg")
    d.arc_wire(c2, r_circ, 25, 80, cls="ad", current_dir="ccw", current_cls="a", arrow_offset_r=10, arrow_span_deg=34)
    tip = (c2[0] + r_circ * math.cos(math.radians(48)), c2[1] - r_circ * math.sin(math.radians(48)))
    d.current_arrow(c2, tip, text="", cls="a")
    d.text(tip[0] + 18, tip[1] - 12, "E⃗(t)", cls="sa", anchor="start")
    d.text(c2[0] - r_circ - 8, c2[1] + 16, "E₀", cls="s", anchor="end")
    d.text(c2[0], 208, "Circular: amplitud E₀ gira con ω", cls="t")
    return d


def poynting_receptor():
    d = FieldGeometryDiagram(460, 235, "Onda plana incidiendo sobre un receptor cuadrado perpendicular a z")
    ox, oy = 90, 125
    # Wave propagation axis +z stops cleanly before receiver
    d.raw(arrow(40, oy, 304, oy, line_cls="m", head_cls="mf", head_len=6, head_w=3), layer="bg")

    # Triad E (+x up), B (+y oblique down-left), S (+z right)
    d.current_arrow((ox, oy), (ox, oy - 70), text="E⃗", cls="a", label_side="left", offset=10)
    d.current_arrow((ox, oy), (ox - 46, oy + 36), text="", cls="c")
    d.text(ox - 54, oy + 52, "B⃗", cls="sc", anchor="end")
    d.current_arrow((ox, oy), (ox + 80, oy), text="S⃗", cls="w", label_side="bottom", offset=16)

    for dy in (-36, 36):
        d.raw(arrow(195, oy + dy, 285, oy + dy, line_cls="ad", head_cls="af", head_len=6, head_w=3), layer="bg")

    rx, ry = 338, oy
    dx, dy = 24, -18
    h = 56
    p1 = (rx - dx, ry + h - dy)
    p2 = (rx + dx, ry + h + dy)
    p3 = (rx + dx, ry - h + dy)
    p4 = (rx - dx, ry - h - dy)
    pts = f"{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]} {p4[0]},{p4[1]}"
    d.raw(f'<polygon class="soft w" points="{pts}"/>', layer="wires")
    d.text(rx, ry + 5, "A = a²", cls="s")
    d.current_arrow((rx + dx, ry), (rx + dx + 48, ry), text="n̂ = ẑ", cls="m", label_side="top", offset=10)
    d.text(rx + dx + 56, ry + 4, "z", cls="s", anchor="start")
    d.dimension((p1[0] - 12, p4[1]), (p1[0] - 12, p1[1]), text="a", label_side="left", label_offset=8)
    d.text(rx, 215, "Receptor perpendicular a ẑ", cls="t")
    return d


def arq1_2025_1_p5():
    d = FieldGeometryDiagram(460, 230, "Circuito AC serie del Examen 2025-1 P5 con dos R, dos L y C")
    d.node("bl", 102, 175, draw_dot=False)
    d.node("tl", 102, 50, draw_dot=False)
    d.node("tm", 232, 50, draw_dot=False)
    d.node("tr", 365, 50, draw_dot=False)
    d.node("br", 365, 175, draw_dot=False)
    d.node("bm", 232, 175, draw_dot=False)

    d.ac_source("bl", "tl", text="", label_side="left")
    d.text(78, 110, "V(t)", cls="s", anchor="end")
    d.text(78, 128, "V₀ cos ωt", cls="t", anchor="end")

    d.resistor("tl", "tm", text="R", label_side="top", offset=18)
    d.capacitor("tm", "tr", text="C", label_side="top", offset=18)
    d.inductor("tr", "br", turns=4, r_coil=6.5, text="L", label_side="left", offset=18)
    d.inductor("br", "bm", turns=4, r_coil=6.5, text="L", label_side="bottom", offset=20)
    d.resistor("bm", "bl", text="R", label_side="bottom", offset=20)

    d.node("va", 365, 62, draw_dot=True)
    d.node("vb", 365, 163, draw_dot=True)
    d.current_arrow((402, 152), (402, 72), text="", cls="a")
    _hat_sub_label(d, 415, 117, "V", "L", cls="sa", anchor="start")
    return d


def arq2_2025_2_p3():
    d = FieldGeometryDiagram(460, 230, "Circuito AC mixto R en paralelo con rama RLC del Examen 2025-2 P3")
    d.terminal_open("in_t", 75, 50, text="", label_dir="left")
    d.terminal_open("in_b", 75, 185, text="", label_dir="left")
    d.node("jt", 210, 50, draw_dot=True)
    d.node("jb", 210, 185, draw_dot=True)
    d.node("tr", 355, 50, draw_dot=False)
    d.node("m1", 355, 100, draw_dot=False)
    d.node("m2", 355, 145, draw_dot=False)
    d.node("br", 355, 185, draw_dot=False)

    d.wire("in_t", "jt")
    d.wire("in_b", "jb", "br")
    d.resistor("jt", "jb", text="R", label_side="left", offset=18)
    d.resistor("jt", "tr", text="R", label_side="top", offset=18)
    d.inductor("tr", "m1", turns=3, r_coil=5.5, text="L", label_side="right", offset=18)
    d.wire("m1", "m2")
    d.capacitor("m2", "br", text="C", label_side="right", offset=18)
    d.text(56, 120, "U(t)", cls="s", anchor="end")
    d.current_arrow((100, 34), (155, 34), text="I(t)", cls="a", label_side="top", offset=6)
    return d


def prac_mixto():
    d = FieldGeometryDiagram(460, 235, "Circuito mixto con R en serie con rama L-C₁ en paralelo con C₂")
    d.node("bl", 85, 185, draw_dot=False)
    d.node("tl", 85, 52, draw_dot=False)
    d.node("jt", 240, 52, draw_dot=True)
    d.node("jb", 240, 185, draw_dot=True)
    d.node("tr", 370, 52, draw_dot=False)
    d.node("br", 370, 185, draw_dot=False)
    d.node("jm", 240, 118, draw_dot=False)

    d.ac_source("bl", "tl", text="V(t)", label_side="left", offset=24)
    d.wire("tl", (135, 52))
    d.resistor((135, 52), "jt", text="R", label_side="top", offset=18)
    d.wire("bl", "jb", "br")
    d.wire("jt", "tr")

    d.inductor("jt", "jm", turns=3, r_coil=5.5, text="L", label_side="left", offset=18)
    d.capacitor("jm", "jb", text="", label_side="left", offset=18)
    _sub_label(d, 217, 155, "C", "1", cls="s", anchor="end")

    d.capacitor("tr", "br", text="", label_side="right", offset=20)
    _sub_label(d, 390, 122, "C", "2", cls="s", anchor="start")
    d.current_arrow((95, 34), (132, 34), text="I(t)", cls="a", label_side="top", offset=6)
    return d


def prac_dos_c():
    d = FieldGeometryDiagram(460, 225, "Circuito RLC serie con dos condensadores C₁ y C₂")
    d.node("bl", 75, 175, draw_dot=False)
    d.node("tl", 75, 50, draw_dot=False)
    d.node("tr", 365, 50, draw_dot=False)
    d.node("rm", 365, 112, draw_dot=False)
    d.node("br", 365, 175, draw_dot=False)

    d.ac_source("bl", "tl", text="V(t)", label_side="left", offset=24)
    d.resistor("tl", "tr", text="R", label_side="top", offset=18)
    d.capacitor("tr", "rm", text="", label_side="right")
    _sub_label(d, 386, 85, "C", "1", cls="s", anchor="start")
    d.inductor("rm", "br", turns=3, r_coil=5.5, text="L", label_side="right", offset=18)
    d.capacitor("br", "bl", text="", label_side="bottom")
    _sub_label(d, 220, 204, "C", "2", cls="s")
    d.current_arrow((115, 34), (165, 34), text="I(t)", cls="a", label_side="top", offset=6)
    return d


def prac_pasa_altos():
    d = FieldGeometryDiagram(440, 230, "Filtro RC pasa-altos: fuente Vin en serie con C; la salida Vout se toma sobre R")
    yt, yb = 50, 180
    d.node("s_t", 70, yt, draw_dot=False)
    d.node("s_b", 70, yb, draw_dot=False)
    d.ac_source("s_b", "s_t", text="Vᵢₙ", label_side="left", offset=26)
    d.capacitor("s_t", (260, yt), text="C", label_side="top", offset=20)
    d.node("n1", 260, yt, draw_dot=True)
    d.resistor("n1", (260, yb), text="R", label_side="left", offset=22)
    d.node("n2", 260, yb, draw_dot=True)
    d.wire("s_b", "n2")
    d.wire("n1", (350, yt))
    d.wire("n2", (350, yb))
    d.terminal_open("op", 350, yt, text="+", label_dir="right", offset=10)
    d.terminal_open("om", 350, yb, text="−", label_dir="right", offset=10)
    d.text(382, 120, "Vₒᵤₜ", cls="sa")
    d.current_arrow((84, yt - 16), (128, yt - 16), text="I", cls="a", label_side="top", offset=6)
    return d


def figures():
    return {
        "u11-fasores-rlc": fasores_rlc(),
        "u11-circuito-rlc": circuito_rlc(),
        "u11-resonancia": resonancia(),
        "u11-potencia-ca": potencia_ca(),
        "u11-onda-em": onda_em(),
        "u11-polarizacion": polarizacion(),
        "u11-poynting-receptor": poynting_receptor(),
        "u11-arq1-2025-1-p5": arq1_2025_1_p5(),
        "u11-arq2-2025-2-p3": arq2_2025_2_p3(),
        "u11-prac-mixto": prac_mixto(),
        "u11-prac-dos-c": prac_dos_c(),
            "u11-prac-pasa-altos": prac_pasa_altos(),
}
