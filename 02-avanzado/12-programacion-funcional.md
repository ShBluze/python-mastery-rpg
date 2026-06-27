# 12 — Programación funcional

> `map`, `filter`, `reduce`, `itertools`, `functools`, inmutabilidad, pipelines.

---

## Funciones built-in de orden superior

### `map` — Transformar

```python
# Aplica función a cada elemento
list(map(str.upper, ["a", "b", "c"]))  # ['A', 'B', 'C']

# Con lambda
list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]

# Múltiples iterables (para en el más corto)
list(map(lambda x, y: x + y, [1, 2], [10, 20]))  # [11, 22]

# Equivalente comprehension (preferido)
[x * 2 for x in [1, 2, 3]]
```

### `filter` — Filtrar

```python
# Solo elementos donde función devuelve True
list(filter(lambda x: x % 2 == 0, range(10)))  # [0, 2, 4, 6, 8]

# Con función nombrada
def es_vocal(c): return c in "aeiou"
list(filter(es_vocal, "programacion"))  # ['o', 'a', 'a', 'i', 'o']

# Equivalente comprehension
[x for x in range(10) if x % 2 == 0]
```

### `reduce` — Acumular (en `functools`)

```python
from functools import reduce

# Reduce a valor único
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15

# Con valor inicial
reduce(lambda x, y: x + y, [1, 2, 3], 10)  # 16

# Funcionamiento:
# paso 1: x=1, y=2 → 3
# paso 2: x=3, y=3 → 6
# paso 3: x=6, y=4 → 10
# paso 4: x=10, y=5 → 15
```

---

## `itertools` — Iteradores infinitos y combinatorios

```python
import itertools

# Infinitos
itertools.count(10, 2)        # 10, 12, 14, 16...
itertools.cycle([1, 2, 3])    # 1, 2, 3, 1, 2, 3...
itertools.repeat(7, 3)        # 7, 7, 7

# Combinatorios
itertools.combinations([1,2,3], 2)   # (1,2), (1,3), (2,3)
itertools.permutations([1,2,3], 2)   # (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)
itertools.product([1,2], [3,4])      # (1,3), (1,4), (2,3), (2,4)

# Filtrado/transformación lazy
itertools.islice(itertools.count(), 5)     # 0,1,2,3,4 (primeros 5)
itertools.takewhile(lambda x: x<5, count())  # 0,1,2,3,4
itertools.dropwhile(lambda x: x<3, [1,2,3,4])  # 3,4
itertools.filterfalse(lambda x: x%2, range(6))  # 0,2,4 (opuesto a filter)

# Agrupación
itertools.groupby([1,1,2,2,2,3], key=lambda x: x)
# (1, [1,1]), (2, [2,2,2]), (3, [3])
```

---

## `functools` — Herramientas funcionales

```python
from functools import partial, reduce, lru_cache, cache, singledispatch

# partial — fijar argumentos
def potencia(base, exp):
    return base ** exp

cuadrado = partial(potencia, exp=2)
cubo = partial(potencia, exp=3)
cuadrado(5)  # 25

# lru_cache / cache — memoización
@lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# singledispatch — sobrecarga por tipo
@singledispatch
def procesar(x):
    raise NotImplementedError(type(x))

@procesar.register(int)
def _(x): return x * 2

@procesar.register(str)
def _(x): return x.upper()

procesar(5)      # 10
procesar("hola") # "HOLA"
```

---

## Inmutabilidad

```python
# Tuplas (inmutables)
punto = (10, 20)
# punto[0] = 5  # TypeError

# Named tuples
from collections import namedtuple
Punto = namedtuple("Punto", "x y")
p = Punto(1, 2)
# p.x = 3  # AttributeError

# Dataclasses frozen (Python 3.7+)
from dataclasses import dataclass

@dataclass(frozen=True)
class Punto:
    x: int
    y: int

p = Punto(1, 2)
# p.x = 3  # FrozenInstanceError

# typing.Final (solo static check)
from typing import Final
MAX: Final = 100
# MAX = 200  # mypy error
```

---

## Pipelines funcionales

```python
# Composición: f(g(h(x)))
from functools import reduce

def pipe(valor, *funcs):
    return reduce(lambda v, f: f(v), funcs, valor)

resultado = pipe(
    [1, 2, 3, 4, 5],
    lambda xs: filter(lambda x: x % 2 == 0, xs),
    lambda xs: map(lambda x: x * 10, xs),
    list
)
# [20, 40]

# O con operador | (Python 3.11+ para dict, pero no para funciones)
# Usa librería `toolz` o `funcy` para pipe nativo
```

---

## `operator` — Funciones como operadores

```python
from operator import itemgetter, attrgetter, methodcaller, add, mul

# Acceso por clave/atributo
usuarios = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 30}]
sorted(usuarios, key=itemgetter("edad"))
# [{'nombre': 'Ana', 'edad': 25}, {'nombre': 'Luis', 'edad': 30}]

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre, self.edad = nombre, edad

usuarios_obj = [Usuario("Ana", 25), Usuario("Luis", 30)]
sorted(usuarios_obj, key=attrgetter("edad"))

# Llamar método
palabras = ["hola", "mundo"]
list(map(methodcaller("upper"), palabras))  # ['HOLA', 'MUNDO']

# Operadores como funciones
reduce(add, [1, 2, 3, 4])  # 10
reduce(mul, [1, 2, 3, 4])  # 24
```

---

## Comparativa: Funcional vs Imperativo

```python
# Imperativo
pares_cuadrados = []
for x in range(10):
    if x % 2 == 0:
        pares_cuadrados.append(x ** 2)

# Funcional (comprehension)
pares_cuadrados = [x**2 for x in range(10) if x % 2 == 0]

# Funcional (map/filter)
pares_cuadrados = list(map(lambda x: x**2, filter(lambda x: x%2==0, range(10))))

# Funcional (pipeline con itertools)
from itertools import islice, filterfalse
pares = filterfalse(lambda x: x%2, range(10))
cuadrados = map(lambda x: x**2, pares)
list(islice(cuadrados, 5))
```

> 💡 **Preferir comprehensions** en Python: más legibles, pythonic, y a menudo más rápidas.

---

## Cuándo usar estilo funcional

| ✅ Bueno para | ❌ Evitar para |
|---------------|----------------|
| Transformaciones de datos (ETL) | Lógica de negocio compleja con estado |
| Pipelines de datos | Código con muchos side effects |
| Paralelización (map → multiprocessing) | Algoritmos que necesitan mutación local |
| Código matemático/estadístico | UI, eventos, I/O blocking |

---

## 🎯 Ejercicios

Practica programación funcional en [ejercicios.md](./ejercicios.md#12--programación-funcional).

**Mini-ejercicio**: Pipeline `pares_cuadrados = filter(lambda x: x%2==0, map(lambda x: x**2, range(20)))`. Convierte a list comprehension y compara.

---

## Véase también

- [05-comprehensions-generators](../01-fundamentos/05-comprehensions-generators.md) — Comprehensions vs map/filter
- [11-funciones-avanzadas](./11-funciones-avanzadas.md) — HOF, closures, partial
- [13-async-concurrencia](./13-async-concurrencia.md) — `asyncio.gather`, `run_in_executor`
- [21-dataclasses-pydantic](../03-poo/21-dataclasses-pydantic.md) — `frozen=True`
- [ejercicios.md](./ejercicios.md) — Práctica recomendada