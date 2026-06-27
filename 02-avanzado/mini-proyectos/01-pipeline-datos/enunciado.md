# 🔄 Mini-Proyecto 01 — Pipeline de Transformación de Datos

**Dificultad**: 🟡 Medio | **XP**: 100 | **Módulo**: 02-avanzado

---

## 📖 Historia

Como analista de datos de la torre, recibes datos crudos y necesitas transformarlos con un pipeline funcional. Usa composición de funciones, no bucles imperativos.

## 🎯 Requisitos funcionales

- [ ] Función `cargar_datos()` que genera lista de dicts con nombres, edades, emails (datos fake)
- [ ] Pipeline `limpiar()` que elimina nulos y espacios
- [ ] Pipeline `filtrar()` que filtra por condición (ej: edad > 18)
- [ ] Pipeline `transformar()` que aplica map (ej: email a minúsculas)
- [ ] Pipeline `ordenar()` por campo específico
- [ ] Pipeline `resumir()` que genera estadísticas básicas
- [ ] Decorador `@timer` que mide cada etapa
- [ ] Decorador `@log` que registra cuántos registros entran/salen

## 📋 Criterios de éxito

- Cada etapa es una función pura (no modifica input)
- El pipeline se compone con functools.reduce o composición manual
- Los decoradores no modifican el comportamiento de las etapas
- Tipado completo con type hints

## 🔗 Recursos

- [10-type-hints](../10-type-hints.md)
- [11-funciones-avanzadas](../11-funciones-avanzadas.md)
- [12-programacion-funcional](../12-programacion-funcional.md)
