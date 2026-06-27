# 28 — Packaging & Distribución

> `pyproject.toml`, `hatchling`, `setuptools`, `twine`, `pip`, `uv`, publicación en PyPI.

---

## Estructura de Proyecto

```
mi_paquete/
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       ├── modulo_a.py
│       └── modulo_b.py
├── tests/
│   ├── __init__.py
│   ├── test_modulo_a.py
│   └── test_modulo_b.py
├── docs/
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

> 💡 La carpeta `src/` evita importar el paquete desde el directorio raíz del proyecto.

---

## `pyproject.toml` — Configuración Moderna (PEP 621)

```toml
[project]
name = "mi-paquete"
version = "0.1.0"
description = "Descripción corta del paquete"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Tu Nombre", email = "tu@email.com"},
]
maintainers = []
keywords = ["python", "utilidad"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Typing :: Typed",
]
dependencies = [
    "requests>=2.31",
    "pydantic>=2.0",
]
optional-dependencies = {
    "dev": [
        "pytest>=7.4",
        "ruff>=0.1",
        "mypy>=1.5",
        "pytest-cov>=4.1",
    ],
    "docs": [
        "mkdocs>=1.5",
        "mkdocstrings[python]>=0.23",
    ],
    "speed": [
        "orjson>=3.9",
    ],
}

[project.urls]
Homepage = "https://github.com/tu/mi-paquete"
Documentation = "https://mi-paquete.readthedocs.io"
Repository = "https://github.com/tu/mi-paquete.git"
Changelog = "https://github.com/tu/mi-paquete/blob/main/CHANGELOG.md"

[project.scripts]
mi-cli = "mi_paquete.cli:main"

[project.entry-points."mi_paquete.plugins"]
plugin_a = "mi_paquete.plugin_a"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/mi_paquete"]
```

---

## Build Backends

| Backend       | Ventajas                              | Recomendado para              |
|---------------|---------------------------------------|-------------------------------|
| `hatchling`   | Rápido, moderno, integrado con `hatch`| Proyectos nuevos              |
| `setuptools`  | Estándar, muchas extensiones          | Proyectos legacy              |
| `flit`        | Simple, mínimo boilerplate            | Paquetes pequeños             |
| `pdm-backend` | Integrado con `pdm`                   | Proyectos con PDM             |
| `maturin`     | Para extensiones Rust (PyO3)          | Proyectos Rust+Python         |

---

## Construir el Paquete

```bash
# Instalar build
pip install build

# Construir wheel + source distribution
python -m build

# Output:
# dist/
#   mi_paquete-0.1.0-py3-none-any.whl
#   mi_paquete-0.1.0.tar.gz
```

---

## Publicar en PyPI

### TestPyPI (pruebas)

```bash
pip install twine

twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Instalar desde TestPyPI
pip install --index-url https://test.pypi.org/simple/ mi-paquete
```

### PyPI oficial

```bash
twine upload dist/*

# Se pedirá usuario y contraseña (o token)
# Alternativa: usar __token__ como usuario
```

### Automatización con GitHub Actions

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: pypi
    permissions:
      id-token: write  # Para Trusted Publishing

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v3

      - name: Build
        run: uv build

      - name: Publish
        uses: pypa/gh-action-pypi-publish@release/v1
```

> 🔑 **Trusted Publishing**: No necesitas tokens — GitHub confía automáticamente en PyPI.

---

## Versionado

### `hatch-vcs` (desde git tags)

```toml
# pyproject.toml
[tool.hatch.version]
source = "vcs"
```

```bash
git tag v0.1.0
```

### `bump2version`

```bash
pip install bump2version
```

```ini
# .bumpversion.cfg
[bumpversion]
current_version = 0.1.0
commit = True
tag = True

[bumpversion:file:pyproject.toml]
```

```bash
bump2version patch  # 0.1.0 → 0.1.1
bump2version minor  # 0.1.1 → 0.2.0
bump2version major  # 0.2.0 → 1.0.0
```

### `setuptools-scm`

```toml
[build-system]
requires = ["setuptools", "setuptools-scm"]
build-backend = "setuptools.backends._legacy:_Backend"

[tool.setuptools_scm]
write_to = "src/mi_paquete/_version.py"
```

---

## Dependencias Opcionales (Extras)

```toml
[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]
db = ["sqlalchemy", "asyncpg"]
all = ["mi-paquete[dev,db]"]
```

```bash
pip install mi-paquete[dev]
pip install mi-paquete[db]
pip install mi-paquete[all]
```

---

## Lockfiles y Reproducibilidad

### `uv`

```bash
uv lock              # Genera uv.lock
uv sync --frozen     # Instala desde lock
uv lock --upgrade-package requests  # Actualiza una dep
```

### `pip-tools`

```bash
pip install pip-tools

# Compilar requirements
pip-compile pyproject.toml --extra dev -o requirements.txt
pip-compile pyproject.toml --extra dev -o dev-requirements.txt

# Sincronizar
pip-sync requirements.txt dev-requirements.txt
```

---

## 🎯 Ejercicios

Practica packaging en [ejercicios.md](./ejercicios.md#28--packaging).

**Mini-ejercicio**: Crea paquete `saludos/` con `__init__.py` que exporte `hola()` y `adios()`. Instálalo con `pip install -e .`.

---

## Véase también

- [26-tooling](./26-tooling.md) — `uv`, `ruff`, `mypy` en CI
- [27-logging-debugging](./27-logging-debugging.md) — Logging en producción
- [ejercicios.md](./ejercicios.md) — Práctica recomendada
