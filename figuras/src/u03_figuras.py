"""U3 Electric Potential figures. Generate with: python3 scripts/build_figures.py u03"""

import math
from svg_primitives import FieldGeometryDiagram, arrow


def trabajo_trayectoria():
    d = FieldGeometryDiagram(460, 265, "Trayectoria arbitraria de a a b en el campo radial de una carga +q")
    ox, oy = 105, 160
    d.point_charge((ox, oy), sign="+", r=10, text="+q", label_dir="left", radial_rays=0)
    for deg in (-22, 12, 48):
        p_end = d._polar_svg(ox, oy, 290, deg)
        d.line((ox, oy), p_end, cls="fldl")
    ra, rb = 105, 225
    d.angle_arc((ox, oy), -15, 52, r=ra, text="", cls="md")
    d.angle_arc((ox, oy), -15, 52, r=rb, text="", cls="md")
    d.text(ox + ra * math.cos(math.radians(-12)) - 4, oy - ra * math.sin(math.radians(-12)) + 16, "r₁", cls="s")
    d.text(ox + rb * math.cos(math.radians(-10)) + 8, oy - rb * math.sin(math.radians(-10)) + 16, "r₂", cls="s")

    pa = d._polar_svg(ox, oy, ra, 38)
    pb = d._polar_svg(ox, oy, rb, 8)
    pm = d._polar_svg(ox, oy, 165, 25)
    d.raw(
        f'<path class="w nofill" d="M {pa[0]:.1f} {pa[1]:.1f} '
        f'Q {pm[0] - 25:.1f} {pm[1] - 42:.1f} {pm[0]:.1f} {pm[1]:.1f} '
        f'T {pb[0]:.1f} {pb[1]:.1f}"/>',
        layer="wires",
    )
    d.node("a", pa[0], pa[1], text="a", label_dir="top", offset=10)
    d.node("b", pb[0], pb[1], text="b", label_dir="right", offset=10)
    d.point_charge(pm, sign="+", r=6, text="q₀", label_dir="left")
    f_tip = d._polar_svg(pm[0], pm[1], 60, 25)
    dl_tip = d._polar_svg(pm[0], pm[1], 52, -12)
    d.current_arrow(pm, f_tip, cls="a")
    d.text(f_tip[0] - 8, f_tip[1] - 12, "F⃗ = q₀E⃗", cls="sa", anchor="middle")
    d.current_arrow(pm, dl_tip, cls="c")
    d.text(dl_tip[0] - 6, dl_tip[1] + 18, "dℓ⃗", cls="sc", anchor="middle")
    d.angle_arc(pm, -12, 25, r=26, text="φ", cls="m")
    d.text(342, 42, "E⃗ radial", cls="sa", anchor="start")
    d.text(342, 62, "solo importa r₁ y r₂", cls="t", anchor="start")
    return d


def placas_energia():
    d = FieldGeometryDiagram(450, 240, "Placas paralelas con campo uniforme y carga acelerada entre A y B")
    x0, x1 = 90, 320
    y_top, y_bot = 46, 184
    d.raw(f'<rect class="csoft w" x="{x0}" y="{y_top - 8}" width="{x1 - x0}" height="8"/>', layer="wires")
    d.raw(f'<rect class="soft w" x="{x0}" y="{y_bot}" width="{x1 - x0}" height="8"/>', layer="wires")
    d.text((x0 + x1) / 2, y_top - 16, "+ + + + + + +", cls="tc")
    d.text((x0 + x1) / 2, y_bot + 24, "− − − − − − −", cls="ta")
    for ex in (125, 205, 285):
        d.layers["bg"].append(arrow(ex, y_top + 6, ex, y_bot - 6, line_cls="a", head_cls="af"))
    d.text(137, 118, "E⃗", cls="sa", anchor="start")
    d.node("B", 242, y_top + 26, text="B (mayor V)", label_dir="right", offset=10, cls="t")
    d.node("A", 242, y_bot - 26, text="A (menor V)", label_dir="right", offset=10, cls="t")
    d.point_charge((242, y_top + 26), sign="+", r=6)
    d.dimension((x1 + 26, y_top), (x1 + 26, y_bot), text="d", label_side="right", label_offset=8)
    d.text(18, 118, "ΔV = −Ed", cls="t", anchor="start")
    return d


