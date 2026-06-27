# 29 — Desarrollo Web

> Flask, FastAPI, Django, APIs REST, bases de datos, templates, despliegue.

---

## Frameworks Web

### Flask — Microframework

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensaje": "Hola mundo"}

@app.route("/api/usuarios", methods=["GET", "POST"])
def usuarios():
    if request.method == "POST":
        data = request.get_json()
        return jsonify({"creado": data}), 201
    return jsonify([{"id": 1, "nombre": "Ana"}])

@app.route("/api/usuarios/<int:uid>")
def usuario(uid):
    return jsonify({"id": uid, "nombre": "Usuario"})
```

```bash
pip install flask
flask run
# o: python -m flask run --port 5000
```

#### Templates con Jinja2

```python
from flask import render_template

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return render_template("saludo.html", nombre=nombre, activo=True)
```

```html
<!-- templates/saludo.html -->
<!DOCTYPE html>
<html>
<body>
  <h1>Hola {{ nombre }}!</h1>
  {% if activo %}
    <p>Cuenta activa</p>
  {% endif %}
</body>
</html>
```

### FastAPI — Moderno + Async + Tipos

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int | None = None

@app.get("/")
def root():
    return {"mensaje": "FastAPI"}

@app.get("/api/usuarios")
def listar():
    return [{"id": 1, "nombre": "Ana"}]

@app.post("/api/usuarios", status_code=201)
def crear(usuario: Usuario):
    return {"id": 2, **usuario.model_dump()}

@app.get("/api/usuarios/{uid}")
def obtener(uid: int):
    if uid <= 0:
        raise HTTPException(status_code=404, detail="No encontrado")
    return {"id": uid, "nombre": "Usuario"}
```

```bash
pip install fastapi uvicorn[standard]
uvicorn main:app --reload --port 8000
# Docs automáticas: http://localhost:8000/docs
```

#### Async con FastAPI

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/api/proxy")
async def proxy():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.example.com/data")
    return resp.json()
```

### Django — Full-Stack Framework

```bash
pip install django
django-admin startproject mi_proyecto
cd mi_proyecto
python manage.py startapp mi_app
python manage.py runserver
```

#### Modelos + Admin

```python
# mi_app/models.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField(null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## Comparativa Rápida

| Aspecto            | Flask          | FastAPI           | Django               |
|--------------------|----------------|-------------------|----------------------|
| **Tipo**           | Microframework | Microframework    | Full-stack (baterías incluidas) |
| **Rendimiento**    | Medio          | Alto (async)      | Medio                |
| **Async**          | Opcional       | Nativo            | 3.1+ (vía ASGI)      |
| **ORM**            | SQLAlchemy/peewee | SQLAlchemy    | Django ORM (incluido)|
| **Admin**          | No             | No                | Sí (incluido)        |
| **Docs automáticas**| No            | Sí (Swagger/Redoc)| No                   |
| **Curva**          | Baja           | Media             | Alta                 |
| **Ecosistema**     | Extensiones    | Nuevo, creciendo  | Maduro, enorme       |

---

## APIs REST — Buenas Prácticas

```python
# Convenciones REST
GET    /api/usuarios        # Listar
POST   /api/usuarios        # Crear
GET    /api/usuarios/{id}   # Obtener uno
PUT    /api/usuarios/{id}   # Reemplazar
PATCH  /api/usuarios/{id}   # Actualizar parcial
DELETE /api/usuarios/{id}   # Eliminar
```

### Paginación

```python
@app.get("/api/usuarios")
def listar(skip: int = 0, limit: int = 10):
    # skip/offset + limit
    usuarios = db.query(Usuario).offset(skip).limit(limit).all()
    total = db.query(Usuario).count()
    return {
        "items": usuarios,
        "total": total,
        "skip": skip,
        "limit": limit,
    }
```

### Versionado

```python
# URL: /api/v1/usuarios
app = FastAPI()

@app.get("/api/v1/usuarios")
def listar_v1(): ...

@app.get("/api/v2/usuarios")
def listar_v2(): ...
```

---

## Bases de Datos

### SQLAlchemy + FastAPI

```bash
pip install sqlalchemy asyncpg
```

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)

Base.metadata.create_all(bind=engine)
```

### Alembic — Migraciones

```bash
pip install alembic
alembic init alembic
alembic revision --autogenerate -m "crear usuarios"
alembic upgrade head
```

---

## Proyectos Recomendados

| Proyecto                | Stack sugerido                          |
|-------------------------|-----------------------------------------|
| **Blog**                | Django + SQLite + Bootstrap             |
| **API REST**            | FastAPI + SQLAlchemy + PostgreSQL       |
| **To-Do List**          | Flask + SQLite + HTMX                   |
| **E-commerce**          | Django + PostgreSQL + Stripe            |
| **Chat en tiempo real** | FastAPI + WebSockets + Redis            |

---

---
## 🎯 Ruta completa

La ruta Web se ha expandido. Consulta [`29-web/README.md`](29-web/README.md) para el plan de estudio detallado con ejercicios y boss final.

---

## Véase también

- [30-data-science](./30-data-science.md) — Análisis de datos en web
- [33-gui](./33-gui.md) — Interfaces gráficas de escritorio
- [32-automatizacion-cli](./32-automatizacion-cli.md) — CLI tools
- [29-web/README.md](29-web/README.md) — Ruta Web completa
