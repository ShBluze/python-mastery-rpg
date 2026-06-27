"""Ejemplo: type hints."""

from typing import Optional


def saludar(nombre: str, edad: Optional[int] = None) -> str:
    """Saluda a una persona, opcionalmente con edad."""
    base = f"Hola {nombre}"
    if edad is not None:
        return f"{base}, tienes {edad} años"
    return base


def sumar_lista(numeros: list[int | float]) -> float:
    """Suma una lista de números."""
    return sum(numeros)


if __name__ == "__main__":
    print(saludar("Ana"))
    print(saludar("Luis", 30))
    print(f"Suma: {sumar_lista([1, 2, 3, 4.5])}")
