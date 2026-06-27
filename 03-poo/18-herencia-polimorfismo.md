# 18 — Herencia y Polimorfismo

> Herencia simple/múltiple, `super()`, MRO, mixins, composición vs herencia, polimorfismo.

---

## Herencia Básica

```python
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def hablar(self) -> str:
        return "..."

class Perro(Animal):
    def hablar(self) -> str:
        return "Guau!"

class Gato(Animal):
    def hablar(self) -> str:
        return "Miau!"

perro = Perro("Rex")
gato = Gato("Michi")
print(perro.hablar())  # Guau!
print(gato.hablar())   # Miau!
```

---

## `super()` — Llamar a padre

```python
class Animal:
    def __init__(self, nombre: str, especie: str):
        self.nombre = nombre
        self.especie = especie

class Perro(Animal):
    def __init__(self, nombre: str, raza: str):
        super().__init__(nombre, "Canis lupus")  # Llama a Animal.__init__
        self.raza = raza

rex = Perro("Rex", "Labrador")
print(rex.nombre)   # Rex
print(rex.especie)  # Canis lupus
print(rex.raza)     # Labrador
```

### `super()` en métodos

```python
class Base:
    def saludar(self):
        return "Hola desde Base"

class Derivada(Base):
    def saludar(self):
        return super().saludar() + " -> Derivada"

print(Derivada().saludar())  # Hola desde Base -> Derivada
```

---

## Herencia Múltiple

```python
class Volador:
    def volar(self):
        return "Volando"

class Nadador:
    def nadar(self):
        return "Nadando"

class Pato(Volador, Nadador):
    pass

p = Pato()
print(p.volar())  # Volando
print(p.nadar())  # Nadando
```

### Orden de resolución (MRO)

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

**Regla C3 (Python):**
1. Hijo antes que padres
2. Padres en orden de declaración
3. Mantener orden relativo de abuelos

```python
# Diamond problem resuelto
class Base: pass
class Izq(Base): pass
class Der(Base): pass
class Hijo(Izq, Der): pass

# MRO: Hijo -> Izq -> Der -> Base -> object
```

---

## Mixins — Comportamiento reutilizable

Clases pequeñas que añaden funcionalidad, no estado principal.

```python
class SerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, data):
        import json
        obj = cls.__new__(cls)
        obj.__dict__ = json.loads(data)
        return obj

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.creado = datetime.now()

class Usuario(TimestampMixin, SerializableMixin):
    def __init__(self, nombre: str, email: str):
        super().__init__()
        self.nombre = nombre
        self.email = email

u = Usuario("Ana", "ana@mail.com")
print(u.creado)           # TimestampMixin
print(u.to_json())        # SerializableMixin
```

### Convención Mixin
- Nombre termina en `Mixin`
- No instanciar directamente
- `super().__init__()` obligatorio para cadena de inicialización

---

## Polimorfismo

**Mismo interfaz, comportamiento diferente.**

```python
def hacer_hablar(animal: Animal) -> None:
    print(animal.hablar())

hacer_hablar(Perro("Rex"))  # Guau!
hacer_hablar(Gato("Michi")) # Miau!
hacer_hablar(Animal("Genérico"))  # ...
```

### Duck Typing (Tipado pato)

> "Si camina como pato y grazna como pato, es un pato."

```python
# No necesita herencia común
class Perro:
    def hablar(self): return "Guau"

class Robot:
    def hablar(self): return "Beep boop"

def saludar(objeto):
    print(objeto.hablar())

saludar(Perro())   # Guau
saludar(Robot())   # Beep boop
```

---

## Composición vs Herencia

| Herencia | Composición |
|----------|-------------|
| "Es un" (`Perro es Animal`) | "Tiene un" (`Coche tiene Motor`) |
| Acoplamiento fuerte | Acoplamiento débil |
| Difícil cambiar en runtime | Fácil cambiar componentes |
| Jerarquía rígida | Flexible |

```python
# ❌ Herencia forzada
class CocheElectrico(Coche, Electrico): ...

# ✅ Composición
class Motor:
    def arrancar(self): ...

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor
    
    def arrancar(self):
        self.motor.arrancar()

coche = Coche(MotorElectrico())
coche = Coche(MotorCombustion())  # Cambio en runtime
```

> 💡 **Preferir composición** salvo que la relación "es un" sea verdadera y estable.

---

## Abstract Base Classes (ABC) — Contratos

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        pass
    
    def describir(self) -> str:  # Método concreto
        return f"Área: {self.area():.2f}"

class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio
    
    def area(self) -> float:
        return 3.14159 * self.radio ** 2
    
    def perimetro(self) -> float:
        return 2 * 3.14159 * self.radio

# f = Figura()  # TypeError: Can't instantiate abstract class
c = Circulo(5)
print(c.describir())  # Área: 78.54
```

### `@abstractmethod` + `@property`

```python
class Base(ABC):
    @property
    @abstractmethod
    def nombre(self) -> str:
        pass

