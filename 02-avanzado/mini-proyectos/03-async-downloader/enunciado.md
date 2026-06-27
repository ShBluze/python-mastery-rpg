# ⚡ Mini-Proyecto 03 — Descargador Async

**Dificultad**: 🔴 Difícil | **XP**: 150 | **Módulo**: 02-avanzado

---

## 📖 Historia

Necesitas recolectar datos de múltiples torres de conocimiento (URLs). Hazlo en paralelo para ser eficiente, como un verdadero mago del tiempo.

## 🎯 Requisitos funcionales

- [ ] Leer lista de URLs desde un archivo `urls.txt`
- [ ] Descargar cada URL en paralelo usando asyncio + aiohttp
- [ ] Mostrar barra de progreso (porcentaje completado)
- [ ] Guardar cada respuesta en `downloads/{nombre}.html`
- [ ] Mostrar estadísticas: URLs totales, exitosas, fallidas, tiempo total
- [ ] Timeout configurable por URL (10s por defecto)
- [ ] Reintentar URLs fallidas (máx 2 intentos)
- [ ] Modo verbose para ver progreso detallado

## 📋 Criterios de éxito

- Usa asyncio + aiohttp (no requests síncrono)
- El tiempo total debe ser ~el máximo individual (no suma)
- Maneja errores de red, timeouts, URLs inválidas
- CLI con argparse para opciones

## 🔗 Recursos

- [13-async-concurrencia](../13-async-concurrencia.md)
- [14-context-managers](../14-context-managers.md)
