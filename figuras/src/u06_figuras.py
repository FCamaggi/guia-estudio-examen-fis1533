"""U6 DC circuits, Kirchhoff, measuring instruments and RC circuits figures.
Generate with: python3 scripts/build_figures.py u06
"""

import math
from svg_primitives import FieldGeometryDiagram, arrow, node


def _sub_label(d, x: float, y: float, base: str, sub: str, cls: str = "s", anchor: str = "middle", post: str = ""):
    """Draw a serif/body label with a clean tspan subscript (avoids '_' and Unicode tofu)."""
    post_span = f'<tspan dy="-3.5">{post}</tspan>' if post else ""
    d.raw(
        f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}">'
        f'{base}<tspan class="sb" dy="3.5">{sub}</tspan>{post_span}</text>',
        layer="labels",
    )


def serie_paralelo():
    d = FieldGeometryDiagram(510, 248, "Asociación de resistores en serie, en paralelo y puente de Wheatstone")
    # Panel a) Serie (left)
    d.text(78, 22, "a) Serie (misma I)", cls="tb")
    d.node("sa", 20, 102, text="a", label_dir="top", offset=10)
    d.node("sm", 78, 102, draw_dot=False)
    d.node("sb", 136, 102, text="b", label_dir="top", offset=10)
    d.resistor("sa", "sm", text="R₁", label_side="top", offset=18)
    d.resistor("sm", "sb", text="R₂", label_side="top", offset=18)
    d.current_arrow((32, 135), (124, 135), text="I", cls="a", label_side="bottom", offset=14)
    _sub_label(d, 78, 188, "R", "eq", cls="tb", post=" = R₁ + R₂")

    # Divider 1
    d.line((154, 18), (154, 228), cls="md")

    # Panel b) Paralelo (middle)
    d.text(236, 22, "b) Paralelo (mismo ΔV)", cls="tb")
    d.node("pa", 172, 102, text="a", label_dir="top", offset=12)
    d.node("pb", 300, 102, text="b", label_dir="top", offset=12)
    d.parallel_group(
        "pa", "pb",
        branches=[
            {"kind": "resistor", "dy": -30, "label": "R₁", "label_side": "top", "offset": 16},
            {"kind": "resistor", "dy": 30, "label": "R₂", "label_side": "bottom", "offset": 20},
        ],
        lead=16,
    )
    _sub_label(d, 236, 188, "1/R", "eq", cls="tb", post=" = 1/R₁ + 1/R₂")

    # Divider 2
    d.line((320, 18), (320, 228), cls="md")

    # Panel c) Puente (right)
    d.text(416, 22, "c) Puente (no reducible)", cls="tb")
    top = (416, 58)
    right = (476, 114)
    bottom = (416, 170)
    left = (356, 114)
    d.wheatstone_bridge(
        top, right, bottom, left,
        arms=[
            {"kind": "resistor", "label": "R₂", "label_side": "top", "offset": 22},
            {"kind": "resistor", "label": "R₄", "label_side": "bottom", "offset": 22},
            {"kind": "resistor", "label": "R₃", "label_side": "bottom", "offset": 22},
            {"kind": "resistor", "label": "R₁", "label_side": "top", "offset": 22},
        ],
        center_arm={"kind": "resistor", "label": "R₅", "label_side": "top", "offset": 16},
        node_labels=("a", "c", "d", "b"),
    )
    d.text(416, 220, "Equilibrio: R₁R₄ = R₂R₃", cls="ta")
    return d


def kirchhoff_convencion():
    d = FieldGeometryDiagram(500, 358, "Leyes de Kirchhoff: regla de nodos y convención de signos al recorrer una malla")
    # Left panel: Node rule
    d.text(98, 24, "Regla de nodos (LCK)", cls="tb")
    nx, ny = 95, 160
    d.node("P", nx, ny, text="nodo", label_dir="bottom", offset=10)
    d.wire((25, ny), (nx, ny))
    d.wire((nx, ny), (155, 102))
    d.wire((nx, ny), (155, 212))
    d.current_arrow((34, ny - 14), (74, ny - 14), text="I₁", cls="a", label_side="top", offset=8)
    d.current_arrow((114, 132), (146, 100), text="I₂", cls="a", label_side="top", offset=14)
    d.current_arrow((114, 188), (146, 220), text="I₃", cls="a", label_side="bottom", offset=15)
    d.text(95, 272, "I₁ = I₂ + I₃", cls="tb")
    d.text(95, 294, "∑ I entran = ∑ I salen", cls="t")

    d.line((182, 16), (182, 342), cls="md")

    # Right panel: Loop sign convention (4 cases, recorrido a -> b)
    d.text(340, 24, "Regla de mallas (recorrido a → b)", cls="tb")
    rows = [
        ("resistor", True, 66, "ΔV = −IR"),
        ("resistor", False, 148, "ΔV = +IR"),
        ("battery", True, 230, "ΔV = +ε"),
        ("battery", False, 306, "ΔV = −ε"),
    ]
    for kind, forward, y, eq_txt in rows:
        pa, pb = (212, y), (336, y)
        d.node(f"ka{y}", pa[0], pa[1], text="a", label_dir="top", offset=10)
        d.node(f"kb{y}", pb[0], pb[1], text="b", label_dir="top", offset=10)
        if kind == "resistor":
            d.resistor(pa, pb, text="R", label_side="top", offset=18)
            if forward:
                d.current_arrow((248, y + 20), (300, y + 20), text="I", cls="a", label_side="bottom", offset=14)
            else:
                d.current_arrow((300, y + 20), (248, y + 20), text="I", cls="a", label_side="bottom", offset=14)
        else:
            pos_at = "p2" if forward else "p1"
            d.battery(pa, pb, text="ε", positive_at=pos_at, show_polarity=True, label_side="top", offset=18)
        d.text(360, y + 4, eq_txt, cls="tb", anchor="start")
    return d


def medidores():
    d = FieldGeometryDiagram(610, 240, "Conexión de amperímetro real, voltímetro real y puente de Wheatstone")
    # Panel a) Ammeter in series
    d.text(98, 22, "a) Amperímetro (serie)", cls="tb")
    d.node("a1", 42, 56, draw_dot=False)
    d.node("a2", 152, 56, draw_dot=False)
    d.node("a3", 152, 168, draw_dot=False)
    d.node("a4", 42, 168, draw_dot=False)
    d.battery("a1", "a4", text="ε", positive_at="p1", label_side="left", offset=18)
    d.meter("a1", "a2", symbol="A", text="", label_side="top")
    d.text(97, 82, "rₐ ideal = 0", cls="ta")
    d.resistor("a2", "a3", text="R", label_side="right", offset=18)
    d.wire("a3", "a4")
    _sub_label(d, 98, 206, "I", "med", cls="t", post=" = ε / (R + rₐ)")

    d.line((204, 16), (204, 226), cls="md")

    # Panel b) Voltmeter in parallel
    d.text(314, 22, "b) Voltímetro (paralelo)", cls="tb")
    d.node("b1", 248, 56, draw_dot=False)
    d.node("b2", 308, 56, draw_dot=True)
    d.node("b3", 308, 168, draw_dot=True)
    d.node("b4", 248, 168, draw_dot=False)
    d.node("b5", 358, 56, draw_dot=False)
    d.node("b6", 358, 168, draw_dot=False)
    d.battery("b1", "b4", text="ε", positive_at="p1", label_side="left", offset=18)
    d.wire("b1", "b2", "b5")
    d.wire("b4", "b3", "b6")
    d.resistor("b2", "b3", text="R", label_side="left", offset=16)
    d.meter("b5", "b6", symbol="V", text="", label_side="right")
    d.text(376, 117, "rᵥ → ∞", cls="ta", anchor="start")
    d.text(314, 206, "Mide ΔV entre nodos", cls="t")

    d.line((434, 16), (434, 226), cls="md")

    # Panel c) Balanced Wheatstone bridge
    d.text(522, 22, "c) Puente nulo", cls="tb")
    top = (522, 52)
    right = (584, 108)
    bottom = (522, 164)
    left = (460, 108)
    d.wheatstone_bridge(
        top, right, bottom, left,
        arms=[
            {"kind": "resistor", "label": "R₂", "label_side": "top", "offset": 20},
            {"kind": "resistor", "label": "Rₓ", "label_side": "bottom", "offset": 22},
            {"kind": "resistor", "label": "R₃", "label_side": "bottom", "offset": 22},
            {"kind": "resistor", "label": "R₁", "label_side": "top", "offset": 20},
        ],
        center_arm=None,
        node_labels=("", "", "", ""),
    )
    d.meter(left, right, symbol="G", r=11, text="", label_side="top")
    _sub_label(d, 522, 134, "I", "G", cls="ta", post=" = 0")
    d.text(522, 206, "Rₓ = R₃(R₂/R₁)", cls="tb")
    return d


def rc_circuito():
    d = FieldGeometryDiagram(460, 248, "Circuito RC con interruptor de dos posiciones para carga y descarga")
    d.node("tl", 75, 48, draw_dot=False)
    d.node("bl", 75, 185, draw_dot=False)
    d.battery("tl", "bl", text="ε", positive_at="p1", label_side="left", offset=22)
    d.node("sw_a", 155, 48, text="a", label_dir="top", offset=10)
    d.node("sw_b", 155, 185, text="b", label_dir="bottom", offset=10)
    d.node("sw_p", 205, 48, draw_dot=True)
    d.wire("tl", "sw_a")
    d.wire("bl", "sw_b")
    d.switch_spdt("sw_p", "sw_a", "sw_b", text="S", label_offset=(-14, -18))
    d.node("tr", 385, 48, draw_dot=False)
    d.node("br", 385, 185, draw_dot=False)
    d.node("bm", 205, 185, draw_dot=True)
    d.wire("sw_b", "bm", "br")
    d.resistor("sw_p", "tr", text="R", label_side="top", offset=20)
    d.capacitor("tr", "br", text="C", label_side="right", offset=22)
    d.text(364, 96, "+q", cls="tc")
    d.text(364, 144, "−q", cls="ta")
    d.current_arrow((225, 28), (275, 28), text="i(t)", cls="a", label_side="top", offset=6)
    d.text(230, 232, "a: carga con fuente ε   |   b: descarga solo por R", cls="t")
    return d


def rc_curvas():
    d = FieldGeometryDiagram(515, 230, "Curvas de carga y descarga de un capacitor en un circuito RC")
    pts_up = [(t / 20, 1 - math.exp(-t / 20)) for t in range(0, 101)]
    pts_dn = [(t / 20, math.exp(-t / 20)) for t in range(0, 101)]
    d.function_plot(
        76, 35, 150, 130, (0, 5), (0, 1.12), [pts_up],
        v_lines=[(1, "τ")], h_lines=[(1, "Q∞"), (1 - math.exp(-1), "0,63 Q∞")],
        x_label="t", y_label="q(t)", cls="a",
    )
    d.text(151, 198, "Carga: Q∞(1 − exp(−t/τ))", cls="ta")
    d.function_plot(
        330, 35, 150, 130, (0, 5), (0, 1.12), [pts_dn],
        v_lines=[(1, "τ")], h_lines=[(1, "Q₀"), (math.exp(-1), "0,37 Q₀")],
        x_label="t", y_label="q(t)", cls="c",
    )
    d.text(405, 198, "Descarga: Q₀ exp(−t/τ)", cls="tc")
    return d


def rc_thevenin():
    d = FieldGeometryDiagram(590, 235, "Red RC de dos mallas y sus equivalentes en t = 0+ y t → ∞")
    # Left: original 2-loop RC network
    d.text(112, 22, "Red original", cls="tb")
    d.node("n1", 42, 56, draw_dot=False)
    d.node("n2", 124, 56, draw_dot=True)
    d.node("n3", 184, 56, draw_dot=False)
    d.node("m1", 42, 168, draw_dot=False)
    d.node("m2", 124, 168, draw_dot=True)
    d.node("m3", 184, 168, draw_dot=False)
    d.battery("n1", "m1", text="ε", positive_at="p1", label_side="left", offset=18)
    d.resistor("n1", "n2", text="R₁", label_side="top", offset=18)
    d.resistor("n2", "m2", text="R₂", label_side="left", offset=16)
    d.wire("n2", "n3")
    d.capacitor("n3", "m3", text="C", label_side="right", offset=18)
    d.wire("m1", "m2", "m3")
    d.text(112, 206, "τ = (R₁ ∥ R₂) C", cls="tb")

    d.line((226, 16), (226, 220), cls="md")

    # Middle: t = 0+ (C = corto)
    d.text(318, 22, "t = 0⁺ (C = corto)", cls="tb")
    d.node("c1", 266, 56, draw_dot=False)
    d.node("c2", 328, 56, draw_dot=True)
    d.node("c3", 370, 56, draw_dot=False)
    d.node("d1", 266, 168, draw_dot=False)
    d.node("d2", 328, 168, draw_dot=True)
    d.node("d3", 370, 168, draw_dot=False)
    d.battery("c1", "d1", text="ε", positive_at="p1", label_side="left", offset=16)
    d.resistor("c1", "c2", text="R₁", label_side="top", offset=16)
    d.resistor("c2", "d2", text="R₂", label_side="left", offset=14)
    d.wire("c2", "c3", "d3", "d2", cls="a")
    d.wire("d1", "d2")
    d.text(318, 206, "ΔV = 0 en C", cls="ta")

    d.line((394, 16), (394, 220), cls="md")

    # Right: t -> inf (C = abierto)
    d.text(486, 22, "t → ∞ (C = abierto)", cls="tb")
    d.node("e1", 434, 56, draw_dot=False)
    d.node("e2", 500, 56, draw_dot=True)
    d.node("f1", 434, 168, draw_dot=False)
    d.node("f2", 500, 168, draw_dot=True)
    d.battery("e1", "f1", text="ε", positive_at="p1", label_side="left", offset=16)
    d.resistor("e1", "e2", text="R₁", label_side="top", offset=16)
    d.resistor("e2", "f2", text="R₂", label_side="left", offset=14)
    d.wire("f1", "f2")
    d.wire("e2", (534, 56))
    d.wire("f2", (534, 168))
    d.terminal_open("oc1", 534, 56, text="", label_dir="right")
    d.terminal_open("oc2", 534, 168, text="", label_dir="right")
    _sub_label(d, 486, 206, "I", "C", cls="tc", post=" = 0, divisor")
    return d


def ej1_voltimetro():
    d = FieldGeometryDiagram(510, 225, "Circuito serie-paralelo con voltímetro no ideal en paralelo con R2 y R3")
    d.node("tl", 100, 50, draw_dot=False)
    d.node("bl", 100, 175, draw_dot=False)
    d.node("tm", 256, 50, draw_dot=True)
    d.node("bm", 256, 175, draw_dot=True)
    d.node("tr1", 346, 50, draw_dot=True)
    d.node("br1", 346, 175, draw_dot=True)
    d.node("tr2", 428, 50, draw_dot=False)
    d.node("br2", 428, 175, draw_dot=False)
    d.battery("tl", "bl", text="ε = 18 V", positive_at="p1", label_side="left", offset=24)
    d.resistor("tl", "tm", text="R₁ = 4 Ω", label_side="top", offset=18)
    d.wire("tm", "tr1", "tr2")
    d.wire("bl", "bm", "br1", "br2")
    d.resistor("tm", "bm", text="R₂ = 6 Ω", label_side="left", offset=18)
    d.resistor("tr1", "br1", text="R₃ = 3 Ω", label_side="left", offset=18)
    d.meter("tr2", "br2", symbol="V", text="rᵥ = 6 Ω", label_side="right", offset=20)
    d.current_arrow((108, 34), (140, 34), text="I", cls="a", label_side="top", offset=6)
    return d


def ej2_mallas():
    d = FieldGeometryDiagram(530, 240, "Circuito de dos mallas con dos baterías reales entre los nodos a y b")
    d.node("tl", 115, 45, draw_dot=False)
    d.node("bl", 115, 195, draw_dot=False)
    d.node("a", 265, 45, text="a", label_dir="top", offset=12)
    d.node("b", 265, 195, text="b", label_dir="bottom", offset=12)
    d.node("tr", 415, 45, draw_dot=False)
    d.node("br", 415, 195, draw_dot=False)
    d.real_battery("tl", "bl", emf_text="ε₁ = 14 V", r_text="r₁ = 1 Ω", positive_at="p1", label_side="left")
    d.wire("tl", "a", "tr")
    d.wire("bl", "b", "br")
    d.resistor("a", "b", text="R₂ = 2 Ω", label_side="left", offset=18)
    d.real_battery("tr", "br", emf_text="ε₂ = 4 V", r_text="r₂ = 2 Ω", positive_at="p1", label_side="right")
    d.current_arrow((165, 29), (215, 29), text="I₁", cls="a", label_side="top", offset=6)
    d.current_arrow((282, 92), (282, 148), text="I₂", cls="a", label_side="right", offset=10)
    d.current_arrow((315, 29), (365, 29), text="I₃", cls="a", label_side="top", offset=6)
    return d


def ej3_rc_red():
    d = FieldGeometryDiagram(550, 225, "Red RC con fuente de 12 V, interruptor S, R1, R2 y C en paralelo")
    d.node("tl", 105, 50, draw_dot=False)
    d.node("bl", 105, 178, draw_dot=False)
    d.battery("tl", "bl", text="ε = 12 V", positive_at="p1", label_side="left", offset=24)
    d.node("s1", 148, 50, draw_dot=True)
    d.node("s2", 184, 50, draw_dot=True)
    d.wire("tl", "s1")
    d.switch_spdt("s1", "s2", text="S", label_offset=(18, -16))
    d.node("tm", 346, 50, draw_dot=True)
    d.node("bm", 346, 178, draw_dot=True)
    d.node("tr", 452, 50, draw_dot=False)
    d.node("br", 452, 178, draw_dot=False)
    d.resistor("s2", "tm", text="R₁ = 6 Ω", label_side="top", offset=18)
    d.resistor("tm", "bm", text="R₂ = 3 Ω", label_side="left", offset=18)
    d.wire("tm", "tr")
    d.capacitor("tr", "br", text="C = 5 μF", label_side="right", offset=22)
    d.wire("bl", "bm", "br")
    d.current_arrow((190, 34), (218, 34), text="i₁", cls="a", label_side="top", offset=6)
    d.current_arrow((364, 90), (364, 138), text="i₂", cls="a", label_side="right", offset=10)
    _sub_label(d, 399, 22, "i", "C", cls="sa")
    d.current_arrow((378, 34), (420, 34), cls="a")
    return d


def ex_2021_2_ej1():
    d = FieldGeometryDiagram(420, 225, "Circuito DC del Examen 2021-2 Ej 1 con fuente E y resistencias R1, R2, R3")
    d.node("tl", 75, 48, draw_dot=False)
    d.node("bl", 75, 178, draw_dot=False)
    d.node("tm", 230, 48, draw_dot=True)
    d.node("bm", 230, 178, draw_dot=True)
    d.node("tr", 355, 48, draw_dot=False)
    d.node("br", 355, 178, draw_dot=False)
    d.battery("tl", "bl", text="E", positive_at="p1", label_side="left", offset=22)
    d.resistor("tl", "tm", text="R₁", label_side="top", offset=18)
    d.resistor("tm", "bm", text="R₂", label_side="left", offset=18)
    d.wire("tm", "tr")
    d.resistor("tr", "br", text="R₃", label_side="right", offset=18)
    d.wire("bl", "bm", "br")
    d.current_arrow((100, 102), (100, 66), text="I₁", cls="a", label_side="right", offset=10)
    d.current_arrow((248, 86), (248, 128), text="I₂", cls="a", label_side="right", offset=10)
    d.current_arrow((336, 86), (336, 128), text="I₃", cls="a", label_side="left", offset=10)
    return d


def ex_2022_2_p5():
    d = FieldGeometryDiagram(430, 272, "Circuito de dos mallas del Examen 2022-2 P5 con tres fem y nodos P1, P2, P3")
    # 3 rows: y=48 (top), y=138 (mid), y=228 (bot)
    # Left x=75, right x=345
    d.node("tl", 75, 48, draw_dot=False)
    d.node("ml", 75, 138, draw_dot=True)
    d.node("bl", 75, 228, draw_dot=False)
    d.node("tr", 345, 48, draw_dot=False)
    d.node("mr", 345, 138, draw_dot=True)
    d.node("br", 345, 228, draw_dot=False)

    # Top: P1 and upper-right R1
    d.node("P1", 210, 48, text="P₁", label_dir="top", offset=10)
    d.wire("tl", "P1", "tr")
    d.resistor("tr", "mr", text="R₁", label_side="right", offset=20)

    # Left vertical: eps1 (+ top, - bottom) and wire down to bl
    d.battery("tl", "ml", text="ε₁", positive_at="p1", show_polarity=False, label_side="left", offset=22)
    d.wire("ml", "bl")

    # Middle horizontal: R2, P2, eps2 (- left, + right)
    d.node("mp_a", 195, 138, draw_dot=False)
    d.node("P2", 210, 138, text="P₂", label_dir="top", offset=10)
    d.resistor("ml", "mp_a", text="R₂", label_side="bottom", offset=22)
    d.wire("mp_a", "P2")
    d.battery("P2", "mr", text="ε₂", positive_at="p2", show_polarity=False, label_side="bottom", offset=22)

    # Bottom: eps3 (- left, + right) and P3 on lower-right vertical with I3 down
    d.battery("bl", "br", text="ε₃", positive_at="p2", show_polarity=False, label_side="bottom", offset=22)
    d.node("P3", 345, 195, text="P₃", label_dir="left", offset=12)
    d.wire("mr", "P3", "br")
    d.current_arrow((365, 165), (365, 210), text="I₃", cls="a", label_side="right", offset=10)
    # Show reference I1 and I2 arrows subtly
    d.current_arrow((135, 34), (175, 34), text="I₁", cls="a", label_side="top", offset=6)
    d.current_arrow((225, 124), (255, 124), text="I₂", cls="a", label_side="top", offset=6)
    return d


def ex_2026_1_p1b():
    d = FieldGeometryDiagram(480, 265, "Puente DC del Examen 2026-1 P1B con capacitor C y resistencia R5 en la rama central")
    # Source loop on left (x=58) connected to top (a) and bottom (d) of diamond
    top = (310, 42)
    right = (420, 132)
    bottom = (310, 222)
    left = (200, 132)
    d.node("sl_t", 58, 42, draw_dot=False)
    d.node("sl_m1", 58, 72, draw_dot=True)
    d.node("sl_m2", 58, 108, draw_dot=True)
    d.node("sl_b", 58, 222, draw_dot=False)
    d.wire("sl_t", "sl_m1")
    d.switch_spdt("sl_m1", "sl_m2", text="S", label_offset=(-18, 4))
    d.battery("sl_m2", "sl_b", text="E", positive_at="p1", label_side="left", offset=22)
    d.wire("sl_t", top)
    d.resistor("sl_b", bottom, text="R₆", label_side="bottom", offset=22)

    # Diamond bridge arms: top->right R3, right->bottom R4, bottom->left R2, left->top R1
    d.resistor(left, top, text="R₁", label_side="top", offset=20)
    d.resistor(top, right, text="R₃", label_side="top", offset=20)
    d.resistor(left, bottom, text="R₂", label_side="bottom", offset=22)
    d.resistor(right, bottom, text="R₄", label_side="bottom", offset=22)

    # Center branch: b (left) -- C -- mid -- R5 -- c (right)
    mid_c = (310, 132)
    d.capacitor(left, mid_c, text="C", label_side="top", offset=18)
    d.resistor(mid_c, right, text="R₅", label_side="top", offset=18)

    d.node("a", top[0], top[1], text="a", label_dir="top", offset=10)
    d.node("b", left[0], left[1], text="b", label_dir="left", offset=12)
    d.node("c", right[0], right[1], text="c", label_dir="right", offset=12)
    d.node("d", bottom[0], bottom[1], text="d", label_dir="bottom", offset=12)
    return d


def prac1_red():
    d = FieldGeometryDiagram(510, 235, "Red de tres mallas con dos baterías del Control 2 2025-2")
    # x columns: 48 (R1/R8), 128 (R7), 220 (R6), 315 (eps1), 435 (R5)
    # y rows: 48 (top), 118 (mid left), 188 (bot)
    d.node("tl", 48, 48, draw_dot=False)
    d.node("ml", 48, 118, draw_dot=True)
    d.node("bl", 48, 188, draw_dot=False)
    d.node("m7", 128, 118, draw_dot=False)
    d.node("b7", 128, 188, draw_dot=True)
    d.node("t6", 220, 48, draw_dot=True)
    d.node("b6", 220, 188, draw_dot=True)
    d.node("te", 315, 48, draw_dot=True)
    d.node("be", 315, 188, draw_dot=True)
    d.node("tr", 435, 48, draw_dot=False)
    d.node("br", 435, 188, draw_dot=False)

    d.resistor("tl", "ml", text="R₁", label_side="left", offset=18)
    d.resistor("ml", "bl", text="R₈", label_side="left", offset=18)
    d.wire("ml", "m7")
    d.resistor("m7", "b7", text="R₇", label_side="right", offset=16)
    d.resistor("tl", "t6", text="R₂", label_side="top", offset=16)
    d.resistor("t6", "b6", text="R₆", label_side="left", offset=16)
    d.resistor("t6", "te", text="R₃", label_side="top", offset=16)
    d.battery("te", "be", text="ε₁", positive_at="p1", label_side="left", offset=20)
    d.resistor("te", "tr", text="R₄", label_side="top", offset=16)
    d.resistor("tr", "br", text="R₅", label_side="right", offset=18)
    d.battery("be", "br", text="ε₂", positive_at="p2", show_polarity=False, label_side="bottom", offset=20)
    d.wire("bl", "b7", "b6", "be")

    d.current_arrow((356, 145), (356, 95), text="i₁", cls="a", label_side="right", offset=8)
    d.current_arrow((68, 136), (68, 172), text="i₂", cls="a", label_side="right", offset=8)
    return d


def prac2_rc_2mallas():
    d = FieldGeometryDiagram(450, 220, "Circuito RC de dos mallas de I2 2025-2 con R1 en serie y R2 paralelo a C")
    d.node("tl", 65, 50, draw_dot=False)
    d.node("bl", 65, 175, draw_dot=False)
    d.battery("tl", "bl", text="E", positive_at="p1", label_side="left", offset=22)
    d.node("s1", 104, 50, draw_dot=True)
    d.node("s2", 140, 50, draw_dot=True)
    d.wire("tl", "s1")
    d.switch_spdt("s1", "s2", text="S", label_offset=(18, -16))
    d.node("tm", 265, 50, draw_dot=True)
    d.node("bm", 265, 175, draw_dot=True)
    d.node("tr", 375, 50, draw_dot=False)
    d.node("br", 375, 175, draw_dot=False)
    d.resistor("s2", "tm", text="R₁", label_side="top", offset=18)
    d.resistor("tm", "bm", text="R₂", label_side="left", offset=18)
    d.wire("tm", "tr")
    d.capacitor("tr", "br", text="C", label_side="right", offset=20)
    d.wire("bl", "bm", "br")
    d.current_arrow((160, 34), (195, 34), text="i₁", cls="a", label_side="top", offset=6)
    d.current_arrow((282, 88), (282, 134), text="i₂", cls="a", label_side="right", offset=10)
    _sub_label(d, 322, 22, "i", "C", cls="sa")
    d.current_arrow((302, 34), (344, 34), cls="a")
    return d


def prac3_c2_2026():
    d = FieldGeometryDiagram(440, 270, "Circuito plano con nodo central e y cinco resistencias del Control 2 2026-1")
    a = (95, 50)
    b = (335, 50)
    c = (335, 220)
    dn = (95, 220)
    e = (205, 135)
    d.resistor(a, b, text="R₂", label_side="top", offset=18)
    d.resistor(a, dn, text="R₁", label_side="left", offset=20)
    d.resistor(dn, c, text="R₅", label_side="bottom", offset=20)
    d.battery(b, c, text="E₁", positive_at="p1", label_side="right", offset=22)
    d.battery(a, e, text="E₂", positive_at="p1", show_polarity=False, label_side="top", offset=18)
    d.resistor(b, e, text="R₃", label_side="top", offset=18)
    d.resistor(dn, e, text="R₄", label_side="bottom", offset=20)

    d.node("a", a[0], a[1], text="a", label_dir="top", offset=10)
    d.node("b", b[0], b[1], text="b", label_dir="top", offset=10)
    d.node("c", c[0], c[1], text="c", label_dir="bottom", offset=12)
    d.node("d", dn[0], dn[1], text="d", label_dir="bottom", offset=12)
    d.node("e", e[0], e[1], text="e", label_dir="right", offset=12)

    # Current direction arrows as in pauta
    d.current_arrow((245, 70), (190, 70), text="I₂", cls="a", label_side="bottom", offset=12)
    d.current_arrow((112, 98), (112, 138), text="I₁", cls="a", label_side="right", offset=8)
    d.current_arrow((190, 200), (245, 200), text="I₅", cls="a", label_side="top", offset=8)
    d.current_arrow((300, 94), (260, 120), text="I₃", cls="a", label_side="bottom", offset=14)
    d.current_arrow((122, 177), (156, 150), text="I₄", cls="a", label_side="top", offset=12)
    return d


def prac4_dos_cap():
    d = FieldGeometryDiagram(460, 235, "Circuito de dos mallas con interruptor SPDT y dos capacitores C1 y C2")
    d.node("tl", 60, 48, draw_dot=False)
    d.node("bl", 60, 182, draw_dot=False)
    d.battery("tl", "bl", text="E", positive_at="p1", label_side="left", offset=22)
    d.node("p1", 160, 48, text="1", label_dir="top", offset=10)
    d.node("piv", 220, 48, draw_dot=True)
    d.node("p2", 285, 48, text="2", label_dir="top", offset=10)
    d.wire("tl", "p1")
    d.switch_spdt("piv", "p1", "p2", text="S", label_offset=(0, -18))

    d.node("bm", 220, 182, draw_dot=True)
    d.node("mr", 220, 115, draw_dot=False)
    d.resistor("piv", "mr", text="R₁", label_side="left", offset=16)
    d.capacitor("mr", "bm", text="C₁", label_side="left", offset=18)

    d.node("tr", 375, 48, draw_dot=False)
    d.node("mr2", 375, 115, draw_dot=False)
    d.node("br", 375, 182, draw_dot=False)
    d.wire("p2", "tr")
    d.resistor("tr", "mr2", text="R₂", label_side="right", offset=18)
    d.capacitor("mr2", "br", text="C₂", label_side="right", offset=18)

    d.resistor("bl", "bm", text="R₃", label_side="bottom", offset=20)
    d.wire("bm", "br")
    return d


def ex_2026_2_i2_p1():
    d = FieldGeometryDiagram(500, 250, "Circuito de la I2 2026-2 P1: fuente V0 con interruptor S que carga C1 y C2 en paralelo, que se descargan por R1 y R2; Vout se mide en R2")
    yt, yb = 52, 200
    d.node("src_t", 62, yt, draw_dot=False)
    d.node("src_b", 62, yb, draw_dot=False)
    d.battery("src_t", "src_b", text="V₀", positive_at="p1", label_side="left", offset=24)
    d.wire("src_t", (118, yt))
    d.node("sw_p", 118, yt, draw_dot=True)
    d.node("sw_c", 168, yt, draw_dot=True)
    d.switch_spdt("sw_p", (162, yt - 24), text="S", label_offset=(18, -30))
    d.wire("sw_c", (232, yt))
    d.node("n1", 232, yt, draw_dot=True)
    d.capacitor("n1", (232, yb), text="C₁", label_side="left", offset=22)
    d.wire("n1", (302, yt))
    d.node("n2", 302, yt, draw_dot=True)
    d.capacitor("n2", (302, yb), text="C₂", label_side="left", offset=22)
    d.resistor("n2", (402, yt), text="R₁", label_side="top", offset=20)
    d.node("n3", 402, yt, draw_dot=True)
    d.resistor("n3", (402, yb), text="R₂", label_side="left", offset=22)
    d.wire("src_b", (232, yb), (302, yb), (402, yb))
    d.node("n4", 402, yb, draw_dot=True)
    d.wire("n3", (452, yt))
    d.wire("n4", (452, yb))
    d.terminal_open("op", 452, yt, text="+", label_dir="right", offset=10)
    d.terminal_open("om", 452, yb, text="−", label_dir="right", offset=10)
    d.text(472, 132, "Vₒᵤₜ", cls="sa", anchor="middle")
    d.text(143, 238, "S se cierra un instante cada T", cls="t")
    return d


def figures():
    return {
        "u06-serie-paralelo": serie_paralelo(),
        "u06-kirchhoff-convencion": kirchhoff_convencion(),
        "u06-medidores": medidores(),
        "u06-rc-circuito": rc_circuito(),
        "u06-rc-curvas": rc_curvas(),
        "u06-rc-thevenin": rc_thevenin(),
        "u06-ej1-voltimetro": ej1_voltimetro(),
        "u06-ej2-mallas": ej2_mallas(),
        "u06-ej3-rc-red": ej3_rc_red(),
        "u06-ex-2021-2-ej1": ex_2021_2_ej1(),
        "u06-ex-2022-2-p5": ex_2022_2_p5(),
        "u06-ex-2026-1-p1b": ex_2026_1_p1b(),
        "u06-prac1-red": prac1_red(),
        "u06-prac2-rc-2mallas": prac2_rc_2mallas(),
        "u06-prac3-c2-2026": prac3_c2_2026(),
        "u06-prac4-dos-cap": prac4_dos_cap(),
            "u06-ex-2026-2-i2-p1": ex_2026_2_i2_p1(),
}
