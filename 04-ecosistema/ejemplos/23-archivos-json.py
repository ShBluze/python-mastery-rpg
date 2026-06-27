"""Ejemplo: persistencia con JSON."""

import json
from pathlib import Path

ARCHIVO = Path("datos.json")


def guardar(notas: list[dict]) -> None:
    with ARCHIVO.open("w", encoding="utf-8") as f:
        json.dump(notas, f, indent=2, ensure_ascii=False)


def cargar() -> list[dict]:
    if not ARCHIVO.exists():
        return []
    with ARCHIVO.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    notas = cargar()
    notas.append({"titulo": input("Título: "), "contenido": input("Contenido: ")})
    guardar(notas)
    print(f"\nNotas guardadas ({len(notas)} total):")
    for n in notas:
        print(f"  - {n['titulo']}: {n['contenido'][:30]}...")


if __name__ == "__main__":
    main()
