# ⚔️ BOSS FIGHT — Pipeline de Datos

> 🔮 **El Guardián de la Torre** te reta a construir un pipeline de transformación de datos profesional.

**Módulo**: 02-avanzado | **XP**: 200 | **HP mínimo**: 60 | **Dificultad**: 🟡 Intermedio

---

## 📖 Historia

La Torre del Conocimiento recibe datos caóticos de múltiples fuentes. Necesitas construir un pipeline funcional que los limpie, transforme y analice usando type hints, decoradores, programación funcional y context managers.

## 🎯 Requisitos del Boss

### Obligatorios
- [ ] Pipeline funcional componible (cada etapa es una función pura)
- [ ] Type hints en todas las funciones
- [ ] Decorador `@etapa(nombre)` que registre entrada/salida de cada etapa
- [ ] Context manager `PipelineTimer` que mida tiempo total del pipeline
- [ ] Al menos 3 etapas: `cargar`, `limpiar`, `transformar`, `analizar`, `exportar`
- [ ] Etapa `cargar`: lee CSV con datos sucios (nulos, formatos incorrectos)
- [ ] Etapa `limpiar`: elimina nulos, normaliza formatos, lanza errores claros
- [ ] Etapa `transformar`: usa map/filter/reduce o comprehensions
- [ ] Etapa `analizar`: usa itertools.groupby para agrupar datos
- [ ] Etapa `exportar`: guarda JSON limpio + CSV de resultados
- [ ] Mypy pasa sin errores (strict mode)

### Bonus
- [ ] async para carga paralela de múltiples archivos
- [ ] Modo verbose con logging configurable
- [ ] Generar gráfico simple con matplotlib (opcional)

## 📋 Estructura sugerida

```
pipeline-datos/
├── main.py
├── pipeline.py       # Composición del pipeline
├── etapas/
│   ├── __init__.py
│   ├── carga.py
│   ├── limpieza.py
│   ├── transformacion.py
│   ├── analisis.py
│   └── exportacion.py
├── decorators.py     # @etapa, @timer
├── context_managers.py  # PipelineTimer
├── datos_entrada.csv
└── pyproject.toml    # ruff + mypy config
```

## 🔗 Recursos

- [10-type-hints](../../02-avanzado/10-type-hints.md)
- [11-funciones-avanzadas](../../02-avanzado/11-funciones-avanzadas.md)
- [12-programacion-funcional](../../02-avanzado/12-programacion-funcional.md)
- [14-context-managers](../../02-avanzado/14-context-managers.md)
