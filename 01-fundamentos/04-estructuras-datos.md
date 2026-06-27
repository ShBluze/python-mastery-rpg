# 04 — Estructuras de datos

> Listas, tuplas, diccionarios, sets — cuándo y cómo usar cada una.

---

## Tabla comparativa

| Estructura | Acceso | Mutable | Duplicados | Ordenada | Métodos clave | Uso principal |
|------------|--------|---------|------------|----------|---------------|---------------|
| **`list`** | Índice `l[0]` | ✅ | ✅ | ✅ | `append`, `pop`, `remove`, `sort`, `reverse` | Secuencias dinámicas |
| **`tuple`** | Índice `t[0]` | ❌ | ✅ | ✅ | `count`, `index` | Datos fijos, claves dict |
| **`dict`** | Clave `d["k"]` | ✅ | Claves: no | ✅ (3.7+) | `get`, `keys`, `values`, `items`, `update` | Objetos, JSON, config |
| **`set`** | Sin índice | ✅ | ❌ | ❌ | `add`, `remove`, `union`, `intersection` | Unicidad, ops. matemáticas |

> 🔑 **Regla**: Elige por **cómo accedes** (índice vs clave) y **mutabilidad** necesaria.

---

## Listas (`list`)

### Creación
```python
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]
lista3 = list(range(5))        # [0, 1, 2, 3, 4]
lista4 = list("hola")          # ['h', 'o', 'l', 'a']
```

### Acceso e índice
```python
frutas = ["manzana", "pera", "uva"]
print(frutas[0])    # manzana
print(frutas[-1])   # uva (índice negativo = desde el final)
print(frutas[1:3])  # ['pera', 'uva'] (slicing)
```

### Métodos mutadores
```python
nums = [1, 2, 3]
nums.append(4)       # [1, 2, 3, 4]
nums.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
nums.insert(0, 0)    # [0, 1, 2, 3, 4, 5, 6]
nums.pop()           # 6 → [0, 1, 2, 3, 4, 5]
nums.pop(0)          # 0 → [1, 2, 3, 4, 5]
nums.remove(3)       # [1, 2, 4, 5] (elimina primera ocurrencia)
nums.clear()         # []
```

### Ordenación
```python
nums = [3, 1, 4, 1, 5]
nums.sort()          # [1, 1, 3, 4, 5] (in-place)
nums.sort(reverse=True)  # [5, 4, 3, 1, 1]

# sorted() devuelve NUEVA lista
ordenada = sorted([3, 1, 4])  # [1, 3, 4]
```

### Slicing (rebanadas)
```python
nums = [0, 1, 2, 3, 4, 5]
nums[1:4]      # [1, 2, 3]
nums[:3]       # [0, 1, 2]
nums[3:]       # [3, 4, 5]
nums[::2]      # [0, 2, 4] (cada 2)
nums[::-1]     # [5, 4, 3, 2, 1, 0] (invertido)
```

---

## Tuplas (`tuple`)

Inmutables, hashables, menos memoria.

```python
t = (1, 2, 3)
punto = (10, 20)
x, y = punto          # Desempaquetado: x=10, y=20

# Métodos (solo 2)
t = (1, 2, 3, 2, 4, 2)
t.count(2)   # 3
t.index(3)   # 2

# Conversión
lista = [1, 2, 3]
tupla = tuple(lista)   # (1, 2, 3)
lista2 = list(tupla)   # [1, 2, 3]

# Tuplas anidadas
matriz = ((1, 2), (3, 4), (5, 6))
matriz[1][0]  # 3
```

> 💡 Usa tuplas para: coordenadas, claves de dict, retorno múltiple, datos que no deben cambiar.

---

## Diccionarios (`dict`)

### Básico
```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])  # Ana

# Claves: str, int, tuple (inmutables). Valores: cualquier cosa.
```

### Operaciones CRUD
```python
usuario = {"nombre": "Luis", "edad": 30}

# Leer (seguro)
usuario.get("nombre")           # "Luis"
usuario.get("telefono")         # None
usuario.get("telefono", "N/A")  # "N/A" (default)

# Escribir / Actualizar
usuario["edad"] = 31
usuario["email"] = "luis@email.com"

# Eliminar
del usuario["edad"]
email = usuario.pop("email")    # devuelve y elimina
```

