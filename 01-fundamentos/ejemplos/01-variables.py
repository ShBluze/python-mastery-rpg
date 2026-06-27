"""Ejemplo: variables, tipos y casting."""

nombre = "Ana"
edad = 28
altura = 1.65
es_estudiante = True

print(f"Nombre: {nombre} ({type(nombre).__name__})")
print(f"Edad: {edad} ({type(edad).__name__})")
print(f"Altura: {altura} ({type(altura).__name__})")
print(f"Estudiante: {es_estudiante} ({type(es_estudiante).__name__})")

# Casting
edad_str = str(edad)
altura_int = int(altura)
print(f"\nCasting: str(edad) -> {edad_str!r}, int(altura) -> {altura_int}")
