# 08 — Módulos e Imports

> Sistema de módulos: `import`, paquetes, stdlib, imports relativos/absolutos, `__main__`.

---

## Importar módulos

### Formas básicas

```python
# Importar módulo completo
import math
print(math.sqrt(16))  # 4.0

# Importar nombres específicos
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793

# Renombrar (alias)
import numpy as np
import pandas as pd
from collections import defaultdict as dd

# Importar todo (⚠️ evitar en producción)
from math import *  # Contamina namespace
```

---

## Módulos propios

### Estructura típica

```
mi_proyecto/
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── usuario.py
│   └── producto.py
└── servicios/
    ├── __init__.py
    └── auth.py
```

### `modelos/usuario.py`
```python
def crear_usuario(nombre: str, email: str) -> dict:
    return {"nombre": nombre, "email": email, "activo": True}

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
```

### `main.py` — Imports absolutos (recomendados)
```python
# Desde raíz del paquete
from modelos.usuario import crear_usuario, Usuario
from servicios.auth import autenticar

usuario = crear_usuario("Ana", "ana@email.com")
```

### `servicios/auth.py` — Imports relativos
```python
# Un nivel arriba (..), mismo nivel (.)
from ..modelos.usuario import Usuario
from . import helpers  # mismo paquete
```

---

## `__init__.py` — Hacer directorio paquete

```python
# modelos/__init__.py
from .usuario import crear_usuario, Usuario
from .producto import Producto

__all__ = ["crear_usuario", "Usuario", "Producto"]  # Exportación explícita
```

Permite:
```python
from modelos import crear_usuario, Usuario  # Limpio
```

---

## `__main__.py` — Punto de entrada

```
paquete/
├── __main__.py    # python -m paquete
├── __init__.py
└── cli.py
```

```python
# __main__.py
from .cli import main

if __name__ == "__main__":
    main()
```

---

## `if __name__ == "__main__"`

```python
# archivo.py
def funcion_principal():
    print("Ejecutado directamente")

if __name__ == "__main__":
    funcion_principal()  # Solo si python archivo.py

# Si se importa: import archivo → no se ejecuta
```

---

## Módulos de la biblioteca estándar (stdlib) útiles

| Módulo | Uso |
|--------|-----|
| `os`, `pathlib` | FS, paths, env vars |
| `sys` | Argumentos, versión, path, stdout |
| `json`, `csv`, `toml` | Serialización |
| `datetime`, `time`, `calendar` | Fechas/horas |
| `random`, `secrets` | Aleatoriedad (secrets = crypto) |
| `math`, `statistics`, `decimal`, `fractions` | Matemáticas |
| `collections` | `defaultdict`, `Counter`, `deque`, `namedtuple` |
| `itertools`, `functools` | Programación funcional |
| `re` | Expresiones regulares |
| `hashlib`, `hmac` | Hashing, crypto |
| `logging` | Logs estructurados |
| `argparse` | CLI arguments |
| `dataclasses`, `typing` | Tipos, datos |
| `unittest`, `doctest` | Testing built-in |
| `venv`, `subprocess`, `shutil` | Entornos, procesos, archivos |
| `importlib` | Import dinámico, metadata |
| `asyncio`, `threading`, `multiprocessing` | Concurrencia |

---

## Import dinámico (`importlib`)

```python
import importlib

# Importar por string
modulo = importlib.import_module("json")
modulo.dumps({"a": 1})

# Recargar módulo (desarrollo)
import mi_modulo
importlib.reload(mi_modulo)

# Verificar si existe
spec = importlib.util.find_spec("modulo_opcional")
if spec:
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
```

---

## `sys.path` y `PYTHONPATH`

```python
import sys

# Rutas donde busca imports
print(sys.path)
# ['', '/usr/lib/python3.11', ...]

# Añadir ruta temporal
sys.path.insert(0, "/ruta/a/mi/proyecto")

# O variable de entorno
# PYTHONPATH=/ruta/a/proyecto python main.py
```

---

## Buenas prácticas

| ✅ Hacer | ❌ Evitar |
|----------|-----------|
| Imports absolutos desde raíz | Imports relativos profundos (`../../..`) |
| Agrupar: stdlib → third-party → local | Mezclar orden aleatorio |
| Usar `__all__` en `__init__.py` | `from modulo import *` |
| `import modulo` para namespaces | Nombres colisionando |
| `from modulo import nombre` para uso frecuente | Importar 20 nombres de una vez |

```python
# ✅ Orden recomendado (PEP 8)
# 1. Stdlib
import os
import sys
from pathlib import Path
from typing import List, Optional

# 2. Third-party (pip install)
import numpy as np
import requests
from pydantic import BaseModel

# 3. Local
from mi_paquete.modulo import Clase
from . import helpers
```

---

## Errores comunes

### `ModuleNotFoundError`
- Módulo no instalado → `pip install nombre`
- Nombre incorrecto (case-sensitive)
- `sys.path` no incluye el directorio

### `ImportError` / Circular imports
```python
# a.py
from b import func_b

# b.py
from a import func_a  # ← Circular!
```
**Solución**: Mover imports al interior de funciones, o refactorizar a módulo compartido.

### `AttributeError: module 'X' has no attribute 'Y'`
- Nombre mal escrito
- Módulo shadowing (archivo local `json.py` oculta `import json`)
- Versión incorrecta instalada

---

## `pkgutil` / `importlib.metadata` — Introspección

```python
import pkgutil
import importlib.metadata

# Listar submódulos
for _, name, _ in pkgutil.iter_modules(mi_paquete.__path__):
    print(name)

# Metadata de paquete instalado
dist = importlib.metadata.distribution("requests")
print(dist.version)
print(dist.requires)
```

---

---
## 🎯 Ejercicios

Practica módulos en [ejercicios.md](./ejercicios.md#08--módulos-e-imports).

**Mini-ejercicio**: Crea `matematicas.py` con `suma`, `resta`, `multiplica`. Impórtalo desde `main.py`. Añade `if __name__`.

---

## Véase también

- [01-variables-tipos](./01-variables-tipos.md) — `import keyword`
- [09-comentarios-docstrings](./09-comentarios-docstrings.md) — Docstrings en módulos
- [28-packaging](../04-ecosistema/28-packaging.md) — Crear paquetes instalables
- [26-tooling](../04-ecosistema/26-tooling.md) — `ruff` detecta imports no usados
- [ejercicios.md](./ejercicios.md) — Práctica recomendada