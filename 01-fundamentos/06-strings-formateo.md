# 06 — Strings y Formateo

> f-strings, format(), slicing, escapes, I/O básico y métodos de string.

---

## f-strings (Python 3.6+) — Recomendadas

```python
nombre = "Carlos"
edad = 25

# Básico
print(f"Me llamo {nombre} y tengo {edad} años")
# Me llamo Carlos y tengo 25 años

# Expresiones dentro de {}
a, b = 10, 5
print(f"Suma: {a + b}, Producto: {a * b}")

# Llamadas a métodos
print(f"Mayúsculas: {nombre.upper()}")
# Mayúsculas: CARLOS

# Formato numérico
pi = 3.14159265
print(f"Pi: {pi:.2f}")      # 3.14
print(f"Pi: {pi:.4f}")      # 3.1416
print(f"Porcentaje: {0.25:.0%}")  # 25%

# Bases numéricas
n = 255
print(f"Hex: {n:#x}")   # 0xff
print(f"Bin: {n:b}")    # 11111111
print(f"Oct: {n:#o}")   # 0o377

# Alineación y relleno
texto = "Python"
print(f"'{texto:>10}'")   # '    Python' (derecha)
print(f"'{texto:<10}'")   # 'Python    ' (izquierda)
print(f"'{texto:^10}'")   # '  Python  ' (centro)
print(f"'{texto:*^10}'")  # '**Python**' (relleno *)
```

> 💡 **f-strings son más rápidas y legibles** que `.format()` y `%`.

---

## `.format()` (Legacy, aún útil)

```python
# Posicional
"Me llamo {} y tengo {} años".format("Ana", 30)
# Me llamo Ana y tengo 30 años

# Por índice
"{1} y {0}".format("primero", "segundo")
# segundo y primero

# Por nombre
"Nombre: {nombre}, Edad: {edad}".format(nombre="Luis", edad=28)
# Nombre: Luis, Edad: 28

# Desempaquetar lista/dict
datos = ["Ana", 30, "Madrid"]
"Nombre: {}, Edad: {}, Ciudad: {}".format(*datos)

persona = {"nombre": "Luis", "edad": 28}
"Nombre: {nombre}, Edad: {edad}".format(**persona)
```

---

## `%` formatting (Muy legacy)

```python
# Solo para compatibilidad con código antiguo
"Nombre: %s, Edad: %d" % ("Ana", 25)
# Nombre: Ana, Edad: 25
```

---

## `str()` — Conversión a string

```python
numero = 123
texto = str(numero)
print(texto)       # "123"
print(type(texto)) # <class 'str'>

# Útil en concatenación (aunque f-string es mejor)
edad = 25
print("Tienes " + str(edad) + " años")
```

---

## Slicing (Substrings)

```python
texto = "Python"
#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

texto[0:3]   # "Pyt" (inicio incluido, fin excluido)
texto[1:4]   # "yth"
texto[:3]    # "Pyt" (desde inicio)
texto[3:]    # "hon" (hasta final)
texto[:]     # "Python" (copia)
texto[::2]   # "Pto" (cada 2)
texto[::-1]  # "nohtyP" (invertido)
```

---

## Caracteres de escape

| Escape | Significado | Ejemplo |
|--------|-------------|---------|
| `\n` | Salto de línea | `"Línea1\nLínea2"` |
| `\t` | Tabulación | `"Col1\tCol2"` |
| `\\` | Backslash literal | `"C:\\Users"` |
| `\'` | Comilla simple | `'It\'s ok'` |
| `\"` | Comilla doble | `"Dijo \"Hola\""` |
| `\r` | Retorno de carro | Windows line ending |

```python
print("Hola\nMundo")
# Hola
# Mundo

print("Nombre:\tAna")
print("Edad:\t25")
# Nombre:  Ana
# Edad:    25
```

---

## Multilínea con triple comillas

```python
# Automáticamente incluye \n
texto = """Línea 1
Línea 2
Línea 3"""
print(texto)

poema = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you.
"""
```

---

## I/O Básico — `input()` y `print()`

### `print()`
```python
print("Hola", "Mundo")           # Hola Mundo (sep=' ')
print("Hola", "Mundo", sep="|")  # Hola|Mundo
print("Hola", end=" ")           # Sin salto de línea
print("Mundo")                    # Hola Mundo

# Archivo (redirect)
with open("log.txt", "w") as f:
    print("Log guardado", file=f)
```

### `input()`
```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")

# Conversión inmediata
edad = int(input("Edad: "))
precio = float(input("Precio: "))

# Múltiples valores
a, b = input("Dos números: ").split()
a, b = int(a), int(b)
```

---

## Métodos de string esenciales

### Búsqueda y verificación
```python
s = "Hola Mundo"

s.find("Mundo")      # 5 (índice, -1 si no)
s.index("Mundo")     # 5 (ValueError si no)
"Mundo" in s         # True
s.startswith("Ho")   # True
s.endswith("do")     # True
s.count("o")         # 2
```

### Modificación y limpieza
```python
s = "  Hola Mundo  "

s.strip()        # "Hola Mundo"
s.lstrip()       # "Hola Mundo  "
s.rstrip()       # "  Hola Mundo"

s.lower()        # "  hola mundo  "
s.upper()        # "  HOLA MUNDO  "
s.title()        # "  Hola Mundo  "
s.capitalize()   # "  hola mundo  "
s.swapcase()     # "  hOLA mUNDO  "

s.replace("Hola", "Adiós")  # "  Adiós Mundo  "
s.replace("o", "0", 1)      # "  Hell0 Mundo  " (max 1)
```

### División y unión
```python
"manzana,pera,uva".split(",")     # ['manzana', 'pera', 'uva']
"  a  b  c  ".split()             # ['a', 'b', 'c'] (whitespace)
"-".join(["a", "b", "c"])         # "a-b-c"
"\n".join(["línea1", "línea2"])   # "línea1\nlínea2"
```

### Alineación y formato
```python
"Python".center(20)   # "       Python       "
"Python".ljust(20)    # "Python              "
"Python".rjust(20)    # "              Python"
"Python".zfill(8)     # "00Python" (padding con ceros)
```

### Verificación de contenido
```python
"123".isdigit()       # True
"abc".isalpha()       # True
"abc123".isalnum()    # True
"  ".isspace()        # True
"Hola".istitle()      # True
```

### Codificación
```python
"ñ".encode("utf-8")   # b'\xc3\xb1'
b'\xc3\xb1'.decode("utf-8")  # "ñ"
len("ñ")              # 1 (carácter, no byte)
```

---

## Tabla resumen: Métodos más usados

| Categoría | Métodos |
|-----------|---------|
| **Búsqueda** | `find`, `index`, `count`, `startswith`, `endswith`, `in` |
| **Caso** | `lower`, `upper`, `title`, `capitalize`, `swapcase` |
| **Limpieza** | `strip`, `lstrip`, `rstrip`, `replace`, `removeprefix` (3.9+), `removesuffix` (3.9+) |
| **Split/Join** | `split`, `rsplit`, `splitlines`, `join`, `partition`, `rpartition` |
| **Formato** | `center`, `ljust`, `rjust`, `zfill`, `format` |
| **Check** | `isalpha`, `isdigit`, `isalnum`, `isspace`, `istitle`, `islower`, `isupper` |
| **Encoding** | `encode`, `decode` |

---

## Buenas prácticas

1. **f-strings por defecto** — más rápidas, legibles, potentes
2. **`strip()` inputs** — `input().strip()` evita espacios accidentales
3. **`split()` sin args** — divide por cualquier whitespace, ignora vacíos
4. **`join` en bucles** — mejor que `+=` para concatenar muchos strings
5. **`str.isdigit()` vs `int()`** — valida antes de convertir

```python
# ✅ Bueno
partes = []
for item in items:
    partes.append(procesar(item))
resultado = "".join(partes)

# ❌ Malo (O(n²) por strings inmutables)
resultado = ""
for item in items:
    resultado += procesar(item)
```

---

---
## 🎯 Ejercicios

Practica strings en [ejercicios.md](./ejercicios.md#06--strings-y-formateo).

**Mini-ejercicio**: Función `enmascarar_email(email)` que muestra "a***@***.com". Usa slicing y f-strings.

---

## Véase también

- [01-variables-tipos](./01-variables-tipos.md) — Tipo `str` básico
- [03-funciones-esenciales](./03-funciones-esenciales.md) — `str()` en casting
- [04-estructuras-datos](./04-estructuras-datos.md) — Strings como secuencias
- [10-type-hints](../02-avanzado/10-type-hints.md) — `str` en anotaciones
- [ejercicios.md](./ejercicios.md) — Práctica recomendada