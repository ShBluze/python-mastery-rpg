# 15 — Clases y Objetos

> Fundamentos de POO en Python: clases, instancias, `__init__`, atributos, visibilidad.

---

## Conceptos base

| Concepto | Descripción |
|----------|-------------|
| **Clase** | Molde/plano (ej: `Coche`) |
| **Objeto/Instancia** | Creación concreta (ej: `mi_coche = Coche("Seat")`) |
| **Atributo** | Estado/datos (`self.modelo = "Seat"`) |
| **Método** | Comportamiento/funciones (`def acelerar(self): ...`) |
| **Identidad** | Cada objeto es único (`id(obj)`) |

---

## Definición básica

```python
class Coche:
    def __init__(self, modelo: str):
        self.modelo = modelo  # Atributo de instancia
    
    def arrancar(self) -> None:
        print(f"{self.modelo} arranca")

mi_coche = Coche("Seat")
mi_coche.arrancar()  # Seat arranca
```

---

## `__init__` — Constructor

Se ejecuta **automáticamente** al crear la instancia.

```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 30)  # __init__ llamado aquí
```

### Parámetros con valores por defecto

```python
class Producto:
    def __init__(self, nombre: str, precio: float = 0.0, stock: int = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

p1 = Producto("Pan")           # precio=0.0, stock=0
p2 = Producto("Leche", 1.5)    # stock=0
p3 = Producto("Huevos", 2.0, 12)
```

---

## Atributos de instancia

Únicos por cada objeto.

```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)
print(p1.nombre)  # Ana
print(p2.nombre)  # Luis
```

---

## Atributos de clase

Compartidos por **todas** las instancias. Definidos fuera de `__init__`.

```python
class Empleado:
    contador = 0  # Atributo de clase
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        Empleado.contador += 1  # Acceso via clase

e1 = Empleado("Ana")
e2 = Empleado("Luis")
print(Empleado.contador)  # 2
```

### Cuándo usar
- Contadores de instancias
- Configuración global
- Constantes compartidas

```python
class Config:
    version = "1.0"
    debug = False
    MAX_CONEXIONES = 100
```

---

## Visibilidad (Convenciones)

Python **no tiene private real**, usa convenciones:

| Prefijo | Significado | Ejemplo |
|---------|-------------|---------|
| `publico` | Acceso libre | `self.nombre` |
| `_protegido` | "No tocar desde fuera" (convención) | `self._precio` |
| `__privado` | Name mangling (evita colisiones) | `self.__saldo` |

### Name mangling (`__`)

```python
class Cuenta:
    def __init__(self, saldo: float):
        self._titular = "Por defecto"   # Protegido (convención)
        self.__saldo = saldo            # Privado (name mangling)
    
    def mostrar_saldo(self) -> float:
        return self.__saldo

c = Cuenta(1000)
print(c._titular)          # Accesible (pero "no tocar")
# print(c.__saldo)         # AttributeError
print(c._Cuenta__saldo)    # 1000 (acceso real via name mangling)
print(c.mostrar_saldo())         # 1000
```

> 🔑 **Regla**: Name mangling protege contra **colisiones en herencia**, no contra acceso intencional.

---

## `__dict__` — Almacenamiento interno

```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 30)
print(p.__dict__)  # {'nombre': 'Ana', 'edad': 30}
```

- Cada instancia tiene su `__dict__` (salvo `__slots__`)
- `self.attr = valor` → `self.__dict__["attr"] = valor`

---

## `__slots__` — Optimizar memoria

```python
class Punto:
    __slots__ = ("x", "y")  # Solo permite estos atributos
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

p = Punto(1, 2)
# p.z = 3  # AttributeError
print(p.__dict__)  # AttributeError (no existe)
```

| Ventaja | Descripción |
|---------|-------------|
| Memoria | ~40-50% menos por instancia |
| Velocidad | Acceso a atributos más rápido |
| Prevención | Evita atributos accidentales |

> ⚠️ **Tradeoff**: No permite `__dict__`, herencia múltiple requiere `__slots__` en todas las clases.

---

## Properties (Getters/Setters controlados)

```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.titular = titular
        self.__saldo = saldo_inicial
    
    @property
    def saldo(self) -> float:
        """Getter: lectura controlada"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor: float) -> None:
        """Setter: validación al escribir"""
        if valor < 0:
            raise ValueError("Saldo no puede ser negativo")
        self.__saldo = valor
    
    def depositar(self, monto: float) -> None:
        if monto > 0:
            self.__saldo += monto

cuenta = CuentaBancaria("Ana", 1000)
print(cuenta.saldo)      # 1000 (usa getter)
cuenta.saldo = 1500      # usa setter
cuenta.depositar(500)
print(cuenta.saldo)      # 2000
```

---

## Resumen: Estructura típica de clase

```python
class MiClase:
    # Atributos de clase
    contador = 0
    VERSION = "1.0"
    
    def __init__(self, obligatorio: str, opcional: int = 0):
        # Atributos de instancia
        self.obligatorio = obligatorio
        self.opcional = opcional
        self._protegido = "interno"
        self.__privado = "name mangling"
        MiClase.contador += 1
    
    # Property
    @property
    def obligatorio(self) -> str:
        return self._obligatorio
    
    @obligatorio.setter
    def obligatorio(self, valor: str) -> None:
        if not valor:
            raise ValueError("Obligatorio requerido")
        self._obligatorio = valor
    
    # Método de instancia
    def metodo_instancia(self) -> str:
        return f"{self.obligatorio} - {self.__privado}"
    
    # Método de clase
    @classmethod
    def total_instancias(cls) -> int:
        return cls.contador
    
    # Método estático
    @staticmethod
    def utilidad(x: int) -> int:
        return x * 2
    
    # Representación
    def __repr__(self) -> str:
        return f"MiClase(obligatorio={self.obligatorio!r})"
```

---

---
## 🎯 Ejercicios

Practica clases en [ejercicios.md](../03-poo/ejercicios.md#15--clases-y-objetos).

**Mini-ejercicio**: Clase `Cancion` con título, artista, duración. Método `info()` que devuelve f-string. Crea 3 instancias.

---

## Véase también

- [16-tipos-metodos](./16-tipos-metodos.md) — Instance/Class/Static methods en profundidad
- [17-metodos-magicos](./17-metodos-magicos.md) — `__str__`, `__repr__`, operadores, contenedores
- [19-encapsulamiento](./19-encapsulamiento.md) — Encapsulamiento avanzado, `__del__`, ref counting
- [21-dataclasses-pydantic](../03-poo/21-dataclasses-pydantic.md) — `@dataclass`, `pydantic.BaseModel`
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada