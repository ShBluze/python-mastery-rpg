# 22 — Patrones de Diseño en Python

> Implementaciones pythonicas de patrones clásicos: Factory, Strategy, Observer, Builder, Decorator, Singleton, Adapter, etc.

---

## Patrones Creacionales

### Factory Method

```python
from abc import ABC, abstractmethod

class Producto(ABC):
    @abstractmethod
    def operacion(self) -> str: ...

class ProductoA(Producto):
    def operacion(self) -> str: return "Resultado A"

class ProductoB(Producto):
    def operacion(self) -> str: return "Resultado B"

class Creador(ABC):
    @abstractmethod
    def factory_method(self) -> Producto: ...
    
    def operacion(self) -> str:
        producto = self.factory_method()
        return f"Creador: {producto.operacion()}"

class CreadorA(Creador):
    def factory_method(self) -> Producto:
        return ProductoA()

class CreadorB(Creador):
    def factory_method(self) -> Producto:
        return ProductoB()

# Uso
creador_a = CreadorA()
print(c.operacion())  # Creador: Resultado A
```

### Abstract Factory

```python
from abc import ABC, abstractmethod

class Boton(ABC):
    @abstractmethod def render(self): ...

class BotonWin(Boton):
    def render(self): return "Botón Windows"

class BotonMac(Boton):
    def render(self): return "Botón Mac"

class Checkbox(ABC):
    @abstractmethod def render(self): ...

class CheckboxWin(Checkbox):
    def render(self): return "Checkbox Windows"

class CheckboxMac(Checkbox):
    def render(self): return "Checkbox Mac"

class FabricaGUI(ABC):
    @abstractmethod def crear_boton(self) -> Boton: ...
    @abstractmethod def crear_checkbox(self) -> Checkbox: ...

class FabricaWin(FabricaGUI):
    def crear_boton(self) -> Boton: return BotonWin()
    def crear_checkbox(self) -> Checkbox: return CheckboxWin()

class FabricaMac(FabricaGUI):
    def crear_boton(self) -> Boton: return BotonMac()
    def crear_checkbox(self) -> Checkbox: return CheckboxMac()

def cliente(fabrica: FabricaGUI):
    b = fabrica.crear_boton()
    c = fabrica.crear_checkbox()
    print(b.render(), c.render())

cliente(FabricaWin())  # Botón Windows Checkbox Windows
cliente(FabricaMac())  # Botón Mac Checkbox Mac
```

### Builder

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Computadora:
    cpu: str
    ram: str
    almacenamiento: str
    gpu: Optional[str] = None
    wifi: bool = False
    bluetooth: bool = False

class ComputadoraBuilder:
    def __init__(self):
        self._cpu = "i5"
        self._ram = "8GB"
        self._almacenamiento = "256GB SSD"
        self._gpu = None
        self._wifi = False
        self._bluetooth = False
    
    def cpu(self, cpu: str) -> "ComputadoraBuilder":
        self._cpu = cpu
        return self
    
    def ram(self, ram: str) -> "ComputadoraBuilder":
        self._ram = ram
        return self
    
    def almacenamiento(self, alm: str) -> "ComputadoraBuilder":
        self._almacenamiento = alm
        return self
    
    def gpu(self, gpu: str) -> "ComputadoraBuilder":
        self._gpu = gpu
        return self
    
    def wifi(self) -> "ComputadoraBuilder":
        self._wifi = True
        return self
    
    def bluetooth(self) -> "ComputadoraBuilder":
        self._bluetooth = True
        return self
    
    def build(self) -> Computadora:
        return Computadora(
            cpu=self._cpu, ram=self._ram, almacenamiento=self._almacenamiento,
            gpu=self._gpu, wifi=self._wifi, bluetooth=self._bluetooth
        )

# Uso fluido
pc = (ComputadoraBuilder()
      .cpu("i9")
      .ram("32GB")
      .almacenamiento("1TB NVMe")
      .gpu("RTX 4090")
      .wifi()
      .bluetooth()
      .build())
