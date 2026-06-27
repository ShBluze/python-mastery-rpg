# ✅ Criterios de Aprobación — Boss: Paquete Python

---

## Obligatorios

- [ ] Estructura src-layout correcta
- [ ] pyproject.toml con metadata completa (name, version, authors, license, requires-python, dependencies)
- [ ] 3+ módulos funcionales dentro del paquete
- [ ] CLI entry point funcional (`mi-comando --help` muestra ayuda)
- [ ] pytest pasa con ≥ 80% coverage
- [ ] ruff: 0 errores
- [ ] mypy: 0 errores (strict mode recomendado)
- [ ] .pre-commit-config.yaml con ruff hook
- [ ] GitHub Actions workflow: ruff → mypy → pytest
- [ ] logging.getLogger(__name__) en cada módulo
- [ ] README.md con instalación, ejemplo rápido, documentación de API
- [ ] `pip install -e .` funciona y el paquete se importa correctamente
- [ ] `python -m mi_paquete` funciona (__main__.py)

## Bonus

- [ ] Publicado en TestPyPI
- [ ] Documentación con mkdocs/sphinx
- [ ] Badges en README

---

## Resultado

- **Obligatorios**: _/13
- **Bonus**: _/3
- **¿Pasa?**: ❌ No / ✅ Sí

> 🎉 Si pasas este Boss, ¡habrás completado el nivel Intermedio! Especialización desbloqueada.
