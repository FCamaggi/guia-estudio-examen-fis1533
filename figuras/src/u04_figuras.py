"""U4 Capacitance & Dielectrics figures. Generate with: python3 scripts/build_figures.py u04"""

import math
from svg_primitives import FieldGeometryDiagram, arrow


def _arrow_on(d, p1, p2, cls="a"):
    hcls = {"a": "af", "c": "cf", "m": "mf", "w": "inkf"}.get(cls, "af")
    d.raw(arrow(p1[0], p1[1], p2[0], p2[1], line_cls=cls, head_cls=hcls, head_len=7, head_w=3.5))


def _rad_label(d, cx, cy, r, deg, txt, text_frac=0.58, off_deg=14, cls="s"):
    p = d._polar_svg(cx, cy, r, deg)
    d.line((cx, cy), p, cls="m")
    lp = d._polar_svg(cx, cy, r * text_frac, deg + off_deg)
    d.text(lp[0], lp[1] + 5, txt, cls=cls)


def geometrias():
    d = FieldGeometryDiagram(590, 225, "Tres geometrías básicas de capacitores y sus superficies gaussianas")
    # Panel 1: Placas paralelas
    px, py, pw, ph = 28, 56, 120, 92
    d.raw(f'<rect class="csoft w" x="{px}" y="{py-8}" width="{pw}" height="8"/>', layer="wires")
    d.raw(f'<rect class="soft w" x="{px}" y="{py+ph}" width="{pw}" height="8"/>', layer="wires")
    d.text(px + pw / 2, py - 15, "+Q (+σ)", cls="tc")
    d.text(px + pw / 2, py + ph + 24, "−Q (−σ)", cls="ta")
    for k in (0.25, 0.5, 0.75):
        ex = px + pw * k
        _arrow_on(d, (ex, py + 8), (ex, py + ph - 8), cls="a")
    d.text(px + pw * 0.5 + 14, py + ph * 0.5 + 4, "E⃗", cls="sa", anchor="start")
    d.dimension((px + pw + 10, py), (px + pw + 10, py + ph), text="d", label_side="right", label_offset=8)
    d.text(px + pw / 2, 208, "(a) Placas paralelas (área A)", cls="t")

    # Panel 2: Cilíndrico
    cx2, cy2 = 295, 102
    d.concentric_system(
        (cx2, cy2),
        shells=[
            {"r_out": 64, "fill": "paperf", "stroke": "wk"},
            {"r_out": 20, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[{"r": 42, "cls": "ad"}],
    )
    d.text(cx2 - 12, cy2 + 5, "+Q", cls="tc", anchor="end")
    _rad_label(d, cx2, cy2, 20, -45, "ra", text_frac=1.35, off_deg=18)
    _rad_label(d, cx2, cy2, 64, 15, "rb", text_frac=0.72, off_deg=16)
    p_g = d._polar_svg(cx2, cy2, 42, 130)
    d.text(p_g[0] - 8, p_g[1] - 4, "r", cls="sa", anchor="end")
    p_e1 = d._polar_svg(cx2, cy2, 24, 72)
    p_e2 = d._polar_svg(cx2, cy2, 54, 72)
    _arrow_on(d, p_e1, p_e2, cls="a")
    p_el = d._polar_svg(cx2, cy2, 74, 72)
    d.text(p_el[0] + 4, p_el[1], "E⃗", cls="sa", anchor="start")
    d.text(cx2, 208, "(b) Cilíndrico coaxial (largo L)", cls="t")

    # Panel 3: Esférico
    cx3, cy3 = 492, 102
    d.concentric_system(
        (cx3, cy3),
        shells=[
            {"r_out": 68, "fill": "soft", "stroke": "w"},
            {"r_out": 58, "fill": "paperf", "stroke": "w"},
            {"r_out": 22, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[{"r": 40, "cls": "ad"}],
    )
    d.text(cx3 - 10, cy3 + 5, "+Q", cls="tc", anchor="end")
    _rad_label(d, cx3, cy3, 22, -45, "ra", text_frac=1.35, off_deg=18)
    _rad_label(d, cx3, cy3, 58, 15, "rb", text_frac=0.72, off_deg=16)
    d.text(cx3 - 50, cy3 - 56, "−Q", cls="ta", anchor="end")
    p_g3 = d._polar_svg(cx3, cy3, 40, 125)
    d.text(p_g3[0] - 8, p_g3[1] - 4, "r", cls="sa", anchor="end")
    d.text(cx3, 208, "(c) Cascarones esféricos", cls="t")
    return d


def serie_paralelo():
    d = FieldGeometryDiagram(540, 236, "Capacitores en serie (izquierda) y en paralelo (derecha)")
    # Izquierda: Serie
    d.node("sa", 40, 100, text="a", label_dir="left", offset=10)
    d.node("sb", 230, 100, text="b", label_dir="right", offset=10)
    d.capacitor("sa", (135, 100), text="C₁", label_side="top", offset=24)
    d.capacitor((135, 100), "sb", text="C₂", label_side="top", offset=24)
    d.node("sm", 135, 100, draw_dot=True)
    d.text(105, 76, "+", cls="tc")
    d.text(120, 76, "−", cls="ta")
    d.text(150, 76, "+", cls="tc")
    d.text(165, 76, "−", cls="ta")
    d.text(135, 136, "isla aislada (q neta = 0)", cls="t")
    d.text(135, 182, "Misma carga Q", cls="ta")
    d.text(135, 204, "V = V₁ + V₂", cls="s")

    # Separador
    d.line((268, 22), (268, 218), cls="md")

    # Derecha: Paralelo
    d.node("pa", 300, 100, text="a", label_dir="left", offset=10)
    d.node("pb", 500, 100, text="b", label_dir="right", offset=10)
    d.parallel_group(
        "pa", "pb",
        branches=[
            {"kind": "capacitor", "dy": -40, "label": "C₁", "label_side": "top", "offset": 20},
            {"kind": "capacitor", "dy": 40, "label": "C₂", "label_side": "bottom", "offset": 24},
        ],
        lead=35,
    )
    d.text(400, 204, "Mismo voltaje V · Q = Q₁ + Q₂", cls="ta")
    return d


def energia_u():
    d = FieldGeometryDiagram(530, 230, "Trabajo de carga como área bajo la recta v(q) = q/C")
    pts = [(0.0, 0.0), (1.0, 1.0)]
    x0, y0, w, h = 60, 34, 200, 140
    tri = f"{x0},{y0+h} {x0+w},{y0+h} {x0+w},{y0}"
    d.raw(f'<polygon class="soft" points="{tri}"/>', layer="bg")
    fx = x0 + 0.50 * w
    fw = 12
    fh = 0.50 * h
    d.raw(f'<rect class="csoft c" x="{fx:.1f}" y="{y0+h-fh:.1f}" width="{fw}" height="{fh:.1f}"/>', layer="bg")
    d.function_plot(x0, y0, w, h, (0, 1), (0, 1), [pts], v_lines=[(1, "Q")], h_lines=[(1, "V")], x_label="q", y_label="v(q)")
    d.text(fx + fw / 2, y0 + h + 16, "dq", cls="sc")
    d.text(x0 + 0.77 * w, y0 + h - 30, "U = ½ QV", cls="sa")
    d.text(295, 82, "dW = v dq = (q/C) dq", cls="s", anchor="start")
    d.text(295, 114, "U = Q²/(2C) = ½ CV²", cls="s", anchor="start")
    d.text(295, 146, "u = ½ ε E²  (J/m³)", cls="sa", anchor="start")
    return d


def polarizacion():
    d = FieldGeometryDiagram(460, 240, "Polarización de un dieléctrico entre placas paralelas y cargas ligadas superficiales")
    d.raw('<rect class="csoft w" x="45" y="45" width="16" height="140"/>', layer="wires")
    d.raw('<rect class="soft w" x="385" y="45" width="16" height="140"/>', layer="wires")
    d.text(53, 35, "+σ", cls="tc")
    d.text(393, 35, "−σ", cls="ta")

    bx, by, bw, bh = 105, 52, 236, 126
    d.raw(f'<rect class="paperf w" x="{bx}" y="{by}" width="{bw}" height="{bh}"/>', layer="bg")
    d.raw(f'<rect class="soft nostroke" x="{bx}" y="{by}" width="18" height="{bh}"/>', layer="bg")
    d.raw(f'<rect class="csoft nostroke" x="{bx+bw-18}" y="{by}" width="18" height="{bh}"/>', layer="bg")
    for row in (78, 115, 152):
        for col in (138, 200, 262):
            d.raw(f'<ellipse class="m nofill" cx="{col+22}" cy="{row}" rx="22" ry="10"/>', layer="wires")
            d.text(col + 10, row + 4, "−", cls="ta")
            d.text(col + 34, row + 4, "+", cls="tc")
        d.text(bx + 9, row + 4, "−", cls="ta")
        d.text(bx + bw - 9, row + 4, "+", cls="tc")

    d.text(bx + 9, by - 10, "−σb", cls="sa")
    d.text(bx + bw - 9, by - 10, "+σb", cls="sc")

    _arrow_on(d, (bx, 115), (bx - 30, 115), cls="w")
    d.text(bx - 22, 103, "n̂", cls="s")
    _arrow_on(d, (bx + bw, 115), (bx + bw + 30, 115), cls="w")
    d.text(bx + bw + 22, 103, "n̂", cls="s")

    _arrow_on(d, (165, 204), (275, 204), cls="a")
    d.text(220, 224, "E⃗ y P⃗", cls="sa")
    return d


def gauss_diel():
    d = FieldGeometryDiagram(510, 235, "Ley de Gauss para el desplazamiento eléctrico en un dieléctrico concéntrico")
    cx, cy = 140, 118
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 84, "fill": "soft", "stroke": "w"},
            {"r_out": 32, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[{"r": 58, "cls": "cd"}],
    )
    d.text(cx - 10, cy + 5, "+Q", cls="tc", anchor="end")
    _rad_label(d, cx, cy, 32, -45, "a", text_frac=0.65, off_deg=20)
    _rad_label(d, cx, cy, 84, 15, "b", text_frac=0.80, off_deg=12)
    pg = d._polar_svg(cx, cy, 58, 130)
    d.text(pg[0] - 8, pg[1] - 4, "r", cls="sc", anchor="end")
    p1 = d._polar_svg(cx, cy, 38, 72)
    p2 = d._polar_svg(cx, cy, 76, 72)
    _arrow_on(d, p1, p2, cls="c")
    pdl = d._polar_svg(cx, cy, 96, 72)
    d.text(pdl[0] + 4, pdl[1], "D⃗", cls="sc", anchor="start")
    d.text(258, 70, "D⃗", cls="sc", anchor="start")
    d.text(275, 70, "solo ve Q libre = +Q", cls="tc", anchor="start")
    d.text(258, 100, "∮ D⃗·dA⃗ = Q libre", cls="s", anchor="start")
    d.text(258, 132, "E⃗ = D⃗/ε  (en el dieléctrico)", cls="sa", anchor="start")
    d.text(258, 162, "P⃗ = (ε − ε₀) E⃗", cls="s", anchor="start")
    d.text(258, 192, "−σb en r = a,  +σb en r = b", cls="t", anchor="start")
    return d


def diel_serie_paralelo():
    d = FieldGeometryDiagram(510, 240, "Dieléctricos en serie (izquierda) vs en paralelo (derecha)")
    d.dielectric_capacitor(
        40, 48, 165, 110,
        blocks=[
            {"y_frac": 0.0, "h_frac": 0.45, "fill": "soft", "label": "ε₁, d₁"},
            {"y_frac": 0.45, "h_frac": 0.55, "fill": "csoft", "label": "ε₂, d₂"},
        ],
        plate_labels=("+Q", "−Q"),
    )
    d.text(122, 198, "Serie: mismo D, distinto E", cls="ta")
    d.text(122, 216, "1/Ceq = 1/C₁ + 1/C₂", cls="s")

    d.line((252, 24), (252, 224), cls="md")

    d.dielectric_capacitor(
        295, 48, 175, 110,
        blocks=[
            {"x_frac": 0.0, "w_frac": 0.48, "fill": "soft", "label": "ε₁, A₁"},
            {"x_frac": 0.48, "w_frac": 0.52, "fill": "csoft", "label": "ε₂, A₂"},
        ],
        plate_labels=("+Q = Q₁ + Q₂", "−Q"),
    )
    d.text(382, 198, "Paralelo: mismo E, distinto D", cls="tc")
    d.text(382, 216, "Ceq = C₁ + C₂", cls="s")
    return d


def bateria_diel():
    d = FieldGeometryDiagram(500, 220, "Inserción de dieléctrico κ con capacitor aislado vs conectado a batería")
    d.dielectric_capacitor(
        55, 55, 140, 82,
        blocks=[{"x_frac": 0.3, "w_frac": 0.7, "fill": "soft", "label": "κ"}],
        plate_labels=("+Q₀ (fija)", "−Q₀"),
    )
    _arrow_on(d, (112, 96), (76, 96), cls="a")
    d.text(125, 176, "(a) Aislado: Q constante", cls="ta")
    d.text(125, 196, "V = V₀/κ,  U = U₀/κ", cls="s")

    d.line((245, 22), (245, 206), cls="md")

    d.node("bt", 290, 55, draw_dot=False)
    d.node("bb", 290, 137, draw_dot=False)
    d.battery("bt", "bb", text="V₀", label_side="left", offset=18)
    d.wire("bt", (335, 55))
    d.wire("bb", (335, 137))
    d.dielectric_capacitor(
        335, 55, 135, 82,
        blocks=[{"x_frac": 0.3, "w_frac": 0.7, "fill": "csoft", "label": "κ"}],
        plate_labels=("+Q = κQ₀", "−Q"),
    )
    _arrow_on(d, (388, 96), (354, 96), cls="c")
    d.text(382, 176, "(b) Batería conectada: V fija", cls="tc")
    d.text(382, 196, "Q = κQ₀,  U = κU₀", cls="s")
    return d


def lamina_parcial():
    d = FieldGeometryDiagram(420, 215, "Capacitor con lámina de vidrio y capa de aire en serie")
    d.dielectric_capacitor(
        90, 52, 200, 100,
        blocks=[
            {"y_frac": 0.0, "h_frac": 0.28, "fill": "soft", "label": "vidrio κ₁ = 4"},
            {"y_frac": 0.28, "h_frac": 0.72, "fill": "paperf", "label": "aire κ₂ = 1"},
        ],
        plate_labels=("+Q  (V = 6,5 kV)", "−Q"),
    )
    d.dimension((305, 52), (305, 80), text="d₁", label_side="right", label_offset=10)
    d.dimension((305, 80), (305, 152), text="d₂", label_side="right", label_offset=10)
    d.text(345, 70, "1 mm", cls="t", anchor="start")
    d.text(345, 120, "3 mm", cls="t", anchor="start")
    return d


def esferico_dos_capas():
    d = FieldGeometryDiagram(490, 235, "Capacitor esférico con dos capas dieléctricas concéntricas")
    cx, cy = 135, 118
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 92, "fill": "csoft", "stroke": "wk"},
            {"r_out": 60, "fill": "soft", "stroke": "w"},
            {"r_out": 24, "fill": "paperf", "stroke": "w"},
        ],
    )
    d.text(cx - 8, cy + 5, "+Q", cls="tc", anchor="end")
    _rad_label(d, cx, cy, 24, -50, "a", text_frac=0.65, off_deg=22)
    _rad_label(d, cx, cy, 60, 5, "b", text_frac=0.72, off_deg=14)
    _rad_label(d, cx, cy, 92, 65, "c", text_frac=0.82, off_deg=10)
    p_k1 = d._polar_svg(cx, cy, 42, 130)
    p_k2 = d._polar_svg(cx, cy, 76, 135)
    d.text(p_k1[0], p_k1[1] + 4, "κ₁", cls="sa")
    d.text(p_k2[0], p_k2[1] + 4, "κ₂", cls="sc")
    d.text(cx - 72, cy - 72, "−Q", cls="ta", anchor="end")
    d.text(255, 82, "a < r < b : ε₁ = κ₁ε₀", cls="sa", anchor="start")
    d.text(255, 114, "b < r < c : ε₂ = κ₂ε₀", cls="sc", anchor="start")
    d.text(255, 146, "Mismo D(r) = Q/(4πr²)", cls="s", anchor="start")
    d.text(255, 178, "Capas en serie", cls="t", anchor="start")
    return d


