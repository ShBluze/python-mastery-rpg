# 20 — Clases Abstractas e Interfaces

> `abc.ABC`, `@abstractmethod`, `@abstractproperty`, Protocol, interfaces implícitas.

---

## ¿Por qué clases abstractas?

Definen **contratos** que las subclases **deben cumplir**. Evitan instanciación incompleta.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self) -> str:
        pass
    
    @abstractmethod
    def mover(self) -> None:
        pass

# a = Animal()  # TypeError: Can't instantiate abstract class

class Perro(Animal):
    def hablar(self) -> str:
        return "Guau"
    
    def mover(self) -> None:
        print("Corriendo")

p = Perro()  # ✅ OK: implementa todos los abstractos
```

---

## `ABC` y `@abstractmethod`

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        pass
    
    # Método concreto (heredado tal cual)
    def describir(self) -> str:
        return f"Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}"

class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio
    
    def area(self) -> float:
        return 3.14159 * self.radio ** 2
    
    def perimetro(self) -> float:
        return 2 * 3.14159 * self.radio

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

figuras = [Circulo(5), Rectangulo(3, 4)]
for f in figuras:
    print(f.describir())
# Área: 78.54, Perímetro: 31.42
# Área: 12.00, Perímetro: 14.00
```

---

## `@abstractmethod` en propiedades

```python
from abc import ABC, abstractmethod

class Configuracion(ABC):
    @property
    @abstractmethod
    def version(self) -> str:
        pass
    
    @property
    @abstractmethod
    def debug(self) -> bool:
        pass

class ProdConfig(Configuracion):
    @property
    def version(self) -> str:
        return "1.0.0"
    
    @property
    def debug(self) -> bool:
        return False
```

---

## `@classmethod` / `@staticmethod` abstractos

```python
from abc import ABC, abstractmethod

class Factory(ABC):
    @classmethod
    @abstractmethod
    def crear(cls, **kwargs) -> "Producto":
        pass
    
    @staticmethod
    @abstractmethod
    def validar(datos: dict) -> bool:
        pass
```

---

## `ABCMeta` — Metaclase personalizada

```python
from abc import ABCMeta

class MiABCMeta(ABCMeta):
    def __instancecheck__(cls, instancia):
        # Lógica personalizada para isinstance()
        return hasattr(instancia, "metodo_requerido")

class MiABC(metaclass=MiABCMeta):
    pass
```

---

## `__subclasshook__` — Subclase virtual

Registra clases como subclases **sin herencia**.

```python
from abc import ABC

class Serializable(ABC):
    @classmethod
    def __subclasshook__(cls, subclase):
        if cls is Serializable:
            # Verifica protocolo estructural
            if hasattr(subclase, "to_json") and callable(subclase.to_json):
                return True
        return NotImplemented

class MiClase:
    def to_json(self): return "{}"

print(issubclass(MiClase, Serializable))  # True
print(isinstance(MiClase(), Serializable))  # True
```

---

## Protocolos (Structural Typing) — Python 3.8+

Alternative a ABC **sin herencia**. Duck typing tipado.

```python
from typing import Protocol

class Volador(Protocol):
    def volar):
    def volar(self) -> None: ...

class Aguila:
    def volar(self) -> None:
        print("Volando alto")

class Drone:
    def volar(self) -> None:
        print("Zumbando")

def hacer_volar(v: Volador) -> None:
    v.volar()

hacer_volar(Aguila())  # ✅
hacer_volar(Drone())   # ✅ (no hereda de Volador)
```

### `@runtime_checkable` — `isinstance` en runtime (3.11+)

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Serializable(Protocol):
    def to_json(self) -> str: ...

class Usuario:
    def to_json(self) -> str: return '{"nombre": "Ana"}'

u = Usuario()
print(isinstance(u, Serializable))  # True (3.11+)
```

---

## ABC vs Protocol

| Característica | `ABC` | `Protocol` |
|----------------|-------|------------|
| **Tipo** | Nominal (herencia) | Estructural (duck typing) |
| `isinstance(x, ABC)` | ✅ Funciona | ❌ No (salvo `@runtime_checkable`) |
| `issubclass(X, ABC)` | ✅ Funciona | ❌ No |
| Requiere modificar clase | Sí (`class X(ABC)`) | No (cero intrusión) |
| Múltiples implementaciones | Herencia simple | Composición implícita |
| Uso típico | Framework internos | APIs públicas, plugins |

---

## Casos de uso típicos

### 1. Plugin System (Protocol)

```python
from typing import Protocol

