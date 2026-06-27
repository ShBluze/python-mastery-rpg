# ⚔️ RPG System — Mundo del Juego

> Centro de comando: HP, bosses, dificultad dinámica y estado del mundo.

---

## 👤 Estado del Jugador

```
HP:   ████████████████████ 100/100  🟢 Saludable
Nivel:  1 — 🥚 Novato
XP:     0
Racha:  0 días
Modo:   NORMAL 🟡
```

---

## 🗺️ Mundo — Progreso por Regiones

| Región | Nivel req. | HP req. | Estado | Boss |
|--------|:----------:|:-------:|:------:|:----:|
| 🏘️ Aldea Básico | 1+ | — | 📘 Disponible | 🔒 |
| 🏰 Torre Avanzado | 3+ | ≥ 50 | 🔒 Bloqueado | 🔒 |
| 🏛️ Templo POO | 4+ | ≥ 60 | 🔒 Bloqueado | 🔒 |
| ⚙️ Forja Ecosistema | 5+ | ≥ 70 | 🔒 Bloqueado | 🔒 |
| 🗻 Especialización | 6+ | ≥ 80 | 🔒 Bloqueado | 🔒 |

---

## 💀 Sistema de Vida (HP)

### Eventos que afectan HP

| Evento | Cambio |
|--------|:------:|
| Ejercicio 🟢 first try | +5 HP |
| Ejercicio 🟡 first try | +3 HP |
| Ejercicio 🔴 first try | +2 HP |
| Error en ejercicio 🟢 | -5 HP |
| Error en ejercicio 🟡 | -10 HP |
| Error en ejercicio 🔴 | -15 HP |
| Error en Boss Fight | -20 HP |
| Pasar Boss Fight | +30 HP |
| Sin actividad 7 días | -10 HP |

### Umbrales de estado

| Rango HP | Estado | Efecto |
|:--------:|:------:|--------|
| 100-70 | 🟢 Saludable | Normal, dificultad estándar |
| 69-40 | 🟡 Precaución | Ejercicios de repaso recomendados |
| 39-10 | 🔴 Peligro | Boss bloqueado. Modo Review activado |
| 9-0 | 💀 Derrota | Repetir ejercicios básicos del módulo |

---

## ⚔️ Boss Fights

| Módulo | Boss | XP | HP req. | Estado |
|--------|:----:|:--:|:-------:|:------:|
| 01-fundamentos | 🧙‍♂️ Gestión de Usuarios | 150 | ≥ 50 | 🔒 |
| 02-avanzado | 🔮 Pipeline de Datos | 200 | ≥ 60 | 🔒 |
| 03-poo | 🐉 Batalla OOP | 250 | ≥ 60 | 🔒 |
| 04-ecosistema | 🤖 Paquete Python | 300 | ≥ 70 | 🔒 |
| Especialización | 👑 Proyecto Final | 500 | ≥ 80 | 🔒 |

### Historial de Bosses

| Boss | Intentos | HP perdido | XP ganado | Estado |
|:----:|:--------:|:----------:|:---------:|:------:|
| — | — | — | — | 🔒 |

---

## 🔄 Dificultad Dinámica

### Modos según rendimiento

| Modo | Condición | XP mult. | Efecto |
|:----:|-----------|:--------:|--------|
| 🟢 Review | HP < 40 o error rate > 40% | ×0.5 | Ejercicios con pistas, simplificados |
| 🟡 Normal | HP 40-70, error rate < 30% | ×1.0 | Estándar |
| 🔴 Hard | HP > 70, error rate < 10% | ×2.0 | Sin pistas, edge cases, más estrictos |

### Últimos ejercicios

| Ejercicio | Resultado | XP | HP cambio |
|:---------:|:---------:|:--:|:---------:|
| — | — | — | — |

**Error rate actual**: 0% | **Modo actual**: NORMAL 🟡

---

## 📊 Estadísticas globales

| Estadística | Valor |
|-------------|:-----:|
| Ejercicios completados | 0 |
| Bosses derrotados | 0 / 5 |
| Errores totales | 0 |
| First try completados | 0 |
| Tiempo estimado invertido | — |

---

> 💡 **Cómo usar**: Mantén este archivo actualizado como tu ficha de personaje. Refleja tu progreso real en el mundo de Python.
