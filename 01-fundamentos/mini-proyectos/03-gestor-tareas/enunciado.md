# 📋 Mini-Proyecto 03 — Gestor de Tareas (CLI)

**Dificultad**: 🟡 Medio | **XP**: 120 | **Módulo**: 01-fundamentos

---

## 📖 Historia

Necesitas organizar tus misiones. Construye un gestor de tareas desde terminal que permita crear, listar, completar y eliminar tareas.

## 🎯 Requisitos funcionales

- [ ] Agregar tarea (con título, descripción opcional, fecha límite opcional)
- [ ] Listar tareas (todas, pendientes, completadas, vencidas)
- [ ] Completar tarea (marcar como hecha)
- [ ] Eliminar tarea
- [ ] Buscar tareas por texto
- [ ] Las tareas tienen: id, título, descripción, fecha creación, fecha límite, estado
- [ ] Prioridad: alta/ media/ baja
- [ ] Mostrar estadísticas: total, pendientes, completadas

## 📋 Criterios de éxito

- Usa diccionarios para representar tareas
- Lista de tareas en memoria (lista de dicts)
- IDs auto-incrementales
- Fechas con datetime (módulo estándar)
- Validación de entrada en todas las opciones
- Al menos 5 funciones modulares

## 💡 Pistas

- Usa `from datetime import datetime` para fechas
- Los IDs pueden ser un contador simple
- Para filtrar: `[t for t in tareas if t["estado"] == "pendiente"]`

## 🔗 Recursos

- [04-estructuras-datos](../04-estructuras-datos.md)
- [06-strings-formateo](../06-strings-formateo.md)
- [08-modulos-imports](../08-modulos-imports.md)
