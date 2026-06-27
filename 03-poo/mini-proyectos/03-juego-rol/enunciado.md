# ⚔️ Mini-Proyecto 03 — Juego de Rol (RPG)

**Dificultad**: 🔴 Difícil | **XP**: 150 | **Módulo**: 03-poo

---

## 📖 Historia

Diseña el sistema de combate de un RPG por turnos. Usa todo lo aprendido en POO: clases, herencia, composición, patrones.

## 🎯 Requisitos funcionales

- [ ] Clase base `Personaje` con nombre, hp, ataque, defensa, nivel
- [ ] Subclases: `Guerrero` (espada, escudo), `Mago` (hechizos, mana), `Arquero` (crítico, distancia)
- [ ] Sistema de combate por turnos (jugador vs enemigo)
- [ ] Enemigos: `Goblin`, `Esqueleto`, `JefeFinal` (cada uno con comportamiento único)
- [ ] Patrón Strategy para `Habilidad`: AtaqueNormal, HechizoFuego, Curacion, FlechaPenetrante
- [ ] Patrón Observer para eventos: "Golpe crítico", "Muerte", "Subida de nivel"
- [ ] Dataclasses para: `Estadisticas`, `Item`, `Mision`
- [ ] Property para validar hp (nunca < 0, nunca > max_hp)

## 📋 Criterios de éxito

- Al menos 4 patrones de diseño implementados
- Herencia + composición combinados
- Métodos mágicos para representación (__str__, __repr__)
- Excepción personalizada `PersonajeDerrotadoError`

## 🔗 Recursos

- [15-clases-objetos](../15-clases-objetos.md) → [22-patrones-diseno](../22-patrones-diseno.md)
