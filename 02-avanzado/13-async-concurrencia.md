# 13 — Async y Concurrencia

> `asyncio`, `TaskGroup` (3.11+), `threading`, `multiprocessing`, `concurrent.futures`.

---

## Async/Await básico

```python
import asyncio

async def tarea(nombre: str, duracion: float):
    print(f"{nombre}: inicio")
    await asyncio.sleep(duracion)
    print(f"{nombre}: fin")
    return nombre

async def main():
    # Secuencial
    await tarea("A", 1)
    await tarea("B", 1)
    
    # Concurrente con gather
    resultados = await asyncio.gather(
        tarea("A", 1),
        tarea("B", 1),
        tarea("C", 1)
    )
    print(resultados)  # ['A', 'B', 'C']

asyncio.run(main())
```

---

## `asyncio.TaskGroup` (Python 3.11+)

Manejo estructurado de múltiples tareas con cancelación automática.

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(tarea("A", 1))
        t2 = tg.create_task(tarea("B", 2))
        t3 = tg.create_task(tarea("C", 0.5))
    
    # Si alguna falla, las demás se cancelan automáticamente
    print(t1.result(), t2.result(), t3.result())

asyncio.run(main())
```

---

## Patrones comunes

### Timeout

```python
async def main():
    try:
        await asyncio.wait_for(tarea_lenta(), timeout=2.0)
    except asyncio.TimeoutError:
        print("Tardó demasiado")

asyncio.run(main())
```

### Semáforo (limitar concurrencia)

```python
async def worker(sem, nombre):
    async with sem:
        await tarea(nombre, 1)

async def main():
    sem = asyncio.Semaphore(2)  # Máx 2 concurrentes
    await asyncio.gather(*(worker(sem, f"T{i}") for i in range(5)))
```

### Productor-Consumidor (Queue)

```python
async def productor(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(0.1)
    await queue.put(None)  # Señal fin

async def consumidor(queue):
    while True:
        item = await queue.get()
        if item is None: break
        print(f"Procesado: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(productor(queue), consumidor(queue))
    await queue.join()
```

---

## `threading` — Hilos (I/O bound, GIL)

```python
import threading
import time

def trabajador(nombre, duracion):
    print(f"{nombre}: inicio")
    time.sleep(duracion)
    print(f"{nombre}: fin")

# Crear hilos
t1 = threading.Thread(target=trabajador, args=("Hilo-1", 1))
t2 = threading.Thread(target=trabajador, args=("Hilo-2", 1))

t1.start()
t2.start()
t1.join()
t2.join()
print("Todos terminaron")
```

### `ThreadPoolExecutor` (alto nivel)

```python
from concurrent.futures import ThreadPoolExecutor

def descargar(url):
    return f"Contenido de {url}"

urls = [f"http://site{i}.com" for i in range(10)]

with ThreadPoolExecutor(max_workers=4) as executor:
    resultados = list(executor.map(descargar, urls))
```

---

## `multiprocessing` — Procesos (CPU bound, sin GIL)

```python
import multiprocessing

def cpu_intensivo(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        resultados = pool.map(cpu_intensivo, [100000] * 4)
    print(resultados)
```

### `ProcessPoolExecutor`

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=4) as executor:
    futuros = [executor.submit(cpu_intensivo, 100000) for _ in range(4)]
    for f in futuros:
        print(f.result())
```

---

## `concurrent.futures` — Interfaz unificada

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# as_completed: procesar en orden de finalización
with ThreadPoolExecutor(4) as executor:
    futuros = {executor.submit(tarea, i): i for i in range(10)}
    for f in as_completed(futuros):
        print(f"Tarea {futuros[f]}: {f.result()}")
```

---

## Diferencias clave

| Aspecto | `asyncio` | `threading` | `multiprocessing` |
|---------|-----------|-------------|-------------------|
| **Modelo** | Event loop (single thread) | Hilos OS | Procesos OS |
| **GIL** | No aplica (1 thread) | Bloquea CPU | Sin GIL |
| **Memoria** | Compartida | Compartida | Separada |
| **I/O bound** | ✅ Ideal | ✅ Bueno | ❌ Overhead |
| **CPU bound** | ❌ No | ❌ GIL | ✅ Ideal |
| **Escalabilidad** | 10k+ tasks | ~100 threads | ~CPU cores |

---

## `asyncio` + `threading` / `multiprocessing`

```python
# Ejecutar función bloqueante en thread pool
async def main():
    loop = asyncio.get_running_loop()
    resultado = await loop.run_in_executor(
        None,  # ThreadPoolExecutor por defecto
        funcion_bloqueante, 
        arg1, arg2
    )

# En process pool
async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        resultado = await loop.run_in_executor(pool, cpu_intensivo, 100000)
```

---

## Variables de contexto (`contextvars`)

```python
import contextvars

request_id = contextvars.ContextVar("request_id")

async def manejar_request(req_id):
    request_id.set(req_id)
    await procesar()

async def procesar():
    print(f"Request: {request_id.get()}")  # Acceso al contexto

asyncio.run(manejar_request("req-123"))
```

---

## Buenas prácticas

1. **`asyncio` por defecto** para I/O (HTTP, DB, archivos, websockets)
2. **`ThreadPoolExecutor`** para librerías síncronas blocking
3. **`ProcessPoolExecutor`** para CPU intenso (ML, procesamiento imagen, crypto)
4. **`TaskGroup` (3.11+)** para gestión estructurada
5. **Evita mezclar** `asyncio` + `threading` sin `run_in_executor`
6. **Cancela correctamente**: `task.cancel()`, `asyncio.wait_for()`

---

## 🎯 Ejercicios

Practica async en [ejercicios.md](./ejercicios.md#13--async-y-concurrencia).

**Mini-ejercicio**: 3 corrutinas que hacen request HTTP simulados (asyncio.sleep). Ejecuta con gather. Compara tiempo total vs secuencial.

---

## Véase también

- [11-funciones-avanzadas](./11-funciones-avanzadas.md) — Funciones async básicas
- [14-context-managers](./14-context-managers.md) — `async with`, `@asynccontextmanager`
- [25-testing](../04-ecosistema/25-testing.md) — `pytest-asyncio`
- [27-logging-debugging](../04-ecosistema/27-logging-debugging.md) — Logging en async
- [ejercicios.md](./ejercicios.md) — Práctica recomendada