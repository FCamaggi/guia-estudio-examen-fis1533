"""U1 Electrostatics figures. Generate with: python3 scripts/build_figures.py u01"""

import math
from svg_primitives import FieldGeometryDiagram


def induccion():
    d = FieldGeometryDiagram(520, 175, "Carga por inducción en cuatro pasos con esfera conductora y conexión a tierra")
    panels = [
        (68, "1. Polarización"),
        (192, "2. Conexión a tierra"),
        (318, "3. Se corta tierra"),
        (444, "4. Carga neta +Q"),
    ]
    for cx, title in panels:
        d.text(cx, 18, title, cls="tb")
        d.line((cx, 118), (cx, 152), cls="m")
        d.line((cx - 18, 152), (cx + 18, 152), cls="wk")

    cx1, cy = 68, 92
    d.raw(f'<rect class="soft a" x="14" y="{cy-8}" width="24" height="16" rx="3"/>', layer="wires")
    d.text(26, cy + 4, "−−", cls="ta")
    d.raw(f'<circle class="paperf w" cx="{cx1}" cy="{cy}" r="26"/>', layer="wires")
    d.text(cx1 - 13, cy + 4, "+", cls="tc")
    d.text(cx1 + 13, cy + 4, "−", cls="ta")

    cx2 = 192
    d.raw(f'<rect class="soft a" x="138" y="{cy-8}" width="24" height="16" rx="3"/>', layer="wires")
    d.text(150, cy + 4, "−−", cls="ta")
    d.raw(f'<circle class="paperf w" cx="{cx2}" cy="{cy}" r="26"/>', layer="wires")
    d.text(cx2 - 13, cy + 4, "+", cls="tc")
    d.wire((cx2 + 26, cy), (cx2 + 44, cy), (cx2 + 44, cy + 16))
    d.ground((cx2 + 44, cy + 16), stem=4)
    d.current_arrow((cx2 + 28, cy - 12), (cx2 + 46, cy - 12), cls="a")
    d.text(cx2 + 37, cy - 18, "e⁻", cls="ta")

    cx3 = 318
    d.raw(f'<rect class="soft a" x="264" y="{cy-8}" width="24" height="16" rx="3"/>', layer="wires")
    d.text(276, cy + 4, "−−", cls="ta")
    d.raw(f'<circle class="csoft w" cx="{cx3}" cy="{cy}" r="26"/>', layer="wires")
    d.text(cx3 - 13, cy + 4, "++", cls="tc")

    cx4 = 444
    d.raw(f'<circle class="csoft w" cx="{cx4}" cy="{cy}" r="26"/>', layer="wires")
    for deg in (45, 135, 225, 315):
        px, py = d._polar_svg(cx4, cy, 16, deg)
        d.text(px, py + 4, "+", cls="tc")
    return d


def coulomb():
    d = FieldGeometryDiagram(480, 210, "Ley de Coulomb en forma vectorial: repulsión y atracción")
    d.text(120, 22, "q₁ q₂ > 0: repulsión", cls="tb")
    p1 = (80, 145)
    p2 = (165, 85)
    d.line(p1, p2, cls="md")
    d.current_arrow((92, 136), (126, 112), text="r̂₁₂", cls="m", label_side="bottom", offset=16)
    d.current_arrow(p2, (205, 57), text="F⃗₁₂", cls="c", label_side="top", offset=10)
    d.current_arrow(p1, (40, 173), text="F⃗₂₁", cls="c", label_side="top", offset=10)
    d.point_charge(p1, sign="+", r=9, text="q₁", label_dir="bottom")
    d.point_charge(p2, sign="+", r=9, text="q₂", label_dir="bottom")

    d.text(360, 22, "q₁ q₂ < 0: atracción", cls="tb")
    q1 = (310, 145)
    q2 = (405, 85)
    d.line(q1, q2, cls="md")
    d.current_arrow(q2, (365, 110), text="F⃗₁₂", cls="c", label_side="top", offset=12)
    d.current_arrow(q1, (350, 120), text="F⃗₂₁", cls="c", label_side="top", offset=12)
    d.point_charge(q1, sign="+", r=9, text="q₁", label_dir="bottom")
    d.point_charge(q2, sign="-", r=9, text="q₂", label_dir="bottom")
    return d


