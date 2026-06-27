# Apéndice C — Cheatsheets

Referencias rápidas de sintaxis, operadores, built-ins y stdlib.

---

## Operadores

### Aritméticos

| Operador | Nombre | Ejemplo |
|----------|--------|---------|
| `+` | Suma | `3 + 2` → `5` |
| `-` | Resta | `3 - 2` → `1` |
| `*` | Multiplicación | `3 * 2` → `6` |
| `/` | División real | `5 / 2` → `2.5` |
| `//` | División entera | `5 // 2` → `2` |
| `%` | Módulo (resto) | `5 % 2` → `1` |
| `**` | Potencia | `3 ** 2` → `9` |

### Comparación (encadenables)

```python
a == b   # igualdad (valor)
a != b   # diferente
a < b    # menor
a <= b   # menor o igual
a > b    # mayor
a >= b   # mayor o igual
a is b       # misma identidad (objeto)
a is not b   # distinta identidad
a in b       # pertenencia
a not in b   # no pertenencia

# Encadenamiento:
1 < x < 10        # equivalente a: 1 < x and x < 10
```

### Lógicos (short-circuit)

```python
a and b   # → b si a es truthy, sino a
a or b    # → a si a es truthy, sino b
not a     # → True si a es falsy
```

### Bitwise

| Op | Nombre | Ejemplo |
|----|--------|---------|
| `&` | AND | `5 & 3` → `1` |
| `\|` | OR | `5 \| 3` → `7` |
| `^` | XOR | `5 ^ 3` → `6` |
| `~` | NOT | `~5` → `-6` |
| `<<` | Shift izq | `5 << 1` → `10` |
| `>>` | Shift der | `5 >> 1` → `2` |

### Asignación aumentada

```python
x += 5   # x = x + 5
x -= 5   # x = x - 5
x *= 5   # x = x * 5
x /= 5   # x = x / 5
x //= 5  # x = x // 5
x %= 5   # x = x % 5
x **= 2  # x = x ** 2
x |= 3   # x = x | 3
x &= 3   # x = x & 3
# Walrus (3.8+):
(x := len(s)) > 0
```

### Precedencia (de mayor a menor)

| Nivel | Operadores |
|-------|------------|
| 1 | `(...)`, `[...]`, `{...}` |
| 2 | `x[i]`, `x.attr`, `f(...)` |
| 3 | `**` |
| 4 | `+x`, `-x`, `~x` (unarios) |
| 5 | `*`, `/`, `//`, `%` |
| 6 | `+`, `-` (binarios) |
| 7 | `<<`, `>>` |
| 8 | `&` |
| 9 | `^` |
| 10 | `\|` |
| 11 | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` |
| 12 | `not` |
| 13 | `and` |
| 14 | `or` |
| 15 | `:=` (walrus) |
| 16 | `lambda` |

---

## Magic Methods (dunder)

### Creación y representación

```python
__new__(cls, ...)    # Crear instancia (constructor real)
__init__(self, ...)  # Inicializar instancia
__del__(self)        # Destructor (no confiar)
__repr__(self)       # Representación "oficial" → repr(obj)
__str__(self)        # Representación "bonita" → str(obj)
__format__(self, fmt) # Formato → f"{obj:fmt}"
__bytes__(self)      # → bytes(obj)
__hash__(self)       # → hash(obj)
```

### Comparación

```python
__eq__(self, other)  # ==
__ne__(self, other)  # !=
__lt__(self, other)  # <
__le__(self, other)  # <=
__gt__(self, other)  # >
__ge__(self, other)  # >=
```

### Operadores aritméticos

```python
__add__(self, other)    # +
__sub__(self, other)    # -
__mul__(self, other)    # *
__truediv__(self, o)    # /
__floordiv__(self, o)   # //
__mod__(self, other)    # %
__pow__(self, other)    # **
__and__(self, other)    # &
__or__(self, other)     # |
__xor__(self, other)    # ^
__lshift__(self, o)     # <<
__rshift__(self, o)     # >>

# Versiones reversed (r) e in-place (i):
__radd__, __iadd__, ...
```

### Contenedores

```python
__len__(self)           # len(obj)
__getitem__(self, k)    # obj[k]
__setitem__(self, k, v) # obj[k] = v
__delitem__(self, k)    # del obj[k]
__contains__(self, x)   # x in obj
__iter__(self)          # iter(obj)
__next__(self)          # next(obj)
__reversed__(self)      # reversed(obj)
__missing__(self, k)    # dict[missing_key]
```

### Context manager

```python
__enter__(self)    # with obj as x:
__exit__(self, exc_type, exc_val, tb)
```

### Callable

```python
__call__(self, ...)  # obj(...)
```

---

## Built-ins por categoría

### Conversión de tipos

```python
int(x)        # entero (base 10)
float(x)      # flotante
str(x)        # string
bool(x)       # booleano
bytes(x)      # bytes
list(x)       # lista
tuple(x)      # tupla
set(x)        # conjunto
frozenset(x)  # conjunto inmutable
dict(x)       # diccionario
complex(r, i) # número complejo
chr(i)        # int → caracter Unicode
ord(c)        # caracter → int Unicode
bin(i)        # int → binario "0b101"
hex(i)        # int → hex "0xff"
oct(i)        # int → octal "0o77"
```

### Iteración y colecciones

```python
len(s)          # longitud
enumerate(s)    # (índice, valor)
zip(*iters)     # agrupa iterables
map(f, it)      # aplica función
filter(f, it)   # filtra con función
reversed(s)     # inversa
sorted(s, key, reverse)  # ordena
all(it)         # True si todos truthy
any(it)         # True si alguno truthy
sum(it)         # suma numérica
min(it)         # mínimo
max(it)         # máximo
range(start, stop, step)  # rango numérico
slice(start, stop, step)  # rebanada
```

### Introspectión y metaprogramación

```python
type(obj)           # clase del objeto
isinstance(o, cls)  # comprobación runtime
issubclass(c1, c2)  # herencia
hasattr(o, name)    # existe atributo
getattr(o, n, d)    # leer atributo
setattr(o, n, v)    # escribir atributo
delattr(o, n)       # eliminar atributo
dir(obj)            # lista atributos
vars(obj)           # __dict__
id(obj)             # identidad única
callable(obj)       # es invocable?
super()             # delegar a clase padre
__name__            # nombre del módulo
__file__            # ruta del módulo
```

### Entrada/salida

```python
print(*objs, sep=" ", end="\n", file=sys.stdout)
input(prompt)         # entrada de texto
open(file, mode)      # abrir archivo
format(x, spec)       # formatear
repr(obj)             # representación debug
ascii(obj)            # representación ASCII
```

### Matemáticas

```python
abs(x)        # valor absoluto
pow(x, y, m)  # potencia con módulo
round(x, n)   # redondeo
divmod(a, b)  # (a // b, a % b)
```

### Gestión de objetos

```python
del x              # eliminar referencia
breakpoint()       # debugger (3.7+)
help(obj)          # documentación interactiva
exit()             # salir del REPL
```

---

## Strings — Formateo rápido

### F-strings (3.6+, preferido)

```python
f"Hello {name}"
f"{pi:.2f}"           # 3.14
f"{num:>10}"          # alinear derecha
f"{num:<10}"          # alinear izquierda
f"{num:^10}"          # centrar
f"{num:010}"          # rellenar con ceros
f"{val:.2%}"          # porcentaje
f"{val:,}"            # separador miles
f"{val:_}"            # separador miles (_)
f"{val!r}"            # repr()
f"{val!s}"            # str()
f"{val!a}"            # ascii()
f"{dict(zip(keys, vals))!s}"  # expresiones
```

### `str.format()`

```python
"{} {}".format(a, b)
"{0} {1} {0}".format(a, b)
"{name} {age}".format(name="X", age=5)
"{:.2f}".format(3.14159)
```

### Métodos útiles

```python
s.upper()
s.lower()
s.strip() / s.lstrip() / s.rstrip()
s.split(sep) / s.rsplit()
s.join(iterable)
s.replace(old, new)
s.find(sub) / s.index(sub)
s.startswith(prefix) / s.endswith(suffix)
s.count(sub)
s.isdigit() / s.isalpha() / s.isalnum()
s.zfill(width)
```

---

## Comprehensions

```python
# Lista
[x * 2 for x in range(10)]
[x * 2 for x in range(10) if x % 2 == 0]

# Set
{x % 3 for x in range(20)}

# Dict
{x: x ** 2 for x in range(5)}
{k: v for k, v in dict.items() if v > 0}

# Generador (tuple NO es comprehension)
(x ** 2 for x in range(1000000))  # lazy, no consume memoria

# Anidado (tabla de multiplicar)
[[i * j for j in range(1, 11)] for i in range(1, 11)]
```

---

## Decoradores comunes

```python
# built-in
@property        # getter sin paréntesis
@staticmethod  # método sin self
@classmethod   # método recibe cls
@dataclass     # genera __init__, __repr__, __eq__, ...

# stdlib
@functools.lru_cache(maxsize=128)  # memoización
@functools.cache                   # memoización (3.9+)
@functools.wraps(func)             # preservar metadatos
@contextlib.contextmanager         # context manager con yield
@abc.abstractmethod                # método abstracto
@typing.overload                   # sobrecarga de tipos
```

---

## Context Manager (`with`)

```python
# Clase
class MiContexto:
    def __enter__(self):
        return self.recurso
    def __exit__(self, exc_type, exc_val, tb):
        self.recurso.close()

# contextlib
from contextlib import contextmanager
@contextmanager
def mi_contexto():
    recurso = abrir()
    try:
        yield recurso
    finally:
        recurso.close()

# stdlib útiles
with open("file.txt") as f: ...
with lock: ...                          # threading.Lock
with closing(obj): ...                  # contextlib.closing
with suppress(FileNotFoundError): ...   # contextlib.suppress
with ExitStack() as stack: ...          # contextlib.ExitStack
```

---

## Excepciones — Jerarquía

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration / StopAsyncIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── FloatingPointError
    │   └── OverflowError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError / ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError / UnboundLocalError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   ├── TimeoutError
    │   ├── ConnectionError
    │   │   ├── ConnectionRefusedError
    │   │   ├── ConnectionAbortedError
    │   │   └── ConnectionResetError
    │   └── IsADirectoryError / NotADirectoryError
    ├── RuntimeError
    │   ├── NotImplementedError
    │   └── RecursionError
    ├── TypeError
    ├── ValueError / UnicodeError
    ├── DeprecationWarning
    └── Warning
        ├── UserWarning
        ├── SyntaxWarning
        └── ResourceWarning
```

---

## Type Hints — Sintaxis rápida

```python
# Variables
x: int = 5
name: str
items: list[int] | None = None

# Funciones
def suma(a: int, b: int) -> int: ...

# Colecciones
list[int]
tuple[int, str]
dict[str, int]
set[int]
frozenset[int]

# Opcional / Unión
from typing import Optional, Union
x: Optional[int] = None     # int | None (3.10+)
x: int | None               # 3.10+
y: Union[int, str]          # int | str (3.10+)
y: int | str                # 3.10+

# Any, Never
from typing import Any, Never
x: Any          # cualquier tipo
y: Never        # nunca retorna

# Callable
from collections.abc import Callable
fn: Callable[[int, int], int]  # (int, int) → int

# Self (3.11+)
from typing import Self
class Foo:
    def clone(self) -> Self: ...

# TypeVar / Generic
from typing import TypeVar, Generic
T = TypeVar("T")
class Stack(Generic[T]):
    def push(self, item: T) -> None: ...

# Protocol (duck typing estructural)
from typing import Protocol
class Drawable(Protocol):
    def draw(self) -> None: ...

# TypedDict
from typing import TypedDict
class User(TypedDict):
    name: str
    age: int

# Literal, Final, TypeAlias
from typing import Literal, Final, TypeAlias
mode: Literal["r", "w", "a"]
PI: Final = 3.14159
Vector: TypeAlias = list[float]
```