def examen_2025_2_p1():
    d = FieldGeometryDiagram(450, 240, "Tres placas conductoras paralelas con dieléctricos ε₁ y ε₂ y terminal central a")
    x0, x1 = 115, 315
    y_top, y_mid, y_bot = 46, 118, 190
    d.raw(f'<rect class="soft nostroke" x="{x0}" y="{y_top+6}" width="{x1-x0}" height="{y_mid-y_top-6}"/>', layer="bg")
    d.raw(f'<rect class="csoft nostroke" x="{x0}" y="{y_mid+6}" width="{x1-x0}" height="{y_bot-y_mid-6}"/>', layer="bg")
    d.text((x0 + x1) / 2, (y_top + y_mid) / 2 + 7, "ε₁", cls="sa")
    d.text((x0 + x1) / 2, (y_mid + y_bot) / 2 + 7, "ε₂", cls="sc")

    for yp in (y_top, y_mid, y_bot):
        d.raw(f'<rect class="inkf nostroke" x="{x0}" y="{yp}" width="{x1-x0}" height="6"/>', layer="wires")
    d.text(x0 + 26, y_mid - 6, "+Q", cls="tc")

    d.wire((x0, y_mid + 3), (62, y_mid + 3), (62, 222))
    d.terminal_open("ta", 62, 222, text="a", label_dir="left", offset=10)

    d.wire((x1, y_top + 3), (368, y_top + 3), (368, 222))
    d.wire((x1, y_bot + 3), (368, y_bot + 3))
    d.node("nj", 368, y_bot + 3, draw_dot=True)
    d.terminal_open("tb", 368, 222, text="b", label_dir="right", offset=10)

    d.dimension((x0 - 16, y_top + 6), (x0 - 16, y_mid), text="d", label_side="left", label_offset=10)
    d.dimension((x0 - 16, y_mid + 6), (x0 - 16, y_bot), text="d", label_side="left", label_offset=10)
    d.text(215, 226, "Vab = Va − Vb", cls="s")
    d.text(215, 26, "Placas de área A", cls="t")
    return d


