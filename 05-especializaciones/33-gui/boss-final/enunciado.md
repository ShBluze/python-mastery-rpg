# 👑 Boss Final — Aplicación de Escritorio

**Ruta**: 🖥️ GUI | **XP**: 500 | **HP mínimo**: 80

---

## 📖 Historia

Eres el artesano de interfaces del reino. Construye una aplicación de escritorio completa usando PySide6 (o Tkinter si prefieres nativo). Una app de gestión de proyectos con tareas, tiempos y reportes.

## 🎯 Requisitos obligatorios

- [ ] Ventana principal con menús (Archivo, Editar, Ayuda)
- [ ] CRUD de proyectos (nombre, descripción, fecha inicio, fecha fin)
- [ ] CRUD de tareas dentro de cada proyecto
- [ ] Temporizador Pomodoro o seguimiento de tiempo
- [ ] Barra de progreso del proyecto
- [ ] Persistencia de datos (JSON o SQLite)
- [ ] Diálogos: acerca de, confirmación al eliminar, error
- [ ] Atajos de teclado
- [ ] Tests de la lógica (no UI) con pytest
- [ ] README con capturas de pantalla

## 📋 Criterios de éxito

- La app se abre y funciona sin errores
- Los datos persisten entre sesiones
- Interfaz responsive (se redimensiona bien)
- Código separado: UI / lógica / datos

## 📦 Stack

- PySide6 (recomendado) o Tkinter
- SQLite (sqlite3)
- datetime, pathlib
- pytest (tests de lógica)
