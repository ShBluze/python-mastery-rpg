<<<<<<< HEAD
# python-mastery-rpg
Aprende Python como si fuera un juego: XP, niveles, bosses, streaks y progresión secuencial. 94 archivos, 84+ ejercicios. Markdown puro.
=======
# 🎮 Python Guide — RPG Educativo

> Una guía de Python convertida en juego educativo con XP, niveles, bosses y progresión secuencial.

🎯 **Empieza aquí**: [00-roadmap.md](00-roadmap.md) — Ruta de aprendizaje obligatoria
📊 **Tu progreso**: [progress.md](progress.md) — Checklist global
🎮 **Tu perfil**: [gamification.md](gamification.md) — XP, nivel, racha, logros
⚔️ **Estado del mundo**: [rpg-system.md](rpg-system.md) — HP, bosses, dificultad dinámica

## 📚 Navegación rápida

### 🟢 01-fundamentos — Base sólida
| # | Archivo | Temas clave |
|---|---------|-------------|
| 01 | [variables-tipos](./01-fundamentos/01-variables-tipos.md) | Variables, operadores, tipos básicos, casting |
| 02 | [control-flujo](./01-fundamentos/02-control-flujo.md) | if/elif/else, match/case, for, while, break/continue |
| 03 | [funciones-esenciales](./01-fundamentos/03-funciones-esenciales.md) | def, params, *args/**kwargs, return, lambda básico, desempaquetado |
| 04 | [estructuras-datos](./01-fundamentos/04-estructuras-datos.md) | list, tuple, dict, set, métodos, tabla comparativa |
| 05 | [comprehensions-generators](./01-fundamentos/05-comprehensions-generators.md) | List/dict/set comp, generadores, lazy vs eager |
| 06 | [strings-formateo](./01-fundamentos/06-strings-formateo.md) | f-strings, format(), slices, escapes, I/O básico |
| 07 | [manejo-errores](./01-fundamentos/07-manejo-errores.md) | try/except, ExceptionGroup, custom exceptions |
| 08 | [modulos-imports](./01-fundamentos/08-modulos-imports.md) | import, from, __main__, stdlib, paquetes propios |
| 09 | [comentarios-docstrings](./01-fundamentos/09-comentarios-docstrings.md) | #, """docstrings""", convenciones |

### 🟡 02-avanzado — Python profesional
| # | Archivo | Temas clave |
|---|---------|-------------|
| 10 | [type-hints](./02-avanzado/10-type-hints.md) | Anotaciones, Union, Optional, Generic, Protocol, TypedDict |
| 11 | [funciones-avanzadas](./02-avanzado/11-funciones-avanzadas.md) | Closures, decoradores, callbacks, HOF, recursión, async |
| 12 | [programacion-funcional](./02-avanzado/12-programacion-funcional.md) | map/filter/reduce, itertools, functools, inmutabilidad |
| 13 | [async-concurrencia](./02-avanzado/13-async-concurrencia.md) | asyncio, TaskGroup, threading, multiprocessing, executors |
| 14 | [context-managers](./02-avanzado/14-context-managers.md) | with, @contextmanager, ExitStack, suppress |

### 🔵 03-poo — Diseño orientado a objetos
| # | Archivo | Temas clave |
|---|---------|-------------|
| 15 | [clases-objetos](./03-poo/15-clases-objetos.md) | class, __init__, atributos, visibilidad (_/_) |
| 16 | [tipos-metodos](./03-poo/16-tipos-metodos.md) | instance, @classmethod, @staticmethod, @property |
| 17 | [metodos-magicos](./03-poo/17-metodos-magicos.md) | __str__/__repr__, __eq/__hash__, __getitem__, __len__, operadores |
| 18 | [herencia-polimorfismo](./03-poo/18-herencia-polimorfismo.md) | Herencia, super(), MRO, mixins, polimorfismo |
| 19 | [encapsulamiento](./03-poo/19-encapsulamiento.md) | Name mangling, properties, ref counting, __del__ |
| 20 | [clases-abstractas](./03-poo/20-clases-abstractas.md) | ABC, @abstractmethod, Protocol, runtime_checkable |
| 21 | [dataclasses-pydantic](./03-poo/21-dataclasses-pydantic.md) | @dataclass, slots, pydantic, validación, serialización |
| 22 | [patrones-diseno](./03-poo/22-patrones-diseno.md) | Factory, Strategy, Observer, Builder, etc. en Python |

### 🟣 04-ecosistema — Herramientas de producción
| # | Archivo | Temas clave |
|---|---------|-------------|
| 23 | [archivos-persistencia](./04-ecosistema/23-archivos-persistencia.md) | txt, csv, json, pickle, sqlite, pathlib |
| 24 | [pathlib-os](./04-ecosistema/24-pathlib-os.md) | Path, os, shutil, glob, walk, variables entorno |
| 25 | [testing](./04-ecosistema/25-testing.md) | pytest, fixtures, mock, parametrize, coverage |
| 26 | [tooling](./04-ecosistema/26-tooling.md) | ruff, mypy, black, uv, pyproject.toml, pre-commit |
| 27 | [logging-debugging](./04-ecosistema/27-logging-debugging.md) | logging, structlog, rich, pdb, icecream |
| 28 | [packaging](./04-ecosistema/28-packaging.md) | build, twine, src-layout, versionado |

### 🟠 05-especializaciones — Referencia rápida (esqueletos)
| # | Archivo | Stack |
|---|---------|-------|
| 29 | [web](./05-especializaciones/29-web.md) | FastAPI, Django, Flask |
| 30 | [data-science](./05-especializaciones/30-data-science.md) | NumPy, Pandas, Matplotlib/Seaborn |
| 31 | [ia-ml](./05-especializaciones/31-ia-ml.md) | PyTorch, TensorFlow, Keras, sklearn |
| 32 | [automatizacion-cli](./05-especializaciones/32-automatizacion-cli.md) | click/typer, schedule, watchdog |
| 33 | [gui](./05-especializaciones/33-gui.md) | Tkinter, PySide6, Textual |

### 📚 Apéndices
| Archivo | Contenido |
|---------|-----------|
| [A-glosario-tecnico](./apendices/A-glosario-tecnico.md) | legacy, fallback, runtime, boilerplate, code smell, isinstance |
| [B-cli-ui-gui](./apendices/B-cli-ui-gui.md) | Definiciones CLI/UI/GUI, Runtime vs Compile-time |
| [C-cheatsheets](./apendices/C-cheatsheets.md) | Operadores, magic methods, built-ins, stdlib quick-ref |
| [D-recursos-roadmap](./apendices/D-recursos-roadmap.md) | Libros, cursos, newsletters, roadmap aprendizaje |

---

## 🔗 Convenciones de navegación

- **Cross-refs internos**: `[Texto](./ruta/archivo.md#ancla)` — rutas relativas
- **Anclas**: `### nombre-seccion` → `#nombre-seccion` (kebab-case)
- **Callouts**: `> 💡 Tip`, `> ⚠️ Cuidado`, `> 🔑 Clave`, `> 🆕 Python 3.11+`

## 📦 Origen
Contenido migrado desde `../Usando Python.md` (archivo monolítico de 4075 líneas) reorganizado en arquitectura modular.
>>>>>>> dadb6f4 (feat: sistema RPG educativo completo)
