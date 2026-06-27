# 27 — Logging & Debugging

> `logging`, `pdb`, `breakpoint()`, `devtools`, depuración efectiva.

---

## `logging` — Registro Estructurado

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

log.debug("Solo en desarrollo")
log.info("Proceso iniciado")
log.warning("Recurso cercano al límite")
log.error("Falló la operación: %s", err)
log.critical("Sistema inestable")
```

### Niveles de logging

| Nivel    | Valor | Cuándo usarlo                        |
|----------|-------|--------------------------------------|
| `DEBUG`  | 10    | Diagnóstico detallado, desarrollo    |
| `INFO`   | 20    | Confirmación de flujo normal         |
| `WARNING`| 30    | Algo inesperado pero no crítico      |
| `ERROR`  | 40    | Falló una operación                  |
| `CRITICAL`| 50   | El programa no puede continuar       |

> ⚠️ No uses `print()` para logging. Usa `logging` — es configurable, filtrable y produccion-safe.

### Configuración con archivo

```ini
# logging.conf
[loggers]
keys = root,mi_app

[handlers]
keys = console,file

[formatters]
keys = simple,detailed

[logger_root]
level = WARNING
handlers = console

[logger_mi_app]
level = DEBUG
handlers = console,file
qualname = mi_app

[handler_console]
class = StreamHandler
level = DEBUG
formatter = simple
args = (sys.stdout,)

[handler_file]
class = handlers.RotatingFileHandler
level = INFO
formatter = detailed
args = ("app.log", maxBytes=10485760, backupCount=5)

[formatter_simple]
format = %(levelname)s | %(message)s

[formatter_detailed]
format = %(asctime)s | %(levelname)-8s | %(name)s | %(message)s
```

```python
import logging.config
logging.config.fileConfig("logging.conf")
```

### Buenas prácticas

```python
# ✅ Usar getLogger con __name__
log = logging.getLogger(__name__)

# ✅ Loggear excepciones con exc_info
try:
    peligro()
except Exception:
    log.exception("Algo salió mal")  # Incluye traceback

# ✅ Estructurar datos en logs
log.info("Usuario %s realizó %s", user_id, accion)

# ❌ No formatear manualmente
log.info(f"Usuario {user_id}")  # Evitar f-strings en logging
```

---

## `breakpoint()` — Depuración Interactiva (Python 3.7+)

```python
def procesar(datos):
    resultado = []
    for item in datos:
        breakpoint()  # Pausa aquí
        resultado.append(transformar(item))
    return resultado
```

### Comandos útiles en `pdb`

| Comando | Abrev. | Qué hace                         |
|---------|--------|----------------------------------|
| `next`  | `n`    | Ejecuta línea actual (no entra)  |
| `step`  | `s`    | Entra en la función llamada      |
| `continue` | `c` | Continúa hasta próximo breakpoint |
| `list`  | `l`    | Muestra código alrededor         |
| `print` | `p`    | Evalúa expresión                 |
| `pp`    |        | Pretty-print                     |
| `quit`  | `q`    | Sale del debugger                |

### Variables de entorno

```bash
# Deshabilitar breakpoints en producción
PYTHONBREAKPOINT=0 python app.py

# Usar debugger alternativo (pdbpp, ipdb)
PYTHONBREAKPOINT=ipdb.set_trace python app.py
```

---

## `pdb` — Debugger Clásico

```bash
python -m pdb script.py
```

### Post-mortem (inspeccionar error)

```python
import pdb

try:
    1 / 0
except ZeroDivisionError:
    pdb.post_mortem()
```

---

## Herramientas de Debugging Visual

### `icecream` — Print Debugging Mejorado

```bash
pip install icecream
```

```python
from icecream import ic

def calcular(x):
    resultado = x * 2
    ic(x, resultado)  # ic| x: 5, resultado: 10
    return resultado
```

### `rich` — Pretty Print en Terminal

```bash
pip install rich
```

```python
from rich import print, inspect
from rich.traceback import install

install()  # Tracebacks con colores

datos = {"nombre": "Ana", "edad": 30, "skills": ["Python", "SQL"]}
print(datos)
inspect(datos)
```

### `devtools` — Debug para Desarrollo

```bash
pip install devtools
```

```python
from devtools import debug

debug(variable_1, variable_2)
```

---

## Debugging en VS Code

- **Breakpoints**: clic al margen izquierdo del editor
- **Watch**: variables que quieres monitorear
- **Call Stack**: pila de llamadas actual
- **Debug Console**: ejecuta expresiones en el contexto actual

```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

---

## Profiling — Encontrar Cuellos de Botella

### `cProfile` — Perfilador Estándar

```bash
python -m cProfile -o perfil.prof script.py
```

### `snakeviz` — Visualización

```bash
pip install snakeviz
snakeviz perfil.prof
```

### `py-spy` — Profiler sin Modificar Código

```bash
pip install py-spy
py-spy record -o profile.svg -- python script.py
```

### Timeit — Micro-benchmarks

```python
import timeit

tiempo = timeit.timeit(
    'sum(range(1000))',
    number=10000
)
print(f"{tiempo:.4f}s")
```

---

## 🎯 Ejercicios

Practica logging en [ejercicios.md](./ejercicios.md#27--logging-y-debugging).

**Mini-ejercicio**: Configura logging a archivo `app.log` con formato `[NIVEL] mensaje`. 3 funciones que registren su ejecución.

---

## Véase también

- [25-testing](./25-testing.md) — Debug en tests
- [28-packaging](./28-packaging.md) — Logging en producción
- [ejercicios.md](./ejercicios.md) — Práctica recomendada