class Procesador(Protocol):
    def procesar(self, datos: str) -> str: ...

class ProcesadorMayusculas:
    def procesar(self, datos: str) -> str:
        return datos.upper()

class ProcesadorMinusculas:
    def procesar(self, datos: str) -> str:
        return datos.lower()

def pipeline(procesador: Procesador, datos: str):
    return procesador.procesar(datos)

pipeline(ProcesadorMayusculas(), "Hola")  # HOLA
pipeline(ProcesadorMinusculas(), "Hola")  # hola
```

### 2. Framework Base (ABC)

```python
from abc import ABC, abstractmethod

class ControladorBase(ABC):
    def __init__(self):
        self.inicializar()
    
    @abstractmethod
    def inicializar(self) -> None:
        pass
    
    @abstractmethod
    def manejar_peticion(self, request) -> Response:
        pass
    
    def log(self, msg: str) -> None:
        print(f"[LOG] {msg}")

class ControladorUsuario(ControladorBase):
    def inicializar(self):
        self.log("Inicializando ControladorUsuario")
    
    def manejar_peticion(self, request):
        return Response("OK")
```

### 3. Validación de Config (ABC + hook)

```python
from abc import ABC, abstractmethod

class Validador(ABC):
    @abstractmethod
    def validar(self, config: dict) -> bool:
        pass
    
    @classmethod
    def __subclasshook__(cls, sub):
        if cls is Validador:
            return hasattr(sub, "validar") and callable(sub.validar)
        return NotImplemented

# Cualquier clase con método validar(dict) -> bool es Validador
```

---

## Patrones Comunes

### Interface Segregation (múltiples ABCs pequeños)

```python
# ❌ Un ABC gordo
class Animal(ABC):
    @abstractmethod def volar(self): ...
    @abstractmethod def nadar(self): ...
    @abstractmethod def correr(self): ...

# ✅ Interfaces segregadas
class Volador(ABC):
    @abstractmethod def volar(self): ...

class Nadador(ABC):
    @abstractmethod def nadar(self): ...

class Corredor(ABC):
    @abstractmethod def correr(self): ...

class Pato(Volador, Nadador, Corredor):
    def volar(self): ...
    def nadar(self): ...
    def correr(self): ...
```

### Template Method (ABC con método concreto)

```python
from abc import ABC, abstractmethod

class ProcesadorArchivo(ABC):
    def procesar(self, ruta: str) -> str:
        contenido = self.leer(ruta)
        validado = self.validar(contenido)
        transformado = self.transformar(validado)
        return self.guardar(transformado)
    
    def leer(self, ruta: str) -> str:
        with open(ruta) as f:
            return f.read()
    
    @abstractmethod
    def validar(self, contenido: str) -> str: ...
    
    @abstractmethod
    def transformar(self, contenido: str) -> str: ...
    
    def guardar(self, contenido: str) -> str:
        return contenido  # Default

class ProcesadorCSV(ProcesadorArchivo):
    def validar(self, c): return c.strip()
    def transformar(self, c): return c.split(",")
```

---

## Resumen: Cuándo usar qué

| Escenario | Herramienta |
|-----------|-------------|
| Contrato obligatorio para subclases | `ABC` + `@abstractmethod` |
| Plugin/extensiones sin tocar core | `Protocol` |
| Framework con inicialización obligatoria | `ABC` + `Template Method` |
| APIs públicas, tipado estructural | `Protocol` |
| Verificar protocolo en runtime | `@runtime_checkable` + `Protocol` |
| Subclase virtual (sin herencia) | `__subclasshook__` |

---

---
## 🎯 Ejercicios

Practica clases abstractas en [ejercicios.md](../03-poo/ejercicios.md#20--clases-abstractas).

**Mini-ejercicio**: ABC `Instrumento` con método abstracto `tocar()`. `Guitarra` y `Piano` implementan. Función que acepta cualquier Instrumento.

---

## Véase también

- [18-herencia-polimorfismo](./18-herencia-polimorfismo.md) — Herencia, MRO, mixins
- [16-tipos-metodos](./16-tipos-metodos.md) — `@classmethod` abstracto
- [22-patrones-diseno](./22-patrones-diseno.md) — Template Method, Strategy
- [10-type-hints](../02-avanzado/10-type-hints.md) — `Protocol` en type hints
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada