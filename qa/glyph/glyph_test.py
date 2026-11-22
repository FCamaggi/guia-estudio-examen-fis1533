import sys
sys.path.insert(0, "scripts")
from svg_primitives import FieldGeometryDiagram

d = FieldGeometryDiagram(460, 230, "Glyph test")
d.motional_rail_circuit(85, 65, width=285, height=130, bar_x=275, v_text="v⃗", B_dir="in", left_elem="resistor", left_label="R", bar_label="ℓ")
d.text(60, 215, "B⃗ ⊙ saliendo", cls="tc", anchor="start")
d.text(300, 215, "dE⃗ = k dq r̂ / r²", cls="s", anchor="start")
d.text(300, 30, "μ⃗ y F⃗", cls="sa", anchor="middle")
open("qa/glyph/glyph_test.svg", "w").write(d.render(standalone=True))
d2 = FieldGeometryDiagram(320, 220, "Tilted loop")
d2.tilted_loop_side_view((160, 110), length=120, angle_deg=28)
open("qa/glyph/tilted.svg", "w").write(d2.render(standalone=True))
