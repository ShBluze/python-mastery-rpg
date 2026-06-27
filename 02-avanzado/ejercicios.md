# 📝 Ejercicios — 02 Avanzado

---

## 10 — Type hints

### Ejercicio 10.1 — Función tipada
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: type hints básicos, Optional
- **Criterio de éxito**: Función `buscar_usuario(id: int) -> Optional[dict]` correctamente tipada.

### Ejercicio 10.2 — Generic básico
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: TypeVar, Generic
- **Criterio de éxito**: Clase `Caja[T]` con métodos `guardar(item: T)` y `obtener() -> T`.

### Ejercicio 10.3 — Protocol personalizado
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: Protocol, runtime_checkable
- **Criterio de éxito**: Protocol `Imprimible` con método `imprimir()`. Dos clases que lo implementan sin heredar de él.

---

## 11 — Funciones avanzadas

### Ejercicio 11.1 — Closure contador
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: closures, nonlocal
- **Criterio de éxito**: Función `crear_contador()` que devuelve closure que incrementa y devuelve contador.

### Ejercicio 11.2 — Decorador timer
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: decoradores, functools.wraps, time
- **Criterio de éxito**: Decorador `@timer` que imprime tiempo de ejecución. Usa wraps para preservar metadata.

### Ejercicio 11.3 — Decorador con argumentos
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: decoradores anidados, *args, **kwargs
- **Criterio de éxito**: Decorador `@repetir(n=3)` que ejecuta la función n veces y devuelve el resultado de la última.

---

## 12 — Programación funcional

### Ejercicio 12.1 — Pipeline funcional
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: map, filter, lambda
- **Criterio de éxito**: Pipeline que filtra números pares, eleva al cuadrado y toma solo primeros 5. Todo en una expresión.

### Ejercicio 12.2 — Groupby
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: itertools.groupby, sorted
- **Criterio de éxito**: Agrupar palabras por su primera letra. Input: lista de palabras. Output: dict letra → [palabras].

### Ejercicio 12.3 — Reduce avanzado
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: functools.reduce, operator
- **Criterio de éxito**: Usar reduce para implementar `producto(MATRIZ)` que multiplica todos los elementos de una matriz 3×3.

---

## 13 — Async y concurrencia

### Ejercicio 13.1 — Sleep paralelo
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: async/await, asyncio.sleep
- **Criterio de éxito**: 3 corrutinas que duermen distintos segundos. La ejecución total debe ser ~el máximo, no la suma.

### Ejercicio 13.2 — Web scraper async
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: aiohttp, asyncio.gather
- **Criterio de éxito**: Descargar 10 URLs en paralelo. Mostrar tiempo total y por URL.

### Ejercicio 13.3 — Productor-consumidor
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: asyncio.Queue, TaskGroup (3.11+)
- **Criterio de éxito**: 2 productores y 3 consumidores con cola compartida. Los productores ponen items, los consumidores los procesan.

---

## 14 — Context managers

### Ejercicio 14.1 — CM con clase
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: __enter__, __exit__
- **Criterio de éxito**: Context manager `Temporizador` que mide tiempo de ejecución del bloque with.

### Ejercicio 14.2 — CM con @contextmanager
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: @contextmanager, yield
- **Criterio de éxito**: `@contextmanager` que cambia temporalmente el directorio de trabajo y vuelve al salir.

### Ejercicio 14.3 — ExitStack dinámico
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: ExitStack, contextlib
- **Criterio de éxito**: Gestor que abre N archivos dinámicamente (lista de rutas) y los cierra todos al salir del with.
