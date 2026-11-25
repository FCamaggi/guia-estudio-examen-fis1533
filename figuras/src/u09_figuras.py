"""U9 Induction figures. Generate with: python3 scripts/build_figures.py u09"""

from svg_primitives import FieldGeometryDiagram, field_cross, field_dot


def _crosses_in_circle(d, cx, cy, r, step=28):
    y = cy - r
    while y <= cy + r:
        x = cx - r
        while x <= cx + r:
            if (x - cx) ** 2 + (y - cy) ** 2 <= (r - 8) ** 2:
                d.raw(field_cross(x, y), layer="bg")
            x += step
        y += step


def flujo_angulo():
    d = FieldGeometryDiagram(440, 250, "Espira plana vista de canto en un campo uniforme: normal y ángulos")
    cx, cy = 210, 128
    for y in (34, 222):
        d.current_arrow((30, y), (410, y), cls="c")
    d.text(418, 30, "B⃗", cls="sc", anchor="start")
    a = d._polar_svg(cx, cy, 78, 120)
    b = d._polar_svg(cx, cy, 78, 300)
    d.line(a, b, cls="wk")
    d.text(a[0] - 8, a[1] + 4, "espira (de canto)", cls="t", anchor="end")
    d.line((cx, cy), (cx + 120, cy), cls="md")
    d.text(cx + 128, cy + 5, "dirección del campo", cls="t", anchor="start")
    tip = d._polar_svg(cx, cy, 84, 30)
    d.current_arrow((cx, cy), tip, cls="a")
    d.text(tip[0] + 8, tip[1] - 2, "n̂", cls="sa", anchor="start")
    d.angle_arc((cx, cy), 0, 30, r=46, text="φ")
    d.angle_arc((cx, cy), -60, 0, r=30, text="θ")
    return d


def signo_normal():
    d = FieldGeometryDiagram(460, 210, "Regla de la mano derecha: normal y sentido positivo de la fem")
    for cx, kind, cdir, txt in ((120, "⊙", "ccw", "normal saliendo de la hoja"), (340, "⊗", "cw", "normal entrando a la hoja")):
        cy = 95
        d.raw(f'<circle class="w nofill" cx="{cx}" cy="{cy}" r="58"/>', layer="wires")
        d.arc_wire((cx, cy), 58, 70, 110, cls="w", current_dir=cdir, current_cls="a", arrow_span_deg=60)
        d.arc_wire((cx, cy), 58, 250, 290, cls="w", current_dir=cdir, current_cls="a", arrow_span_deg=60)
        d.text(cx, cy + 7, kind, cls="sa")
        d.text(cx, cy + 92, txt, cls="t")
        d.text(cx, cy + 108, "ε > 0: " + ("antihorario" if cdir == "ccw" else "horario"), cls="ta")
    return d


def espira_entrando():
    d = FieldGeometryDiagram(460, 240, "Espira cuadrada entrando a una región de campo magnético entrante")
    d.field_region(250, 40, 430, 205, step=30, direction="in")
    d.line((232, 20), (232, 220), cls="md")
    d.text(440, 32, "B⃗ ⊗", cls="sc", anchor="end")
    d.wire((172, 70), (292, 70), (292, 190), (172, 190), (172, 70))
    d.current_arrow((180, 50), (250, 50), text="v⃗", cls="a", label_side="top", offset=8)
    d.dimension((232, 205), (292, 205), text="x", offset=0, label_side="bottom", label_offset=10)
    d.dimension((158, 70), (158, 190), text="a", label_side="left", label_offset=8)
    d.text(110, 225, "B = 0", cls="t")
    return d


def alambre_espira():
    d = FieldGeometryDiagram(470, 270, "Alambre infinito con corriente y espira rectangular coplanar que se aleja")
    d.field_region(100, 30, 450, 240, step=30, direction="in")
    d.line((60, 15), (60, 255), cls="wk")
    d.current_arrow((44, 170), (44, 110), text="I", cls="a", label_side="left", offset=8)
    x0, x1, y0, y1 = 150, 310, 75, 195
    d.raw(f'<rect class="soft" x="214" y="{y0}" width="12" height="{y1 - y0}"/>', layer="bg")
    d.wire((x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0))
    d.text(220, y0 - 8, "ds", cls="s")
    d.dimension((60, 220), (x0, 220), text="r", label_side="bottom", label_offset=10)
    d.dimension((x0, 220), (x1, 220), text="w", label_side="bottom", label_offset=10)
    d.dimension((x1 + 14, y0), (x1 + 14, y1), text="ℓ", label_side="right", label_offset=8)
    d.current_arrow((340, 60), (400, 60), text="v⃗", cls="a", label_side="top", offset=8)
    d.text(455, 26, "B⃗ ⊗ (lado derecho)", cls="sc", anchor="end")
    return d


