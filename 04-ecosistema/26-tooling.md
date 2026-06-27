# 26 — Tooling Moderno

> `ruff`, `mypy`, `black`, `uv`, `pyproject.toml`, pre-commit, CI/CD.

---

## `ruff` — Linter + Formatter Unificado (Rust, ultra-rápido)

```bash
pip install ruff
# o: pipx install ruff
```

```bash
ruff check .           # Lint
ruff check --fix .     # Auto-fix
ruff format .          # Format (black-compatible)
ruff format --check .  # Solo verificar formato
```

```toml
# pyproject.toml
[tool.ruff]
target-version = "py311"
line-length = 100
select = [
    "E", "F", "I", "W",  # pycodestyle, pyflakes, isort, warnings
    "UP", "B", "C4", "T20",  # pyupgrade, flake8-bugbear, flake8-comprehensions, flake8-print
    "ARG", "PTH", "ERA", "PL", "TRY", "NPY", "RUF", "SIM", "TID", "QF",
]
ignore = ["E501"]  # line-length manejado por formatter
fixable = ["ALL"]
unfixable = []

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "lf"

[tool.ruff.lint.isort]
known-first-party = ["mi_paquete"]
```

> 💡 **Ruff reemplaza**: `flake8`, `isort`, `black`, `pyupgrade`, `autoflake`, `pydocstyle` (parcial).

---

## `mypy` — Type Checker Estático

```bash
pip install mypy
# Types stubs para librerías externas
pip install types-requests types-pyyaml types-toml
```

```bash
mypy src/                    # Check
mypy --strict src/           # Modo estricto
mypy --html-report report/   # Reporte visual
```

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
implicit_reexport = true

[[tool.mypy.overrides]]
module = ["tests.*", "conftest"]
disallow_untyped_defs = false

# Ignorar librerías sin stubs
[tool.mypy.plugins]
plugins = ["pydantic.mypy"]
```

### Módulos sin stubs

```toml
# pyproject.toml
[[tool.mypy.overrides]]
module = [
    "librería_sin_tipos",
    "otra_lib",
]
ignore_missing_imports = true
```

---

## `black` — Formatter (si no usas ruff format)

```bash
pip install black
black src/
black --check src/  # Solo verificar
```

```toml
# pyproject.toml
[tool.black]
line-length = 100
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

---

## `uv` — Gestor Paquetes Ultra-Rápido (Rust)

```bash
# Instalar
curl -LsSf https://astral.sh/uv/install.sh | sh
# o: pipx install uv
```

### Uso básico

```bash
# Crear proyecto
uv init mi_proyecto
cd mi_proyecto

# Añadir dependencias
uv add requests pydantic
uv add --dev pytest ruff mypy

# Eliminar
uv remove requests

# Sincronizar (desde lockfile)
uv sync
uv sync --dev

# Ejecutar en entorno
uv run pytest
uv run python script.py

# Instalar herramienta global
uv tool install ruff
uv tool run ruff check .
```

### `uv.lock` — Lockfile Universal

```bash
uv lock              # Genera/actualiza uv.lock
uv lock --upgrade    # Actualiza todas
uv lock --upgrade-package requests  # Actualiza una
```

> ✅ **`uv.lock` es compatible con `pip`** — `pip install -r uv.lock` funciona.

### Virtual Environments

```bash
uv venv                    # Crea .venv
uv venv --python 3.11      # Python específico
source .venv/bin/activate  # Activar

# uv usa .venv automáticamente si existe
```

---

## `pyproject.toml` — Configuración Unificada

```toml
[project]
name = "mi_paquete"
version = "0.1.0"
description = "Descripción corta"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [{name = "Tu Nombre", email = "tu@email.com"}]
maintainers = []
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]
dependencies = [
    "requests>=2.31",
    "pydantic>=2.0",
    "click>=8.1",
]
optional-dependencies = {
    "dev": ["pytest>=7.4", "ruff>=0.1", "mypy>=1.5"],
    "docs": ["mkdocs>=1.5", "mkdocstrings[python]>=0.23"],
    "db": ["sqlalchemy>=2.0", "asyncpg>=0.28"],
}

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=7.4",
    "ruff>=0.1",
    "mypy>=1.5",
    "pytest-cov>=4.1",
    "pytest-mock>=3.12",
    "pytest-asyncio>=0.21",
    "hypothesis>=6.8",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --strict-markers --strict-config"
markers = [
    "slow: tests lentos",
    "integration: requieren BD/servicios",
]

[tool.ruff]
# ... (ver sección ruff arriba)

[tool.mypy]
# ... (ver sección mypy arriba)

[tool.coverage.run]
source = ["mi_paquete"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
exclude_lines = ["pragma: no cover", "def __repr__", "raise AssertionError"]
```

---

## `pre-commit` — Git Hooks Automatizados

```bash
pip install pre-commit
pre-commit install
```

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests, types-pyyaml]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-added-large-files
      - id: detect-private-key

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: [-r, src/]

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: uv run pytest -q
        language: system
        pass_filenames: false
        always_run: true
```

```bash
pre-commit run --all-files  # Ejecutar manualmente
pre-commit run --hook-stage push  # Solo en push
```

---

## CI/CD — GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install uv
        uses: astral-sh/setup-uv@v3
        with:
          version: "latest"
      
      - name: Set up Python
        run: uv python install 3.11
      
      - name: Sync dependencies
        run: uv sync --dev --frozen
      
      - name: Ruff check
        run: uv run ruff check .
      
      - name: Ruff format
        run: uv run ruff format --check .
      
      - name: Mypy
        run: uv run mypy src/
      
      - name: Tests with coverage
        run: uv run pytest --cov=mi_paquete --cov-fail-under=80
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        if: always()
```

---

## Versionado Automático

```bash
# Opción 1: hatch-vcs (usa git tags)
pip install hatch-vcs
```

```toml
# pyproject.toml
[tool.hatch.version]
source = "vcs"

[tool.hatch.build.targets.wheel]
packages = ["src/mi_paquete"]
```

```bash
# Opción 2: bump2version
pip install bump2version
bump2version patch  # 0.1.0 -> 0.1.1
bump2version minor  # 0.1.1 -> 0.2.0
bump2version major  # 0.2.0 -> 1.0.0
```

```ini
# .bumpversion.cfg
[bumpversion]
current_version = 0.1.0
commit = True
tag = True

[bumpversion:file:pyproject.toml]
```

---

## Dependencias de Seguridad

```bash
pip install pip-audit safety
uv run pip-audit
uv run safety check
```

```yaml
# .github/workflows/security.yml
- name: Security audit
  run: uv run pip-audit --desc
```

---

## Resumen: Stack Recomendado 2024

| Función | Herramienta | Por qué |
|---------|-------------|---------|
| **Package manager** | `uv` | 10-100x más rápido que pip |
| **Lint + Format** | `ruff` | Unificado, ultra-rápido, Rust |
| **Type checking** | `mypy` | Estándar, maduro, buena integración |
| **Test runner** | `pytest` | Ecosistema rico, fixtures, plugins |
| **Coverage** | `pytest-cov` | Integrado en pytest |
| **Property testing** | `hypothesis` | Encuentra edge cases |
| **Git hooks** | `pre-commit` | Estándar, multiplataforma |
| **CI** | GitHub Actions | Nativo en GitHub |
| **Build backend** | `hatchling` | Moderno, rápido, estándar |
| **Versioning** | `hatch-vcs` / `bump2version` | Automático desde git tags |

---

## 🎯 Ejercicios

Practica tooling en [ejercicios.md](./ejercicios.md#26--tooling).

**Mini-ejercicio**: Crea un `pyproject.toml` mínimo con ruff configurado. Ejecuta `ruff check` sobre un archivo con errores intencionales.

---

## Véase también

- [25-testing](./25-testing.md) — pytest, fixtures, coverage
- [27-logging-debugging](./27-logging-debugging.md) — Debugging tools
- [28-packaging](./28-packaging.md) — Build, publish, pyproject.toml
- [ejercicios.md](./ejercicios.md) — Práctica recomendada