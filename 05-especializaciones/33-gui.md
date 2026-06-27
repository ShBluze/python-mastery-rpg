# 33 — Interfaces Gráficas (GUI)

> `tkinter`, `PySide6` / `PyQt6`, `flet`, `nicegui`, diseño de UI, eventos, layouts.

---

## `tkinter` — GUI Nativa (Baterías Incluidas)

```python
import tkinter as tk

root = tk.Tk()
root.title("Mi App")
root.geometry("400x300")

label = tk.Label(root, text="Hola mundo", font=("Arial", 14))
label.pack()

root.mainloop()
```

### La ventana principal (`root`)

```python
root = tk.Tk()

# Apariencia
root.title("Título")
root.geometry("800x600")           # ancho x alto
root.minsize(400, 300)
root.maxize(1200, 900)
root.resizable(True, False)       # (ancho, alto)
root.configure(bg="lightblue")
root.iconbitmap("icono.ico")

# Estado
root.state("zoomed")              # Maximizada
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.95)   # Transparencia

# Eventos
root.bind("<Escape>", lambda e: root.quit())
root.protocol("WM_DELETE_WINDOW", al_cerrar)

# Ciclo de vida
root.mainloop()    # Inicia bucle
root.quit()        # Cierra bucle (no destruye)
root.destroy()     # Destruye ventana
```

### Widgets básicos

```python
from tkinter import ttk

# Label
label = tk.Label(root, text="Texto", font=("Arial", 12), fg="blue", bg="yellow")
label.pack()

# Button
def click():
    print("Clic!")

btn = tk.Button(root, text="Presionar", command=click)
btn.pack()

# Entry (campo de texto)
entry = tk.Entry(root, width=30)
entry.pack()
texto = entry.get()

# Text (multilínea)
text = tk.Text(root, height=5, width=40)
text.pack()
contenido = text.get("1.0", tk.END)

# Checkbutton
var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Aceptar", variable=var)
check.pack()

# Radiobutton
color = tk.StringVar(value="rojo")
tk.Radiobutton(root, text="Rojo", variable=color, value="rojo").pack()
tk.Radiobutton(root, text="Azul", variable=color, value="azul").pack()

# Combobox (ttk)
combo = ttk.Combobox(root, values=["Opción A", "Opción B", "Opción C"])
combo.pack()

# Spinbox
spin = tk.Spinbox(root, from_=0, to=100, width=5)
spin.pack()
```

### Layouts

| Layout | Descripción                          |
|--------|--------------------------------------|
| `pack`| Apila widgets (top/bottom/left/right) |
| `grid`| Rejilla filas x columnas             |
| `place`| Coordenadas absolutas (x, y, w, h)  |

#### `pack`

```python
tk.Label(root, text="Arriba").pack(side="top")
tk.Label(root, text="Abajo").pack(side="bottom")
tk.Label(root, text="Izquierda").pack(side="left")
tk.Label(root, text="Derecha").pack(side="right", expand=True, fill="both")
```

#### `grid`

```python
label1 = tk.Label(root, text="Fila 0, Col 0")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Fila 0, Col 1")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Fila 1, Col 0-1", bg="lightblue")
label3.grid(row=1, column=0, columnspan=2)

# rowspan
label4 = tk.Label(root, text="Ocupa 2 filas")
label4.grid(row=0, column=2, rowspan=2)
```

#### `place`

```python
label = tk.Label(root, text="Absoluto")
label.place(x=50, y=100, width=200, height=30)
```

### Diálogos

```python
from tkinter import messagebox, filedialog, colorchooser

messagebox.showinfo("Info", "Operación completada")
messagebox.showwarning("Cuidado", "Archivo existente")
messagebox.showerror("Error", "No se pudo guardar")
ok = messagebox.askyesno("Confirmar", "¿Seguro?")

archivo = filedialog.askopenfilename(filetypes=[("Textos", "*.txt")])
ruta = filedialog.asksaveasfilename(defaultextension=".txt")
carpeta = filedialog.askdirectory()
color = colorchooser.askcolor(title="Elige color")
```

### Canvas — Dibujo y gráficos

```python
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_line(10, 10, 200, 100, fill="red", width=2)
canvas.create_rectangle(50, 50, 150, 150, fill="blue", stipple="gray25")
canvas.create_oval(200, 50, 300, 150, fill="green")
canvas.create_text(200, 250, text="Dibujo", font=("Arial", 20))
```

### Eventos

```python
def click_izquierdo(event):
    print(f"Clic en ({event.x}, {event.y})")

def tecla_presionada(event):
    print(f"Tecla: {event.keysym}")

def mover_raton(event):
    print(f"Ratón en ({event.x}, {event.y})")

root.bind("<Button-1>", click_izquierdo)       # Clic izquierdo
root.bind("<Button-3>", click_izquierdo)       # Clic derecho
root.bind("<Key>", tecla_presionada)           # Cualquier tecla
root.bind("<Escape>", lambda e: root.quit())   # Tecla específica
root.bind("<Motion>", mover_raton)             # Movimiento ratón
```

### Ejemplo completo: formulario

