# 🔍 Mini-Proyecto 02 — Scanner de Archivos

**Dificultad**: 🟡 Medio | **XP**: 100 | **Módulo**: 04-ecosistema

---

## 📖 Historia

El herrero de la forja tiene miles de archivos desorganizados. Necesitas construir un escáner que analice el sistema de archivos y genere reportes.

## 🎯 Requisitos funcionales

- [ ] Analizar un directorio recursivamente
- [ ] Por cada archivo: nombre, extensión, tamaño, fecha modificación
- [ ] Reporte CLI con: total archivos, por extensión, tamaño total, duplicados
- [ ] Encontrar archivos duplicados (por hash MD5)
- [ ] Buscar archivos por patrón (nombre, extensión, tamaño > N)
- [ ] Generar reporte en JSON y TXT
- [ ] Modo interactivo (menú) y modo comando (args CLI)

## 📋 Criterios de éxito

- Usa pathlib.Path.rglob()
- Cálculo de hash con hashlib
- logging para seguimiento
- Manejo de errores: permisos, archivos rotos, enlaces simbólicos
- Tests para funciones clave

## 🔗 Recursos

- [24-pathlib-os](../24-pathlib-os.md)
- [23-archivos-persistencia](../23-archivos-persistencia.md)
