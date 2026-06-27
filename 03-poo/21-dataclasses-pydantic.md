# 21 — Dataclasses y Pydantic

> `@dataclass`, `field`, `slots`, herencia, `pydantic.BaseModel`, validación, serialización.

---

## `@dataclass` (Python 3.7+)

Genera automáticamente `__init__`, `__repr__`, `__eq__`, `__hash__` (si `frozen=True`).

```python
from dataclasses import dataclass

@dataclass
class Punto:
    x: int
    y: int

p = Punto(1, 2)
print(p)           # Punto(x=1, y=2)
print(p.x)         # 1
print(p == Punto(1, 2))  # True
```

### Parámetros clave

| Parámetro | Default | Efecto |
|-----------|---------|--------|
| `init` | `True` | Genera `__init__` |
| `repr` | `True` | Genera `__repr__` |
| `eq` | `True` | Genera `__eq__` |
| `order` | `False` | Genera `__lt__`, `__le__`, etc. |
| `frozen` | `False` | Inmutable (como namedtuple) |
| `slots` | `False` | Usa `__slots__` (3.10+) |
| `kw_only` | `False` | Solo keyword args (3.10+) |
| `match_args` | `True` | Soporte `match` (3.10+) |

```python
@dataclass(frozen=True, slots=True, kw_only=True)
class Config:
    host: str = "localhost"
    puerto: int = 8080
    debug: bool = False

c = Config(puerto=3000)  # OK
# c.host = "otro"        # FrozenInstanceError
```

---

## `field()` — Personalizar campos

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Usuario:
    nombre: str
    email: str
    tags: List[str] = field(default_factory=list)  # Mutable default seguro
    _interno: str = field(default="", init=False, repr=False)  # No en __init__
    id: int = field(default=0, compare=False)  # No en __eq__
```

### `field()` parámetros

| Parámetro | Uso |
|-----------|-----|
| `default` | Valor por defecto (inmutable) |
| `default_factory` | Callable para mutables (`list`, `dict`) |
| `init` | Incluir en `__init__` |
| `repr` | Incluir en `__repr__` |
| `compare` | Incluir en `__eq__`/`__lt__` |
| `hash` | Incluir en `__hash__` |
| `metadata` | Dict para herramientas externas |
| `kw_only` | Solo keyword (3.10+) |

---

## `__post_init__` — Lógica post-inicialización

```python
from dataclasses import dataclass, field

@dataclass
class Rectangulo:
    base: float
    altura: float
    area: float = field(init=False, repr=False)
    
    def __post_init__(self):
        if self.base <= 0 or self.altura <= 0:
            raise ValueError("Dimensiones deben ser positivas")
        self.area = self.base * self.altura

r = Rectangulo(3, 4)
print(r.area)  # 12.0
```

---

## Herencia

```python
from dataclasses import dataclass

@dataclass
class Animal:
    nombre: str
    edad: int = 0

@dataclass
class Perro(Animal):
    raza: str
    vacunado: bool = False

rex = Perro("Rex", 3, "Labrador", True)
print(rex)  # Perro(nombre='Rex', edad=3, raza='Labrador', vacunado=True)
```

> Campos de padre **antes** que campos de hijo en `__init__`.

---

## `dataclass` vs `NamedTuple` vs `TypedDict`

| Característica | `@dataclass` | `NamedTuple` | `TypedDict` |
|----------------|--------------|--------------|-------------|
| Mutabilidad | ✅ (o `frozen`) | ❌ Inmutable | ✅ |
| Herencia | ✅ | ❌ | ❌ |
| Métodos propios | ✅ | ✅ | ❌ |
| Type hints | ✅ | ✅ | ✅ |
| Default values | ✅ | ✅ | ⚠️ |
| `__slots__` | 3.10+ | ✅ Nativo | N/A |

---

## Pydantic — Validación + Serialización

```bash
pip install pydantic
```

```python
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)
    email: EmailStr
    edad: int = Field(ge=0, le=150)
    activo: bool = True
    creado: datetime = Field(default_factory=datetime.now)
    tags: list[str] = []
    
    @validator("nombre")
    def nombre_capitalizado(cls, v):
        return v.capitalize()

# Validación automática
u = Usuario(nombre="ana", email="ana@mail.com", edad=25)
print(u)  # nombre='Ana', email='ana@mail.com', edad=25, activo=True, ...

# Error de validación
try:
    Usuario(nombre="a", email="no-email", edad=200)
except Exception as e:
    print(e)
    # 1 validation error for Usuario
    # nombre: ensure this value has at least 2 characters
    # email: value is not a valid email address
    # edad: ensure this value is less than or equal to 150
