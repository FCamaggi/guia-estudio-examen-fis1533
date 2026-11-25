# Guía de estudio · Examen FIS1533 Electricidad y Magnetismo (2026-2)

Guía interactiva para preparar el examen final de FIS1533: 11 unidades autosuficientes (teoría, ejemplos resueltos, problemas de exámenes anteriores con pauta, errores típicos, práctica, autoevaluación y tarjeta de fórmulas), mapa del examen con formulario y notación, dos simulacros con autocorrección y simuladores interactivos de circuitos RL, RLC y fasores.

**Ver la guía:** https://fcamaggi.github.io/guia-estudio-examen-fis1533/

**Material del curso (pruebas anteriores con pauta, clases, ayudantías y apuntes):** https://github.com/FCamaggi/material-fis1533. Los enlaces de `mapa/` apuntan a ese repositorio.

- `index.html`: guía completa (usa `css/` y `js/`).
- `dist/guia-examen.html`: versión en un solo archivo.
- Las fórmulas se renderizan con MathJax desde CDN, así que se necesita conexión a internet.

## Construir

```sh
python3 scripts/build_figures.py        # figuras SVG desde figuras/src/
python3 scripts/check_unit.py unidades/u09-induccion.html   # compuerta de estructura
python3 scripts/build.py                # index.html y dist/guia-examen.html
```

El contrato pedagógico y las compuertas de calidad están en `SPEC-PEDAGOGICO.md`.
