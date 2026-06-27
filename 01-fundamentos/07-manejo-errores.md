# 07 — Manejo de errores

> Excepciones, `try/except/else/finally`, jerarquía, ExceptionGroup (3.11+), excepciones personalizadas.

---

## Sintaxis básica

```python
try:
    # Código que puede fallar
    resultado = 10 / 0
except ZeroDivisionError:
    # Manejo específico
    print("No se puede dividir por cero")
    resultado = None
```

### Múltiples excepciones

```python
try:
    valor = int(input("Número: "))
    resultado = 10 / valor
except ValueError:
    print("Eso no es un número válido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except (KeyboardInterrupt, EOFError):
    print("\nCancelado por el usuario")
```

### Capturar la excepción (acceso al objeto)

```python
try:
    open("archivo_inexistente.txt")
except FileNotFoundError as e:
    print(f"Archivo no encontrado: {e}")
    print(f"Errno: {e.errno}")  # Atributos específicos
```

---

## `else` y `finally`

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("No existe")
    contenido = ""
else:
    # Solo si NO hubo excepción
    print(f"Leídos {len(contenido)} caracteres")
finally:
    # SIEMPRE se ejecuta (hubo error o no)
    archivo.close()
    print("Limpieza completada")
```

> 💡 **Patrón `try/else/finally`**: `else` = éxito, `finally` = limpieza (close, release, unlock).

---

## Jerarquía de excepciones (resumen)

```
BaseException
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── AttributeError
      ├── FileNotFoundError (→ OSError)
      ├── PermissionError (→ OSError)
      ├── ImportError
      └── RuntimeError
           └── RecursionError
```

> 🔑 **Regla**: Captura lo **más específico posible**. Evita `except:` o `except Exception:` salvo en top-level.

---

## `raise` — Lanzar excepciones

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor no puede ser cero")
    return a / b

# Re-lanzar (preserva traceback)
try:
    dividir(10, 0)
except ZeroDivisionError:
    print("Log local...")
    raise  # Propaga la misma excepción
```

### `raise ... from` — Encadenar causas (Python 3+)

```python
try:
    int("no es numero")
except ValueError as e:
    raise RuntimeError("Fallo en validación") from e
# Traceback muestra: "The above exception was the direct cause..."
```

---

## Excepciones personalizadas

```python
# Básica
class MiError(Exception):
    pass

# Con atributos extra
class ErrorValidacion(Exception):
    def __init__(self, campo, valor, mensaje="Valor inválido"):
        self.campo = campo
        self.valor = valor
        super().__init__(f"{mensaje}: {campo}={valor}")

# Uso
def validar_edad(edad):
    if edad < 0:
        raise ErrorValidacion("edad", edad, "Edad no puede ser negativa")
    if edad > 150:
        raise ErrorValidacion("edad", edad, "Edad poco realista")

try:
    validar_edad(-5)
except ErrorValidacion as e:
    print(e.campo)   # "edad"
    print(e.valor)   # -5
    print(e)         # "Edad no puede ser negativa: edad=-5"
```

---

## ExceptionGroup y `except*` (Python 3.11+)

Manejo de **múltiples excepciones simultáneas** (ej. `asyncio.TaskGroup`, `concurrent.futures`).

```python
# Simulación: varias tareas fallan
def tareas():
    raise ExceptionGroup("Fallos múltiples", [
        ValueError("dato inválido"),
        TypeError("tipo incorrecto"),
        KeyError("clave perdida"),
    ])

try:
    tareas()
except* ValueError as eg:
    print(f"ValueErrors: {len(eg.exceptions)}")
except* TypeError as eg:
    print(f"TypeErrors: {len(eg.exceptions)}")
except* KeyError as eg:
    print(f"KeyErrors: {len(eg.exceptions)}")
```

### `ExceptionGroup` métodos útiles

```python
try:
    ...
except ExceptionGroup as eg:
    eg.subgroup(ValueError)      # Solo ValueErrors (nuevo ExceptionGroup)
    eg.split(ValueError)         # (match, rest) → (ValueError group, resto)
    eg.derive("nuevo mensaje")   # Nuevo grupo con mismo contenido
```

