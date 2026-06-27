# 02 — Control de flujo

> Condicionales (`if`, `match`), bucles (`for`, `while`) y control de iteración.

---

## Condicionales

### `if` / `elif` / `else`

```python
edad = 18

if edad >= 18:
    print("Mayor de edad")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")
```

- La indentación define los bloques (4 espacios, PEP 8)
- `elif` = `else if` (evita anidamiento)
- Condición vacía → `pass` (placeholder)

### `match` / `case` (Python 3.10+)

Patrón similar a `switch` pero más potente.

```python
comando = "salir"

match comando:
    case "entrar":
        print("Bienvenido")
    case "salir":
        print("Hasta luego")
    case _:
        print("Comando desconocido")
```

**Patrones avanzados:**

```python
# Guardias (condiciones)
match valor:
    case x if x > 0:
        print("Positivo")
    case x if x < 0:
        print("Negativo")
    case 0:
        print("Cero")

# Estructuras
match punto:
    case (0, 0):
        print("Origen")
    case (x, 0):
        print(f"Eje X: {x}")
    case (0, y):
        print(f"Eje Y: {y}")
    case (x, y):
        print(f"Punto ({x}, {y})")

# Clases (Python 3.10+)
match usuario:
    case {"rol": "admin", "nombre": n}:
        print(f"Admin: {n}")
    case {"rol": "user", "nombre": n}:
        print(f"Usuario: {n}")
    case _:
        print("Rol desconocido")
```

> 💡 Usa `match` cuando tengas múltiples casos discretos o patrones estructurales.

---

## Bucles

### `for` — Iteración sobre secuencias

```python
# Rango
for i in range(5):
    print(i)        # 0, 1, 2, 3, 4

for i in range(2, 10, 2):
    print(i)        # 2, 4, 6, 8

# Lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# String
for letra in "Python":
    print(letra)

# Diccionario
for clave, valor in {"a": 1, "b": 2}.items():
    print(clave, valor)

# enumerate() — índice + valor
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# zip() — iterar múltiples
nombres = ["Ana", "Luis"]
edades = [25, 30]
for n, e in zip(nombres, edades):
    print(f"{n} → {e}")
```

### `while` — Condición booleana

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Patrón común: input hasta condición
respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe 'salir' para terminar: ")
```

> ⚠️ **Cuidado**: Si la condición nunca se vuelve falsa → **bucle infinito**.
> Actualiza la variable de control dentro del bucle.

---

## Control de bucles

### `break` — Salida inmediata

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4
```

### `continue` — Saltar iteración actual

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0 1 3 4
```

### `else` en bucles

Se ejecuta **solo si el bucle termina sin `break`**.

```python
for i in range(5):
    if i == 3:
        break
else:
    print("No se encontró")  # No se imprime (hubo break)

for i in range(5):
    if i == 10:
        break
else:
    print("No se encontró")  # Se imprime (no hubo break)
```

---

## Bucles anidados

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Salida:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
```

---

## Resumen rápido

| Bucle | Cuándo usar | Sintaxis clave |
|-------|-------------|----------------|
| `for` | Secuencias conocidas (lista, range, dict) | `for x in seq:` |
| `while` | Condición dinámica, número desconocido de iteraciones | `while cond:` |
| `break` | Salir totalmente | dentro del bucle |
| `continue` | Saltar a siguiente vuelta | dentro del bucle |
| `else` | Acción si no hubo `break` | `for/while ... else:` |

---

## Patrones útiles

```python
# Iterar con índice
for i, item in enumerate(lista):
    ...

# Iterar claves y valores
for k, v in diccionario.items():
    ...

# Iterar múltiples listas
for a, b in zip(lista1, lista2):
    ...

# range() flexible
range(5)           # 0..4
range(2, 10)       # 2..9
range(0, 10, 2)    # 0,2,4,6,8
range(10, 0, -1)   # 10..1

# Comprehension vs bucle
# Bucle
cuadrados = []
for x in range(5):
    cuadrados.append(x**2)

# Comprehension (ver 05-comprehensions-generators.md)
cuadrados = [x**2 for x in range(5)]
```

---

## 🎯 Ejercicios

Practica control de flujo en [ejercicios.md](./ejercicios.md#02--control-de-flujo).

**Mini-ejercicio**: Programa que pida números hasta que ingrese "salir" y muestre suma, promedio, máximo y mínimo.

---

## Véase también

- [01-variables-tipos](./01-variables-tipos.md) — Operadores de comparación
- [03-funciones-esenciales](./03-funciones-esenciales.md) — Funciones con bucles
- [05-comprehensions-generators](./05-comprehensions-generators.md) — Sintaxis compacta
- [ejercicios.md](./ejercicios.md) — Práctica recomendada