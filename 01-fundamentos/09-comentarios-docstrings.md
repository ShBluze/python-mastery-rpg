# 09 — Comentarios y Docstrings

> Documentación en código: comentarios, docstrings, convenciones y herramientas.

---

## Comentarios (`#`)

### Una línea
```python
# Esto es un comentario
x = 1  # Comentario al final de línea
```

### Múltiples líneas
```python
# Esto es un comentario
# multilínea usando
# varias líneas con #
```

> 💡 No existe sintaxis nativa para comentarios multilínea. Usa `#` en cada línea o un string sin asignar (ver abajo).

---

## Docstrings (Documentation Strings)

**No son comentarios** — son strings que quedan en el objeto en runtime (`__doc__`).

### Dónde van

```python
# Módulo (primer string del archivo)
"""Módulo de utilidades para procesamiento de texto."""

# Función
def saludar(nombre: str) -> str:
    """Saluda a una persona.
    
    Args:
        nombre: Nombre de la persona.
    
    Returns:
        Mensaje de saludo.
    """
    return f"Hola, {nombre}!"

# Clase
class Usuario:
    """Representa un usuario del sistema."""
    
    def __init__(self, nombre: str):
        """Inicializa usuario.
        
        Args:
            nombre: Nombre completo.
        """
        self.nombre = nombre
    
    def saludar(self) -> str:
        """Devuelve saludo personalizado."""
        return f"Hola, {self.nombre}!"

# Método mágico
def __repr__(self) -> str:
    """Representación oficial para debugging."""
    return f"Usuario(nombre={self.nombre!r})"
```

### Acceso en runtime

```python
print(saludar.__doc__)
# Saluda a una persona.
# 
# Args:
#     nombre: Nombre de la persona.
# 
# Returns:
#     Mensaje de saludo.

help(saludar)  # Formato bonito en consola
```

---

## Estilos de docstrings

### Google Style (recomendado, legible)

```python
def conectar(host: str, puerto: int = 80, timeout: float = 5.0) -> bool:
    """Conecta a un servidor HTTP.
    
    Args:
        host: Dirección del servidor.
        puerto: Puerto de conexión (default 80).
        timeout: Tiempo máximo de espera en segundos.
    
    Returns:
        True si conexión exitosa.
    
    Raises:
        ConnectionError: Si no se puede conectar.
        ValueError: Si host está vacío.
    
    Example:
        >>> conectar("ejemplo.com")
        True
    """
    ...
```

### NumPy Style (más verbose, científico)

```python
def calcular_media(datos: list[float]) -> float:
    """
    Calcula la media aritmética de una lista de números.
    
    Parameters
    ----------
    datos : list[float]
        Lista de valores numéricos.
    
    Returns
    -------
    float
        Media aritmética.
    
    Raises
    ------
    ValueError
        Si la lista está vacía.
    
    See Also
    --------
    numpy.mean : Versión optimizada para arrays.
    """
    ...
```

### Sphinx / reStructuredText (clásico)

```python
def procesar(item):
    """
    Procesa un item.
    
    :param item: Item a procesar
    :type item: dict
    :returns: Resultado procesado
    :rtype: dict
    :raises KeyError: Si falta campo requerido
    """
    ...
```

> 💡 **Elige uno y sé consistente**. Google style es el más popular hoy.

---

## Type hints en docstrings (legacy, pre-Python 3.5)

```python
# Solo si NO puedes usar anotaciones nativas (Python < 3.5)
def suma(a, b):
    # type: (int, int) -> int
    return a + b

# Variables
x = 10  # type: int
```

---

## Comentarios de tipo (`# type:`)

```python
# Para variables sin anotación (Python 3.5+)
x = []          # type: list[int]
conn = conectar()  # type: Optional[Connection]
```

---

## Herramientas que usan docstrings

| Herramienta | Qué hace |
|-------------|----------|
| `help()` | Muestra docstring en consola |
| `pdoc` / `mkdocstrings` | Genera docs HTML |
| `sphinx` | Docs profesionales (ReadTheDocs) |
| `pydoc` | `python -m pydoc modulo` |
| IDE (VS Code, PyCharm) | Tooltips, autocomplete, go-to-definition |
| `doctest` | Tests en docstrings |
| `mypy` / `pyright` | Lee type hints en docstrings (legacy) |

---

## Doctests — Tests en docstrings

```python
def sumar(a: int, b: int) -> int:
    """Suma dos enteros.
    
    >>> sumar(2, 3)
    5
    >>> sumar(-1, 1)
    0
    """
    return a + b

# Ejecutar: python -m doctest archivo.py -v
```

---

## Convenciones de comentarios

### TODO / FIXME / NOTE / HACK

```python
# TODO: Implementar caché Redis
# FIXME: Race condition en alta concurrencia
# NOTE: Esta función asume datos ordenados
# HACK: Workaround para bug en lib v1.2
```

Muchos IDEs y herramientas (`flake8`, `ruff`, `todo-tree`) los indexan.

### Comentarios de tipo (inline)

```python
x = 1  # type: int
items = []  # type: list[str]
```

### Shebang y encoding (archivo principal)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Módulo principal."""
```

---

## Buenas prácticas

| ✅ Hacer | ❌ Evitar |
|----------|-----------|
| Docstring en **todo** módulo, clase, función pública | Docstrings vacíos o `"TODO"` |
| Describir **qué hace**, no **cómo** (código ya lo muestra) | Repetir nombre de función en docstring |
| Documentar args, returns, raises, side effects | Argumentos obvios (`self`, `cls`) |
| Mantener sincronizado con código | Docstring mentiroso (peor que ninguno) |
| Usar `"""Triple comillas"""` (incluso una línea) | `'''Simple quotes'''` para docstrings |
| Ejemplos ejecutables (doctest) | Ejemplos que no se testean |

```python
# ✅ Bueno
def parsear_fecha(fecha: str) -> datetime:
    """Convierte string ISO 8601 a datetime.
    
    Args:
        fecha: Formato 'YYYY-MM-DD' o 'YYYY-MM-DDTHH:MM:SS'.
    
    Returns:
        datetime naive (sin timezone).
    
    Raises:
        ValueError: Si formato inválido.
    """
    ...

# ❌ Malo
def parsear_fecha(fecha):
    """Parsea fecha."""
    ...
```

---

## Linting de docstrings

```bash
# ruff (rápido, incluye reglas de docstrings)
ruff check --select D .

# pydocstyle (específico docstrings)
pydocstyle .

# flake8-docstrings
flake8 --select=D .
```

---

---
## 🎯 Ejercicios

Practica documentación en [ejercicios.md](./ejercicios.md#09--comentarios-y-docstrings).

**Mini-ejercicio**: Escribe 3 funciones con docstring estilo Google (Args, Returns, Raises). Una de ellas debe tener doctest.

---

## Véase también

- [01-variables-tipos](./01-variables-tipos.md) — `keyword.kwlist`
- [03-funciones-esenciales](./03-funciones-esenciales.md) — `pass` como placeholder
- [08-modulos-imports](./08-modulos-imports.md) — Docstrings en `__init__.py`
- [26-tooling](../04-ecosistema/26-tooling.md) — `ruff`, `mypy`, `pydocstyle`
- [10-type-hints](../02-avanzado/10-type-hints.md) — Anotaciones vs docstrings
- [ejercicios.md](./ejercicios.md) — Práctica recomendada