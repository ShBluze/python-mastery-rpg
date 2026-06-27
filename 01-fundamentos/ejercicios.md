# 📝 Ejercicios — 01 Fundamentos

> Cada ejercicio tiene dificultad, XP asignado y criterios de éxito. Resuélvelos en orden.

---

## 01 — Variables y tipos

### Ejercicio 1.1 — Calculadora de edad
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: Variables, input, int(), print()
- **Criterio de éxito**: El programa pide el año de nacimiento y muestra la edad calculada. Maneja años futuros con un mensaje de error.

### Ejercicio 1.2 — Conversor de unidades
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: Operadores, casting, f-strings
- **Criterio de éxito**: Convierte Celsius a Fahrenheit y viceversa. Muestra 3 decimales.

### Ejercicio 1.3 — Tipos implícitos
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: type(), operadores entre tipos
- **Criterio de éxito**: Dado `3 + 0.5`, `"4" + "2"`, `True + 2`, predice y comprueba el tipo y valor resultante.

---

## 02 — Control de flujo

### Ejercicio 2.1 — Número secreto
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: if/elif/else, while, random
- **Criterio de éxito**: El programa genera un número aleatorio y el usuario tiene 5 intentos para adivinarlo. Pista: "mayor" o "menor".

### Ejercicio 2.2 — Tabla de multiplicar
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: for, range(), print()
- **Criterio de éxito**: Pide un número y muestra su tabla de multiplicar del 1 al 10 con formato alineado.

### Ejercicio 2.3 — Calculadora con menú
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: match/case (3.10+), funciones básicas
- **Criterio de éxito**: Menú interactivo con opciones: sumar, restar, multiplicar, dividir, salir. Maneja división por cero.

---

## 03 — Funciones esenciales

### Ejercicio 3.1 — Función que cuenta
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: def, return, parámetros
- **Criterio de éxito**: Función `contar_palabras(texto)` que devuelve el número de palabras. Usa split().

### Ejercicio 3.2 — Args y kwargs
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: *args, **kwargs
- **Criterio de éxito**: Función `formatear_direccion(**datos)` que acepta calle, numero, ciudad, pais y devuelve string formateado solo con los datos dados.

### Ejercicio 3.3 — Lambda + sorted
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: lambda, sorted(), key
- **Criterio de éxito**: Ordenar lista de diccionarios `[{"nombre": "Ana", "edad": 25}, ...]` por edad usando sorted + lambda.

---

## 04 — Estructuras de datos

### Ejercicio 4.1 — Lista de tareas
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: list, append, remove
- **Criterio de éxito**: Programa CRUD de tareas: agregar, listar, completar (eliminar), salir. Datos en memoria.

### Ejercicio 4.2 — Frecuencia de palabras
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: dict, get(), loops
- **Criterio de éxito**: Función que recibe un texto y devuelve dict con frecuencia de palabras. Ignora mayúsculas y puntuación.

### Ejercicio 4.3 — Unión de conjuntos
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: set, unión, intersección, diferencia
- **Criterio de éxito**: Dados dos sets de usuarios (admin + editores), muestra: ambos grupos, solo admin, solo editores, total sin duplicados.

---

## 05 — Comprehensions y generadores

### Ejercicio 5.1 — Filtrar pares
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: list comprehension, if
- **Criterio de éxito**: Una línea: `[x for x in range(100) if ...]` para obtener pares y múltiplos de 3.

### Ejercicio 5.2 — Dict comprehension inverso
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: dict comprehension, swap clave/valor
- **Criterio de éxito**: Invertir un dict `{"a": 1, "b": 2}` → `{1: "a", 2: "b"}`. Maneja colisiones (valores duplicados).

### Ejercicio 5.3 — Generador infinito
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: generator, yield, itertools.islice
- **Criterio de éxito**: Generador `fibonacci()` infinito. Obtén los primeros 20 números con islice.

---

## 06 — Strings y formateo

### Ejercicio 6.1 — Validador de email
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: f-strings, string methods
- **Criterio de éxito**: Función que valida si un string tiene @ y . después del @. No usa regex.

### Ejercicio 6.2 — Formateo de factura
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: f-strings alineación, decimales
- **Criterio de éxito**: Dada lista de items (nombre, precio, cantidad), genera factura formateada con columnas alineadas y total.

### Ejercicio 6.3 — Pig Latin
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: slicing, string methods
- **Criterio de éxito**: Traductor básico: si empieza por vocal → +"way", consonante → mover primera letra al final +"ay".

---

## 07 — Manejo de errores

### Ejercicio 7.1 — Calculadora segura
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: try/except, ValueError, ZeroDivisionError
- **Criterio de éxito**: Calculadora que no crashea con entrada inválida o división por cero. Muestra mensajes claros.

### Ejercicio 7.2 — Excepción personalizada
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: class Exception, raise
- **Criterio de éxito**: Crear `SaldoInsuficienteError`. Clase `CuentaBancaria` que lo lanza al intentar retirar más del saldo.

### Ejercicio 7.3 — Retry con reintentos
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: try/except, loops, random
- **Criterio de éxito**: Función `ejecutar_con_reintento(fn, intentos=3)` que reintenta si falla. Solo propaga el error si se agotan los intentos.

---

## 08 — Módulos e imports

### Ejercicio 8.1 — Módulo de utilidades
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: import, from, módulo propio
- **Criterio de éxito**: Crea `utilidades.py` con 3 funciones. Impórtalas desde otro archivo y úsalas.

### Ejercicio 8.2 — if __name__
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: __name__, __main__
- **Criterio de éxito**: Script que tiene tests inline en `if __name__ == "__main__"`. Al importarlo, no se ejecutan los tests.

### Ejercicio 8.3 — Paquete con __init__.py
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: paquetes, __init__.py, __all__
- **Criterio de éxito**: Crea paquete `matematicas/` con módulos `aritmetica.py` y `geometria.py`. Usa `__all__` para controlar exports.

---

## 09 — Comentarios y docstrings

### Ejercicio 9.1 — Docstrings en funciones
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: """docstrings""", estilo Google
- **Criterio de éxito**: 5 funciones con docstring estilo Google (Args, Returns, Raises).

### Ejercicio 9.2 — Doctest
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: doctest
- **Criterio de éxito**: Función `sumar(a, b)` con doctest inline. Los tests pasan al ejecutar `python -m doctest`.

### Ejercicio 9.3 — Documentar una clase
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: docstrings en clases, __init__
- **Criterio de éxito**: Clase `Persona` completamente documentada con docstrings en clase, método y atributos.

---

> 💡 **Registro**: Después de cada ejercicio, actualiza `../gamification.md`, `../rpg-system.md` y `../tracking/log-ejercicios.md`.
