"""U2 Gauss's law and conductors figures. Generate with: python3 scripts/build_figures.py u02"""

import math
from svg_primitives import FieldGeometryDiagram, arrow


def flujo_angulo():
    d = FieldGeometryDiagram(455, 240, "Superficie plana inclinada en un campo eléctrico uniforme: normal y ángulos")
    cx, cy = 215, 122
    for y in (36, 80, 164, 208):
        d.current_arrow((30, y), (405, y), cls="a")
    d.text(414, 32, "E⃗", cls="sa", anchor="start")
    a = d._polar_svg(cx, cy, 74, 120)
    b = d._polar_svg(cx, cy, 74, 300)
    d.line(a, b, cls="wk")
    d.text(a[0] - 10, a[1] + 4, "superficie (de canto)", cls="t", anchor="end")
    d.text(b[0] + 10, b[1] - 4, "área A", cls="t", anchor="start")
    d.line((cx, cy), (cx + 120, cy), cls="md")
    d.text(cx + 126, cy + 5, "dirección del campo", cls="t", anchor="start")
    tip = d._polar_svg(cx, cy, 86, 30)
    d.current_arrow((cx, cy), tip, cls="c")
    d.text(tip[0] + 8, tip[1] - 2, "n̂", cls="sc", anchor="start")
    d.angle_arc((cx, cy), 0, 30, r=48, text="φ")
    d.angle_arc((cx, cy), -60, 0, r=30, text="θ")
    return d


def cubo_flujo():
    d = FieldGeometryDiagram(480, 240, "Flujo eléctrico por simetría a través de las caras de un cubo")
    d.cube_3d((105, 118), size=84, center_charge="+q", highlight_face="right", show_axes=False)
    d.text(120, 198, "q en el centro", cls="tb")
    d.text(120, 218, "Φcara = q / (6ε₀)", cls="ta")

    d.cube_3d(
        (320, 118),
        size=84,
        vertex_charges=["", "", "", "+q", "", "", "", ""],
        highlight_face="right",
        show_axes=False,
    )
    d.text(335, 198, "q en un vértice", cls="tb")
    d.text(335, 218, "Φcara opuesta = q / (24ε₀)", cls="ta")
    return d


def gauss_superficie():
    d = FieldGeometryDiagram(470, 245, "Ley de Gauss: el flujo no depende de la forma de la superficie y las cargas externas aportan cero")
    cx, cy = 148, 126
    for k in range(8):
        deg = k * 45 + 22
        p_in = d._polar_svg(cx, cy, 13, deg)
        p_out = d._polar_svg(cx, cy, 102, deg)
        d.raw(arrow(p_in[0], p_in[1], p_out[0], p_out[1], line_cls="a", head_cls="af", head_len=6, head_w=3), layer="bg")
    d.point_charge((cx, cy), sign="+", r=9, text="+q", label_dir="right")
    d.raw(f'<circle class="ad nofill" cx="{cx}" cy="{cy}" r="54"/>', layer="overlay")
    d.text(cx + 42, cy - 46, "S₁", cls="sa", anchor="start")
    d.raw(
        '<path class="cd nofill" d="M 60,122 C 55,44 218,32 248,108 C 272,175 190,218 112,202 C 68,192 64,160 60,122 Z"/>',
        layer="overlay",
    )
    d.text(244, 184, "S₂", cls="sc", anchor="start")
    qx, qy = 358, 72
    d.point_charge((qx, qy), sign="+", r=8, text="q₀ (ext)", label_dir="top")
    # Field line from q0 piercing S2 (in at top-right, out at top-left)
    d.raw(arrow(qx - 10, qy + 2, 236, 78, line_cls="m", head_cls="mf", head_len=6, head_w=3), layer="bg")
    d.line((236, 78), (94, 86), cls="md")
    d.raw(arrow(94, 86, 42, 89, line_cls="m", head_cls="mf", head_len=6, head_w=3), layer="bg")
    d.text(365, 146, "línea de q₀ entra y sale de S₂:", cls="t")
    d.text(365, 165, "flujo neto de q₀ = 0", cls="t")
    return d


def esfera_gauss():
    d = FieldGeometryDiagram(480, 250, "Simetría esférica: esfera sólida de radio R y superficies gaussianas interior y exterior")
    cx, cy = 148, 128
    d.concentric_system(
        (cx, cy),
        shells=[{"r_out": 68, "fill": "csoft", "stroke": "w"}],
        gaussian_radii=[
            {"r": 36, "cls": "ad"},
            {"r": 100, "cls": "ad"},
        ],
    )
    rp = d._polar_svg(cx, cy, 68, -40)
    d.line((cx, cy), rp, cls="m")
    d.text(cx + 36, cy + 44, "R", cls="s")
    d.text(cx - 24, cy + 28, "ρ(r)", cls="sc")
    p_r1 = d._polar_svg(cx, cy, 48, 138)
    d.text(p_r1[0], p_r1[1], "r₁", cls="sa")
    p_r2 = d._polar_svg(cx, cy, 114, 52)
    d.text(p_r2[0], p_r2[1], "r₂", cls="sa")
    p_surf = d._polar_svg(cx, cy, 100, 15)
    p_end = d._polar_svg(cx, cy, 140, 15)
    d.current_arrow(p_surf, p_end, text="E⃗", cls="a", label_side="top", offset=10)
    p_da0 = d._polar_svg(cx, cy, 100, -10)
    p_da = d._polar_svg(cx, cy, 128, -10)
    d.current_arrow(p_da0, p_da, text="dA⃗", cls="c", label_side="bottom", offset=12)
    d.text(308, 72, "simetría esférica:", cls="tb", anchor="start")
    d.text(308, 96, "E⃗ = E(r) r̂", cls="sa", anchor="start")
    d.text(308, 122, "E⃗ ∥ dA⃗", cls="s", anchor="start")
    d.text(358, 122, "en toda la esfera", cls="t", anchor="start")
    d.text(308, 148, "∮ E⃗·dA⃗ = E (4πr²)", cls="s", anchor="start")
    d.text(308, 178, "r₁ < R   y   r₂ > R", cls="t", anchor="start")
    return d


def esfera_er():
    d = FieldGeometryDiagram(440, 230, "Magnitud del campo eléctrico E(r) de una esfera maciza con carga uniforme")
    pts1 = [(r / 25, r / 25) for r in range(0, 26)]
    pts2 = [(1 + k / 25, 1.0 / ((1 + k / 25) ** 2)) for k in range(0, 56)]
    d.function_plot(
        82, 38, 310, 142,
        (0, 3.2), (0, 1.18),
        [pts1, pts2],
        v_lines=[(1.0, "R")],
        h_lines=[(1.0, "Emáx")],
        x_label="r", y_label="E(r)",
    )
    d.text(122, 104, "∝ r", cls="sa")
    d.text(245, 98, "∝ 1/r²", cls="sa")
    return d


def cilindro_gauss():
    d = FieldGeometryDiagram(515, 250, "Simetría cilíndrica: cilindro infinito de radio R y cilindro gaussiano coaxial de radio r y largo L")
    y0, R, rg = 132, 42, 72
    x_l, x_r = 65, 365
    gx_l, gx_r = 125, 295
    # Charged cylinder body
    d.raw(f'<rect class="csoft w" x="{x_l}" y="{y0 - R}" width="{x_r - x_l}" height="{2 * R}"/>', layer="bg")
    d.line((x_l - 18, y0), (x_r + 18, y0), cls="md")
    d.text(x_l + 22, y0 + 24, "ρ", cls="sc")
    d.dimension((x_l + 30, y0), (x_l + 30, y0 - R), text="R", label_side="left", label_offset=8)
    # Coaxial Gaussian cylinder (dashed blue)
    d.raw(f'<rect class="ad nofill" x="{gx_l}" y="{y0 - rg}" width="{gx_r - gx_l}" height="{2 * rg}"/>', layer="overlay")
    d.raw(f'<ellipse class="ad nofill" cx="{gx_l}" cy="{y0}" rx="12" ry="{rg}"/>', layer="overlay")
    d.raw(f'<ellipse class="ad nofill" cx="{gx_r}" cy="{y0}" rx="12" ry="{rg}"/>', layer="overlay")
    d.dimension((gx_l, y0 - rg - 16), (gx_r, y0 - rg - 16), text="L", label_side="top", label_offset=8)
    d.dimension((x_l - 12, y0), (x_l - 12, y0 - rg), text="r", label_side="left", label_offset=8)
    # Radial E and dA on mantle
    for xm in (175, 245):
        d.current_arrow((xm, y0 - rg), (xm, y0 - rg - 34), cls="a")
        d.current_arrow((xm, y0 + rg), (xm, y0 + rg + 34), cls="a")
    d.text(175, y0 - rg - 40, "E⃗ ∥ n̂", cls="sa")
    # End cap normal dA perpendicular to E
    d.current_arrow((gx_r + 12, y0), (gx_r + 48, y0), cls="c")
    d.text(gx_r + 34, y0 + 18, "dA⃗", cls="sc")
    d.current_arrow((gx_r + 12, y0), (gx_r + 12, y0 - 34), text="E⃗", cls="a", label_side="right", offset=8)
    d.text(392, 62, "manto:", cls="tb", anchor="start")
    d.text(392, 82, "Φ = E(2πrL)", cls="s", anchor="start")
    d.text(392, 116, "tapas:", cls="tb", anchor="start")
    d.text(392, 136, "E⃗ ⊥ n̂ ⇒ Φ = 0", cls="s", anchor="start")
    return d


def plano_losa():
    d = FieldGeometryDiagram(495, 250, "Simetría planar: losa infinita de espesor 2a con densidad ρ y pastillero gaussiano")
    xc, yc = 200, 118
    ha = 38
    d.raw(f'<rect class="csoft w" x="{xc - ha}" y="25" width="{2 * ha}" height="175"/>', layer="bg")
    d.line((xc, 20), (xc, 208), cls="md")
    d.text(xc + 8, 42, "ρ", cls="sc", anchor="start")
    # Gaussian pillbox
    px0, px1, py0, py1 = 100, 300, 76, 158
    d.raw(f'<rect class="ad nofill" x="{px0}" y="{py0}" width="{px1 - px0}" height="{py1 - py0}"/>', layer="overlay")
    d.raw(f'<ellipse class="ad nofill" cx="{px0}" cy="{yc}" rx="10" ry="{(py1 - py0) / 2}"/>', layer="overlay")
    d.raw(f'<ellipse class="ad nofill" cx="{px1}" cy="{yc}" rx="10" ry="{(py1 - py0) / 2}"/>', layer="overlay")
    d.text(px1 - 14, py0 + 18, "A", cls="sa")
    d.current_arrow((px1 + 10, yc - 10), (px1 + 52, yc - 10), text="E⃗", cls="a", label_side="top", offset=8)
    d.current_arrow((px0 - 10, yc), (px0 - 52, yc), text="E⃗", cls="a", label_side="top", offset=8)
    d.current_arrow((px1 + 10, yc + 16), (px1 + 42, yc + 16), cls="c")
    d.text(px1 + 26, yc + 34, "dA⃗", cls="sc")
    # z-axis at bottom
    az_y = 222
    d.current_arrow((60, az_y), (350, az_y), cls="m")
    d.text(358, az_y + 5, "z", cls="s", anchor="start")
    d.text(xc - ha, az_y + 16, "−a", cls="s")
    d.text(xc, az_y + 16, "0", cls="s")
    d.text(xc + ha, az_y + 16, "+a", cls="s")
    d.text(372, 74, "2 tapas:", cls="tb", anchor="start")
    d.text(372, 94, "Φ = 2EA", cls="s", anchor="start")
    d.text(372, 126, "manto:", cls="tb", anchor="start")
    d.text(372, 146, "E⃗ ⊥ n̂ ⇒ Φ = 0", cls="s", anchor="start")
    return d


