# 📓 Mini-Proyecto 01 — Gestor de Notas con Persistencia

**Dificultad**: 🟡 Medio | **XP**: 100 | **Módulo**: 04-ecosistema

---

## 📖 Historia

El archivero de la forja necesita un sistema de notas que persista entre sesiones. Las notas deben guardarse en JSON y soportar etiquetas.

## 🎯 Requisitos funcionales

- [ ] CRUD completo de notas (crear, leer, actualizar, eliminar)
- [ ] Persistencia en `notas.json`
- [ ] Cada nota: id, título, contenido, fecha creación, fecha modificación, etiquetas
- [ ] Búsqueda por título, contenido o etiqueta
- [ ] Filtrar notas por etiqueta
- [ ] Exportar notas a CSV
- [ ] Backup automático al modificar (notas_backup.json)

## 📋 Criterios de éxito

- Manejo de errores: archivo corrupto, directorio no existe
- pathlib para rutas (no os.path)
- Serialización/deserialización correcta de fechas
- Logger que registra cada operación
- Tests con pytest (al menos 5 tests)

## 🔗 Recursos

- [23-archivos-persistencia](../23-archivos-persistencia.md)
- [24-pathlib-os](../24-pathlib-os.md)
- [27-logging-debugging](../27-logging-debugging.md)