---

## Stdlib — Referencia rápida

### OS / System

```python
import os
os.getcwd()           # directorio actual
os.chdir(path)        # cambiar directorio
os.listdir(path)      # listar archivos
os.mkdir(path)        # crear directorio
os.makedirs(path, exist_ok=True)
os.remove(path)       # eliminar archivo
os.rename(src, dst)   # renombrar
os.environ["VAR"]     # variable de entorno
os.path.join(a, b)    # ruta cross-platform
os.path.exists(path)  # existe?
os.path.isfile(path)  # es archivo?
os.path.isdir(path)   # es directorio?
os.walk(path)         # recorrer árbol
```

### sys

```python
import sys
sys.argv              # argumentos CLI
sys.exit(code)        # salir con código
sys.path              # rutas de import
sys.modules           # módulos cargados
sys.platform          # SO: "linux", "win32", "darwin"
sys.version           # versión Python
sys.stdin / stdout / stderr
sys.getrecursionlimit()
sys.setrecursionlimit(n)
```

### JSON

```python
import json
json.dumps(obj)                # objeto → string
json.dump(obj, file)           # objeto → archivo
json.loads(string)             # string → objeto
json.load(file)                # archivo → objeto
json.dumps(obj, indent=2)      # pretty-print
json.loads(s, object_hook=...) # post-procesar
```

### re (regex)

```python
import re
re.search(pattern, string)   # primera coincidencia
re.match(pattern, string)    # desde inicio
re.findall(pattern, string)  # todas → list[str]
re.finditer(pattern, string) # todas → Iterator
re.sub(repl, string)         # reemplazar
re.split(pattern, string)    # dividir
re.compile(pattern)          # compilar (cache)

# flags
re.IGNORECASE / re.I
re.MULTILINE  / re.M
re.DOTALL     / re.S
re.VERBOSE    / re.X

# grupos
m = re.search(r"(\w+)@(\w+)\.(\w+)", email)
m.group(0)   # match completo
m.group(1)   # primer grupo
m.groups()   # todos los grupos
```

### collections

```python
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict

defaultdict(list)           # valor por defecto
Counter("abracadabra")      # contador de elementos
deque(maxlen=10)            # cola doble con tope
namedtuple("Punto", "x y")  # tupla con nombres
OrderedDict()               # dict ordenado (Python 3.7+ = dict normal)
```

### itertools

```python
from itertools import chain, cycle, count, product, permutations, combinations, groupby, accumulate

chain(iter1, iter2)              # concatenar
cycle(iter)                      # ciclo infinito
count(start=0, step=1)           # contador infinito
product("AB", repeat=2)          # producto cartesiano
permutations(range(3), 2)        # permutaciones
combinations(range(5), 3)        # combinaciones
groupby(iter, key)               # agrupar (ordenado!)
accumulate(range(10))            # suma acumulativa
islice(iter, start, stop)        # rebanada
repeat(x, n)                     # repetir x, n veces
zip_longest(*iters, fillvalue)   # zip con relleno
```

### datetime

```python
from datetime import datetime, date, time, timedelta, timezone

datetime.now()                       # ahora
datetime(2024, 12, 25, 10, 30)
datetime.fromtimestamp(ts)           # timestamp → datetime
datetime.fromisoformat("2024-12-25") # string ISO
dt.strftime("%Y-%m-%d")              # formato
dt.strptime("2024-12-25", fmt)       # parse
dt + timedelta(days=7)               # sumar/restar
dt.replace(day=1)                    # reemplazar
```

