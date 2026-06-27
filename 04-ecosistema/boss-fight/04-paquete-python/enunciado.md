# ⚔️ BOSS FIGHT — Paquete Python Publicable

> 🤖 **El Forjador de la Forja** te reta a empaquetar y publicar tu creación.

**Módulo**: 04-ecosistema | **XP**: 300 | **HP mínimo**: 70 | **Dificultad**: 🔴 Avanzado

---

## 📖 Historia

Has recorrido un largo camino. Ahora el Forjador te pide que demuestres tu maestría creando un paquete Python completo desde cero, con tooling moderno, tests, documentación y listo para publicar.

## 🎯 Requisitos del Boss

### Obligatorios
- [ ] Estructura src-layout (`src/mi_paquete/`)
- [ ] pyproject.toml completo (PEP 621) con: nombre, versión, descripción, autores, license, python requires, dependencies
- [ ] Al menos 3 módulos funcionales dentro del paquete
- [ ] CLI con entry point (`mi-comando --help`)
- [ ] Tests con pytest (cobertura ≥ 80%)
- [ ] ruff: sin errores
- [ ] mypy: sin errores
- [ ] pre-commit configurado con ruff y trailing-whitespace
- [ ] GitHub Actions CI (ruff → mypy → pytest)
- [ ] logging estructurado en todo el paquete
- [ ] README.md con: instalación, uso rápido, ejemplos, documentación API
- [ ] `pip install -e .` funciona correctamente

### Bonus
- [ ] Publicado en TestPyPI
- [ ] Documentación con mkdocs o sphinx
- [ ] Badges en README (CI, coverage, python version)

## 📋 Estructura sugerida

```
mi-paquete/
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       ├── utils.py
│       ├── cli.py
│       └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_utils.py
│   └── test_cli.py
├── docs/              # (bonus)
├── .github/
│   └── workflows/
│       └── ci.yml
├── .pre-commit-config.yaml
├── pyproject.toml
└── README.md
```

## ⚔️ Elección del tema del paquete

Elige UNO para tu paquete:
- **PassGen** — Generador de contraseñas seguras
- **FileSorter** — Organizador de archivos por tipo
- **TempConv** — Conversor de temperaturas y unidades
- **Propio** — Idea propia (aprobada por ti mismo)

## 🔗 Recursos

- [25-testing](../../04-ecosistema/25-testing.md)
- [26-tooling](../../04-ecosistema/26-tooling.md)
- [27-logging-debugging](../../04-ecosistema/27-logging-debugging.md)
- [28-packaging](../../04-ecosistema/28-packaging.md)
