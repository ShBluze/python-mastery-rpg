# 🎲 Mini-Proyecto 02 — Juego de Adivinanza

**Dificultad**: 🟢 Fácil | **XP**: 80 | **Módulo**: 01-fundamentos

---

## 📖 Historia

El mago del pueblo ha escondido un número secreto entre el 1 y el 100. Tu misión es crear un juego donde el usuario intente adivinarlo con pistas.

## 🎯 Requisitos funcionales

- [ ] Número secreto aleatorio entre 1 y 100
- [ ] El usuario ingresa su intento
- [ ] Pistas: "mayor" o "menor"
- [ ] Contador de intentos
- [ ] Dificultad seleccionable: fácil (10 intentos), medio (7), difícil (5)
- [ ] Al ganar: mensaje con número de intentos
- [ ] Al perder: revela el número secreto
- [ ] Opción de jugar otra vez

## 📋 Criterios de éxito

- Usa random.randint()
- Bucle principal claro (while)
- Maneja entradas no numéricas
- Puntuación: menos intentos = mejor mensaje

## 🧪 Flujo esperado

```
=== ADIVINA EL NÚMERO ===
Dificultad (fácil/medio/difícil): medio
Tienes 7 intentos.
Intento 1: 50
⬇️ Menor
Intento 2: 25
⬆️ Mayor
Intento 3: 37
⬆️ Mayor
Intento 4: 43
⬇️ Menor
Intento 5: 40
⬆️ Mayor
Intento 6: 41
⬆️ Mayor
Intento 7: 42
🎉 ¡Correcto! Lo adivinaste en 7 intentos.
```

## 🔗 Recursos

- [02-control-flujo](../02-control-flujo.md)
- [07-manejo-errores](../07-manejo-errores.md)