def dipolo_cero():
    d = FieldGeometryDiagram(480, 235, "Comparación entre dipolo (V = 0, E ≠ 0) y cargas iguales (E = 0, V ≠ 0)")
    cx1, cy = 120, 120
    d.text(cx1, 24, "(a) Dipolo: V = 0, campo ≠ 0", cls="tb")
    d.line((cx1, 46), (cx1, 198), cls="cd")
    d.text(cx1 + 8, 54, "V = 0", cls="sc", anchor="start")
    d.point_charge((cx1 - 56, cy), sign="+", r=8, text="+q", label_dir="bottom")
    d.point_charge((cx1 + 56, cy), sign="-", r=8, text="−q", label_dir="bottom")
    d.node("P1", cx1, cy, text="", draw_dot=True)
    d.current_arrow((cx1, cy), (cx1 + 42, cy), text="E⃗", cls="a", label_side="top", offset=10)

    d.line((240, 20), (240, 218), cls="m")

    cx2 = 360
    d.text(cx2, 24, "(b) Cargas iguales: E = 0, V ≠ 0", cls="tb")
    d.point_charge((cx2 - 58, cy), sign="+", r=8, text="+q", label_dir="bottom")
    d.point_charge((cx2 + 58, cy), sign="+", r=8, text="+q", label_dir="bottom")
    d.node("M", cx2, cy, text="M", label_dir="top", offset=10)
    d.current_arrow((cx2 - 38, cy - 16), (cx2 - 12, cy - 16), cls="a")
    d.current_arrow((cx2 + 38, cy - 16), (cx2 + 12, cy - 16), cls="a")
    d.text(cx2, 188, "V = 4kq / d ≠ 0", cls="ta")
    return d


def cargas_e1():
    d = FieldGeometryDiagram(460, 175, "Dos cargas puntuales sobre el eje x y puntos A y B")
    y = 95
    d.line((30, y), (430, y), cls="m")
    d.layers["overlay"].append(arrow(410, y, 440, y, line_cls="m", head_cls="mf", head_len=6, head_w=3))
    d.text(446, y + 5, "x", cls="s", anchor="start")
    x1, xB, xA, x2 = 70, 170, 220, 370
    d.point_charge((x1, y), sign="+", r=9, text="q₁ = +4 nC", label_dir="top")
    d.point_charge((x2, y), sign="-", r=9, text="q₂ = −2 nC", label_dir="top")
    d.node("B", xB, y, text="B", label_dir="top", offset=12)
    d.node("A", xA, y, text="A", label_dir="top", offset=12)
    d.text(x1, y + 24, "0", cls="t")
    d.text(xB, y + 24, "0,20 m", cls="t")
    d.text(xA, y + 24, "0,30 m", cls="t")
    d.text(x2, y + 24, "0,60 m", cls="t")
    return d


def anillo_disco():
    d = FieldGeometryDiagram(450, 260, "Disco cargado de radio R dividido en anillos diferenciales y punto P en el eje")
    cx, cy = 195, 195
    d.ring_or_disk_3d((cx, cy), rx=85, ry=28, is_disk=True, ring_dr_frac=0.52, target_P=(cx, 58), text="σ")
    d.text(cx - 48, cy - 22, "r'", cls="sa")
    d.text(cx + 12, 125, "x", cls="s", anchor="start")
    d.text(cx + 76, 120, "√(x² + r'²)", cls="ta", anchor="start")
    return d


def esfera_potencial():
    d = FieldGeometryDiagram(470, 235, "Potencial V(r) y campo E(r) de una esfera maciza uniforme de radio R")
    pts_v_in = [(r / 20, 1.5 - 0.5 * (r / 20) ** 2) for r in range(0, 21)]
    pts_v_out = [(r / 20, 1.0 / (r / 20)) for r in range(20, 61)]
    d.function_plot(
        52, 42, 155, 145, (0, 3.0), (0, 1.7),
        [pts_v_in, pts_v_out],
        v_lines=[(1.0, "R")],
        h_lines=[(1.5, "1,5 V₀"), (1.0, "V₀")],
        x_label="r", y_label="V(r)", cls="a",
    )
    pts_e_in = [(0.0, 0.0), (1.0, 1.0)]
    pts_e_out = [(r / 20, 1.0 / (r / 20) ** 2) for r in range(20, 61)]
    d.function_plot(
        275, 42, 155, 145, (0, 3.0), (0, 1.25),
        [pts_e_in, pts_e_out],
        v_lines=[(1.0, "R")],
        h_lines=[(1.0, "E₀")],
        x_label="r", y_label="E(r)", cls="c",
    )
    return d