```python
import tkinter as tk
from tkinter import ttk, messagebox

def enviar():
    nombre = entry_nombre.get()
    edad = spin_edad.get()
    intereses = []
    if var_python.get(): intereses.append("Python")
    if var_data.get(): intereses.append("Data")
    pais = combo_pais.get()

    mensaje = f"Nombre: {nombre}\nEdad: {edad}\nIntereses: {', '.join(intereses)}\nPaís: {pais}"
    messagebox.showinfo("Datos", mensaje)

root = tk.Tk()
root.title("Formulario")
root.geometry("400x350")

# Grid layout
tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Edad:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
spin_edad = tk.Spinbox(root, from_=0, to=120, width=5)
spin_edad.grid(row=1, column=1, sticky="w", padx=5, pady=5)

tk.Label(root, text="Intereses:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
var_python = tk.BooleanVar()
tk.Checkbutton(root, text="Python", variable=var_python).grid(row=2, column=1, sticky="w")
var_data = tk.BooleanVar()
tk.Checkbutton(root, text="Data Science", variable=var_data).grid(row=3, column=1, sticky="w")

tk.Label(root, text="País:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
combo_pais = ttk.Combobox(root, values=["España", "México", "Argentina", "Chile", "Colombia"])
combo_pais.grid(row=4, column=1, padx=5, pady=5)
combo_pais.current(0)

tk.Button(root, text="Enviar", command=enviar, bg="green", fg="white").grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
```

---

## `PySide6` / `PyQt6` — GUIs Profesionales

```bash
pip install PySide6
```

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        label = QLabel("Hola desde PySide6")
        btn = QPushButton("Clic")
        btn.clicked.connect(lambda: label.setText("Clickeado!"))

        layout.addWidget(label)
        layout.addWidget(btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = Ventana()
window.show()
sys.exit(app.exec())
```

> 💡 `PySide6` es la versión oficial (Qt Company). `PyQt6` es la alternativa GPL. Son casi idénticas.

---

## `flet` — GUIs Modernas (Web + Desktop)

```bash
pip install flet
```

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nombre = ft.TextField(label="Nombre", width=200)
    saludo = ft.Text()

    def click(e):
        saludo.value = f"Hola {nombre.value}!"
        page.update()

    page.add(
        ft.Row([nombre, ft.ElevatedButton("Saludar", on_click=click)], alignment=ft.MainAxisAlignment.CENTER),
        saludo,
    )

ft.app(target=main)
```

> 💡 `flet` renderiza en web/nativo con Flutter. Ideal para GUIs rápidas sin HTML.

---

## `nicegui` — GUIs con Python Puro

```bash
pip install nicegui
```

```python
from nicegui import ui

ui.label("Hola mundo")
ui.button("Clic", on_click=lambda: ui.notify("Clickeado!"))

name = ui.input("Nombre")
ui.button("Saludar", on_click=lambda: ui.notify(f"Hola {name.value}!"))

ui.run()
```

> 💡 `nicegui` genera UI web desde Python puro. Sin HTML/CSS/JS.

---

## Comparativa de Frameworks GUI

| Framework    | Tipo          | Platformas       | Curva   | Ideal para                     |
|-------------|---------------|------------------|---------|--------------------------------|
| `tkinter`   | Nativo        | Windows/Linux/Mac| Baja    | Herramientas internas simples  |
| `PySide6`   | Profesional   | Windows/Linux/Mac| Alta    | Apps empresariales, editoras   |
| `flet`      | Moderno       | Web + Desktop    | Media   | Prototipos rápidos, apps web   |
| `nicegui`   | Moderno       | Web              | Baja    | Dashboards, herramientas web   |
| `kivy`      | Multi-touch   | Win/Linux/Mac/Android/iOS| Alta | Apps móviles (kivy) |

---

## Diseño de UI (Principios)

### Estados de la UI

Toda UI es una máquina de estados:

| Estado     | Qué mostrar                        |
|------------|------------------------------------|
| `idle`     | Estado inicial, esperando acción   |
| `loading`  | Spinner / barra de progreso        |
| `empty`    | "No hay datos", mensaje + acción   |
| `error`    | Mensaje claro + botón reintentar   |
| `success`  | Confirmación de operación exitosa  |

### Buenas prácticas

- Un CTA (Call to Action) principal por pantalla
- Feedback inmediato (loading, error, success)
- Mensajes de error específicos ("La contraseña debe tener 8+ caracteres")
- Atajos de teclado para acciones frecuentes
- Consistencia visual (colores, espaciado, tipografía)

---

## Proyectos Recomendados

| Proyecto                     | Framework sugerido        |
|------------------------------|---------------------------|
| Calculadora                  | `tkinter`                 |
| Editor de texto              | `tkinter` / `PySide6`     |
| Gestor de tareas (To-Do)    | `tkinter` + `sqlite3`     |
| Dashboard de datos           | `nicegui` / `flet`        |
| Visor/editor de imágenes     | `PySide6` + `Pillow`      |
| Cliente de escritorio API    | `PySide6` + `httpx`       |

---

---
## 🎯 Ruta completa

La ruta GUI se ha expandido. Consulta [`33-gui/README.md`](33-gui/README.md) para el plan de estudio detallado.

---

## Véase también

- [32-automatizacion-cli](./32-automatizacion-cli.md) — CLI vs GUI
- [29-web](./29-web.md) — GUIs web con Flask/FastAPI
- [B-cli-ui-gui](../apendices/B-cli-ui-gui.md) — CLI, UI, GUI concepts
- [33-gui/README.md](33-gui/README.md) — Ruta GUI completa
