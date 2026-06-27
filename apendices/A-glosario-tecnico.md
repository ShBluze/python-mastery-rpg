# Apéndice A — Glosario técnico

Definiciones de términos recurrentes en ingeniería de software y Python.

---

## legacy code

**Código legacy** es código existente que ya está en producción y que cumple al menos una de estas condiciones:

- Fue escrito hace tiempo
- Usa tecnologías antiguas o estilos obsoletos
- No tiene tests (o muy pocos)
- No tiene tipado
- Es difícil de modificar sin romper algo
- Nadie quiere tocarlo sin miedo

> 👉 **No significa "mal código"**. Significa:
> > _Código crítico para el negocio, pero costoso de mantener o evolucionar._

### Por qué existe tanto legacy code

- Las empresas **no pueden parar sistemas que funcionan**
- Migrar todo tiene coste económico
- Muchas apps nacieron antes de TypeScript / tooling moderno

### Realidad profesional

Como junior o semi-junior:
- **Vas a tocar legacy code**
- Vas a **leer más código del que escribes**
- El tipado estricto suele introducirse **poco a poco** en proyectos legacy

---

## fallback

Un **fallback** es un mecanismo de respaldo: cuando algo no existe o falla, el sistema usa una alternativa por defecto.

En programación: un fallback es el comportamiento secundario que se ejecuta cuando el comportamiento principal no está disponible.

> fallback = alternativa automática cuando falta algo.

### Ejemplos

**1. `__str__` / `__repr__`**
```python
print(str(obj))
# Internamente:
# 1. Intenta obj.__str__()
# 2. Si no existe → fallback a obj.__repr__()
```

**2. Diccionarios**
```python
valor = diccionario.get("clave", "valor_por_defecto")
# Si la clave no existe → fallback al valor por defecto
```

**3. Herencia (MRO)**
```python
# Si una clase hija no tiene un método:
# Python busca en la clase padre → fallback dentro del MRO
```

**4. Web / Infraestructura**
```python
# Si un servidor no responde → se usa un servidor secundario (fallback)
```

---

## CLI (Command Line Interface)

Interfaz donde el usuario interactúa con el sistema escribiendo comandos de texto en una consola o terminal.

**Características técnicas:**
- Interacción basada en texto
- Entrada mediante comandos estructurados
- Salida textual
- Muy utilizada por desarrolladores y administradores de sistemas
- Alta eficiencia para tareas repetitivas y automatización (scripts)

**Ejemplos:**
- Terminal de Linux (bash, zsh, fish)
- PowerShell en Windows
- Consola de Node.js / Python REPL
- Herramientas: `git`, `docker`, `aws-cli`, `kubectl`, `terraform`

---

## UI (User Interface)

Concepto general de interfaz de usuario: cualquier medio mediante el cual el usuario interactúa con un sistema.

- La **CLI es un tipo de UI**
- Pero normalmente "UI" se refiere a **interfaz gráfica** (GUI)

---

## GUI (Graphical User Interface)

Interfaz visual basada en elementos gráficos:
- Ventanas, botones, formularios, iconos, menús, etc.

**Ejemplos:**
- Navegador web, app móvil, panel de configuración de Windows
- Aplicación hecha con React, PySide6, Tkinter, Electron, Tauri

---

## Runtime

**Runtime** es el momento en el que el programa se está ejecutando.

> 👉 Todo lo que ocurre **después de hacer `python app.py` o `node app.js`**.

### Comparación clave

| Fase | Qué ocurre |
|------|------------|
| **Compile-time** | Se analizan tipos, sintaxis, estructura |
| **Runtime** | El código se ejecuta realmente |

### Ejemplos por lenguaje

**JavaScript (dinámico)**
```javascript
function sumar(a, b) { return a + b; }
console.log(sumar(2, "3"));  // "23" → concatena strings
// compile-time: OK (no valida tipos)
// Runtime: Resultado "23" (error lógico silencioso)
```

