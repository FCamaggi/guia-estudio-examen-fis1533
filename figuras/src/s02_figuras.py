"""S2 Mock exam 2 figures. Generate with: python3 scripts/build_figures.py s02"""

import math
from svg_primitives import FieldGeometryDiagram, arrow, field_dot


def _knife_switch(d, p1, p2, closed: bool, text: str, text_dx: float = 0.0, text_dy: float = -16.0):
    """Two terminal dots and a blade; open blade is rotated 30 degrees away from p2."""
    (x1, y1), (x2, y2) = p1, p2
    d.raw(f'<circle class="inkf" cx="{x1:g}" cy="{y1:g}" r="3.4"/><circle class="inkf" cx="{x2:g}" cy="{y2:g}" r="3.4"/>')
    if closed:
        ex, ey = x2, y2
    else:
        ang = math.atan2(y2 - y1, x2 - x1)
        ln = math.hypot(x2 - x1, y2 - y1)
        rot = ang - math.radians(30) if abs(y2 - y1) < 1 else ang + math.radians(30)
        ex, ey = x1 + ln * math.cos(rot), y1 + ln * math.sin(rot)
    d.raw(f'<line class="w" x1="{x1:g}" y1="{y1:g}" x2="{ex:.1f}" y2="{ey:.1f}"/>')
    mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
    d.text(mx + text_dx, my + text_dy, text, cls="s")


def p1a_anillo():
    d = FieldGeometryDiagram(440, 300, "Anillo cargado +Q de radio a con una carga -Q/8 fija en su centro y punto P en el eje z")
    cx, cy = 200, 205
    d.line((cx, 285), (cx, cy), cls="md")
    d.raw(arrow(cx, cy, cx, 28, line_cls="m", head_cls="mf", head_len=7, head_w=3.5))
    d.text(cx + 12, 34, "z", cls="s", anchor="start")
    d.raw(f'<ellipse class="c nofill" cx="{cx}" cy="{cy}" rx="120" ry="34" style="stroke-width:3"/>', layer="wires")
    d.text(cx + 132, cy - 20, "+Q", cls="sc", anchor="start")
    d.text(cx + 132, cy, "(uniforme)", cls="t", anchor="start")
    d.line((cx, cy), (cx + 120, cy), cls="md")
    d.text(cx + 66, cy + 18, "a", cls="s")
    d.point_charge((cx, cy), sign="-", r=8)
    d.text(cx - 14, cy + 24, "−Q/8", cls="sa", anchor="end")
    d.text(cx - 14, cy - 8, "O", cls="s", anchor="end")
    d.node("P", cx, 92, text="P", label_dir="right", offset=12)
    d.dimension((cx - 150, cy), (cx - 150, 92), text="z", label_side="left", label_offset=8)
    d.line((cx - 156, 92), (cx - 6, 92), cls="md")
    return d


def p1b_circuito():
    d = FieldGeometryDiagram(600, 270, "Circuito de tres ramas entre los nodos a y b: epsilon1 con R1 e interruptor S1, rama S R3 C, y epsilon2 con R2")
    xl, xm, xr, yt, yb = 110, 300, 490, 50, 225
    d.node("a", xm, yt, text="a", label_dir="top", offset=12)
    d.node("b", xm, yb, text="b", label_dir="bottom", offset=10)
    # Top and bottom rails, S1 on the top-left wire
    d.wire((xl, yt), (180, yt))
    _knife_switch(d, (180, yt), (222, yt), closed=True, text="S₁", text_dy=-14)
    d.wire((222, yt), (xm, yt), (xr, yt))
    d.wire((xl, yb), (xm, yb), (xr, yb))
    # Left branch: epsilon1 (positive up) and R1
    d.battery((xl, yt), (xl, 135), text="ε₁ = 12 V", positive_at="p1", label_side="left", offset=26)
    d.resistor((xl, 135), (xl, yb), text="R₁ = 2 Ω", label_side="left", offset=18)
    # Middle branch: S (open), R3, C
    d.wire((xm, yt), (xm, 66))
    _knife_switch(d, (xm, 66), (xm, 98), closed=False, text="S", text_dx=-30, text_dy=6)
    d.resistor((xm, 98), (xm, 160), text="R₃ = 2 Ω", label_side="right", offset=16)
    d.capacitor((xm, 160), (xm, yb), text="C = 3 μF", label_side="right", offset=20)
    # Right branch: epsilon2 (positive up) and R2
    d.battery((xr, yt), (xr, 135), text="ε₂ = 6 V", positive_at="p1", label_side="right", offset=26)
    d.resistor((xr, 135), (xr, yb), text="R₂ = 4 Ω", label_side="right", offset=18)
    return d


def p2_espira():
    d = FieldGeometryDiagram(420, 300, "Espira formada por una semicircunferencia de radio a y tres tramos rectos, con corriente antihoraria")
    s = 85
    ox, oy = 190, 150
    d.arc_wire((ox, oy), s, 90, 270, cls="wk", current_dir="ccw", current_cls="a", current_label="I", arrow_span_deg=50)
    d.wire((ox, oy - s), (ox + s, oy - s), (ox + s, oy + s), (ox, oy + s), cls="wk")
    d.current_arrow((ox + 64, oy - s - 14), (ox + 22, oy - s - 14), cls="a")
    d.current_arrow((ox + 22, oy + s + 14), (ox + 64, oy + s + 14), cls="a")
    d.current_arrow((ox + s + 14, oy + 30), (ox + s + 14, oy - 30), cls="a")
    d.node("O", ox, oy)
    d.text(ox - 10, oy + 22, "O", cls="s", anchor="end")
    d.radius_dim((ox, oy), 145, s, text="a")
    d.dimension((ox, oy + s + 34), (ox + s, oy + s + 34), text="a", label_side="bottom", label_offset=10)
    d.dimension((ox + s + 44, oy - s), (ox + s + 44, oy + s), text="2a", label_side="right", label_offset=8)
    d.line((ox, oy - s), (ox, oy + s), cls="md")
    d.axes_2d((50, 262), x_len=36, y_len=36, x_label="x", y_label="y")
    d.raw(field_dot(50, 262, r_outer=5, r_inner=1.6, line_cls="m", fill_cls="mf"))
    d.text(36, 284, "z", cls="s")
    return d


def p3_rieles():
    d = FieldGeometryDiagram(720, 300, "Barra que desliza por rieles inclinados en un campo magnético vertical: vista lateral y vista desde arriba")
    # --- Side view ---
    x0, y0, L = 50, 60, 300
    th = math.radians(30)
    x1, y1 = x0 + L * math.cos(th), y0 + L * math.sin(th)
    d.raw(f'<polygon class="soft" points="{x0:g},{y0:g} {x1:.1f},{y1:.1f} {x0:g},{y1:.1f}"/>', layer="bg")
    d.line((x0 - 10, y1), (x1 + 50, y1), cls="m")
    d.line((x0, y0), (x1, y1), cls="wk")
    d.angle_arc((x1, y1), 150, 180, r=42, text="θ")
    # Resistor end (seen edge-on) and bar cross-section
    d.raw(f'<rect class="w paperf" x="{x0 - 7:g}" y="{y0 - 7:g}" width="14" height="14"/>')
    d.text(x0 - 2, y0 - 16, "R", cls="s")
    ux, uy = math.cos(th), math.sin(th)
    nx, ny = -uy, -ux  # outward normal (up from the incline)
    sb = 190
    bx, by = x0 + sb * ux + 9 * nx, y0 + sb * uy + 9 * ny
    d.raw(f'<circle class="inkf" cx="{bx:.1f}" cy="{by:.1f}" r="8"/>')
    d.text(bx - 8, by - 14, "m", cls="s", anchor="end")
    t0 = (bx + 16 * ux + 6 * nx, by + 16 * uy + 6 * ny)
    t1 = (bx + 66 * ux + 6 * nx, by + 66 * uy + 6 * ny)
    d.current_arrow(t0, t1, cls="a")
    d.text(t1[0] + 2, t1[1] - 14, "v⃗", cls="sa", anchor="start")
    # s along the incline, drawn below the rail
    off = 16
    p_a = (x0 - off * nx, y0 - off * ny)
    p_b = (x0 + sb * ux - off * nx, y0 + sb * uy - off * ny)
    d.line(p_a, p_b, cls="m")
    for p in (p_a, p_b):
        d.line((p[0] - 4 * nx, p[1] - 4 * ny), (p[0] + 4 * nx, p[1] + 4 * ny), cls="m")
    mx, my = x0 + 95 * ux - 34 * nx, y0 + 95 * uy - 34 * ny
    d.text(mx, my + 5, "s", cls="s")
    # Vertical field and gravity
    for bxl in (110, 180, 380):
        d.current_arrow((bxl, 250), (bxl, 40), cls="c")
    d.text(392, 48, "B⃗", cls="sc", anchor="start")
    d.current_arrow((72, 196), (72, 244), cls="m")
    d.text(80, 238, "g⃗", cls="s", anchor="start")
    d.text(150, 292, "vista lateral", cls="t")
    d.axes_2d((300, 274), x_len=32, y_len=26, x_label="x", y_label="z")
    d.text(290, 280, "y ⊗", cls="s", anchor="end")
    # --- Top view ---
    tx0, tx1, ty0, ty1 = 490, 700, 100, 180
    for xx in (525, 565, 650, 690):
        for yy in (122, 158):
            d.raw(field_dot(xx, yy), layer="bg")
    d.line((tx0, ty0), (tx1, ty0), cls="wk")
    d.line((tx0, ty1), (tx1, ty1), cls="wk")
    d.resistor((tx0, ty0), (tx0, ty1), text="R", label_side="right", offset=14)
    d.line((605, ty0 - 8), (605, ty1 + 8), cls="wk")
    d.current_arrow((614, 140), (646, 140), cls="a")
    d.text(630, 133, "v⃗", cls="sa")
    d.dimension((462, ty0), (462, ty1), text="ℓ", label_side="left", label_offset=6)
    d.text(tx1, ty0 - 10, "riel de atrás", cls="t", anchor="end")
    d.text(tx1, ty1 + 22, "riel de adelante", cls="t", anchor="end")
    d.text(640, 236, "B⃗ ⊙ (hacia arriba)", cls="sc")
    d.axes_2d((480, 262), x_len=30, y_len=30, x_label="x", y_label="y")
    d.text(600, 290, "vista desde arriba", cls="t")
    return d


def figures():
    return {
        "s02-p1a-anillo": p1a_anillo(),
        "s02-p1b-circuito": p1b_circuito(),
        "s02-p2-espira": p2_espira(),
        "s02-p3-rieles": p3_rieles(),
    }