def examen_2018_2_p2():
    d = FieldGeometryDiagram(485, 240, "Cable coaxial con dieléctrico ε entre r = a y r = b y cascarón externo entre b y c")
    cx, cy = 140, 120
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 94, "fill": "paperf", "stroke": "wk"},
            {"r_out": 74, "fill": "soft", "stroke": "w"},
            {"r_out": 28, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[{"r": 50, "cls": "cd"}],
    )
    d.text(cx - 10, cy + 5, "+Q", cls="tc", anchor="end")
    _rad_label(d, cx, cy, 28, -50, "a", text_frac=0.65, off_deg=22)
    _rad_label(d, cx, cy, 74, 5, "b", text_frac=0.76, off_deg=14)
    _rad_label(d, cx, cy, 94, 65, "c", text_frac=0.88, off_deg=10)
    pg = d._polar_svg(cx, cy, 50, 128)
    d.text(pg[0] - 8, pg[1] - 4, "r", cls="sc", anchor="end")
    p_e = d._polar_svg(cx, cy, 62, -125)
    d.text(p_e[0], p_e[1] + 5, "ε", cls="sa")
    d.text(cx - 72, cy - 72, "−Q", cls="ta", anchor="end")
    d.text(268, 68, "r < a : conductor (+Q)", cls="tc", anchor="start")
    d.text(268, 98, "a < r < b : dieléctrico ε", cls="sa", anchor="start")
    d.text(268, 128, "b < r < c : conductor (−Q)", cls="t", anchor="start")
    d.text(268, 158, "r > c : exterior", cls="t", anchor="start")
    d.text(268, 190, "L ≫ c", cls="s", anchor="start")
    return d