```

### Serialización

```python
u = Usuario(nombre="Ana", email="ana@mail.com", edad=25)

# A dict
u.dict()           # {'nombre': 'Ana', 'email': 'ana@mail.com', ...}
u.dict(exclude={"edad"})  # Sin edad

# A JSON
u.json()           # '{"nombre": "Ana", "email": "ana@mail.com", ...}'
u.json(indent=2)

# Desde dict/JSON
Usuario.parse_obj({"nombre": "Ana", "email": "ana@mail.com", "edad": 25})
Usuario.parse_raw('{"nombre": "Ana", "email": "ana@mail.com", "edad": 25}')
```

---

## Dataclass vs Pydantic

| Característica | `@dataclass` | `pydantic.BaseModel` |
|----------------|--------------|----------------------|
| **Validación runtime** | ❌ (solo type hints) | ✅ Automática |
| **Serialización** | Manual / `dataclasses.asdict` | ✅ `.dict()`, `.json()` |
| **Parsing** | ❌ | ✅ `parse_obj`, `parse_raw` |
| **Rendimiento** | Muy rápido | Más lento (validación) |
| **Dependencias** | Stdlib | Externa (`pip install pydantic`) |
| **Campos computados** | `__post_init__` | `@property` / `@root_validator` |
| **Settings/Config** | ❌ | ✅ `BaseSettings` (env vars) |

---

## Pydantic v2 (2023+) — Cambios clave

```python
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

class Producto(BaseModel):
    nombre: str
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)
    
    # v2: field_validator (antes @validator)
    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Nombre requerido")
        return v.strip()
    
    # v2: model_validator (antes @root_validator)
    @model_validator(mode="after")
    def verificar_stock_precio(self):
        if self.precio > 1000 and self.stock == 0:
            raise ValueError("Producto caro sin stock")
        return self
```

---

## `BaseSettings` — Config desde env vars

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Mi App"
    debug: bool = False
    database_url: str
    secret_key: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()  # Lee de .env y env vars
print(settings.database_url)
```

```bash
# .env
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=supersecreto
```

---

## `attrs` — Alternativa madura

```bash
pip install attrs
```

```python
import attrs

@attrs.define(slots=True, auto_attribs=True)
class Punto:
    x: int
    y: int
    z: int = 0

p = Punto(1, 2)
print(p)  # Punto(x=1, y=2, z=0)
```

| `attrs` | `@dataclass` |
|---------|--------------|
| Más features (validators, converters) | Stdlib (3.7+) |
| `slots=True` por defecto | `slots=True` (3.10+) |
| Mejor rendimiento | Bueno |
| `frozen`, `kw_only`, `auto_attribs` | Parámetros equivalentes |

---

## Conversión entre tipos

```python
from dataclasses import asdict, astuple
from pydantic import BaseModel

@dataclass
class DC:
    x: int
    y: int

dc = DC(1, 2)
asdict(dc)    # {'x': 1, 'y': 2}
astuple(dc)   # (1, 2)

# Pydantic → Dataclass
class PM(BaseModel):
    x: int
    y: int

pm = PM(x=1, y=2)
dc = DC(**pm.dict())

# Dataclass → Pydantic
pm2 = PM(**asdict(dc))
```

---

## Resumen: Cuándo usar qué

| Caso | Recomendación |
|------|---------------|
| Datos simples, sin validación, stdlib only | `@dataclass` |
| Datos con validación, parsing, serialización | `pydantic.BaseModel` |
| Config desde env vars / .env | `pydantic.BaseSettings` |
| Alto rendimiento, slots, features avanzadas | `attrs` |
| Inmutables, pattern matching | `@dataclass(frozen=True, slots=True)` |
| DTOs, API requests/responses | `pydantic` |

---

---
## 🎯 Ejercicios

Practica dataclasses en [ejercicios.md](../03-poo/ejercicios.md#21--dataclasses-y-pydantic).

**Mini-ejercicio**: Dataclass `Pelicula` con título, año, rating. `__post_init__` que valida año > 1888 y rating entre 0-10.

---

## Véase también

- [15-clases-objetos](./15-clases-objetos.md) — `__slots__`, `__post_init__`
- [16-tipos-metodos](./16-tipos-metodos.md) — Properties vs fields
- [10-type-hints](../02-avanzado/10-type-hints.md) — Type hints en dataclasses
- [28-packaging](../04-ecosistema/28-packaging.md) — `pyproject.toml` con pydantic
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada