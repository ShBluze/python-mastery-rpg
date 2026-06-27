# 01 — Variables, tipos y operadores

> Fundamentos de Python: variables, tipado dinámico, operadores y casting.

---

## Variables

Una **variable** es un nombre que apunta a un valor en memoria.

- No necesitas declarar el tipo (Python es **tipado dinámico**)
- Se asigna con el signo `=`

### Restricciones en nombres

- No pueden empezar ni contener caracteres especiales (excepto `_`)
- No pueden empezar por números
- No pueden ser palabras clave reservadas
- No pueden contener espacios

### Convenciones de命名 (naming)

| Estilo | Ejemplo | Uso típico |
|--------|---------|------------|
| **snake_case** | `nombre_mascota` | Variables, funciones (PEP 8) |
| **camelCase** | `nombreMascota` | JSON, JavaScript interop |
| **PascalCase** | `NombreMascota` | Clases, tipos |
| **kebab-case** | `nombre-mascota` | URLs, CLI flags, archivos |

> 💡 **PEP 8**: Usa `snake_case` para variables y funciones en Python.

### Palabras clave reservadas

No puedes usarlas como nombres de variables:
```
False  None  True  and  as  assert  break  class  continue  def  del
elif  else  except  finally  for  from  global  if  import  in  is
lambda  nonlocal  not  or  pass  raise  return  try  while  with  yield
```

```python
import keyword
print(keyword.kwlist)  # Lista completa
```

### Declaración múltiple

```python
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3
```

### Intercambio de valores (swap)

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

### Desempaquetado

```python
# Tupla
nombre, edad, ciudad = ("Ana", 30, "Madrid")

# Con operador estrella (*)
a, *b, c, d = 1, 2, 3, 4, 5, 6
# a=1, b=[2,3,4], c=5, d=6
```

---

## Tipos de datos básicos

| Tipo | Ejemplo | Descripción |
|------|---------|-------------|
| `int` | `10`, `-5` | Enteros (precisión arbitraria) |
| `float` | `3.14`, `-0.001` | Decimales (IEEE 754 double) |
| `str` | `"Hola"`, `'Python'` | Texto Unicode (inmutable) |
| `bool` | `True`, `False` | Lógicos (subclase de `int`) |
| `list` | `[1, 2]`, `['a','b']` | Ordenada, mutable |
| `tuple` | `(1, 2)`, `(3, 'x')` | Ordenada, inmutable |
| `dict` | `{'clave': 'valor'}` | Clave-valor, mutable |
| `set` | `{1, 2, 3}` | Sin duplicados, no ordenado |
| `complex` | `3+4j` | Números complejos |

> 🔑 **Clave**: `type(x)` te dice el tipo; `isinstance(x, tipo)` valida en runtime.

---

## Operadores

### Aritméticos

| Op | Significado | Ejemplo |
|----|-------------|---------|
| `+` | Suma | `5 + 3 → 8` |
| `-` | Resta | `5 - 3 → 2` |
| `*` | Multiplicación | `5 * 3 → 15` |
| `/` | División (float) | `5 / 2 → 2.5` |
| `//` | División entera | `5 // 2 → 2` |
| `%` | Módulo (resto) | `5 % 2 → 1` |
| `**` | Potencia | `5 ** 2 → 25` |

### Números complejos

```python
z = 3 + 4j
print(z)              # (3+4j)
print(type(z))        # <class 'complex'>

z1 = 3 + 4j
z2 = 1 + 2j
print(z1 + z2)        # (4+6j)
print(z1 * z2)        # (-5+10j)
print(z.conjugate())  # (3-4j)
print(abs(z))         # 5.0 (módulo)
import cmath
print(cmath.phase(z)) # 0.927... rad (argumento)
```

---

## Conversión de tipos (Casting)

### 1. Implícita (coerción) — automática

```python
a = 5      # int
b = 2.5    # float
c = a + b  # Python convierte int → float
print(c)   # 7.5
print(type(c))  # <class 'float'>
```

### 2. Explícita — forzada por el programador

```python
a = "123"
b = int(a)     # str → int
c = float(a)   # str → float
d = str(456)   # int → str

print(b + 1)   # 124
print(c + 1)   # 124.0
print(d)       # "456"
```

### Funciones de casting comunes

| Función | Convierte | Convierte a |
|---------|-------------|
| `int()` | Entero |
| `float()` | Decimal |
| `str()` | Cadena |
| `list()` | Lista |
| `tuple()` | Tupla |
| `set()` | Conjunto |
| `bool()` | Booleano |
| `complex()` | Complejo |

---

## Operadores de comparación y lógicos

### Comparación

| Op | Significado |
|----|-------------|
| `==` | Igualdad |
| `!=` | Desigualdad |
| `<`, `>`, `<=`, `>=` | Orden |
| `is` | Identidad (mismo objeto) |
| `is not` | Distinta identidad |

### Lógicos

| Op | Significado |
|----|-------------|
| `and` | Y lógico (cortocircuito) |
| `or` | O lógico (cortocircuito) |
| `not` | Negación |

### Pertenencia (`in` / `not in`)

```python
print(3 in [1, 2, 3, 4])     # True
print("a" in "Python")       # False
print("y" in "Python")       # True
print("pera" in ["manzana", "pera"])  # True
```

---

## Resumen rápido

```python
# Variables
x = 10
nombre = "Ana"
es_activo = True

# Tipos
type(x)           # <class 'int'>
isinstance(x, int)  # True

# Operadores
5 + 3, 5 - 3, 5 * 3, 5 / 2, 5 // 2, 5 % 2, 5 ** 2

# Casting
int("10"), float("3.14"), str(42), list((1,2)), tuple([1,2])

# Comparación
5 > 3, "a" == "b", x is not None, 3 in [1,2,3]
```

---

## 🎯 Ejercicios

Practica variables y tipos en [ejercicios.md](./ejercicios.md#01--variables-y-tipos).

**Mini-ejercicio**: Escribe un programa que pida nombre y edad, calcule el año de nacimiento y lo muestre. Usa f-strings.

---

## Véase también

- [02-control-flujo](./02-control-flujo.md) — `if`, `match`, `for`, `while`
- [03-funciones-esenciales](./03-funciones-esenciales.md) — `def`, parámetros, `return`
- [10-type-hints](../02-avanzado/10-type-hints.md) — Anotaciones de tipo estático
- [ejercicios.md](./ejercicios.md) — Práctica recomendada