**TypeScript (estático)**
```typescript
function sumar(a: number, b: number): number { return a + b; }
console.log(sumar(2, "3"));  // Error en compile-time
// Argument of type 'string' is not assignable to parameter of type 'number'
```

**Python (type hints — solo compile-time con herramientas)**
```python
def sumar(a: int, b: int) -> int:
    return a + b

print(sumar(2, "3"))  # "23" → se ejecuta sin error en runtime
# - Python ejecuta igual (type hints no afectan runtime)
# - El error es de lógica, no de tipos
# - Necesitas mypy/pyright para detectarlo antes
```

---

## boilerplate

Código repetitivo, estándar y poco específico que necesitas escribir para que algo funcione, pero que no aporta lógica de negocio ni valor directo.

> En términos prácticos: es el **"relleno obligatorio"** para poder empezar a trabajar.

### Definición clara
Boilerplate = código necesario pero redundante, que:
- Se repite en muchos archivos o proyectos
- Cambia muy poco entre usos
- No resuelve el problema principal

### Ejemplos

**JavaScript (antes de arrow functions)**
```javascript
var numbers = [1, 2, 3];
var doubled = numbers.map(function(n) { return n * 2; });
```

**Con arrow function (menos boilerplate)**
```javascript
var numbers = [1, 2, 3];
var doubled = numbers.map(n => n * 2);
```

**Python**
```python
# Menos boilerplate
lambda x: x * 2

# Más boilerplate
def duplicar(x):
    return x * 2
```

### Boilerplate vs claridad (importante)

Reducir boilerplate **no siempre es bueno**:

```python
# Menos boilerplate, peor legibilidad
lambda x, y, z: x + y + z if x > 0 else y - z

# Más boilerplate, mejor legibilidad
def calcular(x, y, z):
    if x > 0:
        return x + y + z
    else:
        return y - z
```

> **Regla profesional**: *menos boilerplate solo si no sacrificas claridad*

---

## code smell

Indicadores de que el código puede tener problemas de diseño (no necesariamente bugs, pero riesgos de mantenimiento).

### Casos comunes

1. **Funciones demasiado largas**
   - Hace más de una cosa
   - Tiene muchas ramas (if, for, try)
   - Difícil de leer de un vistazo
   - Cuesta testearla sin mocks complejos

   > No hay número mágico de líneas, pero si necesitas desplazarte mucho o leerla varias veces, es señal clara.

2. **¿Por qué es un code smell?**
   Viola directamente el **Principio de Responsabilidad Única (SRP)**.

   Cuando una función:
   - Valida datos
   - Aplica lógica de negocio
   - Accede a base de datos
   - Formatea la salida

   → Tiene 4 razones distintas para cambiar = mal diseño

---

## isinstance()

Función built-in para comprobar en **runtime** si un objeto es instancia de una clase o tipo determinado.

> A diferencia de los type hints, `isinstance()` **sí afecta al comportamiento del programa**, porque ejecuta una validación real.

```python
isinstance(objeto, tipo)
```

**Devuelve:**
- `True` si el objeto es del tipo indicado (o subclase)
- `False` en caso contrario

### Ejemplos básicos
```python
print(isinstance(5, int))           # True
print(isinstance("hola", str))      # True
print(isinstance(3.14, int))        # False
```

### Comprobación de varios tipos
```python
print(isinstance(5, (int, float)))      # True (5 es int)
print(isinstance("hola", (int, float))) # False
```

### Qué hace y qué NO hace

| ✅ `isinstance()` SÍ hace | ❌ `isinstance()` NO hace |
|---------------------------|---------------------------|
| Valida tipos en runtime | No es type hint |
| Permite controlar errores | No sustituye a `Union` |
| Imprescindible con datos externos | No mejora autocompletado |
| Funciona con herencia | No define contratos por sí solo |

---