def practica_red():
    d = FieldGeometryDiagram(460, 210, "Red mixta de capacitor plano C₁ en serie con paralelo de C₂ y C₃")
    d.terminal_open("A", 42, 105, text="A", label_dir="left", offset=10)
    d.node("N", 190, 105, draw_dot=True)
    d.terminal_open("B", 418, 105, text="B", label_dir="right", offset=10)
    d.capacitor("A", "N", text="C₁ (plano)", label_side="top", offset=24)
    d.parallel_group(
        "N", "B",
        branches=[
            {"kind": "capacitor", "dy": -42, "label": "C₂ (cilíndrico)", "label_side": "top", "offset": 22},
            {"kind": "capacitor", "dy": 42, "label": "C₃ (esférico)", "label_side": "bottom", "offset": 26},
        ],
        lead=30,
    )
    return d


def practica_hemisferio():
    d = FieldGeometryDiagram(510, 235, "Capacitor esférico con la mitad inferior llena de dieléctrico κ")
    cx, cy = 135, 118
    ra, rb, rc = 26, 74, 84
    d.raw(f'<circle class="paperf wk" cx="{cx}" cy="{cy}" r="{rc}"/>', layer="bg")
    d.raw(f'<circle class="paperf w" cx="{cx}" cy="{cy}" r="{rb}"/>', layer="bg")
    d.raw(
        f'<path class="soft w" d="M {cx-rb} {cy} A {rb} {rb} 0 0 0 {cx+rb} {cy} Z"/>',
        layer="bg",
    )
    d.raw(f'<circle class="csoft w" cx="{cx}" cy="{cy}" r="{ra}"/>', layer="overlay")
    d.line((cx - rb, cy), (cx + rb, cy), cls="md")
    d.text(cx, cy + 5, "+Q", cls="tc")
    d.text(cx, cy - 48, "vacío (κ = 1)", cls="t")
    d.text(cx, cy + 52, "dieléctrico κ", cls="sa")
    _rad_label(d, cx, cy, ra, 140, "ra", text_frac=1.35, off_deg=18)
    _rad_label(d, cx, cy, rb, 22, "rb", text_frac=0.72, off_deg=14)
    d.text(cx - 68, cy - 68, "−Q", cls="ta", anchor="end")
    d.text(248, 86, "Mitad sup. (CU): vacío", cls="t", anchor="start")
    d.text(248, 116, "Mitad inf. (CL): dieléctrico κ", cls="sa", anchor="start")
    d.text(248, 148, "Mismo ΔV → paralelo", cls="s", anchor="start")
    return d


def practica_coaxial_2():
    d = FieldGeometryDiagram(485, 235, "Cable coaxial con dos mantos dieléctricos κ₁ y κ₂ entre R, 2R y 3R")
    cx, cy = 138, 118
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 90, "fill": "paperf", "stroke": "wk"},
            {"r_out": 78, "fill": "csoft", "stroke": "w"},
            {"r_out": 52, "fill": "soft", "stroke": "w"},
            {"r_out": 26, "fill": "csoft", "stroke": "wk"},
        ],
    )
    d.text(cx - 10, cy + 5, "+Q", cls="tc", anchor="end")
    _rad_label(d, cx, cy, 26, -50, "R", text_frac=0.65, off_deg=22)
    _rad_label(d, cx, cy, 52, 5, "2R", text_frac=0.72, off_deg=16)
    _rad_label(d, cx, cy, 78, 70, "3R", text_frac=0.80, off_deg=12)
    p1 = d._polar_svg(cx, cy, 39, 130)
    p2 = d._polar_svg(cx, cy, 65, 135)
    d.text(p1[0], p1[1] + 4, "κ₁", cls="sa")
    d.text(p2[0], p2[1] + 4, "κ₂", cls="sc")
    d.text(255, 76, "R < r < 2R : κ₁", cls="sa", anchor="start")
    d.text(255, 108, "2R < r < 3R : κ₂", cls="sc", anchor="start")
    d.text(255, 140, "3R < r < 3,25R : metal", cls="t", anchor="start")
    d.text(255, 172, "Batería V = 12 V", cls="s", anchor="start")
    return d