def conductor_cavidad():
    d = FieldGeometryDiagram(485, 250, "Conductor en equilibrio con cavidad interior que contiene una carga +Q")
    cx, cy = 152, 126
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 90, "r_in": 44, "fill": "soft", "stroke": "w", "hollow_center": True},
        ],
        gaussian_radii=[{"r": 67, "cls": "cd", "label": "S", "deg": 135}],
    )
    d.point_charge((cx, cy), sign="+", r=8, text="+Q", label_dir="bottom")
    for deg in (20, 110, 200, 290):
        pi = d._polar_svg(cx, cy, 37, deg)
        d.text(pi[0], pi[1] + 4, "−", cls="ta")
        po = d._polar_svg(cx, cy, 82, deg)
        d.text(po[0], po[1] + 4, "+", cls="tc")
    for deg in (0, 60, 150, 240, 310):
        p0 = d._polar_svg(cx, cy, 92, deg)
        p1 = d._polar_svg(cx, cy, 122, deg)
        d.current_arrow(p0, p1, cls="a")
    d.text(286, 40, "E⃗ext", cls="sa", anchor="start")
    d.text(320, 40, "⊥ sup. (E = σ/ε₀)", cls="t", anchor="start")
    d.text(286, 86, "en el metal (S):", cls="tb", anchor="start")
    d.text(286, 108, "E⃗ = 0 ⇒ qint = −Q", cls="sc", anchor="start")
    d.text(286, 142, "superficie exterior:", cls="tb", anchor="start")
    d.text(286, 164, "qext = Qcond + Q", cls="s", anchor="start")
    return d


def superposicion_cavidad():
    d = FieldGeometryDiagram(480, 245, "Superposición en una esfera con cavidad esférica descentrada")
    ox, oy = 152, 124
    R, b, dx = 92, 38, 42
    cx, cy = ox + dx, oy
    d.raw(f'<circle class="csoft w" cx="{ox}" cy="{oy}" r="{R}"/>', layer="bg")
    d.raw(f'<circle class="paperf w" cx="{cx}" cy="{cy}" r="{b}"/>', layer="wires")
    d.node("O", ox, oy, text="O", label_dir="left", offset=8)
    d.node("C", cx, cy, text="C", label_dir="right", offset=8)
    d.current_arrow((ox, oy), (cx, cy), cls="m")
    d.text((ox + cx) / 2, oy + 16, "a⃗", cls="s")
    px, py = cx + 8, cy - 26
    d.node("P", px, py, text="P", label_dir="top", offset=8)
    d.current_arrow((ox, oy), (px, py), text="r⃗", cls="a", label_side="top", offset=8)
    d.current_arrow((cx, cy), (px, py), text="r⃗'", cls="c", label_side="right", offset=8)
    # Uniform field arrow inside cavity
    d.current_arrow((cx - 22, cy + 20), (cx + 18, cy + 20), cls="a")
    d.text(cx + 22, cy + 24, "E⃗cav", cls="sa", anchor="start")
    d.radius_dim((ox, oy), 135, R, text="R")
    d.text(292, 74, "superposición:", cls="tb", anchor="start")
    d.text(292, 98, "(+ρ en O) + (−ρ en C)", cls="s", anchor="start")
    d.text(292, 128, "r⃗ − r⃗' = a⃗", cls="s", anchor="start")
    d.text(292, 156, "E⃗cav = (ρ / 3ε₀) a⃗", cls="sa", anchor="start")
    d.text(292, 180, "(campo uniforme)", cls="t", anchor="start")
    return d


def arq1_esfera_cascaron():
    d = FieldGeometryDiagram(500, 255, "Arquetipo 1 (Examen 2025-1 P1): esfera no conductora con ρ = −3βr³ en cascarón conductor")
    cx, cy = 142, 128
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 106, "r_in": 72, "fill": "soft", "stroke": "w", "hollow_center": True},
            {"r_out": 72, "r_in": 36, "fill": "paperf", "stroke": "w"},
            {"r_out": 36, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[
            {"r": 54, "cls": "ad"},
            {"r": 89, "cls": "cd"},
        ],
    )
    # Non-overlapping radius lines
    p1 = d._polar_svg(cx, cy, 36, -135)
    d.line((cx, cy), p1, cls="m")
    d.text(p1[0] + 10, p1[1] - 10, "R", cls="s")
    p2 = d._polar_svg(cx, cy, 72, -55)
    d.line((cx, cy), p2, cls="m")
    d.text(p2[0] + 10, p2[1] + 12, "2R", cls="s")
    p3 = d._polar_svg(cx, cy, 106, 15)
    d.line((cx, cy), p3, cls="m")
    d.text(p3[0] + 6, p3[1] - 4, "3R", cls="s", anchor="start")
    ps2 = d._polar_svg(cx, cy, 45, 130)
    d.text(ps2[0], ps2[1], "S₂", cls="sa")
    ps3 = d._polar_svg(cx, cy, 80, 122)
    d.text(ps3[0], ps3[1], "S₃", cls="sc")
    d.text(286, 62, "1) 0 < r < R:  ρ = −3βr³", cls="sc", anchor="start")
    d.text(286, 92, "2) R < r < 2R: vacío", cls="t", anchor="start")
    d.text(286, 122, "3) 2R < r < 3R: conductor", cls="sa", anchor="start")
    d.text(302, 142, "qneta = −βπR⁶", cls="s", anchor="start")
    d.text(286, 174, "4) r > 3R: exterior", cls="t", anchor="start")
    return d


