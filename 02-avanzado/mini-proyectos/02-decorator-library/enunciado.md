# 🎨 Mini-Proyecto 02 — Librería de Decoradores

**Dificultad**: 🔴 Difícil | **XP**: 120 | **Módulo**: 02-avanzado

---

## 📖 Historia

Los magos de la torre necesitan una biblioteca de hechizos (decoradores) reutilizables para potenciar sus funciones. Crea una librería modular de decoradores.

## 🎯 Requisitos funcionales

- [ ] `@timer` — muestra tiempo de ejecución
- [ ] `@log_calls` — registra cada llamada (args, resultado)
- [ ] `@retry(max_attempts=3, delay=1)` — reintenta si falla
- [ ] `@memoize` — cachea resultados (como lru_cache)
- [ ] `@validate_types` — valida tipos en runtime
- [ ] `@deprecated(message)` — muestra warning si se usa
- [ ] `@rate_limit(seconds=1)` — no ejecuta más de una vez cada N segundos

## 📋 Criterios de éxito

- Todos usan functools.wraps
- Aceptan argumentos donde corresponda (@retry(5) y @retry)
- Se pueden apilar múltiples decoradores
- Documentación completa (docstring por decorador)
- Tests que verifican cada decorador

## 🔗 Recursos

- [11-funciones-avanzadas](../11-funciones-avanzadas.md)
- [14-context-managers](../14-context-managers.md)
