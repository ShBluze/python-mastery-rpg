# 📦 Mini-Proyecto 03 — Paquete CLI Publicable

**Dificultad**: 🔴 Difícil | **XP**: 150 | **Módulo**: 04-ecosistema

---

## 📖 Historia

Has creado una herramienta útil y quieres compartirla con el mundo. Empaquétala correctamente y prepárala para publicación.

## 🎯 Requisitos funcionales

- [ ] Estructura src-layout: `src/mi_herramienta/`
- [ ] pyproject.toml completo (PEP 621) con: nombre, versión, descripción, autores, licencia
- [ ] CLI con entry point (`mi-herramienta --help`)
- [ ] Al menos un comando real (ej: convertir temperaturas, generar passwords)
- [ ] Tests con pytest (cobertura > 80%)
- [ ] ruff + mypy pasando sin errores
- [ ] README.md con instrucciones de uso
- [ ] pre-commit configurado
- [ ] GitHub Actions: ruff → mypy → pytest en cada push

## 📋 Criterios de éxito

- `pip install -e .` funciona
- `mi-herramienta --version` muestra versión
- Publicado en TestPyPI
- logging configurable

## 🔗 Recursos

- [26-tooling](../26-tooling.md)
- [28-packaging](../28-packaging.md)
- [25-testing](../25-testing.md)
