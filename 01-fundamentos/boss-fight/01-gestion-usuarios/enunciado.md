# ⚔️ BOSS FIGHT — Gestión de Usuarios

> 🧙‍♂️ **El Guardián de la Aldea** te reta a construir un sistema de usuarios funcional.

**Módulo**: 01-fundamentos | **XP**: 150 | **HP mínimo**: 50 | **Dificultad**: 🟢 Básico

---

## 📖 Historia

El Guardián de la Aldea necesita un sistema para registrar, buscar y gestionar los habitantes. Has aprendido lo básico: variables, condicionales, bucles, funciones, errores, estructuras de datos. Ahora demuestra que puedes construir algo real.

## 🎯 Requisitos del Boss

### Obligatorios (pasan el Boss)
- [ ] Menú CLI interactivo
- [ ] CRUD completo: crear, listar, actualizar, eliminar usuarios
- [ ] Cada usuario: id, nombre, email, edad, rol (admin/user)
- [ ] Datos persistentes en JSON (`usuarios.json`)
- [ ] Validaciones: email único, edad ≥ 0, nombre no vacío
- [ ] Manejo de errores: archivo corrupto, ID no existente, email duplicado
- [ ] Funciones modulares (al menos 5 funciones separadas)
- [ ] Búsqueda por nombre (parcial, case-insensitive)

### Bonus (más XP)
- [ ] Exportar usuarios a CSV
- [ ] Login simple (email + contraseña con hash básico)
- [ ] Paginación al listar (5 usuarios por página)

## 📋 Estructura sugerida

```
gestion-usuarios/
├── main.py           # Menú principal + if __name__
├── usuarios.py       # CRUD + persistencia
├── validaciones.py   # Funciones de validación
├── modelos.py        # Constantes, tipos
└── usuarios.json     # Datos (se crea solo)
```

## 🧪 Comportamiento esperado

```
=== SISTEMA DE GESTIÓN DE USUARIOS ===
1. Crear usuario
2. Listar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
6. Exportar CSV
7. Salir
Elige: 1

Nombre: Ana García
Email: ana@email.com
Edad: 28
Rol: admin
✅ Usuario creado con ID: 1
```

## 🔗 Recursos

- [01-variables-tipos](../../01-fundamentos/01-variables-tipos.md) a [09-comentarios-docstrings](../../01-fundamentos/09-comentarios-docstrings.md)
- [ejercicios.md](../../01-fundamentos/ejercicios.md) — Repasa los ejercicios si tienes dudas
- [mini-proyectos](../../01-fundamentos/mini-proyectos/) — Las side quests te preparan

> ⚔️ **¿Estás listo?** Revisa tus HP en `../../rpg-system.md`. Si están ≥ 50, ¡enfrenta al Boss!
