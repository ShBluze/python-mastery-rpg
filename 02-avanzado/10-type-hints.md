# 10 — Type Hints (Anotaciones de tipo)

> Tipado estático opcional para Python: sintaxis, tipos compuestos, genéricos, protocolos.

---

## ¿Qué son y para qué sirven?

Los **type hints** (anotaciones de tipo) indican qué tipo de datos espera una variable, parámetro o retorno.

- **Opcionales** — no afectan ejecución
- **Herramientas**: `mypy`, `pyright`, `ruff` validan en static analysis
- **Beneficios**: autocompletado, detección temprana, documentación viva

> ⚠️ Python **no valida** en runtime. Usa `pydantic`, `beartype`, `typeguard` si necesitas validación real.

---

## Sintaxis básica

```python
# Variables
nombre: str = "Ana"
edad: int = 25
altura: float = 1.75
activo: bool = True

# Funciones
def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

def sumar(a: int, b: int) -> int:
    return a + b
```

---

## Tipos básicos

| Hint | Significado |
|------|-------------|
| `int`, `float`, `str`, `bool` | Escalares |
| `None` | Ausencia de valor |
| `bytes` | Binario |
| `complex` | Complejo |

---

## Colecciones genéricas (Python 3.9+)

```python
# Sin importar typing
numeros: list[int] = [1, 2, 3]
precios: dict[str, float] = {"pan": 1.5}
punto: tuple[int, int] = (10, 20)
unicos: set[str] = {"a", "b"}
congelados: frozenset[int] = frozenset([1, 2])

# Colecciones anidadas
matriz: list[list[int]] = [[1, 2], [3, 4]]
registros: list[dict[str, int]] = [{"a": 1}, {"b": 2}]
```

> Python < 3.9: `from typing import List, Dict, Tuple, Set, FrozenSet`

---

## Tipos compuestos lógicos

### `Union` / `|` (uno u otro)

```python
# Python 3.10+
def procesar(valor: int | str) -> str:
    return f"Valor: {valor}"

# Python < 3.10
from typing import Union
def procesar(valor: Union[int, str]) -> str:
    ...
```

### `Optional` / `T | None` (puede ser None)

```python
# Python 3.10+
def buscar(id: int) -> str | None:
    datos = {1: "Ana", 2: "Luis"}
    return datos.get(id)

# Equivalente (explícito)
from typing import Optional
def buscar(id: int) -> Optional[str]:
    ...
```

### `Literal` (valores exactos)

```python
from typing import Literal

def configurar(modo: Literal["facil", "normal", "dificil"]) -> None:
    print(f"Modo: {modo}")

configurar("facil")     # ✅
configurar("expert")    # ❌ mypy error
```

### `Any` (cualquier cosa — evitar)

```python
from typing import Any

def imprimir(valor: Any) -> None:
    print(valor)  # Sin checks
```

> Úsalo solo: JSON dinámico, legacy, plugins.

---

## Tipos especiales

### `Never` / `NoReturn` (nunca retorna)

```python
from typing import Never

def fallar(msg: str) -> Never:
    raise ValueError(msg)

def loop_infinito() -> Never:
    while True:
        pass
```

### `TypeAlias` (alias de tipos complejos)

```python
from typing import TypeAlias

JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None
UsuarioID: TypeAlias = int

def buscar(usuario_id: UsuarioID) -> str:
    ...
```

### `Callable` (funciones como tipo)

```python
from typing import Callable

def ejecutar(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

ejecutar(3, 5, lambda x, y: x + y)  # 8
```

### `Protocol` (duck typing estructural)

```python
from typing import Protocol

class Volador(Protocol):
    def volar(self) -> None: ...

class Aguila:
    def volar(self) -> None:
        print("Volando")

def hacer_volar(v: Volador) -> None:
    v.volar()

hacer_volar(Aguila())  # ✅ cumple protocolo sin herencia
```

### `TypeVar` (genéricos)

```python
from typing import TypeVar, Generic

T = TypeVar('T')

def primer_elemento(lista: list[T]) -> T:
    return lista[0]

# Clase genérica
class Caja(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor
    def obtener(self) -> T:
        return self.valor

caja_int = Caja(42)        # Caja[int]
caja_str = Caja("hola")    # Caja[str]
```

### `Self` (retorno de la propia clase — Python 3.11+)

```python
from typing import Self

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def con_nombre(self, nombre: str) -> Self:
        self.nombre = nombre
        return self  # Fluido: u.con_nombre("A").con_email("a@b.com")
```

---

## Tabla resumen

| Hint | Propósito | Ejemplo |
|------|-----------|---------|
| `T \| U` | Union | `int \| str` |
| `T \| None` | Optional | `str \| None` |
| `Literal[...]` | Valores exactos | `Literal["a", "b"]` |
| `Any` | Cualquier (evitar) | `Any` |
| `Never` | No retorna | `def f() -> Never` |
| `TypeAlias` | Alias | `ID = int` |
| `Callable[[A], R]` | Función | `Callable[[int], str]` |
| `Protocol` | P` | Protocolo | `class X(P): ...` |
| `TypeVar` | Genérico | `T = TypeVar('T')` |
| `Self` | Propia clase | `def m() -> Self` |
| `Generic[T]` | Clase genérica | `class Box(Generic[T])` |
| `Final` | Constante | `MAX: Final = 100` |
| `ClassVar` | Variable de clase | `count: ClassVar[int] = 0` |
| `Annotated` | Metadatos extra | `Annotated[int, Range(0, 100)]` |

---

## Buenas prácticas

1. **Siempre tipa retorno** `-> Tipo`
2. **Evita `Any`** — usa `object` o genéricos
3. **Usa `|` (3.10+)** en vez de `Union`
4. **`Optional` = `T | None`** — prefiere sintaxis nueva
5. **Type hints en `__init__.py`** para API pública
6. **`pyproject.toml`**: configura `mypy`, `pyright`

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

---

## 🎯 Ejercicios

Practica type hints en [ejercicios.md](./ejercicios.md#10--type-hints).

**Mini-ejercicio**: Tipa una función `procesar_usuarios(usuarios: list[dict]) -> list[str]` que extraiga nombres. Añade tipos a todo.

---

## Véase también

- [03-funciones-esenciales](../01-fundamentos/03-funciones-esenciales.md) — Funciones con type hints
- [11-funciones-avanzadas](./11-funciones-avanzadas.md) — `Callable`, `TypeVar` en decoradores
- [21-dataclasses-pydantic](../03-poo/21-dataclasses-pydantic.md) — Validación runtime con type hints
- [26-tooling](../04-ecosistema/26-tooling.md) — `mypy`, `pyright`, `ruff`
- [ejercicios.md](./ejercicios.md) — Práctica recomendada