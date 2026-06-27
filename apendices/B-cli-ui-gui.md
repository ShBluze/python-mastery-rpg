# Apéndice B — CLI vs UI vs GUI + Runtime

Definiciones claras para diferenciar conceptos que a menudo se confunden.

---

## CLI (Command Line Interface)

**Definición:** Interfaz donde el usuario interactúa con el sistema escribiendo comandos de texto en una consola o terminal.

**Características técnicas:**
- Interacción basada en texto (stdin/stdout/stderr)
- Entrada mediante comandos estructurados (`comando --flag valor`)
- Salida textual (logs, tablas, JSON, texto plano)
- Muy utilizada por desarrolladores, DevOps, administradores de sistemas
- Alta eficiencia para tareas repetitivas, automatización, scripting
- Fácil de probar, documentar y versionar
- Accesible vía SSH, CI/CD, contenedores

**Ejemplos:**
| Herramienta | Tipo |
|-------------|------|
| bash, zsh, fish, PowerShell | Shell interactivo |
| `git`, `docker`, `kubectl`, `terraform`, `aws-cli` | CLI tools |
| `python -m http.server`, `npm run build` | Comandos de runtime |
| Scripts propios (`./deploy.sh`, `python migrate.py`) | Automatización |

**Cuándo usar CLI:**
- Automatización / CI/CD
- Administración de servidores
- Herramientas de desarrollo (linters, test runners, migraciones)
- Procesamiento por lotes (batch)
- Entornos sin interfaz gráfica (servidores, contenedores)

---

## UI (User Interface) — Concepto general

**Definición:** Cualquier medio mediante el cual el usuario interactúa con un sistema.

> La **CLI es un tipo de UI**. También lo son: GUI, VUI (voz), TUI (terminal UI), API (máquina a máquina).

**Clasificación por modalidad:**

| Modalidad | Ejemplo | Usuario objetivo |
|-----------|---------|------------------|
| **CLI** | Terminal, scripts | Devs, admins, automatización |
| **GUI** | App escritorio, web, móvil | Usuario final general |
| **TUI** | `htop`, `lazygit`, `textual` apps | Devs en terminal |
| **VUI** | Alexa, Siri, Google Assistant | Usuario final (voz) |
| **API** | REST, GraphQL, gRPC | Otros sistemas / microservicios |

---

## GUI (Graphical User Interface)

**Definición:** Interfaz visual basada en elementos gráficos: ventanas, botones, formularios, iconos, menús, drag-and-drop, gráficos.

**Características:**
- Feedback visual inmediato
- Descubrimiento por exploración (affordances)
- Curva de aprendizaje inicial más suave para no técnicos
- Requiere más recursos (RAM, GPU, pantalla)
- Difícil de automatizar / testear end-to-end

**Ejemplos por tecnología:**

| Stack | Tipo | Ejemplos |
|-------|------|----------|
| **Web** | HTML/CSS/JS + React/Vue/Svelte | Dashboard, SaaS, e-commerce |
| **Desktop (Python)** | Tkinter, PySide6/Qt, wxPython, Dear PyGui | Herramientas internas, apps científicas |
| **Desktop (Cross-platform)** | Electron, Tauri, Flutter, .NET MAUI | VS Code, Discord, Slack |
| **Móvil** | SwiftUI, Jetpack Compose, React Native, Flutter | Apps iOS/Android |
| **Terminal (TUI)** | Textual, Rich, curses, blessed | `lazygit`, `btop`, `k9s` |

---

## Comparativa rápida: CLI vs GUI

| Aspecto | CLI | GUI |
|---------|-----|-----|
| **Curva de aprendizaje** | Alta (memorizar comandos) | Baja (exploración visual) |
| **Automatización** | Nativa (scripts, pipes) | Difícil (requiere herramientas extra) |
| **Descubrimiento** | `man`, `--help`, `tab` | Menús, tooltips, icons |
| **Precisión** | Alta (parámetros exactos) | Media (clicks, arrastres) |
| **Repetibilidad** | Perfecta (historial, scripts) | Manual, propensa a errores |
| **Remoto/SSH** | Nativo | Requiere X11/Wayland forwarding o VNC/RDP |
| **Accesibilidad** | Lectores de pantalla funcionan bien | Requiere ARIA, semántica, testing |
| **Pipelines CI/CD** | Trivial | Complejo (headless browsers, playwright) |

---

## Runtime vs Compile-time

### Definiciones

| Concepto | Momento | Qué ocurre |
|----------|---------|------------|
| **Compile-time** | Antes de ejecutar | Análisis estático: tipos, sintaxis, imports, dead code |
| **Runtime** | Durante la ejecución | El código corre realmente: I/O, memoria, red, excepciones |

### Por lenguaje

| Lenguaje | Compile-time | Runtime |
|----------|--------------|---------|
| **C / C++ / Rust / Go** | Compilación nativa (binario) | Ejecución directa del binario |
| **Java / Kotlin / Scala** | `javac` → bytecode (`.class`) | JVM interpreta/JIT compila bytecode |
| **TypeScript** | `tsc` → `.js` + type checking | Node.js / Browser ejecuta JS |
| **Python** | **Ninguno nativo** (opcional: mypy/pyright) | Interpreter CPython ejecuta `.py` |
| **JavaScript** | Ninguno (JIT en runtime) | V8/SpiderMonkey compila en caliente |

### Python: particularidades

```python
# Type hints: SOLO compile-time (con mypy/pyright)
def sumar(a: int, b: int) -> int:
    return a + b

print(sumar(2, "3"))  # "23" → Runtime: SE EJECUTA sin error
# mypy sumar.py → ERROR: Argument 2 has incompatible type "str"
```

**Implicaciones prácticas:**
- Los type hints **no protegen en runtime** (salvo que uses `pydantic`, `beartype`, `typeguard`)
- Las validaciones de datos externos **deben hacerse en runtime** (`isinstance`, `pydantic`, `marshmallow`)
- `isinstance()` **sí es runtime** — úsalo para validar entradas de red, archivos, user input

---

## Decision matrix: ¿CLI, TUI o GUI?

| Requisito | Recomendación |
|-----------|---------------|
| Solo developers / CI/CD / servidores | **CLI** (Typer, Click, argparse) |
| Developers que viven en terminal, datos tabulares | **TUI** (Textual, Rich) |
| Usuario final no técnico / visualización rica | **GUI Web** (FastAPI + React, Streamlit, Gradio) |
| App de escritorio multiplataforma nativa | **PySide6/Qt** o **Tauri** |
| Herramienta interna rápida, datos simples | **Tkinter** o **Streamlit** |
| Prototipo de ML/Data Science para stakeholders | **Gradio** / **Streamlit** / **Marimo** |

---

## Recursos relacionados

- [Apéndice A: Glosario técnico](./A-glosario-tecnico.md) — legacy, fallback, boilerplate, code smell
- [Apéndice C: Cheatsheets](./C-cheatsheets.md) — Referencias rápidas
- [05-especializaciones/32-automatizacion-cli.md](../05-especializaciones/32-automatizacion-cli.md) — CLI tools en Python
- [05-especializaciones/33-gui.md](../05-especializaciones/33-gui.md) — GUI en Python (Tkinter, PySide6, Textual)