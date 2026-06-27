# 17 — Métodos Mágicos (Dunder Methods)

> `__str__`, `__repr__`, operadores, comparaciones, contenedores, protocolo numérico.

---

## ¿Qué son?

Métodos con **doble guion bajo** (`__metodo__`) que Python llama **automáticamente** ante ciertas operaciones. Permiten que tus objetos se comporten como tipos nativos.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):        # self + otro
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)  ← __add__ llamado automáticamente
```

---

## Representación: `__str__` vs `__repr__`

| Método | Propósito | Cuándo se usa |
|--------|-----------|---------------|
| `__str__` | Legible para **usuario** | `print(obj)`, `str(obj)`, `f"{obj}"` |
| `__repr__` | Exacto para **desarrollador** | `repr(obj)`, `print([obj])`, debugging, REPL |

```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.edad} años)"
    
    def __repr__(self) -> str:
        return f"Persona({self.nombre!r}, {self.edad})"

p = Persona("Ana", 30)
print(str(p))   # Ana (30 años)
print(repr(p))  # Persona('Ana', 30)
print([p])      # [Persona('Ana', 30)]  ← usa __repr__
```

### Regla práctica

| Situación | Recomendación |
|-----------|---------------|
| Clase simple | `__str__ = __repr__` |
| Clase técnica/library | Solo `__repr__` (fallback a `print`) |
| Orientada a usuario | Separar ambos |

```python
# Solo __repr__ (común en librerías)
class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"
__str__ = __repr__  # Alias
```

---

## Operadores Aritméticos

| Operador | Método | Reflejado (si `self` no soporta) |
|----------|--------|----------------------------------|
| `+` | `__add__` | `__radd__` |
| `-` | `__sub__` | `__rsub__` |
| `*` | `__mul__` | `__rmul__` |
| `/` | `__truediv__` | `__rtruediv__` |
| `//` | `__floordiv__` | `__rfloordiv__` |
| `%` | `__mod__` | `__rmod__` |
| `**` | `__pow__` | `__rpow__` |
| `@` | `__matmul__` | `__rmatmul__` |

### In-place (modifican `self`)

| Operador | Método |
|----------|--------|
| `+=` | `__iadd__` |
| `-=` | `__isub__` |
| `*=` | `__imul__` |
| etc. | ... |

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __iadd__(self, otro):  # +=
        self.x += otro.x
        self.y += otro.y
        return self
    
    def __mul__(self, escalar):  # vector * 2
        return Vector(self.x * escalar, self.y * escalar)
    
    def __rmul__(self, escalar):  # 2 * vector
        return self * escalar
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(1, 2)
print(v + Vector(3, 4))  # Vector(4, 6)
print(v * 3)             # Vector(3, 6)
print(3 * v)             # Vector(3, 6)  ← __rmul__
v += Vector(1, 1)        # v modificado in-place
```

---

## Comparaciones

| Operador | Método |
|----------|--------|
| `==` | `__eq__` |
| `!=` | `__ne__` (auto si `__eq__`) |
| `<` | `__lt__` |
| `<=` | `__le__` |
| `>` | `__gt__` |
| `>=` | `__ge__` |

### `@total_ordering` (solo define `__eq__` + uno)

```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, major, minor, patch):
        self.tupla = (major, minor, patch)
    
    def __eq__(self, otro):
        return self.tupla == otro.tupla
    
    def __lt__(self, otro):
        return self.tupla < otro.tupla

v1 = Version(1, 2, 3)
v2 = Version(1, 3, 0)
print(v1 < v2)   # True
print(v1 <= v2)  # True (generado)
print(v1 > v2)   # False (generado)
```

---

## Contenedores (Protocolo Sequence/Mapping)

| Operación | Método |
|-----------|--------|
| `len(obj)` | `__len__` |
| `obj[key]` | `__getitem__` |
| `obj[key] = val` | `__setitem__` |
| `del obj[key]` | `__delitem__` |
| `key in obj` | `__contains__` |
| `iter(obj)` | `__iter__` |
| `reversed(obj)` | `__reversed__` |

```python
class Rango:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
    
    def __len__(self):
        return self.fin - self.inicio
    
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return [self.inicio + i for i in range(*idx.indices(len(self)))]
        if idx < 0: idx += len(self)
        if 0 <= idx < len(self):
            return self.inicio + idx
        raise IndexError
    
    def __contains__(self, valor):
        return self.inicio <= valor < self.fin
    
    def __iter__(self):
        return iter(range(self.inicio, self.fin))
    
    def __repr__(self):
        return f"Rango({self.inicio}, {self.fin})"

r = Rango(0, 5)
print(len(r))       # 5
print(r[2])         # 2
print(r[1:4])       # [1, 2, 3]
print(3 in r)       # True
print(list(r))      # [0, 1, 2, 3, 4]
```

---

## Conversión y Protocolo Numérico

| Operación | Método |
|-----------|--------|
| `int(obj)` | `__int__` |
| `float(obj)` | `__float__` |
| `complex(obj)` | `__complex__` |
| `bool(obj)` | `__bool__` |
| `hash(obj)` | `__hash__` |
| `bytes(obj)` | `__bytes__` |
| `format(obj, spec)` | `__format__` |

```python
class Fraccion:
    def __init__(self, num, den):
        self.num, self.den = num, den
    
    def __float__(self):
        return self.num / self.den
    
    def __int__(self):
        return self.num // self.den
    
    def __bool__(self):
        return self.num != 0
    
    def __hash__(self):
        return hash((self.num, self.den))
    
    def __repr__(self):
        return f"Fraccion({self.num}, {self.den})"

f = Fraccion(3, 4)
print(float(f))  # 0.75
print(int(f))    # 0
print(bool(f))   # True
d = {f: "valor"}  # Funciona como clave (hashable)
```

---

## Llamada y Atributos Dinámicos

| Operación | Método |
|-----------|--------|
| `obj()` | `__call__` |
| `obj.attr` (lectura) | `__getattribute__` / `__getattr__` |
| `obj.attr = val` | `__setattr__` |
| `del obj.attr` | `__delattr__` |
| `dir(obj)` | `__dir__` |

```python
class Multiplicador:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

doble = Multiplicador(2)
print(doble(5))  # 10  ← se llama como función
```

### `__getattr__` vs `__getattribute__`

```python
class Dynamic:
    def __init__(self):
        self.data = {"a": 1}
    
    def __getattr__(self, name):  # Solo si NO existe
        return self.data.get(name, f"no {name}")
    
    def __getattribute__(self, name):  # SIEMPRE (cuidado: recursión)
        return super().__getattribute__(name)

d = Dynamic()
print(d.a)      # 1 (existe en data)
print(d.b)      # "no b" (usa __getattr__)
```

> ⚠️ `__getattribute__` se llama **siempre** — fácil recursión infinita. Usa `__getattr__` para fallback.

---

## Context Managers

```python
class Archivo:
    def __init__(self, ruta, modo):
        self.ruta, self.modo = ruta, modo
        self.f = None
    
    def __enter__(self):
        self.f = open(self.ruta, self.modo)
        return self.f
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()
        return False  # No suprimir excepciones

with Archivo("datos.txt", "w") as f:
    f.write("Hola")
# __exit__ cierra automáticamente
```

---

## Ciclo de Vida

| Método | Cuándo |
|--------|--------|
| `__new__(cls, ...)` | Creación **antes** de `__init__` (raro) |
| `__init__(self, ...)` | Inicialización (común) |
| `__del__(self)` | Destrucción (GC, no garantizado cuándo) |

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True
```

### `__del__` — Cuidado

```python
class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Creado: {nombre}")
    
    def __del__(self):
        print(f"Destruido: {self.nombre}")

# ⚠️ No confíes en __del__ para limpieza crítica
# Usa context managers (with) o try/finally
```

---

## Tabla Resumen Completa

| Categoría | Métodos |
|-----------|---------|
| **Representación** | `__str__`, `__repr__`, `__format__`, `__bytes__` |
| **Aritmética** | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__matmul__` + `__r*__`, `__i*__` |
| **Comparación** | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` |
| **Contenedor** | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`, `__reversed__` |
| **Conversión** | `__int__`, `__float__`, `__complex__`, `__bool__`, `__hash__`, `__index__` |
| **Atributos** | `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__` |
| **Llamada** | `__call__` |
| **Context Manager** | `__enter__`, `__exit__` |
| **Ciclo vida** | `__new__`, `__init__`, `__del__` |
| **Descriptores** | `__get__`, `__set__`, `__delete__`, `__set_name__` |
| **Class creation** | `__init_subclass__`, `__class_getitem__` |

---

## Buenas prácticas

1. **Siempre `__repr__`** en clases serias
2. **`@total_ordering`** para comparaciones
3. **`__slots__`** si muchos objetos + memoria
4. **Devuelve `NotImplemented`** (no `False`) en operadores binarios si tipo no soportado
5. **Inmutables**: `__hash__` + `__eq__` consistentes

```python
def __add__(self, otro):
    if not isinstance(otro, MiClase):
        return NotImplemented  # Deja que Python intente otro.__radd__
    return MiClase(self.valor + otro.valor)
```

---

---
## 🎯 Ejercicios

Practica métodos mágicos en [ejercicios.md](../03-poo/ejercicios.md#17--métodos-mágicos).

**Mini-ejercicio**: Clase `Vector2D` con `__add__`, `__sub__`, `__mul__` (escalar), `__repr__`. Opera como `v1 + v2`.

---

## Véase también

- [15-clases-objetos](./15-clases-objetos.md) — `__init__`, `__dict__`, `__slots__`
- [16-tipos-metodos](./16-tipos-metodos.md) — Properties, classmethods
- [19-encapsulamiento](./19-encapsulamiento.md) — `__del__`, ref counting, name mangling
- [21-dataclasses-pydantic](../03-poo/21-dataclasses-pydantic.md) — Generan `__init__`, `__repr__`, `__eq__` automáticamente
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada