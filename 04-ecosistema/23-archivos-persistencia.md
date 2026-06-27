# 23 — Archivos y Persistencia

> TXT, CSV, JSON, Pickle, SQLite, formatos ML — lectura/escritura, modos, mejores prácticas.

---

## Archivos de Texto (TXT)

```python
# Lectura completa
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

# Lectura línea a línea (memory efficient)
with open("archivo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())

# Escritura
with open("salida.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\n")
    f.writelines(["Línea 2\n", "Línea 3\n"])

# Añadir (append)
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nueva entrada\n")
```

### Modos de apertura

| Modo | Descripción | Cursor | Crea | Trunca |
|------|-------------|--------|------|--------|
| `r` | Leer | Inicio | ❌ | ❌ |
| `w` | Escribir | Inicio | ✅ | ✅ |
| `a` | Añadir | Final | ✅ | ❌ |
| `r+` | Leer/Escribir | Inicio | ❌ | ❌ |
| `w+` | Leer/Escribir | Inicio | ✅ | ✅ |
| `rb`/`wb` | Binario | — | — | — |

> 💡 **Siempre usa `with`**: cierra automáticamente, incluso si hay excepción.

---

## CSV — Datos Tabulares

```python
import csv

# Escritura
with open("datos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["nombre", "edad", "ciudad"])
    writer.writerows([
        ["Ana", 25, "Madrid"],
        ["Luis", 30, "Barcelona"]
    ])

# Lectura
with open("datos.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    encabezados = next(reader)
    for fila in reader:
        print(dict(zip(encabezados, fila)))

# DictReader/DictWriter (más cómodo)
with open("datos.csv", "r") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(fila["nombre"], fila["edad"])
```

### CSV con tipos personalizados

```python
import csv
from datetime import date

def serializar_fecha(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError

with open("fechas.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["evento", "fecha"])
    writer.writerow(["Lanzamiento", date(2024, 1, 15)])
```

---

## JSON — Estructuras de Datos

```python
import json

datos = {
    "usuarios": [
        {"nombre": "Ana", "edad": 25, "activo": True},
        {"nombre": "Luis", "edad": 30, "activo": False}
    ],
    "metadata": {"version": 1, "tags": ["api", "v1"]}
}

# Escritura
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)

# Lectura
with open("datos.json", "r", encoding="utf-8") as f:
    cargados = json.load(f)
```

### Encoder/Decoder personalizado

```python
import json
from datetime import datetime, date

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def custom_decoder(dct):
    for k, v in dct.items():
        if isinstance(v, str):
            try:
                dct[k] = datetime.fromisoformat(v)
            except ValueError:
                pass
    return dct

json.dumps(obj, cls=CustomEncoder)
json.loads(s, object_hook=custom_decoder)
```

---

## Pickle — Objetos Python Completos

```python
import pickle

# Cualquier objeto Python
datos = {
    "modelo": MiClase(),
    "lista": [1, 2, 3],
    "funcion": lambda x: x * 2  # ⚠️ No serializa lambdas bien
}

# Escritura binaria
with open("datos.pkl", "wb") as f:
    pickle.dump(datos, f, protocol=pickle.HIGHEST_PROTOCOL)

# Lectura
with open("datos.pkl", "rb") as f:
    cargados = pickle.load(f)
```

> ⚠️ **Seguridad**: `pickle.load()` ejecuta código arbitrario. **Nunca** deserialices datos no confiables.
> Para datos externos → usa JSON.

### `joblib` (mejor para arrays grandes / ML)

```bash
pip install joblib
```

```python
import joblib
import numpy as np

arr = np.random.rand(10000, 100)
joblib.dump(arr, "array.joblib", compress=3)  # Compresión
arr2 = joblib.load("array.joblib")
```

---

## SQLite — Base de Datos Relacional

```python
import sqlite3

# Conexión (crea archivo si no existe)
conn = sqlite3.connect("datos.db")
cursor = conn.cursor()

# Tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE,
        edad INTEGER,
        creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Inserción (parámetros seguros contra SQL injection)
cursor.execute(
    "INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)",
    ("Ana", "ana@mail.com", 25)
)
conn.commit()

# Consulta
cursor.execute("SELECT * FROM usuarios WHERE edad > ?", (18,))
for fila in cursor.fetchall():
    print(fila)

# Context manager (auto-commit/rollback)
with sqlite3.connect("datos.db") as conn:
    conn.execute("INSERT INTO usuarios (nombre) VALUES (?)", ("Luis",))

conn.close()
```

### Row Factory (acceso por nombre)

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM usuarios")
for row in cursor:
    print(row["nombre"], row["email"])  # Acceso por columna
```

---

## Formatos ML / IA

| Formato | Uso | Librería |
|---------|-----|----------|
| `.pkl` / `.joblib` | Modelos scikit-learn, pipelines | `pickle`, `joblib` |
| `.h5` / `.keras` | Modelos Keras/TensorFlow | `model.save()` |
| `.pt` / `.pth` | Modelos PyTorch | `torch.save()` |
| `.onnx` | Interoperabilidad | `torch.onnx.export()` |
| `.tflite` | TensorFlow Lite (móvil) | `tf.lite.TFLiteConverter` |

```python
# Keras/TensorFlow
model.save("modelo.keras")  # Formato nativo (Keras 3+)
model.save("modelo.h5")     # Legacy

# PyTorch
torch.save(model.state_dict(), "modelo.pt")
model.load_state_dict(torch.load("modelo.pt"))

# scikit-learn
joblib.dump(pipeline, "pipeline.joblib")
pipeline = joblib.load("pipeline.joblib")
```

---

## Resumen: Cuándo usar qué

| Necesidad | Formato | Por qué |
|-----------|---------|---------|
| Texto simple, logs | TXT | Simple, legible |
| Tablas, Excel, ETL | CSV | Estándar, streaming |
| APIs, config, datos anidados | JSON | Universal, tipado |
| Objetos Python internos | Pickle / joblib | Serialización nativa |
| Datos relacionales, consultas | SQLite | SQL, ACID, sin servidor |
| Modelos ML | joblib / .keras / .pt | Optimizados por framework |

---

## Buenas Prácticas

1. **Encoding explícito**: `encoding="utf-8"` siempre
2. **`with` obligatorio**: Cierre garantizado
3. **Rutas con `pathlib`**: `Path("datos") / "archivo.json"`
4. **Validar JSON de entrada**: `jsonschema`, `pydantic`
5. **No pickle datos externos**: Riesgo de RCE
6. **Backup antes de escribir crítico**: `.bak` + atomic write
7. **Streaming para archivos grandes**: `csv.reader`, `ijson`, `pandas.chunksize`

```python
# Escritura atómica (evita archivos corruptos)
import tempfile
import os

def escribir_atomico(ruta, contenido):
    with tempfile.NamedTemporaryFile(
        mode="w", dir=os.path.dirname(ruta), delete=False
    ) as tmp:
        tmp.write(contenido)
        tmp_path = tmp.name
    os.replace(tmp_path, ruta)  # Atómico en POSIX
```

---

## 🎯 Ejercicios

Practica archivos en [ejercicios.md](./ejercicios.md#23--archivos-y-persistencia).

**Mini-ejercicio**: Programa que lee `datos.csv`, filtra filas donde edad > 30, guarda resultado en `mayores.csv`. Usa el módulo csv.

---

## Véase también

- [24-pathlib-os](./24-pathlib-os.md) — Rutas, FS, variables entorno
- [28-packaging](../04-ecosistema/28-packaging.md) — `pyproject.toml`, data files
- [31-ia-ml](../05-especializaciones/31-ia-ml.md) — Persistencia modelos
- [ejercicios.md](./ejercicios.md) — Práctica recomendada