```

### Singleton

```python
# ❌ Naive (no thread-safe)
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# ✅ Thread-safe (Python 3.7+)
class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# ✅ Module-level (pythonico)
# config.py
class _Config:
    def __init__(self):
        self.debug = False

config = _Config()  # Singleton natural

# Uso
from config import config
config.debug = True
```

### Prototype

```python
import copy

class Prototipo:
    def __init__(self):
        self._objetos = {}
    
    def registrar(self, nombre: str, obj):
        self._objetos[nombre] = obj
    
    def crear(self, nombre: str, **attrs):
        obj = copy.deepcopy(self._objetos[nombre])
        for k, v in attrs.items():
            setattr(obj, k, v)
        return obj

# Uso
proto = Prototipo()
proto.registrar("rect", Rectangulo(10, 20))
r1 = proto.crear("rect")
r2 = proto.crear("rect", color="rojo")
```

---

## Patrones Estructurales

### Adapter

```python
# Interfaz esperada
class Pago:
    def pagar(self, monto: float) -> bool: ...

# API externa (incompatible)
class PasarelaExterna:
    def procesar_pago(self, amount: int, currency: str) -> dict: ...

# Adapter
class AdapterPago(Pago):
    def __init__(self, pasarela: PasarelaExterna):
        self.pasarela = pasarela
    
    def pagar(self, monto: float) -> bool:
        resultado = self.pasarela.procesar_pago(int(monto * 100), "USD")
        return resultado.get("success", False)
```

### Decorator (Patrón, no sintaxis `@`)

```python
from abc import ABC, abstractmethod

class Cafe(ABC):
    @abstractmethod def costo(self) -> float: ...
    @abstractmethod def descripcion(self) -> str: ...

class CafeSimple(Cafe):
    def costo(self) -> float: return 1.0
    def descripcion(self) -> str: return "Café simple"

class Decorador(Cafe):
    def __init__(self, cafe: Cafe):
        self._cafe = cafe
    
    def costo(self) -> float: return self._cafe.costo()
    def descripcion(self) -> str: return self._cafe.descripcion()

class Leche(Decorador):
    def costo(self) -> float: return self._cafe.costo() + 0.5
    def descripcion(self) -> str: return self._cafe.descripcion() + ", leche"

class Azucar(Decorador):
    def costo(self) -> float: return self._cafe.costo() + 0.2
    def descripcion(self) -> str: return self._cafe.descripcion() + ", azúcar"

# Uso
cafe = Azucar(Leche(CafeSimple()))
print(cafe.descripcion())  # Café simple, leche, azúcar
print(cafe.costo())        # 1.7
```

### Facade

```python
# Subsistemas complejos
class CPU:
    def congelar(self): ...
    def saltar(self, pos): ...
    def ejecutar(self): ...

class Memoria:
    def cargar(self, pos, datos): ...

class DiscoDuro:
    def leer(self, lba, size): ...

# Facade
class ComputadoraFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memoria = Memoria()
        self.disco = DiscoDuro()
    
    def iniciar(self):
        self.cpu.congelar()
        self.memoria.cargar(0, self.disco.leer(0, 1024))
        self.cpu.saltar(0)
        self.cpu.ejecutar()

# Uso simple
pc = ComputadoraFacade()
pc.iniciar()
```

### Proxy

```python
class Imagen:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self._cargar()
    
    def _cargar(self):
        print(f"Cargando {self.archivo}...")
    
    def mostrar(self):
        print(f"Mostrando {self.archivo}")

class ProxyImagen:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self._imagen_real = None
    
    def mostrar(self):
        if self._imagen_real is None:
            self._imagen_real = Imagen(self.archivo)
        self._imagen_real.mostrar()

# Uso (lazy loading)
img = ProxyImagen("foto.jpg")
img.mostrar()  # Carga y muestra
img.mostrar()  # Ya cargada, solo muestra
```

---

## Patrones de Comportamiento

### Strategy

```python
from abc import ABC, abstractmethod