def barra_rieles():
    d = FieldGeometryDiagram(460, 240, "Barra conductora sobre rieles con resistencia en un campo entrante")
    d.motional_rail_circuit(85, 60, width=290, height=130, bar_x=270, v_text="v⃗", B_dir="in",
                            left_elem="resistor", left_label="R", bar_label="ℓ")
    d.text(440, 36, "B⃗ ⊗", cls="sc", anchor="end")
    d.text(200, 225, "x: distancia de R a la barra", cls="t")
    return d


def barra_bateria():
    d = FieldGeometryDiagram(460, 240, "Barra sobre rieles con batería en un campo saliente")
    d.motional_rail_circuit(85, 60, width=290, height=130, bar_x=270, v_text="v⃗", B_dir="out",
                            left_elem="battery", left_label="V₀", bar_label="b")
    d.text(440, 36, "B⃗ ⊙", cls="sc", anchor="end")
    d.text(225, 225, "R: resistencia total del circuito", cls="t")
    return d


def frenado_vt():
    import math
    d = FieldGeometryDiagram(420, 230, "Velocidad de la barra frenada: decaimiento exponencial")
    pts = [(t / 20, math.exp(-t / 20)) for t in range(0, 101)]
    d.function_plot(60, 40, 300, 140, (0, 5), (0, 1.1), [pts], v_lines=[(1, "τ")],
                    h_lines=[(1, "v₀"), (math.exp(-1), "0.37 v₀")], x_label="t", y_label="v(t)")
    return d


def solenoide_e():
    d = FieldGeometryDiagram(470, 280, "Sección de un solenoide con campo creciente y campo eléctrico inducido")
    cx, cy, b = 165, 140, 72
    d.raw(f'<circle class="soft" cx="{cx}" cy="{cy}" r="{b}"/>', layer="bg")
    _crosses_in_circle(d, cx, cy, b)
    d.raw(f'<circle class="w nofill" cx="{cx}" cy="{cy}" r="{b}"/>', layer="wires")
    d.amperian_loop((cx, cy), 40, ccw=True, cls="a", dashed=True)
    d.amperian_loop((cx, cy), 112, ccw=True, cls="a", dashed=True)
    d.radius_dim((cx, cy), -35, b, text="b")
    d.text(cx, cy - 40 - 10, "E⃗", cls="sa")
    d.text(cx + 14, cy - 112 - 6, "E⃗", cls="sa", anchor="start")
    d.text(310, 70, "B⃗(t) ⊗ dentro", cls="sc", anchor="start")
    d.text(310, 92, "B crece", cls="t", anchor="start")
    d.text(310, 130, "curvas de radio r:", cls="t", anchor="start")
    d.text(310, 148, "r < b (dentro)", cls="t", anchor="start")
    d.text(310, 166, "r > b (fuera)", cls="t", anchor="start")
    d.text(310, 200, "E⃗ tangente, antihorario", cls="ta", anchor="start")
    return d


def espira_cayendo():
    d = FieldGeometryDiagram(440, 290, "Espira cuadrada en el plano yz cayendo en un campo que depende de z")
    d.field_region(135, 60, 345, 225, step=30, direction="out")
    d.line((40, 250), (360, 250), cls="m")
    d.text(372, 254, "z = 0", cls="t", anchor="start")
    x0, x1, ztop, zbot = 145, 255, 80, 190
    d.wire((x0, ztop), (x1, ztop), (x1, zbot), (x0, zbot), (x0, ztop))
    d.text(200, 140, "m, R", cls="s")
    d.dimension((x0, zbot + 14), (x1, zbot + 14), text="a", label_side="bottom", label_offset=8)
    d.dimension((115, 250), (115, zbot), text="z", label_side="left", label_offset=8)
    d.dimension((95, 250), (95, ztop), text="z + a", label_side="left", label_offset=8)
    d.current_arrow((300, 110), (300, 170), cls="m")
    d.text(310, 150, "g⃗", cls="s", anchor="start")
    d.axes_2d((385, 200), x_len=40, y_len=40, x_label="y", y_label="z")
    d.raw(field_dot(385, 200, r_outer=5, r_inner=1.6, line_cls="m", fill_cls="mf"))
    d.text(372, 222, "x", cls="s")
    d.text(430, 30, "B⃗  =  (B₀ − αz) x̂", cls="sc", anchor="end")
    return d


