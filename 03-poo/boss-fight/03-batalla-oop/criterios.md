# ✅ Criterios de Aprobación — Boss: Batalla OOP

---

## Obligatorios

- [ ] ABC `Personaje` con @abstractmethod (atacar, recibir_daño, esta_vivo)
- [ ] 4 subclases de personaje con comportamientos distintos
- [ ] 3 tipos de enemigos con AI básica
- [ ] Sistema de turnos funcional (jugador elige acción, CPU responde)
- [ ] Dataclass `Estadisticas` con validación de tipos
- [ ] __str__ muestra info del personaje, __repr__ muestra datos completos
- [ ] Property `hp` con validación (no < 0, no > max_hp)
- [ ] Patrón Strategy con mínimo 3 estrategias de habilidad
- [ ] Excepción `PersonajeDerrotadoError` con mensaje claro
- [ ] Herencia bien aplicada (al menos 2 niveles de profundidad)
- [ ] Composición (personaje tiene habilidades, no hereda de ellas)
- [ ] Tests con pytest (mínimo 8 tests)

## Bonus

- [ ] Observer pattern para eventos de combate
- [ ] Guardar/cargar partida en JSON
- [ ] Sistema de niveles: al vencer enemigos, el personaje sube de nivel

---

## Resultado

- **Obligatorios**: _/12
- **Bonus**: _/3
- **¿Pasa?**: ❌ No / ✅ Sí
