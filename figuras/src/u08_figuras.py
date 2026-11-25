"""U8 Magnetostatics figures. Generate with: python3 scripts/build_figures.py u08"""

import math
from svg_primitives import FieldGeometryDiagram, arrow, field_cross, field_dot


def biot_savart():
    d = FieldGeometryDiagram(460, 235, "Campo magnético de un elemento de corriente según la ley de Biot-Savart")
    d.raw('<path class="wk" d="M 45,190 Q 115,65 215,120 T 385,65"/>', layer="wires")
    p0 = (142, 113)
    p1 = (182, 107)
    d.current_arrow(p0, p1, text="dℓ⃗", cls="a", label_side="top", offset=16)
    d.current_arrow((68, 152), (90, 128), cls="a")
    d.text(64, 134, "I", cls="sa")
    px, py = 325, 175
    d.node("P", px, py, text="P", label_dir="right", offset=10)
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    d.current_arrow((mx, my), (px - 5, py - 2), cls="m")
    d.text(238, 165, "r⃗ − r⃗'", cls="s")
    d.angle_arc((mx, my), -19, 10, r=58, text="φ")
    d.wire_z((px - 5, py + 34), direction="in", cls="c", r=9)
    d.text(px + 12, py + 39, "dB⃗", cls="sc", anchor="start")
    d.text(px + 42, py + 39, "(entrando)", cls="tc", anchor="start")
    return d


def alambre_finito():
    d = FieldGeometryDiagram(470, 240, "Campo magnético de un alambre recto finito de corriente en un punto P")
    y_wire = 178
    x1, x2 = 85, 365
    xp, yp = 210, 55
    d.line((x1, y_wire), (x2, y_wire), cls="wk")
    d.current_arrow((100, y_wire - 14), (160, y_wire - 14), text="I", cls="a", label_side="top", offset=8)
    xe = 290
    d.raw(f'<rect class="soft a" x="{xe-7}" y="{y_wire-4}" width="14" height="8"/>', layer="overlay")
    d.text(xe, y_wire + 20, "dx", cls="sa")
    d.line((xp, y_wire), (xp, yp), cls="md")
    d.text(xp - 8, 145, "R", cls="s", anchor="end")
    d.line((x1, y_wire), (xp, yp), cls="m")
    d.line((x2, y_wire), (xp, yp), cls="m")
    d.line((xe, y_wire), (xp, yp), cls="ad")
    d.angle_arc((xp, yp), 225, 270, r=34, text="θ₁")
    d.angle_arc((xp, yp), 270, 321, r=50, text="θ₂")
    d.node("P", xp, yp, text="P", label_dir="top", offset=10)
    d.wire_z((xp + 34, yp + 4), direction="out", cls="c", r=8)
    d.text(xp + 48, yp + 9, "B⃗", cls="sc", anchor="start")
    d.text(x1, y_wire + 20, "x₁", cls="s")
    d.text(x2, y_wire + 20, "x₂", cls="s")
    return d


