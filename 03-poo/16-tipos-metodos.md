# 16 — Tipos de Métodos

> Métodos de instancia, clase, estáticos, properties, y cuándo usar cada uno.

---

## Comparativa rápida

| Método | Decorador | Primer arg | Accede a `self` | Accede a `cls` | Uso típico |
|--------|-----------|------------|-----------------|----------------|------------|
| **Instancia** | (ninguno) | `self` | ✅ | ❌ | Comportamiento por objeto |
| **Clase** | `@classmethod` | `cls` | ❌ | ✅ | Factories, estado compartido |
| **Estático** | `@staticmethod` | (ninguno) | ❌ | ❌ | Utilidades, helpers |
| **Property** | `@property` | `self` | ✅ | ❌ | Getters/setters controlados |

---

## Métodos de Instancia

Reciben `self` (la instancia). Son los más comunes.

```python
class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def saludar(self) -> str:
        return f"Hola, soy {self.nombre}"
    
    def cumplir_anos(self) -> None:
        self.edad = getattr(self, 'edad', 0) + 1

p = Persona("Ana")
print(p.saludar())  # Hola, soy Ana
```

### Qué puede hacer
- Leer/escribir atributos de instancia (`self.attr`)
- Llamar otros métodos de instancia (`self.otro()`)
- Acceder a clase via `type(self)` o `self.__class__`

---

## Métodos de Clase (`@classmethod`)

Reciben `cls` (la clase). Operan sobre la **clase**, no la instancia.

```python
class Persona:
    contador = 0
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        Persona.contador += 1
    
    @classmethod
    def total(cls) -> int:
        return cls.contador
    
    @classmethod
    def desde_nacimiento(cls, año: int, nombre: str) -> "Persona":
        """Factory: constructor alternativo"""
        from datetime import date
        edad = date.today().year - año
        return cls(nombre)  # cls() crea instancia de la clase correcta

# Uso
print(Persona.total())  # 0
p = Persona.desde_nacimiento(2000, "Ana")
print(Persona.total())  # 1
```

### Ventaja clave: Herencia

```python
class Empleado(Persona):
    pass

e = Empleado.desde_nacimiento(1990, "Luis")  # Crea Empleado, no Persona
print(type(e))  # <class 'Empleado'>
```

> 🔑 `cls` es **dinámico** — respeta la subclase que lo llama.

### Cuándo usar
- **Constructores alternativos** (factory methods)
- Modificar **estado de clase** (contadores, config)
- Operaciones que no necesitan instancia específica

---

## Métodos Estáticos (`@staticmethod`)

No reciben `self` ni `cls`. Son funciones dentro del namespace de la clase.

```python
class Matematicas:
    @staticmethod
    def sumar(a: int, b: int) -> int:
        return a + b
    
    @staticmethod
    def es_par(n: int) -> bool:
        return n % 2 == 0

print(Matematicas.sumar(3, 4))  # 7
print(Matematicas.es_par(10))   # True

# También desde instancia (pero no accede a self)
m = Matematicas()
print(m.sumar(1, 2))  # 3
```

### Cuándo usar
- Funciones auxiliares **relacionadas conceptualmente** con la clase
- Lógica **independiente del estado** (ni instancia ni clase)
- Agrupar utilidades: `Validar.email()`, `Formatear.fecha()`

### ❌ Error común

```python
# ❌ MAL: Usar staticmethod para factory
class Persona:
    @staticmethod
    def crear(nombre):
        return Persona(nombre)  # Hardcoded: no respeta herencia

# ✅ BIEN: Usar classmethod
class Persona:
    @classmethod
    def crear(cls, nombre):
        return cls(nombre)  # Dinámico: respeta subclases
```

---

## Properties (`@property`)

Getters/setters/deleters con sintaxis de atributo.

```python
class Cuenta:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.__saldo = saldo
    
    @property
    def saldo(self) -> float:
        """Getter: se accede como atributo"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor: float) -> None:
        """Setter: validación al asignar"""
        if valor < 0:
            raise ValueError("Saldo no puede ser negativo")
        self.__saldo = valor
    
    @saldo.deleter
    def saldo(self) -> None:
        """Deleter: limpieza al borrar"""
        print("Cerrando cuenta...")
        self.__saldo = 0

c = Cuenta("Ana", 1000)
print(c.saldo)      # 1000 (getter)
c.saldo = 1500      # 1500 (setter)
# c.saldo = -100    # ValueError
del c.saldo         # "Cerrando cuenta..." (deleter)
```

### Property solo lectura

```python
class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
    
    @property
    def area(self) -> float:
        return 3.14159 * self.radio ** 2
    
    @property
    def diametro(self) -> float:
        return self.radio * 2

c = Circulo(5)
print(c.area)      # 78.54
# c.area = 10     # AttributeError (no setter)
```

---

## Tabla de decisión

| Necesidad | Método |
|-----------|--------|
| Modificar `self.attr` | Instancia |
| Leer `self.attr` | Instancia / Property |
| Factory / constructor alternativo | `@classmethod` |
| Modificar `Clase.attr` | `@classmethod` |
| Utilidad sin estado | `@staticmethod` |
| Validar al leer/escribir | `@property` |
| Computed field (solo lectura) | `@property` |

---

## Ejemplo integrado

```python
class Usuario:
    total_usuarios = 0  # Estado de clase
    
    def __init__(self, email: str, nombre: str):
        self.email = email
        self.nombre = nombre
        Usuario.total_usuarios += 1
    
    # Instancia: comportamiento por objeto
    def saludar(self) -> str:
        return f"Hola, {self.nombre}"
    
    # Property: acceso controlado
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, valor: str) -> None:
        if "@" not in valor:
            raise ValueError("Email inválido")
        self.__email = valor
    
    # Clase: factory + estado compartido
    @classmethod
    def desde_dict(cls, datos: dict) -> "Usuario":
        return cls(datos["email"], datos["nombre"])
    
    @classmethod
    def total(cls) -> int:
        return cls.total_usuarios
    
    # Estático: utilidad
    @staticmethod
    def validar_email(email: str) -> bool:
        return "@" in email and "." in email.split("@")[1]

# Uso
u1 = Usuario("ana@mail.com", "Ana")
u2 = Usuario.desde_dict({"email": "luis@mail.com", "nombre": "Luis"})

print(u1.saludar())           # Instancia
print(u1.email)               # Property getter
print(Usuario.total())        # Clase
print(Usuario.validar_email("x@y.z"))  # Estático
```

---

---
## 🎯 Ejercicios

Practica tipos de métodos en [ejercicios.md](../03-poo/ejercicios.md#16--tipos-de-métodos).

**Mini-ejercicio**: Clase `Termometro` con property `celsius` y property `fahrenheit` (getter/setter con conversión).

---

## Véase también

- [15-clases-objetos](./15-clases-objetos.md) — Atributos, `__init__`, visibilidad
- [17-metodos-magicos](./17-metodos-magicos.md) — `__str__`, `__repr__`, operadores
- [19-encapsulamiento](./19-encapsulamiento.md) — Encapsulamiento avanzado
- [21-dataclasses-pydantic](../03-poo/21-dataclasses-pydantic.md) — `@dataclass` genera métodos automáticamente
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada