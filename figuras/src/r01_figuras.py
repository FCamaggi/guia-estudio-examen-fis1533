"""R01 course overview map figure. Generate with: python3 scripts/build_figures.py r01"""

from svg_primitives import FieldGeometryDiagram


def mapa_materia():
    d = FieldGeometryDiagram(
        780,
        305,
        "Mapa del curso FIS1533: bloques A, B, C y D conectados por las cuatro ecuaciones de Maxwell y la fuerza de Lorentz",
    )

    # Top row: 4 block cards connected left-to-right (A -> B -> C -> D) with 36px gaps
    cards = [
        (16, "A · Electrostática", "U1–U4", "Cargas en reposo", "E, V, C, dieléctricos", "soft", "a", "ta"),
        (208, "B · Circuitos DC", "U5–U6", "Corriente estacionaria", "J, R, Kirchhoff, RC", "paperf", "w", "tb"),
        (400, "C · Magnetismo", "U7–U8", "Corrientes y cargas", "Fuerza q v×B, Biot-Savart", "csoft", "c", "tc"),
        (592, "D · Inducción y CA", "U9–U11", "Campos variables", "Faraday, L, RLC, ondas", "csoft", "c", "tc"),
    ]
    cw, ch, cy = 156, 108, 18
    for x, title, units, line1, line2, bg_cls, stroke_cls, title_cls in cards:
        d.raw(f'<rect class="{bg_cls}" x="{x}" y="{cy}" width="{cw}" height="{ch}" rx="10"/>', layer="bg")
        d.raw(f'<rect class="{stroke_cls} nofill" x="{x}" y="{cy}" width="{cw}" height="{ch}" rx="10"/>', layer="wires")
        cx = x + cw / 2
        d.text(cx, cy + 24, title, cls=title_cls)
        d.text(cx, cy + 44, units, cls="tb")
        d.text(cx, cy + 68, line1, cls="t")
        d.text(cx, cy + 88, line2, cls="t")

    # Arrows between blocks A -> B -> C -> D
    arrows = [
        (174, 206, "a", "ΔV"),
        (366, 398, "w", "I"),
        (558, 590, "c", "Φ(t)"),
    ]
    for x1, x2, cls, lbl in arrows:
        d.current_arrow((x1, 72), (x2, 72), cls=cls)
        d.text((x1 + x2) / 2, 58, lbl, cls="t")

    # Vertical connectors from blocks down to Maxwell & Lorentz foundation
    for cx in (94, 286, 478, 670):
        d.line((cx, cy + ch + 4), (cx, 158), cls="md")

    # Bottom foundation box: 4 Maxwell equations + Lorentz force
    d.raw('<rect class="paperf" x="16" y="162" width="748" height="126" rx="10"/>', layer="bg")
    d.raw('<rect class="md nofill" x="16" y="162" width="748" height="126" rx="10"/>', layer="wires")
    d.text(390, 184, "Las cuatro ecuaciones de Maxwell y la fuerza de Lorentz unen los cuatro bloques", cls="tb")

    # 4 Maxwell columns inside bottom box
    cols = [
        (106, "1. Gauss eléctrica", "∮ E⃗ · dA⃗ = Q / ε₀", "Cargas crean campo E (U2)", "ta"),
        (286, "2. Gauss magnética", "∮ B⃗ · dA⃗ = 0", "Sin monopolos (U7–U8)", "tb"),
        (466, "3. Faraday-Lenz", "∮ E⃗ · dℓ⃗ = − dΦB / dt", "B(t) crea E (U9)", "tc"),
        (658, "4. Ampère-Maxwell", "∮ B⃗ · dℓ⃗ = μ₀(I + ε₀ dΦE/dt)", "I y E(t) crean B (U8–U9)", "tc"),
    ]
    for cx, name, eq, note, cls in cols:
        d.text(cx, 208, name, cls=cls)
        d.text(cx, 232, eq, cls="s")
        d.text(cx, 252, note, cls="t")

    # Bottom Lorentz + EM wave bar
    d.line((34, 263), (746, 263), cls="m")
    d.text(205, 279, "Lorentz:  F = q(E + v × B)  (U1, U7)", cls="t")
    d.text(575, 279, "Vacío (U11):  c = 1 / √(μ₀ ε₀) ≈ 3×10⁸ m/s", cls="t")

    return d


def figures():
    return {
        "r01-mapa-materia": mapa_materia(),
    }
