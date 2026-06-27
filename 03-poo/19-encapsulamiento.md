# 19 — Encapsulamiento Avanzado

> Name mangling, properties, `__del__`, reference counting, weakref, `__slots__`.

---

## Encapsulamiento en Python

Python **no tiene private real** — usa convenciones y name mangling.

| Nivel | Sintaxis | Acceso | Uso |
|-------|----------|--------|-----|
| Público | `self.attr` | Libre | API pública |
| Protegido | `self._attr` | Convención "interno" | Subclases, internos |
| Privado | `self.__attr` | Name mangling | Evitar colisiones |

---

## Name Mangling (`__`)

```python
class Cuenta:
    def __init__(self, saldo: float):
        self._titular = "Por defecto"   # Protegido (convención)
        self.__saldo = saldo            # Privado → _Cuenta__saldo
    
    def mostrar_saldo(self) -> float:
        return self.__saldo

c = Cuenta(1000)
print(c._titular)              # "Por defecto" (accesible)
print(c._Cuenta__saldo)        # 1000 (acceso real via mangling)
# print(c.__saldo)             # AttributeError
```

### Propósito real
- **Evita colisiones** en herencia (subclase no pisa atributo padre)
- **No es seguridad** — accesible si se conoce el nombre mangled

```python
class Base:
    def __init__(self):
        self.__privado = "base"

class Hija(Base):
    def __init__(self):
        super().__init__()
        self.__privado = "hija"  # Crea _Hija__privado, no toca _Base__privado

h = Hija()
print(h._Base__privado)   # "base"
print(h._Hija__privado)   # "hija"
```

---

## Properties — Acceso Controlado

```python
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.__saldo = saldo
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Saldo no puede ser negativo")
        self.__saldo = valor
    
    @saldo.deleter
    def saldo(self) -> None:
        print("Cuenta cerrada")
        self.__saldo = 0

c = CuentaBancaria("Ana", 1000)
print(c.saldo)      # 1000 (getter)
c.saldo = 1500      # 1500 (setter validado)
# c.saldo = -100    # ValueError
del c.saldo         # "Cuenta cerrada" (deleter)
```

### Property solo lectura (computed)

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
```

---

## `__slots__` — Memoria y Atributos Fijos

```python
class Punto:
    __slots__ = ("x", "y")  # Solo estos atributos permitidos
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

p = Punto(1, 2)
# p.z = 3  # AttributeError
# p.__dict__  # AttributeError (no existe)
```

| Ventaja | Descripción |
|---------|-------------|
| **Memoria** | ~40-50% menos por instancia |
| **Velocidad** | Acceso a atributos más rápido |
| **Prevención** | Evita typos en atributos |

### Herencia con `__slots__`

```python
class Base:
    __slots__ = ("a", "b")

class Hija(Base):
    __slots__ = ("c",)  # Debe redeclarar slots

h = Hija()
h.a = 1
h.c = 3
```

---

## Reference Counting (Conteo de Referencias)

Python usa **reference counting** + **garbage collector** (ciclos).

```python
import sys

a = [1, 2, 3]
b = a
print(sys.getrefcount(a))  # 3 (a, b, argumento getrefcount)

del b
print(sys.getrefcount(a))  # 2
```

### Ciclo de vida

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
    def __del__(self):
        print(f"Destruyendo {self.valor}")

# Ciclo de referencia
a = Nodo(1)
b = Nodo(2)
a.siguiente = b
b.siguiente = a  # Ciclo!

del a, b
# __del__ NO se llama inmediatamente (GC lo recoge después)
# gc.collect() fuerza recolección
```

> ⚠️ **`__del__` no es confiable** para limpieza crítica (archivos, sockets, BD).
> Usa **context managers** (`with`) o `try/finally`.

---

## `__del__` — Destructor

```python
class Recurso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        print(f"Creado: {nombre}")
    
    def __del__(self):
        print(f"Destruido: {self.nombre}")

r = Recurso("test")
del r  # "Destruido: test" (si refcount llega a 0)
```

### Problemas con `__del__`
1. **Orden impredecible** en shutdown
2. **Excepciones silenciadas** (se imprimen en stderr, no propagan)
3. **Resucitación** (objeto revive si `__del__` crea referencia)
4. **Ciclos** requieren `gc.collect()`

```python
# ❌ Malo: confiar en __del__ para cerrar archivo
class Archivo:
    def __init__(self, ruta):
        self.f = open(ruta, "w")
    def __del__(self):
        self.f.close()  # Puede no ejecutarse a tiempo

# ✅ Bueno: context manager
class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.f = None
    def __enter__(self):
        self.f = open(self.ruta, "w")
        return self.f
    def __exit__(self, *args):
        if self.f: self.f.close()

with Archivo("datos.txt") as f:
    f.write("Hola")
```

---

## `weakref` — Referencias Débiles

No incrementan refcount. Útil para caches, observers, evitar ciclos.

```python
import weakref

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None  # Referencia débil al padre

class Arbol:
    def __init__(self):
        self.raiz = Nodo("raiz")
        self.cache = weakref.WeakValueDictionary()
    
    def agregar_hijo(self, padre, valor):
        hijo = Nodo(valor)
        hijo.padre = weakref.ref(padre)  # No crea ciclo
        self.cache[valor] = hijo
        return hijo

# weakref.ref(obj) → llama para acceder: ref()
# weakref.proxy(obj) → acceso directo como obj.attr
# WeakValueDictionary / WeakKeyDictionary → GC automático
```

---

## `__getattr__` / `__setattr__` — Acceso Dinámico

```python
class Config:
    def __init__(self):
        self._datos = {}
    
    def __getattr__(self, name):  # Solo si NO existe
        return self._datos.get(name)
    
    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            self._datos[name] = value

cfg = Config()
cfg.debug = True
print(cfg.debug)  # True (usa __getattr__)
```

---

## Resumen: Niveles de Protección

| Necesidad | Solución |
|-----------|----------|
| "No tocar" por convención | `_atributo` |
| Evitar colisiones herencia | `__atributo` (name mangling) |
| Validar lectura/escritura | `@property` |
| Atributos fijos, menos memoria | `__slots__` |
| Referencias sin ciclo | `weakref` |
| Limpieza garantizada | Context manager (`with`) |
| Solo lectura computada | `@property` sin setter |

---

## Buenas Prácticas

1. **API pública** → sin guión bajo
2. **Internos** → `_protegido`
3. **Herencia segura** → `__privado` si hay riesgo de colisión
4. **Validación** → `@property` con setter
5. **Muchas instancias** → `__slots__`
6. **Caches/Observers** → `weakref`
7. **Limpieza recursos** → `with` / `try/finally` (nunca `__del__`)

---

---
## 🎯 Ejercicios

Practica encapsulamiento en [ejercicios.md](../03-poo/ejercicios.md#19--encapsulamiento).

**Mini-ejercicio**: Clase `CuentaBancaria` con saldo privado. Property que permite consultar pero no modificar directamente. Método transferir con validación.

---

## Véase también

- [15-clases-objetos](./15-clases-objetos.md) — `__dict__`, `__slots__`, visibilidad básica
- [16-tipos-metodos](./16-tipos-metodos.md) — Properties en profundidad
- [17-metodos-magicos](./17-metodos-magicos.md) — `__del__`, `__getattr__`, `__setattr__`
- [14-context-managers](../02-avanzado/14-context-managers.md) — Patrón `with` para recursos
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada