# 05 — Comprehensions y Generadores

> Sintaxis compacta para crear colecciones: list/dict/set comprehensions y generator expressions.

---

## List Comprehension

```python
# Básico
cuadrados = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Con condición (filtro)
pares = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Con transformación + filtro
pares_cuadrados = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# if-else en expresión (transformación condicional)
# Sintaxis: [expr_if_true if cond else expr_if_false for x in seq]
etiquetas = ["par" if x % 2 == 0 else "impar" for x in range(5)]
# ['par', 'impar', 'par', 'impar', 'par']
```

### Múltiples bucles (anidados)

```python
# Equivalente a:
# for i in range(3):
#     for j in range(2):
#         resultado.append((i, j))
pares = [(i, j) for i in range(3) for j in range(2)]
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# Aplanar matriz
matriz = [[1, 2], [3, 4], [5, 6]]
plana = [x for fila in matriz for x in fila]
# [1, 2, 3, 4, 5, 6]
```

### Llamadas a funciones

```python
def procesar(x):
    return x * 10

resultado = [procesar(x) for x in range(3)]
# [0, 10, 20]
```

---

## Dict Comprehension

```python
# Básico
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Desde dos listas
claves = ["a", "b", "c"]
valores = [1, 2, 3]
d = {k: v for k, v in zip(claves, valores)}
# {'a': 1, 'b': 2, 'c': 3}

# Filtrado
pares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Intercambiar claves/valores
original = {"a": 1, "b": 2}
invertido = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b'}
```

---

## Set Comprehension

```python
# Únicos
unicos = {x % 3 for x in range(10)}
# {0, 1, 2}

# Desde string (caracteres únicos)
vocales = {c for c in "aeiouaeiou"}
# {'a', 'e', 'i', 'o', 'u'}
```

---

## Generator Expressions (Generadores)

**Diferencia clave**: Crean un **iterador perezoso (lazy)**, no la colección completa.

```python
# List comprehension → LISTA completa en memoria
lista = [x**2 for x in range(5)]
print(type(lista))  # <class 'list'>

# Generator expression → GENERADOR (bajo memoria)
gen = (x**2 for x in range(5))
print(type(gen))    # <class 'generator'>
```

### Cómo consumir un generador

```python
gen = (x**2 for x in range(5))

# 1. for loop
for valor in gen:
    print(valor)  # 0, 1, 4, 9, 16

# 2. Convertir a lista
gen = (x**2 for x in range(5))
lista = list(gen)  # [0, 1, 4, 9, 16]

# 3. next() uno a uno
gen = (x**2 for x in range(3))
next(gen)  # 0
next(gen)  # 1
next(gen)  # 4
# next(gen)  # StopIteration
```

### ⚠️ Generador = un solo uso

```python
gen = (x for x in [1, 2, 3])
list(gen)  # [1, 2, 3]
list(gen)  # []  ← ¡Vacío! Ya se consumió
```

---

## Lazy vs Eager — Cuándo usar cada uno

| Aspecto | List Comp (Eager) | Generator (Lazy) |
|---------|-------------------|------------------|
| Memoria | O(n) — toda la lista | O(1) — un elemento a la vez |
| Velocidad inicial | Lenta (calcula todo) | Inmediata |
| Reutilizable | Sí | No (se agota) |
| `len()` | ✅ | ❌ |
| Indexado | `l[0]` | ❌ |

### Usa **List Comp** cuando:
- Necesitas la colección completa
- Vas a iterar múltiples veces
- Necesitas `len()` o indexado
- Colección pequeña/mediana

### Usa **Generator** cuando:
- Colección muy grande (millones de items)
- Solo necesitas iterar una vez
- Pipeline de streaming (archivos, red, DB)
- Memoria limitada

```python
# Ejemplo: suma de 1M números sin crear lista
suma = sum(x for x in range(1_000_000))
print(suma)  # 499999500000 (rápido, poca RAM)
```

---

## Equivalencias: Comprehension vs `map`/`filter`

```python
# map → list comp
list(map(lambda x: x*2, range(5)))
[x*2 for x in range(5)]

# filter → list comp con if
list(filter(lambda x: x%2==0, range(10)))
[x for x in range(10) if x%2==0]

# map + filter → list comp con if
list(map(lambda x: x*2, filter(lambda x: x%2==0, range(10))))
[x*2 for x in range(10) if x%2==0]
```

> 💡 **Preferir comprehensions**: más legibles, pythonic, y a menudo más rápidas.

---

## Walrus Operator `:=` (Python 3.8+) en comprehensions

Evita calcular dos veces:

```python
# Sin walrus (calcula f(x) dos veces)
[f(x) for x in datos if f(x) > 10]

# Con walrus (calcula una vez)
[y for x in datos if (y := f(x)) > 10]
```

---

## Resumen de sintaxis

| Tipo | Sintaxis | Resultado |
|------|----------|-----------|
| List | `[expr for x in seq]` | `list` |
| List + filtro | `[expr for x in seq if cond]` | `list` |
| List + if-else | `[a if c else b for x in seq]` | `list` |
| Dict | `{k: v for x in seq}` | `dict` |
| Set | `{expr for x in seq}` | `set` |
| Generator | `(expr for x in seq)` | `generator` |

---

## Buenas prácticas

1. **Una línea, legible**: Si no cabe en una línea → usa `for` normal
2. **No anides demasiado**: 2 niveles máx; más → función auxiliar
3. **Evita side effects**: No uses `print`, `append` a lista externa, I/O
4. **Nombra el generador** si lo reutilizas: `gen = (x for x in ...)`

```python
# ❌ Difícil de leer
[x*y for x in range(10) for y in range(5) if x*y > 10 and x%2==0]

# ✅ Mejor: función o bucle explícito
def generar():
    for x in range(10):
        for y in range(5):
            if x*y > 10 and x%2==0:
                yield x*y
```

---

## 🎯 Ejercicios

Practica comprehensions en [ejercicios.md](./ejercicios.md#05--comprehensions-y-generadores).

**Mini-ejercicio**: Con una línea: extraer emails de un texto. `[palabra for palabra in texto.split() if "@" in palabra]`

---

## Véase también

- [04-estructuras-datos](./04-estructuras-datos.md) — Estructuras base
- [12-programacion-funcional](../02-avanzado/12-programacion-funcional.md) — `map`, `filter`, `itertools`
- [11-funciones-avanzadas](../02-avanzado/11-funciones-avanzadas.md) — Generadores con `yield`
- [ejercicios.md](./ejercicios.md) — Práctica recomendada