---

## `contextlib` — Utilidades para excepciones

### `suppress` — Ignorar excepción específica

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("temp.txt")  # No falla si no existe
```

### `redirect_stdout` / `redirect_stderr`

```python
from contextlib import redirect_stdout
import io

buf = io.StringIO()
with redirect_stdout(buf):
    print("Esto va al buffer")
print(buf.getvalue())  # "Esto va al buffer\n"
```

### `closing` — Garantizar close()

```python
from contextlib import closing
import urllib.request

with closing(urllib.request.urlopen(url)) as response:
    data = response.read()
# response.close() automático
```

---

## Patrones comunes

### Validar y convertir (EAFP vs LBYL)

```python
# EAFP (Easier to Ask Forgiveness than Permission) — Pythonic
try:
    valor = int(dato)
except ValueError:
    valor = 0

# LBYL (Look Before You Leap) — A veces necesario
if isinstance(dato, str) and dato.isdigit():
    valor = int(dato)
else:
    valor = 0
```

### Reintento con backoff

```python
import time
from functools import wraps

def reintentar(max_intentos=3, espera=1, factor=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(max_intentos):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if intento == max_intentos - 1:
                        raise
                    time.sleep(espera * (factor ** intento))
            return None
        return wrapper
    return decorator

@reintentar(max_intentos=3, espera=0.5)
def conexion_inestable():
    ...
```

### Contexto en excepciones (logging)

```python
import logging

try:
    procesar(dato)
except Exception:
    logging.exception("Fallo procesando %s", dato)  # Incluye traceback
    raise
```

---

## Buenas prácticas

| ✅ Hacer | ❌ No hacer |
|----------|-------------|
| Capturar excepciones específicas | `except:` o `except Exception:` genérico |
| Usar `finally` para limpieza | Dejar recursos abiertos en `except` |
| `raise from` para encadenar causas | Perder el traceback original |
| Crear excepciones de dominio | Usar `Exception` genérica para todo |
| Loggear con `logging.exception` | `print(traceback.format_exc())` |
| Documentar qué excepciones lanza tu API | Sorprender al caller con errores no doc |

---

## Excepciones built-in frecuentes

| Excepción | Cuándo ocurre |
|-----------|---------------|
| `ValueError` | Argumento tipo correcto, valor inapropiado (`int("abc")`) |
| `TypeError` | Tipo incorrecto (`len(5)`, `"a" + 1`) |
| `IndexError` | Índice fuera de rango (`lista[10]`) |
| `KeyError` | Clave no existe en dict (`d["x"]`) |
| `AttributeError` | Atributo no existe (`obj.metodo_inexistente()`) |
| `FileNotFoundError` | Archivo no existe (`open("no.txt")`) |
| `PermissionError` | Sin permisos (`open("/root/")`) |
| `ZeroDivisionError` | División por cero (`1/0`) |
| `ImportError` / `ModuleNotFoundError` | Import falla |
| `RecursionError` | Recursión muy profunda |
| `StopIteration` | Iterador agotado (`next(gen)`) |

---

---
## 🎯 Ejercicios

Practica manejo de errores en [ejercicios.md](./ejercicios.md#07--manejo-de-errores).

**Mini-ejercicio**: Función `dividir_seguro(a, b)` que maneja TypeError, ZeroDivisionError y ValueError. Cada error muestra mensaje distinto.

---

## Véase también

- [08-modulos-imports](./08-modulos-imports.md) — `ImportError`, `ModuleNotFoundError`
- [13-async-concurrencia](../02-avanzado/13-async-concurrencia.md) — Excepciones en asyncio
- [25-testing](../04-ecosistema/25-testing.md) — `pytest.raises`, testing de errores
- [27-logging-debugging](../04-ecosistema/27-logging-debugging.md) — Logging de excepciones
- [ejercicios.md](./ejercicios.md) — Práctica recomendada