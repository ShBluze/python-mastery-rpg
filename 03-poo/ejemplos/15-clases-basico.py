"""Ejemplo: clases y objetos básicos."""

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre}"

    def __repr__(self) -> str:
        return f"Persona({self.nombre!r}, {self.edad})"

    def __str__(self) -> str:
        return self.saludar()


class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, curso: str):
        super().__init__(nombre, edad)
        self.curso = curso

    def saludar(self) -> str:
        return f"{super().saludar()} y estudio {self.curso}"


if __name__ == "__main__":
    p = Persona("Ana", 25)
    e = Estudiante("Luis", 22, "Python")
    print(p)
    print(e)
    print(repr(p))
