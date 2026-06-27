# ⚔️ BOSS FIGHT — Batalla OOP

> 🐉 **El Dragón del Templo** te reta a diseñar un sistema de combate por turnos completo.

**Módulo**: 03-poo | **XP**: 250 | **HP mínimo**: 60 | **Dificultad**: 🟡 Intermedio

---

## 📖 Historia

El Dragón del Templo de la POO ha despertado. Solo un diseño OOP impecable podrá derrotarlo. Debes construir un sistema de batalla por turnos usando clases, herencia, composición, métodos mágicos y patrones de diseño.

## 🎯 Requisitos del Boss

### Obligatorios
- [ ] Clase abstracta `Personaje` con atributos y métodos abstractos
- [ ] Subclases: `Guerrero`, `Mago`, `Arquero`, `Paladin` (cada uno con habilidades únicas)
- [ ] Clase `Enemigo` con comportamientos: `Goblin`, `Esqueleto`, `Dragón` (Boss final)
- [ ] Sistema de combate por turnos (jugador vs CPU)
- [ ] Dataclass `Estadisticas` con hp, ataque, defensa, velocidad, nivel
- [ ] Métodos mágicos: __str__, __repr__, __eq__ en Personaje
- [ ] Property con validación (hp entre 0 y max_hp)
- [ ] Patrón Strategy para habilidades intercambiables
- [ ] Excepción personalizada `PersonajeDerrotadoError`
- [ ] Herencia + composición combinados
- [ ] 3+ habilidades diferentes por personaje

### Bonus
- [ ] Patrón Observer para eventos (golpe crítico, muerte, curación)
- [ ] Persistencia de partida (JSON)
- [ ] Sistema de niveles y experiencia

## 📋 Estructura sugerida

```
batalla-oop/
├── main.py
├── personajes/
│   ├── __init__.py
│   ├── base.py           # ABC Personaje
│   ├── guerrero.py
│   ├── mago.py
│   ├── arquero.py
│   └── paladin.py
├── enemigos/
│   ├── __init__.py
│   └── enemigos.py       # Goblin, Esqueleto, Dragon
├── combate/
│   ├── __init__.py
│   └── sistema.py        # Turnos, lógica de batalla
├── habilidades/
│   ├── __init__.py
│   └── estrategias.py    # Strategy pattern
├── modelos.py             # Dataclasses
└── tests/
    └── test_batalla.py
```

## 🔗 Recursos

- [15-clases-objetos](../../03-poo/15-clases-objetos.md) → [22-patrones-diseno](../../03-poo/22-patrones-diseno.md)