def lineas_campo():
    d = FieldGeometryDiagram(500, 220, "Líneas de campo eléctrico: dipolo y dos cargas iguales")
    d.text(125, 20, "Cargas opuestas (+q, −q)", cls="tb")
    xL, xR, cy = 70, 180, 118
    d.current_arrow((xL + 10, cy), (xR - 10, cy), cls="a")
    for h in (28, 58):
        d.raw(f'<path class="a" d="M {xL+6},{cy-6} Q 125,{cy-h} {xR-6},{cy-6}"/>', layer="bg")
        d.raw(f'<path class="a" d="M {xL+6},{cy+6} Q 125,{cy+h} {xR-6},{cy+6}"/>', layer="bg")
    for deg in (135, 180, 225):
        d.current_arrow(d._polar_svg(xL, cy, 12, deg), d._polar_svg(xL, cy, 44, deg), cls="a")
    for deg in (45, 0, -45):
        d.current_arrow(d._polar_svg(xR, cy, 44, deg), d._polar_svg(xR, cy, 12, deg), cls="a")
    d.point_charge((xL, cy), sign="+", r=9, text="+q", label_dir="bottom")
    d.point_charge((xR, cy), sign="-", r=9, text="−q", label_dir="bottom")

    d.text(375, 20, "Cargas iguales (+q, +q)", cls="tb")
    x1, x2 = 315, 435
    xm = (x1 + x2) / 2
    for dy in (-10, 10):
        s = -1 if dy < 0 else 1
        d.raw(f'<path class="a" d="M {x1+8},{cy+dy*0.4} Q {xm-12},{cy+dy*0.8} {xm-8},{cy+s*68}"/>', layer="bg")
        d.raw(f'<path class="a" d="M {x2-8},{cy+dy*0.4} Q {xm+12},{cy+dy*0.8} {xm+8},{cy+s*68}"/>', layer="bg")
    for deg in (120, 180, 240):
        d.current_arrow(d._polar_svg(x1, cy, 12, deg), d._polar_svg(x1, cy, 46, deg), cls="a")
    for deg in (60, 0, -60):
        d.current_arrow(d._polar_svg(x2, cy, 12, deg), d._polar_svg(x2, cy, 46, deg), cls="a")
    d.node("N", xm, cy, text="E = 0", label_dir="bottom", offset=10, draw_dot=True, cls="ta")
    d.point_charge((x1, cy), sign="+", r=9, text="+q", label_dir="bottom")
    d.point_charge((x2, cy), sign="+", r=9, text="+q", label_dir="bottom")
    return d


def campo_nulo():
    d = FieldGeometryDiagram(480, 210, "Regiones para buscar el punto de campo nulo entre dos cargas de distinto signo")
    y = 132
    d.current_arrow((25, y), (455, y), cls="m")
    d.text(462, y + 5, "x", cls="s", anchor="start")
    x1, x2, x0 = 135, 255, 375
    d.point_charge((x1, y), sign="+", r=9, text="+9q (0)", label_dir="bottom")
    d.point_charge((x2, y), sign="-", r=9, text="−q (d)", label_dir="bottom")
    d.node("P", x0, y, text="x₀ = 3d/2", label_dir="bottom", offset=12, cls="ta")

    # Region 1: x < 0
    d.text(72, 22, "x < 0", cls="tb")
    d.current_arrow((92, 56), (44, 56), cls="a")
    d.text(68, 48, "E⃗₁", cls="sa")
    d.current_arrow((56, 86), (80, 86), cls="c")
    d.text(68, 78, "E⃗₂", cls="sc")

    # Region 2: 0 < x < d
    d.text(195, 22, "0 < x < d", cls="tb")
    d.current_arrow((168, 56), (222, 56), cls="a")
    d.text(195, 48, "E⃗₁", cls="sa")
    d.current_arrow((176, 86), (214, 86), cls="c")
    d.text(195, 78, "E⃗₂", cls="sc")
    d.text(195, 190, "nunca se anulan", cls="tc")

    # Region 3: x > d
    d.text(375, 22, "x > d", cls="tb")
    d.current_arrow((x0, 72), (x0 + 46, 72), cls="a")
    d.text(x0 + 23, 62, "E⃗₁", cls="sa")
    d.current_arrow((x0, 72), (x0 - 46, 72), cls="c")
    d.text(x0 - 23, 62, "E⃗₂", cls="sc")
    return d


