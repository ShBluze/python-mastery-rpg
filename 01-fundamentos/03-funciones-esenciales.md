# 03 — Funciones esenciales

> Definición, parámetros, retorno, lambdas básicas y desempaquetado.

---

## ¿Qué es una función?

Bloque de código reutilizable que:
- Recibe **parámetros** (entrada opcional)
- Ejecuta **lógica**
- Devuelve **resultado** (opcional, `None` por defecto)

```python
def nombre_funcion(param1, param2):
    # código
    return resultado
```

### `pass` — Placeholder

```python
def funcion_vacia():
    pass  # Implementaré después
```

---

## Tipos de funciones (esenciales)

### 1. Simples (sin parámetros, sin retorno)

```python
def saludar():
    print("¡Hola mundo!")

saludar()  # ¡Hola mundo!
```

### 2. Parámetros fijos (posicionales)

```python
def sumar(a, b):
    return a + b

print(sumar(3, 5))       # 8
print(sumar(b=5, a=3))   # 8 (keyword args, orden no importa)
```

### 3. Parámetros por defecto

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")           # Hola, Ana!
saludar("Ana", "Hey")    # Hey, Ana!
```

> ⚠️ **Regla**: Parámetros con valor por defecto van **al final**.

### 4. `*args` — Argumentos posicionales variables

```python
def sumar_todo(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sumar_todo(1, 2, 3))           # 6
print(sumar_todo(10, 20, 30, 40, 50))  # 150
```

- `args` es una **tupla** (inmutable)
- Útil cuando no sabes cuántos argumentos recibirás

### 5. `**kwargs` — Argumentos con nombre variables

```python
def saludar(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

saludar(nombre="Ana", edad=25, ciudad="Madrid")
# nombre: Ana
# edad: 25
# ciudad: Madrid
```

- `kwargs` es un **diccionario**
- Útil para configuraciones flexibles, wrappers, APIs

### 6. Combinación completa

```python
def ejemplo(obligatorio, opcional="defecto", *args, **kwargs):
    print(obligatorio, opcional, args, kwargs)

ejemplo(1, 2, 3, 4, a=5, b=6)
# 1 2 (3, 4) {'a': 5, 'b': 6}
```

**Orden obligatorio**: `posicionales` → `*args` → `keyword-only` → `**kwargs`

---

## Retorno (`return`)

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado * 2)  # 16
```

### Retorno múltiple (tupla implícita)

```python
def dividir(dividendo, divisor):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return cociente, resto

c, r = dividir(10, 3)
print(c, r)  # 3 1
```

### Sin retorno explícito → `None`

```python
def mostrar(msg):
    print(msg)

print(mostrar("Hola"))  # Hola \n None
```

---

## Lambdas básicas (funciones anónimas)

```python
# Sintaxis: lambda args: expresión
suma = lambda a, b: a + b
print(suma(3, 5))  # 8

doble = lambda x: x * 2
print(doble(4))    # 8
```

**Cuándo usar lambda:**
- Funciones triviales de una línea
- Argumentos a `map`, `filter`, `sorted`, `key=`
- Callbacks simples

**Cuándo NO usar:**
- Lógica compleja (usa `def`)
- Necesitas docstring, type hints, debugging
- Se reutiliza en varios lugares

---

## Desempaquetado en llamadas

```python
def sumar(a, b, c):
    return a + b + c

# Desde tupla/lista
valores = (1, 2, 3)
print(sumar(*valores))  # 6

# Desde diccionario
kwargs = {"a": 1, "b": 2, "c": 3}
print(sumar(**kwargs))  # 6
```

---

## Mutabilidad en parámetros (clave)

```python
# Inmutables (int, str, tuple) → no cambian el original
def modificar_numero(x):
    x = 10

n = 5
modificar_numero(n)
print(n)  # 5

# Mutables (list, dict, set) → SÍ cambian el original
def agregar(lista, item):
    lista.append(item)

nums = [1, 2, 3]
agregar(nums, 4)
print(nums)  # [1, 2, 3, 4]
```

> 🔑 **Regla de oro**: Si una función modifica un mutable, que sea evidente en el nombre (`agregar_`, `actualizar_`). Si no, devuelve una copia nueva.

---

## Resumen de sintaxis

```python
# Definición completa
def func(
    pos1, pos2,              # Posicionales obligatorios
    opt1="defecto",          # Con default
    *args,                   # Posicionales extra (tupla)
    kw1, kw2,                # Keyword-only (Python 3+)
    **kwargs                 # Keywords extra (dict)
) -> tipo_retorno:           # Type hint (opcional)
    """Docstring."""
    return resultado
```

---

---
## 🎯 Ejercicios

Practica funciones en [ejercicios.md](./ejercicios.md#03--funciones-esenciales).

**Mini-ejercicio**: Función `calc(operacion, *nums)` que suma, resta, multiplica o divide según el string. Usa `*args`.

---

## Véase también

- [02-control-flujo](./02-control-flujo.md) — Bucles dentro de funciones
- [05-comprehensions-generators](./05-comprehensions-generators.md) — Lambdas en `map`/`filter`
- [11-funciones-avanzadas](../02-avanzado/11-funciones-avanzadas.md) — Closures, decoradores, recursión, async
- [10-type-hints](../02-avanzado/10-type-hints.md) — Anotaciones de tipo en funciones
- [ejercicios.md](./ejercicios.md) — Práctica recomendada