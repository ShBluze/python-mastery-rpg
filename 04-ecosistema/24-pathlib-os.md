# 24 — Pathlib y OS

> `pathlib.Path` (objetos ruta), `os`, `shutil`, variables de entorno, filesystem.

---

## `pathlib.Path` — Rutas como Objetos (Python 3.4+)

```python
from pathlib import Path

# Crear ruta
ruta = Path("carpeta") / "subcarpeta" / "archivo.txt"
print(ruta)                    # carpeta/subcarpeta/archivo.txt
print(ruta.name)               # archivo.txt
print(ruta.suffix)             # .txt
print(ruta.stem)               # archivo
print(ruta.parent)             # carpeta/subcarpeta
print(ruta.parents[1])         # carpeta
```

> ⚠️ **Path no crea directorios/archivos** — solo los representa. Usa `.mkdir()`, `.touch()`, etc.

### Propiedades útiles

```python
p = Path("/home/usuario/documentos/archivo.txt")

p.name           # "archivo.txt"
p.suffix         # ".txt"
p.suffixes       # [".txt"] (múltiples: .tar.gz)
p.stem           # "archivo"
p.parent         # /home/usuario/documentos
p.parents        # Iterable de ancestros
p.anchor         # "/" (raíz en Unix)
p.drive          # "C:" (Windows)
p.parts          # ("/", "home", "usuario", "documentos", "archivo.txt")
```

### Operaciones de FS

```python
from pathlib import Path

p = Path("proyecto/datos/archivo.txt")

# Existencia
p.exists()           # True/False
p.is_file()          # Es archivo
p.is_dir()           # Es directorio
p.is_symlink()       # Es symlink

# Crear directorios
p.parent.mkdir(parents=True, exist_ok=True)  # Crea recursivamente

# Crear archivo vacío
p.touch(exist_ok=True)

# Leer/Escribir texto
texto = p.read_text(encoding="utf-8")
p.write_text("contenido", encoding="utf-8")

# Leer/Escribir binario
datos = p.read_bytes()
p.write_bytes(b"\x00\x01")

# Renombrar / Mover
p.rename("nuevo_nombre.txt")
p.replace("otra_ruta.txt")  # Sobrescribe destino

# Eliminar
p.unlink()           # Archivo
p.rmdir()            # Directorio vacío
shutil.rmtree(p)     # Directorio con contenido (ver shutil)
```

### Búsqueda y Listado

```python
base = Path("proyecto")

# Listar
list(base.iterdir())           # Solo hijos inmediatos
list(base.glob("*.py"))        # Patrón simple
list(base.rglob("*.py"))       # Recursivo
list(base.glob("**/*.py"))     # Equivalente a rglob

# Filtros
[h for h in base.iterdir() if h.is_file()]
[h for h in base.iterdir() if h.suffix == ".py"]
```

### Rutas Relativas / Absolutas

```python
p = Path("datos/archivo.txt")

p.absolute()         # /home/user/proyecto/datos/archivo.txt
p.resolve()          # Absoluta + resuelve symlinks
p.relative_to(Path("proyecto"))  # datos/archivo.txt
p.as_posix()         # "datos/archivo.txt" (siempre /)
str(p)               # "datos/archivo.txt" (nativo OS)
```

### Estadísticas

```python
p = Path("archivo.txt")

p.stat()             # os.stat_result (size, mtime, mode, etc.)
p.stat().st_size     # Tamaño en bytes
p.stat().st_mtime    # Modificación (timestamp)
p.stat().st_mode     # Permisos

# Métodos directos
p.lstat()            # No sigue symlinks
p.owner()            # Usuario (Unix)
p.group()            # Grupo (Unix)
```

---

## `os` — Sistema Operativo (Low-level)

```python
import os

# Directorio actual
os.getcwd()                    # "/home/user/proyecto"
os.chdir("/otra/ruta")         # Cambiar directorio

# Listado
os.listdir(".")                # ["archivo.txt", "carpeta", ...]
os.scandir(".")                # Iterator eficiente (DirEntry)

# Rutas
os.path.join("a", "b", "c")    # "a/b/c" (o "a\\b\\c" en Windows)
os.path.abspath("archivo.txt") # Ruta absoluta
os.path.dirname("/a/b/c.txt")  # "/a/b"
os.path.basename("/a/b/c.txt") # "c.txt"
os.path.splitext("archivo.txt")# ("archivo", ".txt")
os.path.exists("archivo.txt")  # True/False
os.path.isfile() / isdir() / islink()

# Archivos
os.rename("viejo.txt", "nuevo.txt")
os.remove("archivo.txt")
os.mkdir("nueva_carpeta")
os.makedirs("a/b/c", exist_ok=True)
os.rmdir("vacía")
os.stat("archivo.txt")         # Stats completos

# Ejecutar comandos
os.system("ls -la")            # Simple (retorna exit code)
os.popen("ls").read()          # Capturar salida (legacy)

# Entorno
os.environ                     # dict-like
os.environ.get("HOME")         # "/home/user"
os.environ["MI_VAR"] = "valor" # Set
os.getenv("VAR", "default")    # Get con default
os.putenv("VAR", "val")        # Set (bajo nivel)
```

> 💡 **Prefiere `pathlib`** para rutas — API más limpia, orientada a objetos.

---

## `shutil` — Operaciones de Alto Nivel

```python
import shutil

# Copiar
shutil.copy("origen.txt", "destino.txt")        # Archivo (metadata básica)
shutil.copy2("origen.txt", "destino.txt")       # + timestamps, permisos
shutil.copytree("carpeta_src", "carpeta_dst")   # Árbol completo

# Mover / Renombrar
shutil.move("origen", "destino")                # Cross-device safe

# Eliminar recursivo
shutil.rmtree("carpeta_con_contenido")          # Fuerza borrado

# Archivos de utilidad
shutil.which("python")                          # Path a ejecutable en PATH
shutil.disk_usage("/")                          # (total, used, free)
shutil.get_archive_formats()                    # Formatos soportados
shutil.make_archive("backup", "zip", "carpeta") # Crear zip/tar
shutil.unpack_archive("backup.zip", "destino")  # Extraer
```

---

## Variables de Entorno

```python
import os

# Lectura
home = os.environ["HOME"]        # KeyError si no existe
home = os.environ.get("HOME")    # None si no existe
home = os.getenv("HOME", "/default")

# Escritura (solo afecta proceso actual y hijos)
os.environ["MI_VAR"] = "valor"
os.putenv("OTRA_VAR", "valor")

# .env files (requiere python-dotenv)
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()  # Carga .env en os.environ
```

### Buenas prácticas

```python
# config.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-in-prod")
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/app.db")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "10"))
```

---

## `tempfile` — Archivos/Carpetas Temporales

```python
import tempfile

# Archivo temporal (se borra al cerrar)
with tempfile.NamedTemporaryFile(mode="w+", delete=True) as tmp:
    tmp.write("datos")
    tmp.flush()
    print(tmp.name)  # Ruta al archivo

# Directorio temporal
with tempfile.TemporaryDirectory() as tmpdir:
    print(tmpdir)  # /tmp/tmpxxxxxx
    # Trabajo con archivos en tmpdir
# Se borra automáticamente al salir

# Rutas del sistema
tempfile.gettempdir()  # /tmp (Unix) o %TEMP% (Windows)
```

---

## `glob` / `fnmatch` — Patrones de Archivos

```python
import glob
from pathlib import Path

# glob (strings)
glob.glob("*.py")                    # Actual
glob.glob("**/*.py", recursive=True) # Recursivo
glob.glob("data/*.csv")

# pathlib (objetos Path)
Path(".").glob("*.py")
Path(".").rglob("*.py")

# fnmatch (filtrar lista)
import fnmatch
archivos = ["a.py", "b.txt", "test.py"]
fnmatch.filter(archivos, "*.py")  # ["a.py", "test.py"]
```

---

## `filecmp` / `hashlib` — Comparación e Integridad

```python
import filecmp
import hashlib

# Comparar archivos
filecmp.cmp("a.txt", "b.txt")           # True/False (contenido)
filecmp.cmp("a.txt", "b.txt", shallow=False)  # Incluye metadata

# Hash de archivo
def hash_archivo(ruta, algo="sha256"):
    h = hashlib.new(algo)
    with open(ruta, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

print(hash_archivo("archivo.txt"))  # sha256 hex
```

---

## `mmap` — Archivos Mapeados en Memoria

```python
import mmap

with open("grande.log", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.readline())  # bytes
    mm[0:4] = b"TEST"     # Modifica archivo directamente
    mm.flush()
```

---

## Resumen: Qué usar cuándo

| Tarea | Herramienta |
|-------|-------------|
| Rutas, leer/escribir, buscar | `pathlib.Path` |
| Variables entorno, proceso | `os` / `os.environ` |
| Copiar/mover/borrar árboles | `shutil` |
| Archivos temporales | `tempfile` |
| Patrones de búsqueda | `pathlib.glob` / `glob` |
| Stats, permisos, symlinks | `os.stat` / `path.stat()` |
| Ejecutar comandos | `subprocess` (no `os.system`) |
| Comparar archivos | `filecmp` |
| Hash integridad | `hashlib` |

---

## Buenas Prácticas

1. **`pathlib` por defecto** para rutas
2. **`subprocess.run()`** en vez de `os.system()` / `os.popen()`
3. **`shutil`** para operaciones de árbol
4. **`tempfile`** para temporales (limpieza automática)
5. **`dotenv`** para config local (`.env` en `.gitignore`)
6. **Rutas relativas a `__file__`** o `Path.cwd()` para portabilidad

```python
# ✅ Portátil
BASE = Path(__file__).parent
DATA = BASE / "data"

# ❌ Frágil
DATA = Path("data")  # Depende de cwd
```

---

## 🎯 Ejercicios

Practica pathlib en [ejercicios.md](./ejercicios.md#24--pathlib-y-os).

**Mini-ejercicio**: Script que lista todos los archivos .py en un directorio, ordenados por fecha de modificación. Usa Path.rglob().

---

## Véase también

- [23-archivos-persistencia](./23-archivos-persistencia.md) — TXT, CSV, JSON, SQLite
- [28-packaging](../04-ecosistema/28-packaging.md) — `data_files`, `include_package_data`
- [32-automatizacion-cli](../05-especializaciones/32-automatizacion-cli.md) — Scripts FS
- [ejercicios.md](./ejercicios.md) — Práctica recomendada