def espira_semi():
    d = FieldGeometryDiagram(440, 270, "Espira rectangular larga cayendo, con su parte inferior dentro de un campo")
    d.field_region(50, 170, 400, 250, step=30, direction="in")
    d.line((30, 155), (420, 155), cls="md")
    d.text(410, 145, "B = 0", cls="t", anchor="end")
    d.text(410, 265, "B⃗ ⊗ uniforme", cls="sc", anchor="end")
    x0, x1, ytop, ybot = 150, 270, 30, 210
    d.wire((x0, ytop), (x1, ytop), (x1, ybot), (x0, ybot), (x0, ytop))
    d.dimension((x0, ybot + 16), (x1, ybot + 16), text="a", label_side="bottom", label_offset=8)
    d.dimension((x1 + 16, 155), (x1 + 16, ybot), text="h", label_side="right", label_offset=8)
    d.text(210, 90, "m, R", cls="s")
    d.current_arrow((330, 60), (330, 120), cls="m")
    d.text(340, 100, "g⃗", cls="s", anchor="start")
    return d


def espiras_coaxiales():
    d = FieldGeometryDiagram(470, 230, "Espira grande con corriente acercándose a una espira pequeña coaxial")
    cy = 110
    d.current_arrow((30, cy), (450, cy), cls="m")
    d.text(455, cy + 18, "z", cls="s", anchor="end")
    d.raw(f'<ellipse class="w nofill" cx="120" cy="{cy}" rx="24" ry="82"/>', layer="wires")
    d.raw(f'<ellipse class="w nofill" cx="330" cy="{cy}" rx="7" ry="24"/>', layer="wires")
    d.current_arrow((84, 90), (84, 130), text="I", cls="a", label_side="left", offset=8)
    d.current_arrow((318, 101), (318, 121), cls="c")
    d.text(312, 100, "dℓ⃗", cls="sc", anchor="end")
    d.current_arrow((150, 30), (210, 30), text="v⃗", cls="a", label_side="top", offset=8)
    d.dimension((120, 205), (330, 205), text="d(t)", label_side="bottom", label_offset=10)
    d.text(120, 18, "R", cls="s")
    d.text(345, 82, "r ≪ R", cls="s", anchor="start")
    return d


def generador():
    d = FieldGeometryDiagram(440, 240, "Espira que gira con velocidad angular constante en un campo uniforme")
    cx, cy = 200, 120
    for y in (32, 212):
        d.current_arrow((30, y), (410, y), cls="c")
    d.text(418, 28, "B⃗", cls="sc", anchor="start")
    a = d._polar_svg(cx, cy, 70, 150)
    b = d._polar_svg(cx, cy, 70, 330)
    d.line(a, b, cls="wk")
    d.raw(f'<circle class="inkf" cx="{cx}" cy="{cy}" r="4"/>')
    d.text(cx - 12, cy + 24, "eje", cls="t")
    d.line((cx, cy), (cx + 110, cy), cls="md")
    tip = d._polar_svg(cx, cy, 82, 60)
    d.current_arrow((cx, cy), tip, cls="a")
    d.text(tip[0] + 6, tip[1], "n̂", cls="sa", anchor="start")
    d.angle_arc((cx, cy), 0, 60, r=40, text="ωt")
    d.arc_wire((cx, cy), 72, 95, 140, cls="m", current_dir="ccw", current_cls="m", arrow_offset_r=0, arrow_span_deg=40)
    d.text(cx - 66, cy - 52, "ω", cls="s")
    return d


def condensador_maxwell():
    d = FieldGeometryDiagram(470, 230, "Condensador de placas circulares cargándose y curva amperiana entre las placas")
    cy = 115
    d.wire((30, cy), (200, cy))
    d.wire((260, cy), (440, cy))
    d.line((200, cy - 70), (200, cy + 70), cls="wk")
    d.line((260, cy - 70), (260, cy + 70), cls="wk")
    d.current_arrow((80, cy - 14), (140, cy - 14), text="i", cls="a", label_side="top", offset=6)
    d.current_arrow((320, cy - 14), (380, cy - 14), text="i", cls="a", label_side="top", offset=6)
    for y in (cy - 45, cy + 45):
        d.current_arrow((208, y), (252, y), cls="a")
    d.text(230, cy - 52, "E⃗", cls="sa")
    d.raw(f'<ellipse class="cd nofill" cx="230" cy="{cy}" rx="10" ry="38"/>', layer="overlay")
    d.text(246, cy + 5, "r", cls="sc", anchor="start")
    d.text(200, cy + 92, "+q", cls="s")
    d.text(260, cy + 92, "−q", cls="s")
    d.dimension((175, cy), (175, cy - 70), text="R", label_side="left", label_offset=8)
    return d