def coaxial():
    d = FieldGeometryDiagram(480, 250, "Sección transversal de un cable coaxial con conductores de radios a, b y c")
    cx, cy = 148, 125
    shells = [
        {"r_out": 102, "r_in": 82, "fill": "soft", "stroke": "w", "hollow_center": True, "r_label": "c", "r_deg": -25},
        {"r_out": 82, "r_in": 32, "fill": "paperf", "stroke": "w", "r_label": "b", "r_deg": 25},
        {"r_out": 32, "r_in": 0, "fill": "csoft", "stroke": "w", "r_label": "a", "r_deg": -145},
    ]
    d.concentric_system((cx, cy), shells, gaussian_radii=[{"r": 58, "cls": "ad", "label": "r", "deg": 135}])
    d.text(282, 84, "+λ en r = a", cls="tc", anchor="start")
    d.text(282, 110, "−λ en r = b", cls="ta", anchor="start")
    d.text(282, 136, "conductor ext.: b ≤ r ≤ c", cls="t", anchor="start")
    d.text(282, 162, "E = 0 para r > c", cls="t", anchor="start")
    return d


def equipotenciales():
    d = FieldGeometryDiagram(480, 245, "Superficies equipotenciales (discontinuas) perpendiculares a las líneas de E")
    cx1, cy = 115, 128
    d.text(cx1, 22, "(a) Carga puntual +q", cls="tb")
    for r_eq in (36, 62, 88):
        d.raw(f'<circle class="cd nofill" cx="{cx1}" cy="{cy}" r="{r_eq}"/>', layer="bg")
    for deg in range(0, 360, 45):
        p0 = d._polar_svg(cx1, cy, 14, deg)
        p1 = d._polar_svg(cx1, cy, 94, deg)
        d.layers["overlay"].append(arrow(p0[0], p0[1], p1[0], p1[1], line_cls="a", head_cls="af", head_len=6, head_w=3))
    d.point_charge((cx1, cy), sign="+", r=9)
    d.text(cx1 + 78, cy - 78, "V₁ > V₂", cls="sc", anchor="start")
    d.text(cx1 + 88, cy + 72, "E⃗", cls="sa", anchor="start")

    d.line((240, 18), (240, 232), cls="m")

    x0, x1 = 275, 445
    d.text(360, 22, "(b) Campo uniforme", cls="tb")
    d.text(360, 50, "E⃗ = −∇V", cls="sa")
    for vx, vlab in ((295, "V₁"), (345, "V₂"), (395, "V₃"), (445, "V₄")):
        d.line((vx, 64), (vx, 198), cls="cd")
        d.text(vx, 218, vlab, cls="sc")
    for ey in (88, 130, 172):
        d.layers["overlay"].append(arrow(x0, ey, x1 - 10, ey, line_cls="a", head_cls="af", head_len=7, head_w=3.5))
    d.text(360, 238, "V₁ > V₂ > V₃ > V₄", cls="t")
    return d


def esferas_conectadas():
    d = FieldGeometryDiagram(470, 230, "Dos esferas conductoras alejadas conectadas por un alambre")
    c1, c2 = (100, 110), (335, 110)
    r1, r2 = 34, 58
    d.raw(f'<circle class="csoft w" cx="{c1[0]}" cy="{c1[1]}" r="{r1}"/>', layer="bg")
    d.raw(f'<circle class="soft w" cx="{c2[0]}" cy="{c2[1]}" r="{r2}"/>', layer="bg")
    d.line(c1, (c1[0] + r1 * 0.707, c1[1] + r1 * 0.707), cls="m")
    d.text(c1[0] + 10, c1[1] - 4, "R₁", cls="s")
    d.line(c2, (c2[0] + r2 * 0.707, c2[1] + r2 * 0.707), cls="m")
    d.text(c2[0], c2[1] - 10, "R₂ = 2R₁", cls="s")
    # Wire with open switch S
    d.wire((c1[0] + r1, c1[1]), (195, c1[1]))
    d.wire((235, c1[1]), (c2[0] - r2, c2[1]))
    d.switch_spdt((195, c1[1]), (233, c1[1] - 20), target_open=None, text="S", label_offset=(20, -24), draw_terminal_dots=True)
    d.raw(f'<circle class="inkf" cx="235" cy="{c1[1]}" r="3.6"/>', layer="overlay")
    d.text(c1[0], 188, "q₁, V₁", cls="s")
    d.text(c2[0], 188, "q₂, V₂", cls="s")
    d.text(215, 36, "d ≫ R₁, R₂  (al cerrar S: V₁ = V₂)", cls="t")
    return d