### pathlib (3.4+, preferido sobre `os.path`)

```python
from pathlib import Path

p = Path("/home/user/file.txt")
p.parent           # /home/user
p.name             # file.txt
p.stem             # file
p.suffix           # .txt
p.exists()
p.is_file() / p.is_dir()
p.read_text()      # leer archivo completo
p.write_text("x")  # escribir archivo
p.mkdir(parents=True, exist_ok=True)
p.glob("*.py")     # globbing
p.rglob("**/*")    # recursivo
```

### logging

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warn")
logging.error("error")
logging.critical("critical")
logger = logging.getLogger(__name__)
```

### random

```python
import random
random.random()              # [0.0, 1.0)
random.randint(a, b)         # int en [a, b]
random.choice(seq)           # elemento aleatorio
random.choices(seq, k=3)     # n elementos (con repetición)
random.sample(seq, k=3)      # n elementos (sin repetición)
random.shuffle(list)         # mezclar in-place
random.seed(42)              # reproducible
```

### functools

```python
from functools import lru_cache, cache, wraps, partial, reduce

@cache              # memoización (3.9+)
@lru_cache(maxsize=None)  # memoización
partial(func, arg)  # fijar argumentos
reduce(fn, iter)    # acumular (antes built-in)
wraps(func)         # decorador: preserva metadatos
```

### hashlib / secrets

```python
import hashlib, secrets
hashlib.sha256(b"data").hexdigest()
secrets.token_hex(16)         # token seguro
secrets.token_urlsafe(32)     # URL-safe
secrets.choice(seq)           # criptográficamente seguro
secrets.compare_digest(a, b)  # comparación timing-safe
```

### threading / multiprocessing

```python
from threading import Thread, Lock, Event
t = Thread(target=fn, args=())
t.start()
t.join()

lock = Lock()
with lock: ...

from multiprocessing import Process, Pool
with Pool(4) as p:
    results = p.map(fn, items)
```

### subprocess

```python
import subprocess
subprocess.run(["ls", "-la"], capture_output=True, text=True)
result.stdout
result.returncode
subprocess.Popen(...)
```

---

## argparse — CLI rápido

```python
import argparse

parser = argparse.ArgumentParser(description="Tool")
parser.add_argument("input", help="Archivo de entrada")
parser.add_argument("-o", "--output", default="out.txt")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--mode", choices=["fast", "safe"])
args = parser.parse_args()
print(args.input, args.output)
```

---

## Test — PyTest rápido

```python
# test_foo.py
def test_upper():
    assert "hola".upper() == "HOLA"

def test_raises():
    with pytest.raises(ValueError):
        int("no")

def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)

@pytest.fixture
def db():
    return setup_db()

def test_with_fixture(db):
    assert db.query() is not None
```

---

## F-strings — Tabla de formato

| Especificador | Salida para `3.14159` |
|---------------|----------------------|
| `:.2f` | `3.14` |
| `:+.2f` | `+3.14` |
| `:.0f` | `3` |
| `:010.2f` | `000003.14` |
| `:>10.2f` | `      3.14` |
| `:<10.2f` | `3.14      ` |
| `:^10.2f` | `  3.14    ` |
| `:.2%` | `314.16%` |
| `:e` | `3.141590e+00` |
| `:_` | `1_000_000` |
| `:,` | `1,000,000` |

---

## Recursos relacionados

- [Apéndice A: Glosario técnico](./A-glosario-tecnico.md) — Definiciones clave
- [Apéndice B: CLI vs UI vs GUI](./B-cli-ui-gui.md) — Interfaces comparadas
- [Apéndice D: Recursos y roadmap](./D-recursos-roadmap.md) — Libros, cursos, plan de estudio
