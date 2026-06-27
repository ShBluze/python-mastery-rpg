# 👑 Boss Final — App Web Completa

**Ruta**: 🌐 Web | **XP**: 500 | **HP mínimo**: 80

---

## 📖 Historia

Eres un arquitecto web. El reino necesita una plataforma de gestión de contenido (CMS) donde los usuarios puedan registrarse, crear artículos, comentar y administrar su perfil. Construye el backend con FastAPI y despliega.

## 🎯 Requisitos obligatorios

- [ ] API REST con FastAPI
- [ ] SQLAlchemy + migraciones (Alembic)
- [ ] Autenticación JWT (registro, login, refresh)
- [ ] Roles: admin, editor, lector
- [ ] CRUD de artículos (título, contenido, tags, fecha)
- [ ] CRUD de comentarios (solo usuarios autenticados)
- [ ] Búsqueda y filtros (por tag, autor, fecha)
- [ ] Paginación
- [ ] Tests (cobertura ≥ 70%)
- [ ] Desplegado en Railway/Render/Fly.io

## 📋 Criterios de éxito

- `GET /api/docs` documentación interactiva funcional
- Registro de usuario + login devuelve JWT
- Endpoints protegidos correctamente
- Validación con Pydantic en todos los endpoints
- logging en cada endpoint

## 📦 Stack

- FastAPI + Uvicorn
- SQLAlchemy 2.0 + Alembic
- Pydantic v2
- python-jose + passlib
- pytest + httpx (async tests)
- PostgreSQL (prod) / SQLite (dev)