def alambres_paralelos():
    d = FieldGeometryDiagram(470, 235, "Fuerza entre conductores paralelos: corrientes iguales atraen, opuestas repelen")
    # Left panel: same direction -> attract
    x1, x2 = 75, 165
    d.line((x1, 38), (x1, 188), cls="wk")
    d.line((x2, 38), (x2, 188), cls="wk")
    d.current_arrow((x1 - 16, 130), (x1 - 16, 70), text="I₁", cls="a", label_side="left", offset=8)
    d.current_arrow((x2 + 16, 130), (x2 + 16, 70), text="I₂", cls="a", label_side="right", offset=8)
    d.current_arrow((x1, 148), (x1 + 32, 148), text="F⃗", cls="c", label_side="top", offset=10)
    d.current_arrow((x2, 148), (x2 - 32, 148), text="F⃗", cls="c", label_side="top", offset=10)
    d.wire_z((x2 + 24, 50), direction="in", cls="c", r=7)
    d.text(x2 + 36, 55, "B⃗₁", cls="sc", anchor="start")
    d.dimension((x1, 195), (x2, 195), text="d", label_side="bottom", label_offset=10)
    d.text(120, 22, "mismo sentido: atracción", cls="tb")

    # Right panel: opposite direction -> repel
    x3, x4 = 305, 395
    d.line((x3, 38), (x3, 188), cls="wk")
    d.line((x4, 38), (x4, 188), cls="wk")
    d.current_arrow((x3 + 16, 130), (x3 + 16, 70), text="I₁", cls="a", label_side="right", offset=8)
    d.current_arrow((x4 - 16, 70), (x4 - 16, 130), text="I₂", cls="a", label_side="left", offset=8)
    d.current_arrow((x3, 148), (x3 - 34, 148), text="F⃗", cls="c", label_side="top", offset=10)
    d.current_arrow((x4, 148), (x4 + 34, 148), text="F⃗", cls="c", label_side="top", offset=10)
    d.dimension((x3, 195), (x4, 195), text="d", label_side="bottom", label_offset=10)
    d.text(350, 22, "opuestos: repulsión", cls="tb")
    return d


def espira_eje():
    d = FieldGeometryDiagram(460, 240, "Campo magnético en el eje de una espira circular de radio R")
    cx, cy = 140, 125
    rx, ry = 28, 76
    d.current_arrow((45, cy), (425, cy), cls="m")
    d.text(432, cy + 5, "z", cls="s", anchor="start")
    d.raw(f'<ellipse class="wk nofill" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>', layer="wires")
    d.current_arrow((cx + 12, cy - ry + 8), (cx - 10, cy - ry + 14), cls="a")
    d.text(cx, cy - ry - 12, "I", cls="sa")
    d.line((cx, cy), (cx, cy - ry), cls="md")
    d.text(cx - 10, cy - ry * 0.45, "R", cls="s", anchor="end")
    px = 320
    d.node("P", px, cy, text="P", label_dir="bottom", offset=12)
    d.dimension((cx, cy + 90), (px, cy + 90), text="z", label_side="bottom", label_offset=10)
    d.current_arrow((cx, cy - ry), (px - 4, cy - 3), cls="a")
    d.text(245, 72, "r⃗ − r⃗'", cls="sa")
    d.current_arrow((px, cy), (px + 65, cy), text="B⃗", cls="c", label_side="top", offset=10)
    d.current_arrow((cx, cy), (cx + 46, cy), cls="c")
    d.text(cx + 48, cy - 10, "μ⃗", cls="sc", anchor="start")
    return d


def arco_segmentos():
    d = FieldGeometryDiagram(450, 255, "Espira formada por dos arcos circulares concéntricos y dos segmentos radiales")
    cx, cy = 115, 175
    ra, rb = 72, 142
    phi = 58
    d.node("P", cx, cy, text="P", label_dir="left", offset=10)
    d.arc_wire((cx, cy), rb, 0, phi, cls="wk", current_dir="ccw", current_cls="a", current_label="I", arrow_offset_r=14)
    d.arc_wire((cx, cy), ra, 0, phi, cls="wk", current_dir="cw", current_cls="a", arrow_offset_r=11)
    la = d._polar_svg(cx, cy, ra + 26, phi * 0.50)
    d.text(la[0], la[1] + 4, "I", cls="sa")
    p_a0 = d._polar_svg(cx, cy, ra, 0)
    p_b0 = d._polar_svg(cx, cy, rb, 0)
    p_ap = d._polar_svg(cx, cy, ra, phi)
    p_bp = d._polar_svg(cx, cy, rb, phi)
    d.wire(p_a0, p_b0, cls="wk")
    d.wire(p_bp, p_ap, cls="wk")
    d.line((cx, cy), p_a0, cls="md")
    d.line((cx, cy), p_ap, cls="md")
    d.current_arrow((cx + ra + 14, cy - 12), (cx + rb - 14, cy - 12), cls="a")
    d.current_arrow((p_bp[0] - 12, p_bp[1] - 4), (p_ap[0] - 12, p_ap[1] - 4), cls="a")
    d.angle_arc((cx, cy), 0, phi, r=34, text="φ")
    d.dimension((cx, cy + 22), (cx + ra, cy + 22), text="a", label_side="bottom", label_offset=8)
    d.dimension((cx, cy + 48), (cx + rb, cy + 48), text="b", label_side="bottom", label_offset=8)
    d.text(305, 85, "tramos rectos", cls="t", anchor="start")
    d.text(305, 103, "colineales con P:", cls="t", anchor="start")
    d.text(305, 122, "dℓ⃗ × r̂ = 0", cls="sa", anchor="start")
    return d


def ampere_lazo():
    d = FieldGeometryDiagram(450, 230, "Curva amperiana cerrada rodeando varias corrientes")
    d.raw(
        '<path class="cd" d="M 110,120 C 100,45 265,35 285,115 C 300,185 135,205 110,120 Z"/>',
        layer="wires",
    )
    d.current_arrow((205, 56), (175, 58), text="dℓ⃗", cls="c", label_side="top", offset=10)
    d.text(286, 174, "C", cls="sc", anchor="start")
    d.wire_z((160, 105), direction="out", text="I₁", cls="a", r=9)
    d.wire_z((205, 130), direction="in", text="I₂", cls="a", r=9)
    d.wire_z((240, 95), direction="out", text="I₃", cls="a", r=9)
    d.wire_z((355, 115), direction="out", text="I₄ (ext)", cls="w", r=9)
    d.text(355, 165, "no aporta a Ienc", cls="t")
    d.text(85, 210, "recorrido antihorario → salen positivas: Ienc = I₁ − I₂ + I₃", cls="ta", anchor="start")
    return d


def cilindro_ampere():
    d = FieldGeometryDiagram(490, 240, "Sección transversal de un alambre cilíndrico grueso y curvas amperianas")
    cx, cy = 150, 120
    R = 66
    d.raw(f'<circle class="soft w" cx="{cx}" cy="{cy}" r="{R}"/>', layer="bg")
    d.amperian_loop((cx, cy), 36, ccw=True, cls="c", dashed=True)
    d.amperian_loop((cx, cy), 98, ccw=True, cls="c", dashed=True)
    d.radius_dim((cx, cy), -35, R, text="R")
    d.wire_z((cx, cy), direction="out", cls="a", r=7)
    d.text(cx + 12, cy - 8, "J⃗", cls="sa", anchor="start")
    d.text(cx, cy + 52, "r₁ < R", cls="sc", anchor="middle")
    d.text(cx + 88, cy - 62, "r₂ > R", cls="sc", anchor="start")
    d.text(320, 88, "simetría cilíndrica:", cls="tb", anchor="start")
    d.text(320, 110, "B⃗ tangente a círculos", cls="tc", anchor="start")
    d.text(320, 134, "∮ B⃗·dℓ⃗ = B(2πr)", cls="s", anchor="start")
    return d


def coaxial_corte():
    d = FieldGeometryDiagram(470, 255, "Sección transversal de un cable coaxial con cascarón externo")
    cx, cy = 165, 128
    d.concentric_system(
        (cx, cy),
        shells=[
            {"r_out": 100, "r_in": 68, "fill": "csoft", "stroke": "w", "hollow_center": True, "r_label": "c", "r_deg": -25},
            {"r_out": 68, "r_in": 36, "fill": "paperf", "stroke": "w", "r_label": "b", "r_deg": -65},
            {"r_out": 36, "fill": "soft", "stroke": "w", "r_label": "a", "r_deg": -145},
        ],
        gaussian_radii=[{"r": 84, "cls": "ad", "label": "r", "deg": 140}],
    )
    d.wire_z((cx - 12, cy - 10), direction="out", cls="a", r=5.5)
    d.text(cx + 6, cy - 8, "J⃗₁", cls="sa", anchor="start")
    d.wire_z((cx + 84, cy), direction="in", cls="c", r=5.5)
    d.text(308, 72, "0 ≤ r < a: J⃗₁ (saliente)", cls="sa", anchor="start")
    d.text(308, 96, "a < r < b: vacío", cls="t", anchor="start")
    d.text(308, 120, "b < r < c: J⃗₂ (entrante)", cls="sc", anchor="start")
    d.text(308, 144, "r > c: exterior", cls="t", anchor="start")
    return d


def coaxial_br():
    d = FieldGeometryDiagram(460, 240, "Gráfico de |B(r)| para el cable coaxial de cuatro regiones (Examen 2024-1)")
    pts1 = [(r / 25, (r / 25) ** 2) for r in range(0, 26)]
    pts2 = [(1 + k / 25, 1 / (1 + k / 25)) for k in range(0, 26)]
    pts3 = [(2 + k / 25, (1 / (2 + k / 25)) * (9 - (2 + k / 25) ** 2) / 5) for k in range(0, 26)]
    pts4 = [(3 + k / 25, 0.0) for k in range(0, 26)]
    d.function_plot(
        85, 38, 320, 145,
        (0, 4), (0, 1.15),
        [pts1, pts2, pts3, pts4],
        v_lines=[(1, "a"), (2, "b"), (3, "c")],
        h_lines=[(1.0, "B(a)"), (0.5, "B(b)")],
        x_label="r", y_label="|B(r)|",
    )
    d.text(146, 152, "∝ r²", cls="sa")
    d.text(218, 72, "∝ 1/r", cls="sa")
    d.text(365, 165, "B = 0", cls="ta")
    return d


def solenoide_ampere():
    d = FieldGeometryDiagram(460, 235, "Corte longitudinal de un solenoide ideal y lazo amperiano rectangular")
    x, y, length, height, turns = 85, 80, 290, 105, 8
    step = length / (turns + 1)
    for k in range(1, turns + 1):
        wx = x + k * step
        d.wire_z((wx, y), direction="in", r=8)
        d.wire_z((wx, y + height), direction="out", r=8)
    for row in (0.28, 0.56, 0.80):
        by = y + row * height
        d.raw(arrow(x + length - 10, by, x + 10, by, line_cls="c", head_cls="cf"), layer="bg")
    d.text(x + length * 0.5, y + height * 0.44, "B⃗", cls="sc")
    rx, rw, ry0, ry1 = x + length * 0.25, length * 0.5, y + height * 0.50, y - 35
    d.raw(f'<rect class="ad nofill" x="{rx:g}" y="{ry1:g}" width="{rw:g}" height="{ry0 - ry1:g}"/>', layer="overlay")
    d.text(rx - 8, ry0 + 4, "a", cls="ta", anchor="end")
    d.text(rx + rw + 8, ry0 + 4, "b", cls="ta", anchor="start")
    d.text(rx + rw + 8, ry1 + 2, "c", cls="ta", anchor="start")
    d.text(rx - 8, ry1 + 2, "d", cls="ta", anchor="end")
    d.dimension((rx, ry1 - 14), (rx + rw, ry1 - 14), text="L", label_side="top", label_offset=8)
    d.text(370, 26, "B ≈ 0 (exterior)", cls="t")
    return d


def toroide_ampere():
    d = FieldGeometryDiagram(515, 250, "Toroide ideal en corte y tres curvas amperianas concéntricas")
    cx, cy = 150, 125
    d.toroid_2d((cx, cy), r_in=50, r_out=96, turns=16, amperian_radii=[28, 73, 116])
    d.radius_dim((cx, cy), -25, 50, text="b")
    d.radius_dim((cx, cy), -58, 96, text="c")
    d.text(290, 82, "1) r < b: B = 0", cls="t", anchor="start")
    d.text(290, 112, "2) b < r < c: B = μ₀NI/(2πr)", cls="tc", anchor="start")
    d.text(290, 142, "3) r > c: Ienc = 0 ⇒ B = 0", cls="t", anchor="start")
    return d


def lamina_ampere():
    d = FieldGeometryDiagram(450, 235, "Lámina infinita con corriente superficial K y lazo amperiano rectangular")
    xs = 215
    d.line((xs, 18), (xs, 215), cls="m")
    for yy in range(35, 205, 24):
        d.wire_z((xs, yy), direction="out", cls="a", r=5.5)
    d.text(xs + 14, 26, "K⃗ (saliente)", cls="sa", anchor="start")
    rx0, rx1, ry0, ry1 = 140, 290, 62, 170
    d.raw(f'<rect class="cd nofill" x="{rx0}" y="{ry0}" width="{rx1 - rx0}" height="{ry1 - ry0}"/>', layer="overlay")
    d.current_arrow((rx1, 135), (rx1, 95), cls="c")
    d.current_arrow((rx0, 95), (rx0, 135), cls="c")
    d.dimension((rx1 + 14, ry0), (rx1 + 14, ry1), text="L", label_side="right", label_offset=8)
    d.current_arrow((100, 150), (100, 80), text="B⃗", cls="c", label_side="left", offset=10)
    d.current_arrow((340, 80), (340, 150), text="B⃗", cls="c", label_side="right", offset=10)
    return d


def espira_cuadrada():
    d = FieldGeometryDiagram(380, 240, "Espira cuadrada de lado 2a centrada en el punto P")
    cx, cy, half = 180, 120, 72
    d.wire((cx - half, cy - half), (cx + half, cy - half), (cx + half, cy + half), (cx - half, cy + half), (cx - half, cy - half))
    d.current_arrow((cx - 20, cy + half), (cx + 20, cy + half), text="I", cls="a", label_side="bottom", offset=10)
    d.current_arrow((cx + half, cy + 20), (cx + half, cy - 20), cls="a")
    d.current_arrow((cx + 20, cy - half), (cx - 20, cy - half), cls="a")
    d.current_arrow((cx - half, cy - 20), (cx - half, cy + 20), cls="a")
    d.node("P", cx, cy, text="P", label_dir="bottom", offset=10)
    d.line((cx, cy), (cx + half, cy), cls="md")
    d.text(cx + half * 0.62, cy + 16, "a", cls="s")
    d.line((cx, cy), (cx + half, cy - half), cls="m")
    d.line((cx, cy), (cx + half, cy + half), cls="m")
    d.angle_arc((cx, cy), 0, 45, r=32, text="45°")
    d.dimension((cx - half, cy - half - 14), (cx + half, cy - half - 14), text="2a", label_side="top", label_offset=8)
    return d


def cilindro_espira():
    d = FieldGeometryDiagram(460, 240, "Cilindro infinito con corriente I₁ y espira rectangular coplanar con I₂")
    cx, w_cyl = 95, 36
    d.raw(f'<rect class="soft w" x="{cx - w_cyl/2}" y="25" width="{w_cyl}" height="190"/>', layer="bg")
    d.line((cx, 20), (cx, 220), cls="md")
    d.current_arrow((cx, 150), (cx, 85), cls="a")
    d.text(cx - w_cyl/2 - 12, 120, "I₁", cls="sa", anchor="end")
    d.dimension((cx, 40), (cx + w_cyl / 2, 40), text="R", label_side="top", label_offset=8)
    x0, x1, y0, y1 = 195, 335, 65, 175
    d.wire((x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0))
    d.current_arrow((x0, 145), (x0, 95), text="I₂", cls="a", label_side="left", offset=8)
    d.current_arrow((245, y0), (285, y0), cls="a")
    d.current_arrow((x1, 95), (x1, 145), cls="a")
    d.current_arrow((285, y1), (245, y1), cls="a")
    d.dimension((cx, 198), (x0, 198), text="a", label_side="bottom", label_offset=10)
    d.dimension((x0, 198), (x1, 198), text="b", label_side="bottom", label_offset=10)
    d.dimension((x1 + 14, y0), (x1 + 14, y1), text="c", label_side="right", label_offset=8)
    d.text(355, 42, "B⃗ ⊗ en la espira", cls="sc")
    return d


def arq_arcos():
    d = FieldGeometryDiagram(440, 255, "Espira de dos semicircunferencias concéntricas en P de radios b > a (Examen 2024-2 P2)")
    cx, cy = 220, 130
    ra, rb = 48, 92
    d.axes_2d((cx, cy), x_len=145, y_len=114, x_label="x", y_label="y", neg_x=145, neg_y=100)
    d.arc_wire((cx, cy), rb, 0, 180, cls="wk")
    # Put CW arrow cleanly on the upper-right quadrant (around 50 deg) away from y-axis
    p_a1 = d._polar_svg(cx, cy, rb + 13, 62)
    p_a2 = d._polar_svg(cx, cy, rb + 13, 32)
    d.raw(f'<path class="a" d="M {p_a1[0]:.1f} {p_a1[1]:.1f} A {rb+13} {rb+13} 0 0 1 {p_a2[0]:.1f} {p_a2[1]:.1f}"/>', layer="overlay")
    # Arrowhead tangent at 32 deg CW
    rad = math.radians(32)
    ux, uy = math.sin(rad), math.cos(rad)
    tip = p_a2
    tail = (tip[0] - 8 * ux, tip[1] - 8 * uy)
    nx, ny = -uy, ux
    d.raw(f'<polygon class="af" points="{tip[0]:.1f},{tip[1]:.1f} {tail[0]+4*nx:.1f},{tail[1]+4*ny:.1f} {tail[0]-4*nx:.1f},{tail[1]-4*ny:.1f}"/>', layer="overlay")
    lp = d._polar_svg(cx, cy, rb + 26, 47)
    d.text(lp[0], lp[1], "I", cls="sa")

    d.arc_wire((cx, cy), ra, -180, 0, cls="wk", current_dir="cw", current_cls="a", arrow_offset_r=14)
    d.text(cx - 24, cy + ra + 24, "I", cls="sa")
    d.wire((cx + rb, cy), (cx + ra, cy), cls="wk")
    d.wire((cx - ra, cy), (cx - rb, cy), cls="wk")
    d.current_arrow((cx + rb - 6, cy - 10), (cx + ra + 6, cy - 10), cls="a")
    d.current_arrow((cx - ra - 6, cy + 10), (cx - rb + 6, cy + 10), cls="a")
    d.node("P", cx, cy, text="P", label_dir="top", offset=10)
    d.text(cx + ra + 10, cy + 18, "a", cls="s")
    d.text(cx + rb + 10, cy + 18, "b", cls="s")
    return d


def coaxial_3reg_br():
    d = FieldGeometryDiagram(470, 230, "Gráfico de |B(r)| para cable coaxial de tres regiones sin hueco (Examen 2025-1 P3)")
    pts1 = [(r / 25, r / 25) for r in range(0, 26)]
    pts2 = [(1 + k / 25, (1 / (1 + k / 25)) * (4 - (1 + k / 25) ** 2) / 3) for k in range(0, 26)]
    pts3 = [(2 + k / 25, 0.0) for k in range(0, 26)]
    d.function_plot(
        85, 38, 310, 140,
        (0, 3), (0, 1.15),
        [pts1, pts2, pts3],
        v_lines=[(1, "a"), (2, "b")],
        h_lines=[(1.0, "B(a)")],
        x_label="r", y_label="|B(r)|",
    )
    d.text(118, 96, "∝ r", cls="sa")
    d.text(275, 76, "(b²−r²)/[r(b²−a²)]", cls="sa", anchor="start")
    d.text(350, 158, "B = 0", cls="ta")
    return d