class Hija(Base):
    @property
    def nombre(self) -> str:
        return "Concreto"
```

---

## Protocolos (Structural Subtyping — Python 3.8+)

Alternative a ABC sin herencia.

```python
from typing import Protocol

class Volador(Protocol):
    def volar(self) -> None: ...

class Aguila:
    def volar(self) -> None:
        print("Volando alto")

class Drone:
    def volar(self) -> None:
        print("Zumbando")

def hacer_volar(v: Volador) -> None:
    v.volar()

hacer_volar(Aguila())  # ✅ Cumple protocolo
hacer_volar(Drone())   # ✅ Cumple protocolo
```

| ABC | Protocol |
|-----|----------|
| Nominal (herencia) | Estructural (duck typing) |
| `isinstance(x, ABC)` funciona | `isinstance(x, Protocol)` **no** (3.11+ sí con `@runtime_checkable`) |
| Requiere modificar clase | Cero intrusión |

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Serializable(Protocol):
    def to_json(self) -> str: ...

class MiClase:
    def to_json(self) -> str: return "{}"

print(isinstance(MiClase(), Serializable))  # True (3.11+)
```

---

## Sobrescritura vs Sobrecarga

| Concepto | Python |
|----------|--------|
| **Sobrescritura** (override) | ✅ Redefinir método en hija |
| **Sobrecarga** (overload) | ❌ No nativo (usa `@singledispatch` o args opcionales) |

```python
# Sobrescritura
class Base:
    def metodo(self): return "Base"

class Hija(Base):
    def metodo(self): return "Hija"  # Override

# Sobrecarga simulada
from functools import singledispatchmethod

class Procesador:
    @singledispatchmethod
    def procesar(self, dato):
        raise NotImplementedError
    
    @procesar.register
    def _(self, dato: int): return dato * 2
    
    @procesar.register
    def _(self, dato: str): return dato.upper()
```

---

## Patrones con Herencia

### Template Method

```python
from abc import ABC, abstractmethod

class ProcesadorDatos(ABC):
    def procesar(self, datos):
        validados = self.validar(datos)
        transformados = self.transformar(validados)
        return self.guardar(transformados)
    
    @abstractmethod
    def validar(self, datos): pass
    
    @abstractmethod
    def transformar(self, datos): pass
    
    def guardar(self, datos):
        print("Guardado genérico")
        return datos

class ProcesadorCSV(ProcesadorDatos):
    def validar(self, datos): return datos.strip()
    def transformar(self, datos): return datos.split(",")

class ProcesadorJSON(ProcesadorDatos):
    def validar(self, datos): return datos
    def transformar(self, datos): return eval(datos)  # demo
```

### Strategy (via composición)

```python
from abc import ABC, abstractmethod

class EstrategiaOrdenacion(ABC):
    @abstractmethod
    def ordenar(self, lista): pass

class Burbuja(EstrategiaOrdenacion):
    def ordenar(self, lista): return sorted(lista)  # demo

class Rapida(EstrategiaOrdenacion):
    def ordenar(self, lista): return sorted(lista, reverse=True)

class Contexto:
    def __init__(self, estrategia: EstrategiaOrdenacion):
        self.estrategia = estrategia
    
    def ejecutar(self, datos):
        return self.estrategia.ordenar(datos)

ctx = Contexto(Burbuja())
ctx.ejecutar([3, 1, 2])  # [1, 2, 3]
ctx.estrategia = Rapida()
ctx.ejecutar([3, 1, 2])  # [3, 2, 1]
```

---

## Resumen: Cuándo usar qué

| Escenario | Técnica |
|-----------|---------|
| "Es un" real, estable | Herencia simple |
| Compartir comportamiento transversal | Mixins |
| Contrato obligatorio | ABC |
| Duck typing sin tocar clases | Protocol |
| Cambiar comportamiento en runtime | Composición + Strategy |
| Algoritmo base con pasos variables | Template Method |

---

---
## 🎯 Ejercicios

Practica herencia en [ejercicios.md](../03-poo/ejercicios.md#18--herencia-y-polimorfismo).

**Mini-ejercicio**: Clase base `Vehiculo` con método `mover()`. Subclases `Coche` (rueda) y `Barco` (flota). Polimorfismo en acción.

---

## Véase también

- [15-clases-objetos](./15-clases-objetos.md) — `super()`, `__init__`
- [16-tipos-metodos](./16-tipos-metodos.md) — `@classmethod` para factories
- [17-metodos-magicos](./17-metodos-magicos.md) — `__init_subclass__`
- [20-clases-abstractas](./20-clases-abstractas.md) — ABC en profundidad
- [22-patrones-diseno](./22-patrones-diseno.md) — Strategy, Template Method, etc.
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada