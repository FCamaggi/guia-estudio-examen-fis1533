"""U5 Current, Resistance & EMF figures. Generate with: python3 scripts/build_figures.py u05"""

from svg_primitives import FieldGeometryDiagram, arrow


def _arrow_on(d, p1, p2, cls="a", head_len=7, head_w=3.5):
    hcls = {"a": "af", "c": "cf", "m": "mf", "w": "inkf"}.get(cls, "af")
    d.raw(arrow(p1[0], p1[1], p2[0], p2[1], line_cls=cls, head_cls=hcls, head_len=head_len, head_w=head_w))


def deriva_j():
    d = FieldGeometryDiagram(560, 240, "Portadores positivos y negativos bajo un campo eléctrico E⃗: velocidad de deriva y densidad de corriente J⃗")

    # Panel superior: portadores positivos + elemento de volumen A v dt
    y_top = 66
    x0, x1 = 42, 340
    d.raw(f'<rect class="paperf w" x="{x0}" y="{y_top-28}" width="{x1-x0}" height="56" rx="4"/>', layer="bg")
    sx0, sx1 = 188, 256
    d.raw(f'<rect class="soft nostroke" x="{sx0}" y="{y_top-28}" width="{sx1-sx0}" height="56"/>', layer="bg")
    d.raw(f'<ellipse class="soft a" cx="{sx0}" cy="{y_top}" rx="8" ry="28"/>', layer="wires")
    d.raw(f'<ellipse class="soft a" cx="{sx1}" cy="{y_top}" rx="8" ry="28"/>', layer="wires")
    d.text(sx1 + 14, y_top - 32, "A", cls="sa", anchor="start")
    d.dimension((sx0, y_top + 36), (sx1, y_top + 36), text="v dt", label_side="bottom", label_offset=10)

    for px, py in ((92, y_top - 10), (132, y_top + 10), (222, y_top - 4)):
        d.point_charge((px, py), sign="+", r=7.5)
        _arrow_on(d, (px + 10, py), (px + 34, py), cls="a")
    d.text(118, y_top - 36, "q > 0", cls="tc")
    d.text(158, y_top - 2, "v⃗", cls="sa")

    # Panel inferior: portadores negativos
    y_bot = 176
    d.raw(f'<rect class="paperf w" x="{x0}" y="{y_bot-28}" width="{x1-x0}" height="56" rx="4"/>', layer="bg")
    for px, py in ((110, y_bot - 10), (185, y_bot + 10), (265, y_bot - 6)):
        d.point_charge((px, py), sign="-", r=7.5)
        _arrow_on(d, (px - 10, py), (px - 34, py), cls="a")
    d.text(118, y_bot - 36, "q < 0", cls="ta")
    d.text(146, y_bot + 14, "v⃗", cls="sa")

    # Flechas de E y J a la derecha
    _arrow_on(d, (380, 62), (465, 62), cls="c")
    d.text(475, 67, "E⃗", cls="sc", anchor="start")
    _arrow_on(d, (380, 96), (465, 96), cls="a")
    d.text(475, 101, "J⃗, I", cls="sa", anchor="start")

    d.text(380, 148, "En ambos casos:", cls="tb", anchor="start")
    d.text(380, 172, "J⃗ = n q v⃗   y   I = n |q| A v", cls="s", anchor="start")
    d.text(380, 196, "Mismo sentido que", cls="t", anchor="start")
    d.text(500, 196, "E⃗", cls="sc", anchor="start")
    return d


def continuidad_ohm():
    d = FieldGeometryDiagram(580, 230, "Continuidad en un conductor que se estrecha y dependencia térmica de la resistividad ρ(T)")

    pts = "28,62 115,62 155,86 262,86 262,130 155,130 115,154 28,154"
    d.raw(f'<polygon class="soft w" points="{pts}"/>', layer="bg")
    d.raw('<ellipse class="csoft w" cx="68" cy="108" rx="10" ry="46"/>', layer="wires")
    d.raw('<ellipse class="csoft w" cx="224" cy="108" rx="6" ry="22"/>', layer="wires")
    d.text(68, 50, "A₁", cls="sc")
    d.text(224, 76, "A₂", cls="sc")

    _arrow_on(d, (34, 92), (56, 92), cls="a")
    _arrow_on(d, (34, 124), (56, 124), cls="a")
    d.text(44, 176, "J₁ = I/A₁", cls="sa")

    _arrow_on(d, (176, 100), (214, 100), cls="a")
    _arrow_on(d, (176, 116), (214, 116), cls="a")
    d.text(215, 176, "J₂ = I/A₂ > J₁", cls="sa")

    d.text(112, 28, "Estacionario: I₁ = I₂", cls="tb")
    d.text(212, 28, "(∇·J⃗ = 0)", cls="sa")
    d.text(145, 210, "(a) Conservación de carga", cls="t")

    d.line((296, 20), (296, 212), cls="md")

    metal = [(0.0, 0.35), (1.0, 0.85)]
    semi = [(0.0, 0.90), (0.35, 0.62), (0.7, 0.42), (1.0, 0.28)]
    d.function_plot(
        345, 42, 195, 125,
        (0, 1), (0, 1),
        [metal],
        v_lines=[(0.4, "T₀")],
        h_lines=[(0.55, "ρ₀")],
        x_label="T", y_label="ρ(T)", cls="c",
    )
    px = lambda vx: 345 + vx * 195
    py = lambda vy: 42 + 125 - vy * 125
    semi_pts = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in semi)
    d.raw(f'<polyline class="a" points="{semi_pts}"/>', layer="overlay")
    d.text(530, 52, "metal (α > 0)", cls="tc", anchor="end")
    d.text(535, 152, "semicond. (α < 0)", cls="ta", anchor="end")
    d.text(442, 210, "(b) Dependencia térmica", cls="t")
    return d


def geometrias_r():
    d = FieldGeometryDiagram(600, 235, "Tres estrategias para calcular resistencia: rebanadas en serie, cáscaras radiales y bloques en paralelo")

    # Panel (a): Cono truncado
    x0, x1, yc = 28, 166, 102
    ra, rb = 18, 46
    cone_pts = f"{x0},{yc-ra} {x1},{yc-rb} {x1},{yc+rb} {x0},{yc+ra}"
    d.raw(f'<polygon class="paperf w" points="{cone_pts}"/>', layer="bg")
    rx_l = ra + (rb - ra) * (94 - x0) / (x1 - x0)
    rx_r = ra + (rb - ra) * (106 - x0) / (x1 - x0)
    sl_pts = f"94,{yc-rx_l:.1f} 106,{yc-rx_r:.1f} 106,{yc+rx_r:.1f} 94,{yc+rx_l:.1f}"
    d.raw(f'<polygon class="soft a" points="{sl_pts}"/>', layer="wires")
    d.line((x0, yc), (x1, yc), cls="md")
    d.text(x0 - 8, yc + 4, "a", cls="s", anchor="end")
    d.text(x1 + 8, yc + 4, "b", cls="s", anchor="start")
    d.text(100, yc - rx_r - 10, "dx", cls="sa")
    _arrow_on(d, (16, yc - 34), (44, yc - 34), cls="a")
    d.text(28, yc - 42, "I", cls="sa")
    d.dimension((x0, yc + 62), (x1, yc + 62), text="h", label_side="bottom", label_offset=10)
    d.text(98, 214, "(a) Serie: dR = ρ dx / A(x)", cls="t")

    # Panel (b): Cilindro hueco flujo radial
    cx, cy = 298, 102
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 64, "fill": "paperf", "stroke": "wk"},
            {"r_out": 20, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[{"r": 42, "cls": "ad"}],
    )
    d.radius_dim((cx, cy), -40, 20, text="a", cls="m")
    d.radius_dim((cx, cy), 18, 64, text="b", cls="m")
    pg = d._polar_svg(cx, cy, 42, 135)
    d.text(pg[0] + 6, pg[1] + 10, "r", cls="sa", anchor="start")
    for deg in (80, 175, 265):
        p1 = d._polar_svg(cx, cy, 24, deg)
        p2 = d._polar_svg(cx, cy, 58, deg)
        _arrow_on(d, p1, p2, cls="a")
    d.text(cx, 214, "(b) Radial: A(r) = 2πrL", cls="t")

    # Panel (c): Paralelo
    bx, by, bw, bh = 434, 54, 128, 96
    d.raw(f'<rect class="inkf nostroke" x="{bx-7}" y="{by}" width="7" height="{bh}"/>', layer="wires")
    d.raw(f'<rect class="inkf nostroke" x="{bx+bw}" y="{by}" width="7" height="{bh}"/>', layer="wires")
    d.raw(f'<rect class="soft w" x="{bx}" y="{by}" width="{bw}" height="{bh/2}"/>', layer="bg")
    d.raw(f'<rect class="csoft w" x="{bx}" y="{by+bh/2}" width="{bw}" height="{bh/2}"/>', layer="bg")
    d.text(bx + bw / 2, by + bh * 0.25 + 5, "σ₁", cls="s")
    d.text(bx + bw / 2, by + bh * 0.75 + 5, "σ₂", cls="s")
    _arrow_on(d, (bx + 18, by + 16), (bx + 54, by + 16), cls="a")
    _arrow_on(d, (bx + 18, by + bh - 16), (bx + 54, by + bh - 16), cls="a")
    d.text(bx - 14, by + bh / 2 + 5, "a", cls="s", anchor="end")
    d.text(bx + bw + 14, by + bh / 2 + 5, "b", cls="s", anchor="start")
    d.text(bx + bw / 2, 214, "(c) Paralelo: 1/R = 1/R₁ + 1/R₂", cls="t")
    return d