def arq2_dos_cilindros():
    d = FieldGeometryDiagram(475, 255, "Arquetipo 2 (Examen 2021-2 Ej. 2): dos cilindros infinitos paralelos de radio R")
    y0 = 110
    x1, x2 = 110, 325
    R = 56
    xp = x2 - 22
    d.raw(f'<circle class="csoft w" cx="{x1}" cy="{y0}" r="{R}"/>', layer="bg")
    d.raw(f'<circle class="soft w" cx="{x2}" cy="{y0}" r="{R}"/>', layer="bg")
    d.line((50, y0), (415, y0), cls="md")
    d.node("O1", x1, y0)
    d.node("O2", x2, y0)
    d.radius_dim((x1, y0), 130, R, text="R")
    d.radius_dim((x2, y0), 50, R, text="R")
    d.text(x1 - 24, y0 + 28, "ρ₁", cls="sc")
    d.text(x2 + 24, y0 + 28, "ρ₂", cls="sa")
    d.node("P", xp, y0, text="P", label_dir="top", offset=10)
    d.current_arrow((xp, y0 - 14), (xp + 34, y0 - 14), text="E⃗₁", cls="c", label_side="top", offset=8)
    d.current_arrow((xp, y0 + 14), (xp - 34, y0 + 14), text="E⃗₂", cls="a", label_side="bottom", offset=10)
    d.dimension((xp, y0 + 66), (x2, y0 + 66), text="d", label_side="bottom", label_offset=8)
    d.dimension((x1, y0 + 100), (x2, y0 + 100), text="D", label_side="bottom", label_offset=8)
    return d


def arq3_cavidad_rellena():
    d = FieldGeometryDiagram(465, 245, "Arquetipo 3 (Examen 2022-2 P11): esfera de radio R = 2b con cavidad rellena de carga Q")
    ox, oy = 165, 128
    b = 46
    R = 2 * b
    d.axes_2d((ox, oy), x_len=150, y_len=105, x_label="x", y_label="y", neg_x=115, neg_y=105)
    d.raw(f'<circle class="csoft w" cx="{ox}" cy="{oy}" r="{R}"/>', layer="bg")
    d.raw(f'<circle class="soft w" cx="{ox + b}" cy="{oy}" r="{b}"/>', layer="wires")
    d.text(ox - 48, oy - 36, "ρ", cls="sc")
    d.text(ox + b, oy - 16, "Q", cls="sa")
    d.node("P1", ox + 2 * b, oy, text="P₁", label_dir="right", offset=8)
    d.text(ox + 2 * b + 12, oy + 22, "(2b, 0)", cls="t", anchor="start")
    d.dimension((ox, oy + b + 24), (ox + b, oy + b + 24), text="b", label_side="bottom", label_offset=8)
    d.dimension((ox, oy + b + 52), (ox + 2 * b, oy + b + 52), text="R = 2b", label_side="bottom", label_offset=8)
    d.text(345, 58, "cavidad centrada", cls="t", anchor="start")
    d.text(345, 76, "en (b, 0), radio b", cls="t", anchor="start")
    return d


def practica_dos_cascarones():
    d = FieldGeometryDiagram(530, 260, "Dos cascarones esféricos conductores concéntricos con esfera aislante central e interruptor")
    cx, cy = 142, 132
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 106, "r_in": 80, "fill": "soft", "stroke": "w", "hollow_center": True},
            {"r_out": 80, "r_in": 56, "fill": "paperf", "stroke": "w"},
            {"r_out": 56, "r_in": 36, "fill": "soft", "stroke": "w", "hollow_center": True},
            {"r_out": 36, "r_in": 18, "fill": "paperf", "stroke": "w"},
            {"r_out": 18, "fill": "csoft", "stroke": "w"},
        ],
    )
    # Clean non-overlapping radius lines
    for rad, deg, txt, dx, dy in (
        (18, 30, "R", 8, -4),
        (36, 150, "a₁", -12, -4),
        (56, -130, "a₂", -12, 12),
        (80, -60, "b₁", 10, 12),
        (106, -15, "b₂", 10, 4),
    ):
        pt = d._polar_svg(cx, cy, rad, deg)
        d.line((cx, cy), pt, cls="m")
        d.text(pt[0] + dx, pt[1] + dy, txt, cls="s")
    d.switch_spdt((cx, cy - 56), (cx + 12, cy - 72), (cx, cy - 80), text="S", label_offset=(18, -8), draw_terminal_dots=True)
    d.text(286, 62, "0 < r < R: aislante (carga 2Q)", cls="sc", anchor="start")
    d.text(286, 94, "a₁ < r < a₂: conductor neutro", cls="sa", anchor="start")
    d.text(286, 126, "b₁ < r < b₂: conductor (carga +Q)", cls="sa", anchor="start")
    d.text(286, 158, "interruptor S conecta a₂ y b₁", cls="t", anchor="start")
    return d


def practica_cilindros_traslapados():
    d = FieldGeometryDiagram(465, 250, "Dos cilindros infinitos traslapados con densidades −ρ y +ρ")
    ox, oy = 225, 128
    x0, R0 = 36, 76
    d.axes_2d((ox, oy), x_len=145, y_len=104, x_label="x", y_label="y", neg_x=145, neg_y=104)
    d.raw(f'<circle class="soft w" fill-opacity="0.55" cx="{ox - x0}" cy="{oy}" r="{R0}"/>', layer="bg")
    d.raw(f'<circle class="csoft w" fill-opacity="0.55" cx="{ox + x0}" cy="{oy}" r="{R0}"/>', layer="bg")
    d.text(ox - x0 - 46, oy - 38, "−ρ", cls="sa")
    d.text(ox + x0 + 46, oy - 38, "+ρ", cls="sc")
    d.node("O1", ox - x0, oy)
    d.node("O2", ox + x0, oy)
    d.text(ox - x0, oy + 20, "−x₀", cls="s")
    d.text(ox + x0, oy + 20, "+x₀", cls="s")
    px, py = ox - 4, oy - 38
    d.node("P", px, py, text="P", label_dir="top", offset=8)
    d.current_arrow((ox - x0, oy), (px, py), text="r⃗₁", cls="a", label_side="left", offset=10)
    d.current_arrow((ox + x0, oy), (px, py), text="r⃗₂", cls="c", label_side="right", offset=10)
    d.current_arrow((ox + 20, oy + 32), (ox - 16, oy + 32), cls="a")
    d.text(ox + 24, oy + 36, "E⃗", cls="sa", anchor="start")
    return d


def figures():
    return {
        "u02-flujo-angulo": flujo_angulo(),
        "u02-cubo-flujo": cubo_flujo(),
        "u02-gauss-superficie": gauss_superficie(),
        "u02-esfera-gauss": esfera_gauss(),
        "u02-esfera-er": esfera_er(),
        "u02-cilindro-gauss": cilindro_gauss(),
        "u02-plano-losa": plano_losa(),
        "u02-conductor-cavidad": conductor_cavidad(),
        "u02-superposicion-cavidad": superposicion_cavidad(),
        "u02-arq1-esfera-cascaron": arq1_esfera_cascaron(),
        "u02-arq2-dos-cilindros": arq2_dos_cilindros(),
        "u02-arq3-cavidad-rellena": arq3_cavidad_rellena(),
        "u02-practica-dos-cascarones": practica_dos_cascarones(),
        "u02-practica-cilindros-traslapados": practica_cilindros_traslapados(),
    }
