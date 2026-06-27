"""Ejemplo: control de flujo."""

import random

numero_secreto = random.randint(1, 10)
intentos = 3

print("Adivina el número (1-10):")
for i in range(intentos):
    try:
        guess = int(input(f"Intento {i + 1}: "))
    except ValueError:
        print("Entrada inválida. Usa números.")
        continue

    if guess == numero_secreto:
        print(f"¡Correcto! Era {numero_secreto}")
        break
    elif guess < numero_secreto:
        print("Mayor")
    else:
        print("Menor")
else:
    print(f"Agotaste intentos. Era {numero_secreto}")

# List comprehension
pares = [x for x in range(20) if x % 2 == 0]
print(f"\nPares hasta 20: {pares}")
