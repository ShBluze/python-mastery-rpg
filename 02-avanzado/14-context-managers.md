# 14 — Context Managers

> `with`, `@contextmanager`, `ExitStack`, `suppress`, `redirect_stdout`, patrones avanzados.

---

## Protocolo `with`

Cualquier objeto con `__enter__` y `__exit__` funciona con `with`.

```python
class MiContexto:
    def __enter__(self):
        print("Entrada")
        return self  # Valor asignado a 'as x'
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Salida")
        # Retorna True para suprimir excepción
        return False

with MiContexto() as ctx:
    print("Dentro")
# Entrada
# Dentro
# Salida
```

### `__exit__` parámetros

| Parámetro | Significado |
|-----------|-------------|
| `exc_type` | Tipo de excepción (`None` si no hubo) |
| `exc_val` | Instancia de la excepción |
| `exc_tb` | Traceback |

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is not None:
        print(f"Excepción: {exc_type.__name__}: {exc_val}")
    return False  # Propaga la excepción
```

---

## `@contextmanager` (generador simple)

```python
from contextlib import contextmanager

@contextmanager
def mi_contexto():
    print("Setup")
    try:
        yield "valor"  # Valor para 'as x'
    finally:
        print("Cleanup")

with mi_contexto() as x:
    print(f"Dentro: {x}")
# Setup
# Dentro: valor
# Cleanup
```

### Con parámetros

```python
@contextmanager
def abrir_archivo(ruta, modo="r"):
    f = open(ruta, modo)
    try:
        yield f
    finally:
        f.close()

with abrir_archivo("datos.txt") as f:
    print(f.read())
```

### Manejo de excepciones en generador

```python
@contextmanager
def transaccion(db):
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise

with transaccion(db) as t:
    t.execute("INSERT ...")
# Commit si ok, rollback si excepción
```

---

## `contextlib` — Utilidades estándar

### `closing` — Garantizar `.close()`

```python
from contextlib import closing
import urllib.request

with closing(urllib.request.urlopen("http://example.com")) as resp:
    html = resp.read()
# resp.close() automático
```

### `suppress` — Ignorar excepción específica

```python
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("temp.txt")  # No falla si no existe

with suppress(KeyError):
    d.pop("clave_inexistente")
```

### `redirect_stdout` / `redirect_stderr`

```python
from contextlib import redirect_stdout
import io

buf = io.StringIO()
with redirect_stdout(buf):
    print("Esto va al buffer")
    print("Otra línea")

print(f"Capturado: {buf.getvalue()}")
# Capturado: Esto va al buffer\nOtra línea\n
```

### `nullcontext` — Context manager que no hace nada (3.7+)

```python
from contextlib import nullcontext

def procesar(archivo=None):
    ctx = open(archivo) if archivo else nullcontext(sys.stdin)
    with ctx as f:
        return f.read()
```

### `chdir` — Cambiar directorio temporal (3.11+)

```python
from contextlib import chdir

with chdir("/tmp"):
    # Código en /tmp
    pass
# Vuelve al directorio original
```

---

## `ExitStack` — Múltiples context managers dinámicos

```python
from contextlib import ExitStack

def procesar_archivos(rutas):
    with ExitStack() as stack:
        archivos = [stack.enter_context(open(r)) for r in rutas]
        # Si falla apertura, cierra los ya abiertos automáticamente
        for f in archivos:
            print(f.read())
```

### Callback de limpieza

```python
from contextlib import ExitStack

with ExitStack() as stack:
    stack.callback(print, "Limpieza 1")
    stack.callback(lambda: print("Limpieza 2"))
    # Se ejecutan en orden LIFO al salir
```

---

## Context managers asíncronos (Python 3.7+)

```python
class AsyncConexion:
    async def __aenter__(self):
        self.conn = await conectar_db()
        return self.conn
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()

async def main():
    async with AsyncConexion() as db:
        await db.query("SELECT 1")
```

### `@asynccontextmanager`

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def transaccion_async(db):
    try:
        yield db
        await db.commit()
    except Exception:
        await db.rollback()
        raise

async def main():
    async with transaccion_async(db) as t:
        await t.execute("INSERT ...")
```

---

## Patrones útiles

### Timer / Medición

```python
import time
from contextlib import contextmanager

@contextmanager
def medir(nombre="Bloque"):
    inicio = time.perf_counter()
    try:
        yield
    finally:
        print(f"{nombre}: {time.perf_counter() - inicio:.4f}s")

with medir("Procesamiento"):
    procesar_datos()
```

### Lock / Sincronización

```python
import threading
from contextlib import contextmanager

lock = threading.Lock()

@contextmanager
def seccion_critica():
    lock.acquire()
    try:
        yield
    finally:
        lock.release()

with seccion_critica():
    # Código thread-safe
    contador += 1
```

### Transacción BD genérica

```python
from contextlib import contextmanager

@contextmanager
def transaccion(session):
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

with transaccion(Session()) as s:
    s.add(usuario)
```

### Mocking temporal (testing)

```python
from contextlib import contextmanager
from unittest.mock import patch

@contextmanager
def mock_time(fecha_fija):
    with patch("time.time", return_value=fecha_fija.timestamp()):
        with patch("datetime.datetime") as mock_dt:
            mock_dt.now.return_value = fecha_fija
            mock_dt.side_effect = lambda *a, **kw: datetime.datetime(*a, **kw)
            yield

with mock_time(datetime(2024, 1, 1)):
    print(datetime.now())  # 2024-01-01 00:00:00
```

---

## `contextvars` + Context Managers

```python
import contextvars

request_id = contextvars.ContextVar("request_id")

@contextmanager
def request_context(rid):
    token = request_id.set(rid)
    try:
        yield
    finally:
        request_id.reset(token)

with request_context("req-123"):
    print(request_id.get())  # req-123
```

---

## Resumen: Cuándo usar qué

| Herramienta | Uso |
|-------------|-----|
| `with Clase()` | Recursos complejos, estado, reutilizable |
| `@contextmanager` | Limpieza simple, setup/teardown |
| `ExitStack` | Número variable de recursos, dinámico |
| `suppress` | Ignorar excepción esperada |
| `redirect_stdout` | Capturar salida |
| `closing` | Objetos con `.close()` sin `__enter__` |
| `@asynccontextmanager` | Recursos async (DB, HTTP, sockets) |

---

## 🎯 Ejercicios

Practica context managers en [ejercicios.md](./ejercicios.md#14--context-managers).

**Mini-ejercicio**: Context manager `ArchivoAbierto` que abre un archivo, asegura cierre incluso si hay error, y registra la operación.

---

## Véase también

- [07-manejo-errores](../01-fundamentos/07-manejo-errores.md) — `try/finally` vs context managers
- [08-modulos-imports](../01-fundamentos/08-modulos-imports.md) — `importlib.resources` (context manager)
- [13-async-concurrencia](./13-async-concurrencia.md) — `async with`
- [25-testing](../04-ecosistema/25-testing.md) — `pytest` fixtures como context managers
- [ejercicios.md](./ejercicios.md) — Práctica recomendada