def barra_mediatriz():
    d = FieldGeometryDiagram(460, 260, "Barra finita sobre el eje y y cancelación por simetría en la mediatriz")
    ox, oy = 115, 130
    d.axes_2d((ox, oy), x_len=305, y_len=110, x_label="x", y_label="y", neg_x=40, neg_y=110)
    y_top, y_bot = oy - 84, oy + 84
    d.raw(f'<rect class="csoft w" x="{ox-6}" y="{y_top}" width="12" height="{y_bot - y_top}" rx="2"/>', layer="wires")
    d.text(ox - 14, y_top + 6, "+a", cls="s", anchor="end")
    d.text(ox - 14, y_bot + 4, "−a", cls="s", anchor="end")
    d.text(ox - 14, oy + 30, "λ", cls="sc", anchor="end")

    yq = 62
    for sgn, lbl in ((-1, "+y"), (1, "−y")):
        cy = oy + sgn * yq
        d.raw(f'<rect class="soft a" x="{ox-6}" y="{cy-5}" width="12" height="10"/>', layer="overlay")
        d.text(ox - 14, cy + 4, lbl, cls="sa", anchor="end")

    px, py = 252, oy
    d.node("P", px, py, text="P", label_dir="top", offset=10)
    d.dimension((ox, oy + 102), (px, oy + 102), text="x", label_side="bottom", label_offset=8)

    d.line((ox, oy - yq), (px, py), cls="ad")
    d.line((ox, oy + yq), (px, py), cls="ad")
    dx, dy = px - ox, yq
    dist = math.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    L_arr = 82
    tip_p = (px + L_arr * ux, py + L_arr * uy)
    tip_m = (px + L_arr * ux, py - L_arr * uy)
    d.current_arrow((px, py), tip_p, cls="a")
    d.current_arrow((px, py), tip_m, cls="a")
    d.text(tip_p[0] + 8, tip_p[1] + 10, "dE⃗₊", cls="sa", anchor="start")
    d.text(tip_m[0] + 8, tip_m[1] - 4, "dE⃗₋", cls="sa", anchor="start")
    d.current_arrow((px, py), (px + 108, py), cls="c")
    d.text(px + 114, py + 5, "dE⃗ₓ", cls="sc", anchor="start")
    deg_a = math.degrees(math.atan2(yq, dx))
    d.angle_arc((px, py), -deg_a, 0, r=42, text="α")
    return d


def anillo_disco():
    d = FieldGeometryDiagram(510, 260, "Anillo uniforme y disco uniforme en su eje")
    d.text(120, 20, "Anillo uniforme (Q, R)", cls="tb")
    d.ring_or_disk_3d((120, 200), rx=66, ry=20, is_disk=False, target_P=(120, 86), text="λ")
    d.text(130, 145, "z", cls="s", anchor="start")

    d.text(380, 20, "Disco uniforme (σ, R)", cls="tb")
    d.ring_or_disk_3d((380, 200), rx=74, ry=22, is_disk=True, ring_dr_frac=0.52, target_P=(380, 86), text="σ")
    d.text(390, 145, "x", cls="s", anchor="start")
    d.text(448, 226, "dr", cls="sa", anchor="start")
    return d


def dipolo():
    d = FieldGeometryDiagram(500, 240, "Dipolo eléctrico: campo en la bisectriz y torque en un campo uniforme")
    d.text(120, 20, "Campo en la bisectriz", cls="tb")
    cx, cy = 75, 130
    p_pos = (cx, cy - 52)
    p_neg = (cx, cy + 52)
    d.line(p_pos, p_neg, cls="m")
    d.line((cx - 12, cy), (218, cy), cls="md")
    d.point_charge(p_pos, sign="+", r=8, text="+q", label_dir="left")
    d.point_charge(p_neg, sign="-", r=8, text="−q", label_dir="left")
    px = 175
    d.node("P", px, cy, text="P", label_dir="top", offset=10)
    d.line(p_pos, (px, cy), cls="ad")
    d.line(p_neg, (px, cy), cls="ad")
    d.current_arrow((px, cy), (px + 40, cy + 28), cls="a")
    d.text(px + 44, cy + 36, "E⃗₊", cls="sa", anchor="start")
    d.current_arrow((px, cy), (px - 40, cy + 28), cls="a")
    d.text(px - 44, cy + 36, "E⃗₋", cls="sa", anchor="end")
    d.current_arrow((px, cy), (px, cy + 56), cls="c")
    d.text(px + 6, cy + 68, "E⃗", cls="sc", anchor="start")
    d.text(122, cy - 8, "x", cls="s")

    d.text(375, 20, "Torque en campo uniforme", cls="tb")
    for yy in (64, 130, 196):
        d.current_arrow((272, yy), (472, yy), cls="a")
    d.text(476, 68, "E⃗", cls="sa", anchor="start")
    mx, my = 370, 130
    q_neg = d._polar_svg(mx, my, 48, 215)
    q_pos = d._polar_svg(mx, my, 48, 35)
    d.dipole(q_neg, q_pos, q_labels=("", ""), p_label="p⃗")
    d.text(q_pos[0] - 12, q_pos[1] - 12, "+q", cls="sc", anchor="end")
    d.text(q_neg[0] + 12, q_neg[1] + 22, "−q", cls="sa", anchor="start")
    d.current_arrow(q_pos, (q_pos[0] + 46, q_pos[1]), cls="c")
    d.text(q_pos[0] + 25, q_pos[1] - 12, "+q E⃗", cls="sc")
    d.current_arrow(q_neg, (q_neg[0] - 46, q_neg[1]), cls="c")
    d.text(q_neg[0] - 25, q_neg[1] - 12, "−q E⃗", cls="sc")
    d.angle_arc((mx, my), 0, 35, r=30, text="φ")
    return d


def proyectil():
    d = FieldGeometryDiagram(460, 215, "Movimiento parabólico de un electrón entre placas paralelas con campo uniforme")
    x0, w, ytop, ybot = 95, 230, 52, 162
    d.raw(f'<rect class="csoft w" x="{x0}" y="{ytop-8}" width="{w}" height="8"/>', layer="wires")
    d.raw(f'<rect class="soft w" x="{x0}" y="{ybot}" width="{w}" height="8"/>', layer="wires")
    d.text(x0 + w / 2, ytop - 16, "+  +  +  +  +  +  +", cls="tc")
    d.text(x0 + w / 2, ybot + 24, "−  −  −  −  −  −  −", cls="ta")
    for ex in (x0 + 45, x0 + 115, x0 + 185):
        d.current_arrow((ex, ytop + 8), (ex, ybot - 8), cls="a")
    d.text(x0 + 196, (ytop + ybot) / 2, "E⃗", cls="sa", anchor="start")

    ymid = (ytop + ybot) / 2
    d.line((x0 - 30, ymid), (x0 + w + 25, ymid), cls="md")
    d.current_arrow((x0 - 45, ymid), (x0 - 4, ymid), text="v⃗₀", cls="c", label_side="top", offset=10)
    d.point_charge((x0 - 52, ymid), sign="-", r=7, text="−e", label_dir="bottom")
    d.raw(f'<path class="c" d="M {x0},{ymid} Q {x0+w*0.55},{ymid} {x0+w},{ytop+14}"/>', layer="overlay")
    d.current_arrow((x0 + w, ytop + 14), (x0 + w + 38, ytop - 4), text="v⃗", cls="c", label_side="top", offset=10)
    d.dimension((x0 + w + 10, ymid), (x0 + w + 10, ytop + 14), text="Δy", label_side="right", label_offset=8)
    d.dimension((x0, ybot + 36), (x0 + w, ybot + 36), text="L", label_side="bottom", label_offset=8)
    return d


