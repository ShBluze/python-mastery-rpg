# 👑 Boss Final — Herramienta CLI Profesional

**Ruta**: ⚙️ Automatización | **XP**: 500 | **HP mínimo**: 80

---

## 📖 Historia

Eres el ingeniero de automatización del reino. Construye una herramienta CLI profesional que resuelva un problema real: organizar descargas, hacer backup, monitorear sistema, o convertir formatos.

## 🎯 Requisitos obligatorios

- [ ] CLI con Typer (o Click)
- [ ] Múltiples subcomandos (mínimo 3)
- [ ] Opciones con valores por defecto
- [ ] logging en archivo y consola
- [ ] Tests con pytest (cobertura ≥ 80%)
- [ ] pyproject.toml completo
- [ ] Entry point instalable (`pip install -e .`)
- [ ] Ruff + mypy pasando
- [ ] pre-commit configurado
- [ ] README con ejemplos de uso
- [ ] GitHub Actions CI

## 📋 Criterios de éxito

- `mi-herramienta --help` muestra todos los comandos
- Cada comando maneja errores y muestra mensajes claros
- Cobertura de tests ≥ 80%
- Publicado en TestPyPI

## 📦 Stack

- Typer (principal)
- pathlib, shutil, logging
- pytest, pytest-cov
- ruff, mypy, pre-commit
- build, twine