def x1_4q_q():
    d = FieldGeometryDiagram(460, 200, "Cargas +4Q en x = 0 y −Q en x = L; punto P en x = 2L donde E = 0")
    ox, y = 70, 110
    d.line((25, y), (435, y), cls="m")
    d.layers["overlay"].append(arrow(415, y, 442, y, line_cls="m", head_cls="mf", head_len=6, head_w=3))
    d.layers["overlay"].append(arrow(ox, 165, ox, 28, line_cls="m", head_cls="mf", head_len=6, head_w=3))
    d.text(446, y + 5, "x", cls="s", anchor="start")
    d.text(ox + 10, 32, "y", cls="s", anchor="start")
    xL, xP = 200, 330
    d.point_charge((ox, y), sign="+", r=10, text="+4Q", label_dir="top")
    d.point_charge((xL, y), sign="-", r=8, text="−Q", label_dir="top")
    d.node("P", xP, y, text="P", label_dir="top", offset=12)
    d.current_arrow((xP, y - 22), (xP + 46, y - 22), text="E⃗₊", cls="c", label_side="top", offset=8)
    d.current_arrow((xP, y + 22), (xP - 46, y + 22), text="E⃗₋", cls="a", label_side="bottom", offset=12)
    d.dimension((ox, y + 48), (xL, y + 48), text="L", label_side="bottom", label_offset=8)
    d.dimension((xL, y + 48), (xP, y + 48), text="L", label_side="bottom", label_offset=8)
    return d


def x2_carga_plano():
    d = FieldGeometryDiagram(460, 230, "Plano infinito con densidad σ y carga puntual q en el origen")
    px, oy = 110, 120
    d.raw(f'<rect class="csoft w" x="{px - 6}" y="25" width="12" height="185"/>', layer="bg")
    d.text(px - 18, 42, "σ", cls="sc", anchor="end")
    d.text(px - 18, 62, "plano", cls="t", anchor="end")
    d.line((px, oy), (425, oy), cls="m")
    d.layers["overlay"].append(arrow(405, oy, 435, oy, line_cls="m", head_cls="mf", head_len=6, head_w=3))
    d.text(440, oy + 5, "x", cls="s", anchor="start")
    d.point_charge((px, oy), sign="+", r=8, text="q", label_dir="top")
    xd, x2d = 225, 340
    d.node("d", xd, oy, text="d", label_dir="bottom", offset=12)
    d.node("2d", x2d, oy, text="2d", label_dir="bottom", offset=12)
    d.point_charge((xd, oy), sign="+", r=6, text="q₀", label_dir="top")
    d.current_arrow((xd + 14, oy - 24), (x2d - 14, oy - 24), text="desplazamiento", cls="a", label_side="top", offset=10)
    d.current_arrow((px + 20, 62), (px + 75, 62), text="E⃗ₚ", cls="c", label_side="top", offset=8)
    return d


def p3_semicirculo():
    d = FieldGeometryDiagram(420, 250, "Semicircunferencia cargada con densidad λ y carga puntual q en A")
    cx, cy, R = 210, 130, 82
    d.line((cx - R - 28, cy), (cx + R + 28, cy), cls="md")
    d.line((cx, cy - R - 24), (cx, cy + R + 32), cls="md")
    d.arc_wire((cx, cy), R, 0, 180, cls="wk")
    d.node("C", cx, cy, text="C", label_dir="top", offset=10)
    d.node("B", cx - R, cy, text="B", label_dir="left", offset=10)
    d.node("D", cx + R, cy, text="D", label_dir="right", offset=10)
    d.radius_dim((cx, cy), 45, R, text="R", cls="m")
    d.point_charge((cx, cy + R), sign="+", r=8, text="q (en A)", label_dir="bottom")
    d.text(cx - R * 0.72, cy - R * 0.72, "λ", cls="sc", anchor="end")
    d.dimension((cx - 24, cy), (cx - 24, cy + R), text="R", label_side="left", label_offset=8)
    return d