def cubo_cargas():
    d = FieldGeometryDiagram(440, 265, "Cubo de arista a con ocho cargas en los vértices y origen en el centro")
    ox0, oy0 = 215, 138
    scale = 120.0

    def proj(x, y, z):
        sx = ox0 + scale * (y - 0.38 * x)
        sy = oy0 + scale * (-z + 0.28 * x)
        return (round(sx, 1), round(sy, 1))

    verts = {
        "Q₁": (proj(-0.5, -0.5, -0.5), "left"),
        "Q₂": (proj(0.5, -0.5, -0.5), "left"),
        "Q₃": (proj(0.5, 0.5, -0.5), "right"),
        "Q₄": (proj(-0.5, 0.5, -0.5), "right"),
        "Q₅": (proj(-0.5, -0.5, 0.5), "left"),
        "Q₆": (proj(0.5, -0.5, 0.5), "left"),
        "Q₇": (proj(0.5, 0.5, 0.5), "right"),
        "Q₈": (proj(-0.5, 0.5, 0.5), "right"),
    }
    p = {k: v[0] for k, v in verts.items()}
    for a, b in [("Q₁", "Q₂"), ("Q₁", "Q₄"), ("Q₁", "Q₅")]:
        d.line(p[a], p[b], cls="md")
    for a, b in [
        ("Q₂", "Q₃"), ("Q₃", "Q₄"), ("Q₅", "Q₆"), ("Q₆", "Q₇"), ("Q₇", "Q₈"), ("Q₈", "Q₅"),
        ("Q₂", "Q₆"), ("Q₃", "Q₇"), ("Q₄", "Q₈"),
    ]:
        d.line(p[a], p[b], cls="w")

    ax_x = proj(0.62, 0, 0)
    ax_y = proj(0, 0.95, 0)
    ax_z = proj(0, 0, 0.95)
    d.current_arrow((ox0, oy0), ax_x, cls="m")
    d.text(ax_x[0] - 6, ax_x[1] - 8, "x", cls="s", anchor="end")
    d.current_arrow((ox0, oy0), ax_y, cls="m")
    d.text(ax_y[0] + 10, ax_y[1] + 5, "y", cls="s", anchor="start")
    d.current_arrow((ox0, oy0), ax_z, cls="m")
    d.text(ax_z[0] + 10, ax_z[1] - 2, "z", cls="s", anchor="start")
    d.node("O", ox0, oy0, text="O", label_dir="bottom", offset=10, draw_dot=True)

    for lbl, (pt, ldir) in verts.items():
        if lbl == "Q₈":
            d.raw(f'<circle class="soft a" cx="{pt[0]}" cy="{pt[1]}" r="6.5"/>', layer="overlay")
            d.text(pt[0] + 12, pt[1] + 4, "Q₈", cls="sa", anchor="start")
        else:
            d.point_charge(pt, sign="+", r=5.5, text=lbl, label_dir=ldir)
    d.text(390, 240, "arista: a", cls="t", anchor="end")
    return d


def anillo_resorte():
    d = FieldGeometryDiagram(460, 220, "Anillo con carga +Q, resorte de constante k₀ y carga negativa q en el eje z")
    cx, cy = 135, 110
    rx, ry = 26, 76
    d.current_arrow((55, cy), (425, cy), cls="m")
    d.text(432, cy + 5, "z", cls="s", anchor="start")
    d.raw(f'<ellipse class="wk nofill" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>', layer="wires")
    d.line((cx, cy), (cx, cy - ry), cls="md")
    d.text(cx - 12, cy - ry * 0.48, "R₀", cls="s", anchor="end")
    d.text(cx, cy - ry - 14, "+Q", cls="sc")
    d.node("A", cx, cy, text="A", label_dir="bottom", offset=12)

    qx = 295
    sx0, sx1 = cx + 8, qx - 10
    n_z = 8
    step = (sx1 - sx0) / n_z
    pts = [(cx, cy), (sx0, cy)]
    for i in range(n_z):
        px = sx0 + (i + 0.5) * step
        py = cy + (9 if i % 2 == 0 else -9)
        pts.append((round(px, 1), py))
    pts.append((sx1, cy))
    pts.append((qx, cy))
    d.wire(*pts, cls="w")
    d.text((sx0 + sx1) / 2, cy - 16, "k₀", cls="s")
    d.point_charge((qx, cy), sign="-", r=9, text="q, m", label_dir="bottom")
    d.dimension((cx, cy + 52), (qx, cy + 52), text="z", label_side="bottom", label_offset=8)
    d.current_arrow((qx, cy - 22), (qx - 45, cy - 22), text="F⃗", cls="c", label_side="top", offset=8)
    return d


def triangulo():
    d = FieldGeometryDiagram(400, 240, "Triángulo equilátero con tres cargas −e en los vértices y carga Q en el centro")
    cx, cy = 200, 145
    L = 138
    h = L * math.sqrt(3) / 2
    p_top = (cx, cy - 2 * h / 3)
    p_bl = (cx - L / 2, cy + h / 3)
    p_br = (cx + L / 2, cy + h / 3)
    d.line(p_top, p_bl, cls="w")
    d.line(p_bl, p_br, cls="w")
    d.line(p_br, p_top, cls="w")
    d.line(p_top, (cx, p_bl[1]), cls="md")
    d.point_charge((cx, cy), sign="+", r=7.5, text="Q", label_dir="right")
    d.point_charge(p_top, sign="-", r=8, text="−e", label_dir="left")
    d.point_charge(p_bl, sign="-", r=8, text="−e", label_dir="left")
    d.point_charge(p_br, sign="-", r=8, text="−e", label_dir="right")
    d.current_arrow(p_top, (p_top[0] - 24, p_top[1] - 42), text="F⃗₁", cls="c", label_side="left", offset=8)
    d.current_arrow(p_top, (p_top[0] + 24, p_top[1] - 42), text="F⃗₂", cls="c", label_side="right", offset=8)
    d.current_arrow(p_top, (p_top[0], p_top[1] + 54), cls="c")
    d.text(p_top[0] + 8, p_top[1] + 54, "F⃗₃", cls="sc", anchor="start")
    d.dimension((p_bl[0], p_bl[1] + 22), (p_br[0], p_br[1] + 22), text="L", label_side="bottom", label_offset=8)
    return d


def pendulo():
    d = FieldGeometryDiagram(380, 225, "Dos esferas cargadas suspendidas en equilibrio formando ángulo θ con la vertical")
    ax, ay = 185, 32
    length, angle_deg = 126.0, 21.0
    d.line((ax - 60, ay), (ax + 60, ay), cls="wk")
    for hx in range(-55, 60, 12):
        d.line((ax + hx, ay), (ax + hx + 6, ay - 7), cls="m")
    d.line((ax, ay), (ax, ay + length * 0.95), cls="md")
    p_l = d._polar_svg(ax, ay, length, 270 - angle_deg)
    p_r = d._polar_svg(ax, ay, length, 270 + angle_deg)
    d.wire((ax, ay), p_l)
    d.wire((ax, ay), p_r)
    d.angle_arc((ax, ay), 270 - angle_deg, 270, r=32, text="θ")
    d.angle_arc((ax, ay), 270, 270 + angle_deg, r=32, text="θ")
    d.point_charge(p_l, sign="+", r=8, text="+q", label_dir="left")
    d.point_charge(p_r, sign="+", r=8)
    d.text(p_r[0] + 12, p_r[1] - 12, "+q", cls="s", anchor="start")
    d.current_arrow(p_r, (p_r[0], p_r[1] + 44), cls="m")
    d.text(p_r[0] - 8, p_r[1] + 40, "mg⃗", cls="s", anchor="end")
    d.current_arrow(p_r, (p_r[0] + 48, p_r[1]), text="F⃗ₑ", cls="c", label_side="bottom", offset=16)
    return d


def horquilla():
    d = FieldGeometryDiagram(420, 235, "Alambre infinito en forma de horquilla en el plano xy")
    ox, oy = 185, 115
    d.axes_2d((ox, oy), x_len=195, y_len=95, x_label="x", y_label="y", neg_x=130, neg_y=95)
    R = 62
    d.line((ox - R, oy), (ox - R, 18), cls="wk")
    d.arc_wire((ox, oy), R, 180, 270, cls="wk")
    d.line((ox, oy + R), (385, oy + R), cls="wk")
    d.text(ox - R - 14, 48, "λ", cls="sc")
    p_arc = d._polar_svg(ox, oy, R, 225)
    d.line((ox, oy), p_arc, cls="md")
    d.text(ox - 20, oy + 36, "R", cls="s")
    d.current_arrow((ox, oy), (ox + 46, oy - 46), text="E⃗", cls="a", label_side="top", offset=10)
    d.node("O", ox, oy, text="O", label_dir="top", offset=10)
    return d


def figures():
    return {
        "u01-induccion": induccion(),
        "u01-coulomb": coulomb(),
        "u01-lineas-campo": lineas_campo(),
        "u01-campo-nulo": campo_nulo(),
        "u01-barra-mediatriz": barra_mediatriz(),
        "u01-anillo-disco": anillo_disco(),
        "u01-dipolo": dipolo(),
        "u01-proyectil": proyectil(),
        "u01-cubo-cargas": cubo_cargas(),
        "u01-anillo-resorte": anillo_resorte(),
        "u01-triangulo": triangulo(),
        "u01-pendulo": pendulo(),
        "u01-horquilla": horquilla(),
    }
