# ✅ Criterios de Aprobación — Boss: Pipeline de Datos

---

## Obligatorios

- [ ] Pipeline componible (las etapas se conectan sin efectos secundarios)
- [ ] Type hints en todas las funciones y métodos
- [ ] Decorador `@etapa` que imprime nombre, tiempo, tamaño entrada/salida
- [ ] Context manager `PipelineTimer` que muestra tiempo total
- [ ] Mínimo 5 etapas funcionales
- [ ] Etapa `cargar` lee CSV con manejo de errores
- [ ] Etapa `limpiar` trata nulos y normaliza
- [ ] Etapa `transformar` usa map/filter/reduce o comprehensions
- [ ] Etapa `analizar` usa itertools.groupby
- [ ] Etapa `exportar` genera JSON + CSV válidos
- [ ] mypy --strict pasa sin errores
- [ ] ruff pasa sin errores
- [ ] Docstrings en todas las funciones públicas

## Bonus

- [ ] Carga paralela con asyncio
- [ ] logging configurable (DEBUG/INFO)
- [ ] Gráfico de resultados

---

## Resultado

- **Obligatorios**: _/13
- **Bonus**: _/3
- **¿Pasa?**: ❌ No / ✅ Sí