class EstrategiaOrdenacion(ABC):
    @abstractmethod
    def ordenar(self, datos: list) -> list: ...

class Burbuja(EstrategiaOrdenacion):
    def ordenar(self, datos: list) -> list:
        return sorted(datos)

class Rapida(EstrategiaOrdenacion):
    def ordenar(self, datos: list) -> list:
        return sorted(datos, reverse=True)

class Contexto:
    def __init__(self, estrategia: EstrategiaOrdenacion):
        self.estrategia = estrategia
    
    def ejecutar(self, datos: list) -> list:
        return self.estrategia.ordenar(datos)

# Cambio en runtime
ctx = Contexto(Burbuja())
print(ctx.ejecutar([3,1,2]))  # [1, 2, 3]
ctx.estrategia = Rapida()
print(ctx.ejecutar([3,1,2]))  # [3, 2, 1]
```

### Observer

```python
from abc import ABC, abstractmethod
from typing import List

class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str): ...

class Sujeto:
    def __init__(self):
        self._observadores: List[Observador] = []
    
    def suscribir(self, obs: Observador):
        self._observadores.append(obs)
    
    def desuscribir(self, obs: Observador):
        self._observadores.remove(obs)
    
    def notificar(self, mensaje: str):
        for obs in self._observadores:
            obs.actualizar(mensaje)

class Logger(Observador):
    def actualizar(self, mensaje: str):
        print(f"[LOG] {mensaje}")

class Alerta(Observador):
    def actualizar(self, mensaje: str):
        if "error" in mensaje.lower():
            print(f"🚨 ALERTA: {mensaje}")

# Uso
sujeto = Sujeto()
sujeto.suscribir(Logger())
sujeto.suscribir(Alerta())
sujeto.notificar("Sistema iniciado")
sujeto.notificar("Error en base de datos")
```

### Command

```python
from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def ejecutar(self): ...
    @abstractmethod
    def deshacer(self): ...

class Luz:
    def encender(self): print("Luz ON")
    def apagar(self): print("Luz OFF")

class EncenderLuz(Comando):
    def __init__(self, luz: Luz):
        self.luz = luz
    def ejecutar(self): self.luz.encender()
    def deshacer(self): self.luz.apagar()

class Invocador:
    def __init__(self):
        self.historial: list[Comando] = []
    
    def ejecutar(self, comando: Comando):
        comando.ejecutar()
        self.historial.append(comando)
    
    def deshacer(self):
        if self.historial:
            self.historial.pop().deshacer()

# Uso
luz = Luz()
inv = Invocador()
inv.ejecutar(EncenderLuz(luz))  # Luz ON
inv.deshacer()                   # Luz OFF
```

### Template Method

```python
from abc import ABC, abstractmethod

class ProcesadorDatos(ABC):
    def procesar(self, datos: str) -> str:
        validados = self.validar(datos)
        transformados = self.transformar(validados)
        return self.guardar(transformados)
    
    @abstractmethod
    def validar(self, datos: str) -> str: ...
    
    @abstractmethod
    def transformar(self, datos: str) -> str: ...
    
    def guardar(self, datos: str) -> str:
        return f"Guardado: {datos}"

class ProcesadorCSV(ProcesadorDatos):
    def validar(self, datos: str) -> str:
        return datos.strip()
    
    def transformar(self, datos: str) -> str:
        return datos.split(",")

class ProcesadorJSON(ProcesadorDatos):
    def validar(self, datos: str) -> str:
        return datos
    
    def transformar(self, datos: str) -> str:
        import json
        return json.loads(datos)
```

### State

```python
from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def manejar(self, contexto): ...

class Apagado(Estado):
    def manejar(self, contexto):
        print("Encendiendo...")
        contexto.estado = Encendido()

class Encendido(Estado):
    def manejar(self, contexto):
        print("Apagando...")
        contexto.estado = Apagado()

