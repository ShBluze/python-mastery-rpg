# 📝 Ejercicios — 03 POO

---

## 15 — Clases y objetos

### Ejercicio 15.1 — Clase Libro
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: class, __init__, atributos
- **Criterio de éxito**: Clase `Libro` con título, autor, año. Método `info()` que devuelve string formateado.

### Ejercicio 15.2 — Biblioteca
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: clases, listas de objetos, métodos
- **Criterio de éxito**: Clase `Biblioteca` que almacena Libros. Métodos: agregar, listar, buscar por autor, prestar/devolver.

### Ejercicio 15.3 — __slots__
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: __slots__, atributos de clase
- **Criterio de éxito**: Clase `Punto` con __slots__ = ("x", "y"). Demostrar que no se pueden añadir atributos dinámicos y que usa menos memoria.

---

## 16 — Tipos de métodos

### Ejercicio 16.1 — @classmethod factory
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: @classmethod, constructores alternativos
- **Criterio de éxito**: Clase `Persona` con constructor normal y factory `desde_csv(linea: str) -> Persona`.

### Ejercicio 16.2 — @property validado
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: @property, getter, setter
- **Criterio de éxito**: Clase `Cuenta` con property `saldo` (getter) que valida en setter que no sea negativo.

### Ejercicio 16.3 — Método estático utilidad
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: @staticmethod
- **Criterio de éxito**: Clase `Matematica` con método estático `factorial(n)`.

---

## 17 — Métodos mágicos

### Ejercicio 17.1 — __str__ y __repr__
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: __str__, __repr__
- **Criterio de éxito**: Clase `Usuario` donde __str__ muestra nombre y __repr__ muestra todos los datos.

### Ejercicio 17.2 — __eq__ y __hash__
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: __eq__, __hash__, sets
- **Criterio de éxito**: Clase `Persona` que es igual si mismo nombre y edad. Debe funcionar en sets como eliminador de duplicados.

### Ejercicio 17.3 — __getitem__ y __len__
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: __getitem__, __len__, protocolo secuencia
- **Criterio de éxito**: Clase `ListaPersonalizada` que envuelve una lista nativa y soporta indexación, slicing y len().

---

## 18 — Herencia y polimorfismo

### Ejercicio 18.1 — Jerarquía de animales
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: herencia, super()
- **Criterio de éxito**: Clase base `Animal` con método `hacer_sonido()`. Subclases `Perro` y `Gato` que sobrescriben.

### Ejercicio 18.2 — Mixin JSONeable
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: mixins, herencia múltiple
- **Criterio de éxito**: Mixin `JSONeable` con método `to_json()`. Clases que lo heredan pueden serializarse.

### Ejercicio 18.3 — MRO y super()
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: MRO, super() en herencia múltiple, **kwargs
- **Criterio de éxito**: Diamante de herencia (A → B, C → D). Cada clase imprime su nombre al init. Verificar orden MRO.

---

## 19 — Encapsulamiento

### Ejercicio 19.1 — Property temperatura
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: @property, encapsulamiento
- **Criterio de éxito**: Clase `Termometro` que almacena en Celsius pero permite get/set en Fahrenheit con conversión automática.

### Ejercicio 19.2 — Name mangling
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: __name mangling
- **Criterio de éxito**: Clase con atributo `__secreto`. Demostrar name mangling y acceso desde fuera (desaconsejado).

### Ejercicio 19.3 — weakref
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: weakref, referencia cíclica, GC
- **Criterio de éxito**: Demostrar una referencia cíclica que impide el GC. Resolver con weakref.

---

## 20 — Clases abstractas

### Ejercicio 20.1 — ABC Figura
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: ABC, @abstractmethod
- **Criterio de éxito**: ABC `Figura` con métodos abstractos `area()` y `perimetro()`. Clases `Circulo` y `Rectangulo`.

### Ejercicio 20.2 — Protocol vs ABC
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: Protocol, ABC, duck typing
- **Criterio de éxito**: Misma funcionalidad implementada con ABC y con Protocol. Demostrar diferencias (herencia vs estructural).

### Ejercicio 20.3 — __subclasshook__
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: __subclasshook__, ABCMeta
- **Criterio de éxito**: ABC que reconoce como subclase virtual a cualquier clase que tenga ciertos métodos, sin herencia explícita.

---

## 21 — Dataclasses y Pydantic

### Ejercicio 21.1 — @dataclass básico
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: @dataclass, field
- **Criterio de éxito**: Dataclass `Producto` con nombre, precio, stock. Campo calculado `valor_total`.

### Ejercicio 21.2 — Pydantic válido
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: BaseModel, validación
- **Criterio de éxito**: Modelo `UsuarioPydantic` con validación: email formato, edad ≥ 18, nombre no vacío.

### Ejercicio 21.3 — Dataclass heredada
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: herencia en dataclasses
- **Criterio de éxito**: Dataclass `Empleado` que hereda de `Persona`. Manejar campos adicionales y orden de init.

---

## 22 — Patrones de diseño

### Ejercicio 22.1 — Singleton
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: Singleton, __new__, metaclases
- **Criterio de éxito**: Clase `Configuracion` que solo puede tener una instancia. Dos variables apuntan al mismo objeto.

### Ejercicio 22.2 — Observer
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: Observer pattern, callbacks
- **Criterio de éxito**: Clase `Subastador` (sujeto) y `Comprador` (observador). Cuando el precio cambia, notifica a todos.

### Ejercicio 22.3 — Strategy
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: Strategy pattern, composición
- **Criterio de éxito**: Sistema de filtros de imágenes con estrategias intercambiables: BlancoYNegro, Sepia, Invertir. El contexto aplica la estrategia elegida.
