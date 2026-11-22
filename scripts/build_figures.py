#!/usr/bin/env python3
"""Generate figuras/svg/*.svg from every figuras/src/*.py module.

Each module defines `figures() -> dict[str, CircuitDiagram | str]` mapping a figure
name (kebab-case, prefixed with the unit id, e.g. "u09-barra-rieles") to a diagram
or an SVG string. Usage: python3 scripts/build_figures.py [module-substring ...]
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SRC, OUT = BASE / "figuras" / "src", BASE / "figuras" / "svg"
sys.path.insert(0, str(BASE / "scripts"))


def main(filters: list[str]) -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for mod_path in sorted(SRC.glob("*.py")):
        if filters and not any(f in mod_path.stem for f in filters):
            continue
        spec = importlib.util.spec_from_file_location(mod_path.stem, mod_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for name, fig in mod.figures().items():
            svg = fig if isinstance(fig, str) else fig.render(standalone=True)
            (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
            written.append(f"figuras/svg/{name}.svg")
    print("\n".join(written))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