def cilindro_cavidad():
    d = FieldGeometryDiagram(420, 240, "Cilindro infinito con cavidad cilíndrica descentrada")
    cx, cy = 190, 120
    R = 85
    dx, ra = 38, 28
    d.raw(f'<circle class="soft w" cx="{cx}" cy="{cy}" r="{R}"/>', layer="bg")
    d.raw(f'<circle class="paperf w" cx="{cx + dx}" cy="{cy}" r="{ra}"/>', layer="wires")
    d.node("O", cx, cy, text="O", label_dir="left", offset=8)
    d.node("O2", cx + dx, cy, text="O'", label_dir="bottom", offset=10)
    d.dimension((cx, cy), (cx + dx, cy), text="d", offset=-12, label_side="top", label_offset=8)
    d.radius_dim((cx, cy), 135, R, text="R")
    p_a = d._polar_svg(cx + dx, cy, ra, -45)
    d.line((cx + dx, cy), p_a, cls="md")
    d.text(cx + dx + 26, cy + 26, "a", cls="s")
    d.wire_z((cx - 42, cy + 25), direction="out", cls="a", r=7)
    d.text(cx - 24, cy + 30, "J⃗", cls="sa", anchor="start")
    d.current_arrow((cx + dx + 8, cy + 14), (cx + dx + 8, cy - 16), text="B⃗", cls="c", label_side="right", offset=8)
    return d


def ex_2026_2_i2_p3():
    d = FieldGeometryDiagram(470, 285, "Alambre semi-infinito sobre el eje z con corriente I hacia el origen que se reparte radialmente en el plano conductor z = 0; lazo amperiano C de radio s a altura z")
    ox, oy = 225, 222
    d.raw(f'<path class="soft w" d="M 50 252 L 330 252 L 410 192 L 130 192 Z"/>', layer="bg")
    d.raw(f'<line class="wk" x1="{ox}" y1="{oy}" x2="{ox}" y2="26"/>', layer="overlay")
    d.current_arrow((ox + 12, 34), (ox + 12, 76), text="I", cls="a", label_side="right", offset=8)
    for dx, dy in ((78, 0), (-78, 0), (52, -20), (-52, 20), (40, 22), (-40, -22)):
        d.current_arrow((ox + dx * 0.28, oy + dy * 0.28), (ox + dx, oy + dy), cls="a")
    d.text(ox - 92, oy + 5, "I", cls="sa", anchor="end")
    zc = 112
    d.raw(f'<ellipse class="c nofill" stroke-dasharray="5 4" cx="{ox}" cy="{zc}" rx="72" ry="22"/>', layer="overlay")
    d.node("P", ox + 72, zc, text="P", label_dir="right", offset=10)
    d.line((ox, zc), (ox + 72, zc), cls="md")
    d.text(ox + 40, zc - 5, "s", cls="s")
    d.text(ox - 82, zc - 8, "C", cls="sc", anchor="end")
    d.dimension((ox + 112, zc), (ox + 112, oy), text="z", label_side="right")
    d.text(ox, 18, "z", cls="s")
    d.node("O", ox, oy, text="O", label_dir="bottom", offset=4)
    d.text(80, 244, "z = 0", cls="t", anchor="start")
    return d


def figures():
    return {
        "u08-biot-savart": biot_savart(),
        "u08-alambre-finito": alambre_finito(),
        "u08-alambres-paralelos": alambres_paralelos(),
        "u08-espira-eje": espira_eje(),
        "u08-arco-segmentos": arco_segmentos(),
        "u08-ampere-lazo": ampere_lazo(),
        "u08-cilindro-ampere": cilindro_ampere(),
        "u08-coaxial-corte": coaxial_corte(),
        "u08-coaxial-br": coaxial_br(),
        "u08-solenoide-ampere": solenoide_ampere(),
        "u08-toroide-ampere": toroide_ampere(),
        "u08-lamina-ampere": lamina_ampere(),
        "u08-espira-cuadrada": espira_cuadrada(),
        "u08-cilindro-espira": cilindro_espira(),
        "u08-arq-arcos": arq_arcos(),
        "u08-coaxial-3reg-br": coaxial_3reg_br(),
        "u08-cilindro-cavidad": cilindro_cavidad(),
            "u08-ex-2026-2-i2-p3": ex_2026_2_i2_p3(),
}