class Interruptor:
    def __init__(self):
        self.estado: Estado = Apagado()
    
    def presionar(self):
        self.estado.manejar(self)

sw = Interruptor()
sw.presionar()  # Encendiendo...
sw.presionar()  # Apagando...
```

### Iterator

```python
class Coleccion:
    def __init__(self, items):
        self._items = items
    
    def __iter__(self):
        return IteradorColeccion(self._items)

class IteradorColeccion:
    def __init__(self, items):
        self._items = items
        self._indice = 0
    
    def __next__(self):
        if self._indice >= len(self._items):
            raise StopIteration
        item = self._items[self._indice]
        self._indice += 1
        return item

# Uso (built-in ya usa __iter__)
c = Coleccion([1, 2, 3])
for x in c:
    print(x)
```

---

## Patrones Pythonicos (Idiomáticos)

### Dependency Injection

```python
# ❌ Acoplado
class Servicio:
    def __init__(self):
        self.db = BaseDatos()  # Hardcoded

# ✅ Inyectado
class Servicio:
    def __init__(self, db: BaseDatos):
        self.db = db

# Uso
servicio = Servicio(BaseDatosProduccion())
servicio_test = Servicio(BaseDatosMock())
```

### Null Object

```python
class Logger:
    def log(self, msg): ...

class NullLogger(Logger):
    def log(self, msg): pass  # No-op

def procesar(logger: Logger = NullLogger()):
    logger.log("Iniciando...")

procesar()              # Silencioso
procesar(LoggerReal())  # Loggea
```

### Module Singleton (Pythonic)

```python
# database.py
class _Pool:
    def __init__(self): self.conexiones = []

pool = _Pool()  # Instancia única al importar

# Uso
from database import pool
pool.conexiones.append(conn)
```

---

## Resumen: Cuándo usar cada uno

| Problema | Patrón |
|----------|--------|
| Crear objetos sin especificar clase exacta | Factory Method / Abstract Factory |
| Construir objeto complejo paso a paso | Builder |
| Una sola instancia global | Singleton (o module-level) |
| Clonar objetos existentes | Prototype |
| Interfaz incompatible | Adapter |
| Añadir comportamiento dinámicamente | Decorator |
| Simplificar subsistema complejo | Facade |
| Controlar acceso / lazy loading | Proxy |
| Cambiar algoritmo en runtime | Strategy |
| Notificar cambios a múltiples | Observer |
| Encapsular petición como objeto | Command |
| Algoritmo con pasos variables | Template Method |
| Comportamiento según estado | State |
| Recorrer colección sin exponer estructura | Iterator |
| Desacoplar dependencias | Dependency Injection |
| Evitar checks de None | Null Object |

---

## Anti-patrones a evitar

| Anti-patrón | Problema | Solución |
|-------------|----------|----------|
| **God Object** | Clase que hace todo | Single Responsibility, separar |
| **Singleton abusivo** | Estado global oculto | Dependency Injection |
| **Factory innecesario** | Complejidad sin necesidad | Constructor directo |
| **Herencia profunda** | Frágil, acoplado | Composición + Protocol |
| **Patrón por patrón** | Over-engineering | KISS, YAGNI |

---

---
## 🎯 Ejercicios

Practica patrones en [ejercicios.md](../03-poo/ejercicios.md#22--patrones-de-diseño).

**Mini-ejercicio**: Implementa **Adapter**: clase `EnchufeEuropeo` y `EnchufeAmericano`. Adaptador que permite conectar uno al otro.

---

## Véase también

- [18-herencia-polimorfismo](./18-herencia-polimorfismo.md) — Strategy, Template Method con herencia
- [20-clases-abstractas](./20-clases-abstractas.md) — ABC para contratos
- [11-funciones-avanzadas](../02-avanzado/11-funciones-avanzadas.md) — Decoradores como patrón
- [14-context-managers](../02-avanzado/14-context-managers.md) — Resource management patterns
- [ejercicios.md](../03-poo/ejercicios.md) — Práctica recomendada