def fuente_real():
    d = FieldGeometryDiagram(585, 240, "Circuito de una malla con fuente real (fem ε y resistencia interna r) y perfil de potencial")

    # Circuito a la izquierda
    d.node("a", 50, 68, text="a", label_dir="left", offset=12)
    d.node("b", 240, 68, text="b", label_dir="right", offset=12)
    d.real_battery("a", "b", emf_text="ε", r_text="r", positive_at="p2", label_side="top")
    d.wire("b", (240, 170))
    d.wire("a", (50, 170))
    d.resistor((240, 170), (50, 170), text="R", label_side="bottom", offset=22)

    d.current_arrow((190, 202), (100, 202), text="I", cls="a", label_side="bottom", offset=12)
    d.text(145, 20, "Batería real: V(b) − V(a) = ε − Ir", cls="tc")

    # Gráfico de potencial a la derecha
    gx, gy, gw, gh = 330, 46, 185, 126
    _arrow_on(d, (gx, gy + gh), (gx + gw + 10, gy + gh), cls="w", head_len=6, head_w=3)
    _arrow_on(d, (gx, gy + gh), (gx, gy - 12), cls="w", head_len=6, head_w=3)
    d.text(gx + gw + 14, gy + gh + 4, "recorrido", cls="t", anchor="start")
    d.text(gx - 6, gy - 14, "V", cls="s", anchor="end")

    y0 = gy + gh
    y_eps = gy + 16
    y_vba = gy + 52
    pts = [
        (gx, y0),
        (gx + 30, y0),
        (gx + 30, y_eps),
        (gx + 54, y_eps),
        (gx + 82, y_vba),
        (gx + 118, y_vba),
        (gx + 164, y0),
        (gx + 180, y0),
    ]
    d.wire(*pts, cls="c")
    d.line((gx, y_eps), (gx + 30, y_eps), cls="md")
    d.text(gx - 6, y_eps + 4, "ε", cls="s", anchor="end")
    d.line((gx, y_vba), (gx + 82, y_vba), cls="md")
    d.text(gx - 6, y_vba + 4, "ε−Ir", cls="s", anchor="end")
    d.text(gx + 15, y0 + 16, "a", cls="s")
    d.text(gx + 42, y0 + 16, "ε", cls="s")
    d.text(gx + 68, y0 + 16, "r", cls="s")
    d.text(gx + 100, y0 + 16, "b", cls="s")
    d.text(gx + 142, y0 + 16, "R", cls="s")
    return d


def potencia_max():
    d = FieldGeometryDiagram(460, 235, "Potencia entregada a la carga R en función de la razón R/r")
    pts = []
    for k in range(0, 81):
        u = k * 0.05
        p = 4.0 * u / ((1.0 + u) ** 2)
        pts.append((u, p))
    d.function_plot(
        78, 36, 260, 142,
        (0, 4.0), (0, 1.15),
        [pts],
        v_lines=[(1.0, "R = r")],
        h_lines=[(1.0, "Pₘₐₓ")],
        x_label="R / r", y_label="P / Pₘₐₓ", cls="a",
    )
    d.text(350, 74, "Pₘₐₓ = ε² / (4r)", cls="sa", anchor="start")
    d.text(350, 98, "en R = r (η = 50 %)", cls="t", anchor="start")
    d.text(350, 134, "si R ≫ r: P baja,", cls="t", anchor="start")
    d.text(350, 152, "pero η → 100 %", cls="t", anchor="start")
    return d


def arq1_coaxial_capas():
    d = FieldGeometryDiagram(490, 240, "Cable coaxial con dos capas cilíndricas de conductividades σ₁ y σ₂ entre radios a, b y c")
    cx, cy = 148, 120
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 90, "fill": "paperf", "stroke": "wk", "label": "σ₂", "label_deg": 135},
            {"r_out": 58, "fill": "soft", "stroke": "w", "label": "σ₁", "label_deg": 135},
            {"r_out": 22, "fill": "csoft", "stroke": "w"},
        ],
        gaussian_radii=[{"r": 58, "cls": "cd"}],
    )
    d.radius_dim((cx, cy), -140, 22, text="a", cls="m")
    d.radius_dim((cx, cy), -42, 58, text="b", cls="m")
    d.radius_dim((cx, cy), 12, 90, text="c", cls="m")
    for deg in (75, 220):
        p1 = d._polar_svg(cx, cy, 26, deg)
        p2 = d._polar_svg(cx, cy, 80, deg)
        _arrow_on(d, p1, p2, cls="a")
    p_j = d._polar_svg(cx, cy, 102, 75)
    d.text(p_j[0] + 4, p_j[1] + 4, "J⃗", cls="sa", anchor="start")

    d.text(274, 56, "Núcleo (r ≤ a) a potencial +V₀", cls="tc", anchor="start")
    d.text(274, 82, "Capa 1 (a < r < b): σ₁", cls="ta", anchor="start")
    d.text(274, 106, "Capa 2 (b < r < c): σ₂", cls="t", anchor="start")
    d.text(274, 132, "Exterior (r = c) a potencial 0", cls="t", anchor="start")
    d.text(274, 164, "Interfaz r = b:", cls="tb", anchor="start")
    d.text(374, 164, "σ₁ E₁ = σ₂ E₂", cls="s", anchor="start")
    d.text(274, 190, "Largo del cable: L", cls="t", anchor="start")
    return d


def arq2_esferas():
    d = FieldGeometryDiagram(480, 235, "Cascarones esféricos concéntricos de radios a y b con material conductor óhmico entre ellos")
    cx, cy = 148, 118
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 90, "fill": "paperf", "stroke": "wk"},
            {"r_out": 82, "fill": "soft", "stroke": "w"},
            {"r_out": 24, "fill": "csoft", "stroke": "w", "label": "+Q", "label_cls": "tc", "label_deg": 180},
        ],
        gaussian_radii=[{"r": 54, "cls": "ad"}],
    )
    d.radius_dim((cx, cy), -35, 24, text="a", cls="m")
    d.radius_dim((cx, cy), 15, 82, text="b", cls="m")
    pg = d._polar_svg(cx, cy, 54, 140)
    d.text(pg[0] - 8, pg[1] - 4, "r", cls="sa", anchor="end")
    for deg in (75, 245):
        p1 = d._polar_svg(cx, cy, 28, deg)
        p2 = d._polar_svg(cx, cy, 76, deg)
        _arrow_on(d, p1, p2, cls="a")
    pe = d._polar_svg(cx, cy, 102, 72)
    d.text(pe[0] + 4, pe[1] + 2, "J⃗, E⃗", cls="sa", anchor="start")
    d.text(cx - 60, cy - 72, "−Q", cls="ta", anchor="end")

    d.text(272, 66, "Esfera interior r = a: V = V₀", cls="tc", anchor="start")
    d.text(272, 94, "Cascarón exterior r = b: V = 0", cls="t", anchor="start")
    d.text(272, 126, "Medio óhmico (a < r < b):", cls="ta", anchor="start")
    d.text(272, 150, "conductividad", cls="t", anchor="start")
    d.text(364, 150, "σ (o ρ = 1/σ)", cls="s", anchor="start")
    d.text(272, 180, "Área esférica:", cls="t", anchor="start")
    d.text(362, 180, "A(r) = 4πr²", cls="s", anchor="start")
    return d


