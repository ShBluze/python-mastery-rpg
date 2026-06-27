# 11 — Funciones avanzadas

> Closures, decoradores, callbacks, funciones de orden superior, recursión, async.

---

## Closures

Un **closure** es una función que recuerda variables de su scope externo aunque ese scope ya terminó.

```python
def multiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar

por_tres = multiplicador(3)
por_diez = multiplicador(10)
print(por_tres(5))   # 15
print(por_diez(5))   # 50
```

### Closure con estado (`nonlocal`)

```python
def crear_contador():
    valor = 0
    def incrementar():
        nonlocal valor  # Obligatorio para modificar
        valor += 1
        return valor
    return incrementar

c = crear_contador()
print(c())  # 1
print(c())  # 2
```

### Detección técnica

```python
def externa(x):
    def interna(y):
        return x + y
    return interna

fn = externa(5)
print(fn.__closure__)                    # (<cell at 0x...>,)
print(fn.__closure__[0].cell_contents)   # 5
```

### Casos de uso reales

- **Decoradores** (ver abajo)
- **Cache / Memoización**
- **Configuración de funciones** (`con_impuesto(tasa)`)
- **Validadores parametrizados**
- **Middleware / Callbacks con estado**

---

## Decoradores

Un **decorador** recibe una función, la envuelve y devuelve una nueva función.

### Sintaxis básica

```python
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Después")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Ana")
# Antes
# Hola Ana
# Después
```

### Decorador con parámetros

```python
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("Hola")

saludar()  # Hola x3
```

### `functools.wraps` — Preservar metadata

```python
from functools import wraps

def mi_decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@mi_decorador
def saludar():
    """Docstring original"""
    pass

print(saludar.__name__)   # "saludar" (no "wrapper")
print(saludar.__doc__)    # "Docstring original"
```

### Decoradores útiles de `functools`

| Decorador | Uso |
|-----------|-----|
| `@lru_cache(maxsize=128)` | Memoización automática |
| `@cached_property` | Property cacheada (3.8+) |
| `@singledispatch` | Dispatch por tipo del 1er arg |
| `@total_ordering` | Genera `__lt__`, `__le__`, etc. desde `__eq__` + uno |

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Instantáneo gracias a cache
```

---

## Funciones de orden superior (HOF)

Reciben y/o devuelven funciones.

```python
def aplicar_tres_veces(func, valor):
    return func(func(func(valor)))

resultado = aplicar_tres_veces(lambda x: x * 2, 1)
print(resultado)  # 8

# Factory de funciones
def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar

por_5 = crear_multiplicador(5)
print(por_5(3))  # 15
```

---

## Callbacks

Función pasada como argumento para ejecutar en momento específico.

```python
def procesar_usuarios(usuarios, callback):
    for u in usuarios:
        print(callback(u))

def formatear(u):
    return f"{u['nombre']} ({u['edad']})"

usuarios = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 30}]
procesar_usuarios(usuarios, formatear)
```

### Patrones callback

| Patrón | Descripción |
|--------|-------------|
| **Síncrono** | `func(callback)` — ejecuta callback antes de retornar |
| **Eventos** | `on_click(callback)` — registra para futuro |
| **Async** | `await func(async_callback)` — ver sección async |

---

## Recursión

Función que se llama a sí misma.

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Recursión con memoización

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

### Tail recursion (Python no optimiza)

```python
# Python NO hace tail-call optimization
# Usa bucles o trampolines para recursión profunda
def factorial_iter(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado
```

---

## Funciones async (básico)

```python
import asyncio

async def saludar():
    await asyncio.sleep(1)
    return "Hola"

# Ejecutar
asyncio.run(saludar())
```

> Ver [13-async-concurrencia](./13-async-concurrencia.md) para profundidad.

---

## Resumen: Cuándo usar qué

| Técnica | Para qué |
|---------|----------|
| **Closure** | Estado encapsulado sin clases, factories |
| **Decorador** | Comportamiento transversal (log, timing, auth, retry) |
| **HOF** | Abstracción de patrones de control |
| **Callback** | Inversión de control, eventos |
| **Recursión** | Problemas dividir-vencer, estructuras recursivas |
| **Async** | I/O concurrente (red, DB, archivos) |

---

## 🎯 Ejercicios

Practica funciones avanzadas en [ejercicios.md](./ejercicios.md#11--funciones-avanzadas).

**Mini-ejercicio**: Decorador `@slow(delay=1)` que espera N segundos antes de ejecutar la función. Usa `functools.wraps`.

---

## Véase también

- [10-type-hints](./10-type-hints.md) — `Callable`, `TypeVar` en decoradores
- [12-programacion-funcional](./12-programacion-funcional.md) — `map`, `filter`, `reduce`
- [13-async-concurrencia](./13-async-concurrencia.md) — Async/await, TaskGroup
- [14-context-managers](./14-context-managers.md) — `@contextmanager` (decorador para context managers)
- [22-patrones-diseno](../03-poo/22-patrones-diseno.md) — Decorator pattern
- [ejercicios.md](./ejercicios.md) — Práctica recomendada