def practica_cascara():
    d = FieldGeometryDiagram(485, 235, "Esfera conductora cargada rodeada por vacío y cáscara dieléctrica κ")
    cx, cy = 138, 118
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 88, "fill": "soft", "stroke": "w"},
            {"r_out": 52, "fill": "paperf", "stroke": "w"},
            {"r_out": 24, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[{"r": 70, "cls": "ad"}],
    )
    d.text(cx - 8, cy + 5, "+Q", cls="tc", anchor="end")
    _rad_label(d, cx, cy, 24, -50, "r₀", text_frac=0.65, off_deg=22)
    _rad_label(d, cx, cy, 52, 5, "ri", text_frac=0.72, off_deg=16)
    _rad_label(d, cx, cy, 88, 70, "re", text_frac=0.82, off_deg=12)
    pk = d._polar_svg(cx, cy, 70, -135)
    d.text(pk[0] - 8, pk[1] + 10, "r", cls="sa", anchor="end")
    pk2 = d._polar_svg(cx, cy, 60, 148)
    d.text(pk2[0], pk2[1] + 4, "κ", cls="sa")
    d.text(258, 82, "r < r₀ : conductor (+Q)", cls="tc", anchor="start")
    d.text(258, 114, "r₀ < r < ri : vacío", cls="t", anchor="start")
    d.text(258, 146, "ri < r < re : dieléctrico κ", cls="sa", anchor="start")
    d.text(258, 178, "r > re : vacío", cls="t", anchor="start")
    return d