def p4_cascarones():
    d = FieldGeometryDiagram(460, 275, "Esfera aislante central rodeada por dos cascarones conductores concéntricos con interruptor")
    cx, cy = 165, 138
    shells = [
        {"r_out": 118, "r_in": 98, "fill": "soft", "stroke": "w", "hollow_center": True, "r_label": "b₂", "r_deg": -20},
        {"r_out": 98, "r_in": 70, "fill": "paperf", "stroke": "w", "r_label": "b₁", "r_deg": -55},
        {"r_out": 70, "r_in": 50, "fill": "soft", "stroke": "w", "hollow_center": True, "r_label": "a₂", "r_deg": 20},
        {"r_out": 50, "r_in": 28, "fill": "paperf", "stroke": "w", "r_label": "a₁", "r_deg": 150},
        {"r_out": 28, "r_in": 0, "fill": "csoft", "stroke": "w", "r_label": "R", "r_deg": -135},
    ]
    d.concentric_system((cx, cy), shells)
    p_a2 = (cx, cy - 70)
    p_b1 = (cx, cy - 98)
    d.switch_spdt(p_a2, (cx + 16, cy - 92), target_open=None, text="S", label_offset=(-14, -12), draw_terminal_dots=True)
    d.raw(f'<circle class="inkf" cx="{p_b1[0]}" cy="{p_b1[1]}" r="3.6"/>', layer="overlay")
    d.text(308, 65, "Esfera aislante (R):", cls="tb", anchor="start")
    d.text(308, 84, "ρ(r) = βr², carga 2Q", cls="t", anchor="start")
    d.text(308, 120, "Cascarón interno:", cls="tb", anchor="start")
    d.text(308, 139, "a₁, a₂ (neutro)", cls="t", anchor="start")
    d.text(308, 175, "Cascarón externo:", cls="tb", anchor="start")
    d.text(308, 194, "b₁, b₂ (carga Q)", cls="t", anchor="start")
    return d


def p5_alambre():
    d = FieldGeometryDiagram(420, 260, "Alambre finito de −d a +d sobre el eje z y electrón desplazándose de 4d a 3d")
    cx = 175
    d.line((cx, 238), (cx, 22), cls="m")
    d.layers["overlay"].append(arrow(cx, 35, cx, 14, line_cls="m", head_cls="mf", head_len=6, head_w=3))
    d.text(cx + 12, 22, "z", cls="s", anchor="start")
    z_m, z_0, z_p, z_3d, z_4d = 215, 185, 155, 95, 58
    d.charged_rod((cx, z_m), (cx, z_p), thickness=9, text="")
    d.text(cx - 18, z_0 + 4, "λ", cls="sc", anchor="end")
    d.text(cx + 18, z_m + 4, "−d", cls="s", anchor="start")
    d.text(cx + 18, z_0 + 4, "0", cls="t", anchor="start")
    d.text(cx + 18, z_p + 4, "+d", cls="s", anchor="start")
    d.node("3d", cx, z_3d, text="3d", label_dir="right", offset=12)
    d.node("4d", cx, z_4d, text="4d", label_dir="right", offset=12)
    d.point_charge((cx, z_4d), sign="-", r=7, text="e⁻", label_dir="left")
    d.current_arrow((cx - 26, z_4d + 6), (cx - 26, z_3d - 6), text="v⃗", cls="a", label_side="left", offset=10)
    return d


def figures():
    return {
        "u03-trabajo-trayectoria": trabajo_trayectoria(),
        "u03-placas-energia": placas_energia(),
        "u03-dipolo-cero": dipolo_cero(),
        "u03-cargas-e1": cargas_e1(),
        "u03-anillo-disco": anillo_disco(),
        "u03-esfera-potencial": esfera_potencial(),
        "u03-coaxial": coaxial(),
        "u03-equipotenciales": equipotenciales(),
        "u03-esferas-conectadas": esferas_conectadas(),
        "u03-x1-4q-q": x1_4q_q(),
        "u03-x2-carga-plano": x2_carga_plano(),
        "u03-p3-semicirculo": p3_semicirculo(),
        "u03-p4-cascarones": p4_cascarones(),
        "u03-p5-alambre": p5_alambre(),
    }
