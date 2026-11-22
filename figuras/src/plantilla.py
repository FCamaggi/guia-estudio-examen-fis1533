"""Template figures used by unidades/_plantilla.html (engine smoke test)."""

from svg_primitives import FieldGeometryDiagram


def figures():
    d = FieldGeometryDiagram(440, 240, "Barra conductora sobre rieles en un campo magnético entrante")
    d.motional_rail_circuit(85, 55, width=285, height=130, bar_x=275, v_text="v⃗", B_dir="in",
                            left_elem="resistor", left_label="R", bar_label="ℓ")
    d.text(392, 40, "B⃗ ⊗", cls="sc")
    return {"plantilla-rieles": d}