def prac_conos():
    d = FieldGeometryDiagram(560, 235, "Tres arreglos de dos conos truncados idénticos: dos en serie (I y II) y uno en paralelo (III)")

    def _cone(x0, x1, yc, r0, r1, fill="soft"):
        pts = f"{x0},{yc-r0} {x1},{yc-r1} {x1},{yc+r1} {x0},{yc+r0}"
        d.raw(f'<polygon class="{fill} w" points="{pts}"/>', layer="bg")

    # (I) Serie ancho-con-ancho
    yc1 = 62
    d.line((26, yc1), (42, yc1), cls="w")
    _cone(42, 98, yc1, 10, 22, "soft")
    _cone(98, 154, yc1, 22, 10, "soft")
    d.line((154, yc1), (170, yc1), cls="w")
    d.text(20, yc1 + 4, "A", cls="s", anchor="end")
    d.text(176, yc1 + 4, "B", cls="s", anchor="start")
    d.text(98, 104, "(I) Serie: radios a → b → a", cls="t")

    # (II) Serie angosto-con-angosto
    yc2 = 166
    d.line((26, yc2), (42, yc2), cls="w")
    _cone(42, 98, yc2, 22, 10, "csoft")
    _cone(98, 154, yc2, 10, 22, "csoft")
    d.line((154, yc2), (170, yc2), cls="w")
    d.text(20, yc2 + 4, "A", cls="s", anchor="end")
    d.text(176, yc2 + 4, "B", cls="s", anchor="start")
    d.text(98, 208, "(II) Serie: radios b → a → b", cls="t")

    d.line((220, 24), (220, 214), cls="md")

    # (III) Paralelo entre dos placas equipotenciales A y B
    px0, px1 = 315, 425
    d.raw(f'<rect class="inkf nostroke" x="{px0-7}" y="42" width="7" height="140"/>', layer="wires")
    d.raw(f'<rect class="inkf nostroke" x="{px1}" y="42" width="7" height="140"/>', layer="wires")
    d.line((270, 112), (px0 - 7, 112), cls="w")
    d.line((px1 + 7, 112), (470, 112), cls="w")
    _cone(px0, px1, 78, 10, 22, "soft")
    _cone(px0, px1, 146, 10, 22, "csoft")
    d.text(262, 116, "A", cls="s", anchor="end")
    d.text(478, 116, "B", cls="s", anchor="start")
    _arrow_on(d, (275, 96), (302, 96), cls="a")
    d.text(288, 86, "I", cls="sa")
    d.text(370, 208, "(III) Paralelo entre electrodos", cls="t")
    return d


def figures():
    return {
        "u05-deriva-j": deriva_j(),
        "u05-continuidad-ohm": continuidad_ohm(),
        "u05-geometrias-r": geometrias_r(),
        "u05-fuente-real": fuente_real(),
        "u05-potencia-max": potencia_max(),
        "u05-arq1-coaxial-capas": arq1_coaxial_capas(),
        "u05-arq2-esferas": arq2_esferas(),
        "u05-prac-conos": prac_conos(),
    }