def prac_cuatro_alambres():
    d = FieldGeometryDiagram(500, 300, "Cuatro alambres que parten del origen y se alejan con rapidez v, formando una espira cuadrada de lado 2vt en un campo B0 cos(wt) saliente")
    cx, cy, h = 200, 150, 64
    d.field_region(150, 100, 254, 204, step=34, direction="out")
    for x in (cx - h, cx + h):
        d.raw(f'<line class="wk" x1="{x}" y1="30" x2="{x}" y2="270"/>', layer="overlay")
    for y in (cy - h, cy + h):
        d.raw(f'<line class="wk" x1="60" y1="{y}" x2="340" y2="{y}"/>', layer="overlay")
    d.current_arrow((cx + h, 190), (cx + h + 40, 190), text="v", cls="a", label_side="top", offset=6)
    d.current_arrow((cx - h, 110), (cx - h - 40, 110), text="v", cls="a", label_side="top", offset=6)
    d.current_arrow((160, cy - h), (160, cy - h - 36), text="v", cls="a", label_side="right", offset=6)
    d.current_arrow((240, cy + h), (240, cy + h + 36), text="v", cls="a", label_side="right", offset=6)
    d.node("o", cx, cy, text="O", label_dir="right", offset=6)
    d.dimension((cx - h - 2, cy), (cx - h - 2, cy + h), text="ℓ/2 = vt", label_side="left")
    d.text(352, 120, "B⃗ = B₀ cos(ωt) ẑ", cls="sc", anchor="start")
    d.text(352, 144, "(saliente)", cls="t", anchor="start")
    return d


def prac_disco_faraday():
    d = FieldGeometryDiagram(440, 260, "Disco de Faraday: disco conductor de radio R que gira con velocidad angular Omega en un campo B0 uniforme paralelo al eje")
    cx, cy = 200, 150
    for x in (70, 120, 280, 330):
        d.current_arrow((x, 240), (x, 40), cls="c")
    d.text(345, 52, "B⃗ = B₀ k̂", cls="sc", anchor="start")
    d.raw(f'<ellipse class="soft w" cx="{cx}" cy="{cy}" rx="130" ry="38"/>', layer="overlay")
    d.raw(f'<line class="wk" x1="{cx}" y1="{cy}" x2="{cx}" y2="40"/>', layer="overlay")
    d.raw(f'<path class="a nofill" d="M {cx - 26} 70 A 26 8 0 1 0 {cx + 26} 70"/>', layer="overlay")
    d.current_arrow((cx + 22, 66), (cx + 27, 70), cls="a")
    d.text(cx + 34, 64, "Ω k̂", cls="sa", anchor="start")
    d.raw(f'<line class="md" x1="{cx}" y1="{cy}" x2="{cx + 130}" y2="{cy}"/>', layer="overlay")
    d.text(cx + 66, cy - 6, "R", cls="s")
    d.node("c", cx, cy, text="centro", label_dir="bottom", offset=4)
    d.node("b", cx + 130, cy, text="borde", label_dir="right", offset=8)
    return d


def figures():
    return {
        "u09-flujo-angulo": flujo_angulo(),
        "u09-signo-normal": signo_normal(),
        "u09-espira-entrando": espira_entrando(),
        "u09-alambre-espira": alambre_espira(),
        "u09-barra-rieles": barra_rieles(),
        "u09-barra-bateria": barra_bateria(),
        "u09-frenado-vt": frenado_vt(),
        "u09-solenoide-e": solenoide_e(),
        "u09-espira-cayendo": espira_cayendo(),
        "u09-espira-semi": espira_semi(),
        "u09-espiras-coaxiales": espiras_coaxiales(),
        "u09-generador": generador(),
        "u09-condensador-maxwell": condensador_maxwell(),
            "u09-prac-cuatro-alambres": prac_cuatro_alambres(),
        "u09-prac-disco-faraday": prac_disco_faraday(),
}