def practica_fuerza_diel():
    d = FieldGeometryDiagram(430, 215, "Bloque dieléctrico κ parcialmente insertado en un capacitor cuadrado aislado")
    d.dielectric_capacitor(
        75, 58, 250, 82,
        blocks=[
            {"x_frac": 0.0, "w_frac": 0.42, "fill": "paperf"},
            {"x_frac": 0.42, "w_frac": 0.58, "fill": "soft", "label": "κ"},
        ],
        plate_labels=("+Q (aislado)", "−Q"),
    )
    d.text(127, 82, "vacío", cls="s")
    d.node("O", 75, 140, text="O", label_dir="left", offset=10)
    d.dimension((75, 176), (180, 176), text="x", label_side="bottom", label_offset=10)
    d.dimension((180, 176), (325, 176), text="a − x", label_side="bottom", label_offset=10)
    d.dimension((342, 58), (342, 140), text="d", label_side="right", label_offset=10)
    _arrow_on(d, (176, 114), (128, 114), cls="c")
    d.text(152, 105, "F⃗", cls="sc")
    return d


def figures():
    return {
        "u04-geometrias": geometrias(),
        "u04-serie-paralelo": serie_paralelo(),
        "u04-energia-u": energia_u(),
        "u04-polarizacion": polarizacion(),
        "u04-gauss-diel": gauss_diel(),
        "u04-diel-serie-paralelo": diel_serie_paralelo(),
        "u04-bateria-diel": bateria_diel(),
        "u04-lamina-parcial": lamina_parcial(),
        "u04-esferico-dos-capas": esferico_dos_capas(),
        "u04-examen-2025-2-p1": examen_2025_2_p1(),
        "u04-examen-2018-2-p2": examen_2018_2_p2(),
        "u04-practica-red": practica_red(),
        "u04-practica-hemisferio": practica_hemisferio(),
        "u04-practica-coaxial-2": practica_coaxial_2(),
        "u04-practica-cascara": practica_cascara(),
        "u04-practica-fuerza-diel": practica_fuerza_diel(),
    }