### Métodos clave
```python
usuario = {"nombre": "Luis", "edad": 30, "ciudad": "Madrid"}

usuario.keys()      # dict_keys(['nombre', 'edad', 'ciudad'])
usuario.values()    # dict_values(['Luis', 30, 'Madrid'])
usuario.items()     # dict_items([('nombre', 'Luis'), ...])

# Iterar
for k, v in usuario.items():
    print(f"{k}: {v}")

# Actualizar masivo
usuario.update({"edad": 32, "telefono": "123456789"})
```

### Diccionarios anidados
```python
empresa = {
    "dev1": {"nombre": "Ana", "lenguaje": "Python"},
    "dev2": {"nombre": "Luis", "lenguaje": "Go"}
}
empresa["dev1"]["lenguaje"]  # "Python"
```

### `setdefault` / `defaultdict`
```python
# setdefault: asigna si no existe
d = {}
d.setdefault("key", []).append(1)  # {'key': [1]}

# collections.defaultdict (más limpio)
from collections import defaultdict
d = defaultdict(list)
d["key"].append(1)  # {'key': [1]}
```

---

## Sets (`set`)

Colección **sin duplicados**, no ordenada, mutable.

```python
s = {1, 2, 3, 2, 1}   # {1, 2, 3} (dedup automático)
empty = set()          # {} es dict vacío, usar set()
```

### Operaciones
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.add(5)        # {1, 2, 3, 4, 5}
a.remove(2)     # {1, 3, 4, 5} (KeyError si no existe)
a.discard(99)   # No error si no existe
a.pop()         # Elimina y devuelve elemento arbitrario
```

### Operaciones matemáticas
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # Unión: {1, 2, 3, 4, 5, 6}
a & b   # Intersección: {3, 4}
a - b   # Diferencia: {1, 2}
a ^ b   # Diferencia simétrica: {1, 2, 5, 6}

# In-place
a |= b  # a = a | b
a &= b  # a = a & b
```

### Frozenset (inmutable, hashable)
```python
fs = frozenset([1, 2, 3])
d = {fs: "valor"}  # Puede ser clave de dict
```

---

## Conversión entre estructuras

```python
# list ↔ tuple
list((1, 2))      # [1, 2]
tuple([1, 2])     # (1, 2)

# list ↔ set (dedup)
list({1, 2, 2})   # [1, 2]
set([1, 2, 2])    # {1, 2}

# dict → list/tuple
d = {"a": 1, "b": 2}
list(d)           # ['a', 'b'] (claves)
list(d.keys())    # ['a', 'b']
list(d.values())  # [1, 2]
list(d.items())   # [('a', 1), ('b', 2)]

# dict desde pares
dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
```

---

## Resumen de métodos

| Operación | `list` | `tuple` | `dict` | `set` |
|-----------|--------|---------|--------|-------|
| Longitud | `len(l)` | `len(t)` | `len(d)` | `len(s)` |
| `in` / `not in` | ✅ | ✅ | ✅ (claves) | ✅ |
| Índice | `l[i]` | `t[i]` | `d[k]` | ❌ |
| Slicing | `l[i:j]` | `t[i:j]` | ❌ | ❌ |
| Añadir | `append` | ❌ | `d[k]=v` | `add` |
| Eliminar | `pop`, `remove` | ❌ | `del`, `pop` | `remove`, `discard`, `pop` |
| Ordenar | `sort()` | ❌ | ❌ | ❌ |
| Invertir | `reverse()` | ❌ | ❌ | ❌ |

---

## Cuál elegir (decision tree)

```
¿Necesitas acceso por índice ordenado?
  ├─ Sí → ¿Debe ser mutable?
  │       ├─ Sí → list
  │       └─ No → tuple
  └─ No → ¿Clave-valor?
          ├─ Sí → dict
          └─ No → ¿Unicidad + ops. conjuntos?
                  ├─ Sí → set
                  └─ No → list (por defecto)
```

---

## 🎯 Ejercicios

Practica estructuras de datos en [ejercicios.md](./ejercicios.md#04--estructuras-de-datos).

**Mini-ejercicio**: Dada lista de nombres, cuenta frecuencias con dict, encuentra el más común, ordena alfabéticamente.

---

## Véase también

- [03-funciones-esenciales](./03-funciones-esenciales.md) — Mutabilidad en parámetros
- [05-comprehensions-generators](./05-comprehensions-generators.md) — Crear estructuras compactamente
- [10-type-hints](../02-avanzado/10-type-hints.md) — `list[int]`, `dict[str, int]`, etc.
- [ejercicios.md](./ejercicios.md) — Práctica recomendada