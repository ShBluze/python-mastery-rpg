# 32 — Automatización & CLI

> Scripts, `os`, `shutil`, `pathlib`, `schedule`, `click`, `typer`, `argparse`, tareas repetitivas.

---

## CLIs con la Biblioteca Estándar

### `argparse`

```python
# cli.py
import argparse

parser = argparse.ArgumentParser(description="Procesa archivos")
parser.add_argument("input", help="Archivo de entrada")
parser.add_argument("-o", "--output", default="salida.txt", help="Archivo de salida")
parser.add_argument("-v", "--verbose", action="store_true", help="Modo verbose")
parser.add_argument("--limit", type=int, default=10, help="Límite de resultados")

args = parser.parse_args()
print(f"Procesando {args.input} → {args.output}")
```

```bash
python cli.py datos.csv -o resultado.json --verbose --limit 100
```

### `sys.argv` (mínimo)

```python
import sys

if len(sys.argv) < 2:
    print("Uso: script.py <nombre>")
    sys.exit(1)

nombre = sys.argv[1]
print(f"Hola {nombre}")
```

---

## `click` — CLI Elegante

```bash
pip install click
```

```python
import click

@click.command()
@click.argument("nombre")
@click.option("--saludo", default="Hola", help="Texto del saludo")
@click.option("--mayusculas", is_flag=True, help="Convertir a mayúsculas")
@click.option("--count", default=1, type=int, help="Repeticiones")
def saludar(nombre, saludo, mayusculas, count):
    """Saluda a NOMBRE de forma personalizada."""
    texto = f"{saludo}, {nombre}!"
    if mayusculas:
        texto = texto.upper()
    for _ in range(count):
        click.echo(texto)

if __name__ == "__main__":
    saludar()
```

```bash
python cli.py Ana --saludo "Qué tal" --mayusculas --count 3
```

### Grupos de comandos

```python
@click.group()
def cli():
    pass

@cli.command()
@click.argument("archivo")
def procesar(archivo):
    click.echo(f"Procesando {archivo}")

@cli.command()
@click.argument("archivo")
def limpiar(archivo):
    click.echo(f"Limpiando {archivo}")

if __name__ == "__main__":
    cli()
```

---

## `typer` — CLI Moderna (tipos)

```bash
pip install typer
```

```python
import typer

app = typer.Typer()

@app.command()
def saludar(nombre: str, mayusculas: bool = False, repeticiones: int = 1):
    """Saluda a NOMBRE."""
    texto = f"Hola {nombre}"
    if mayusculas:
        texto = texto.upper()
    for _ in range(repeticiones):
        print(texto)

@app.command()
def adios(nombre: str):
    print(f"Adiós {nombre}")

if __name__ == "__main__":
    app()
```

```bash
python cli.py saludar Ana --mayusculas --repeticiones 3
python cli.py adios Ana
```

---

## Automatización de Archivos

### `pathlib` — Rutas Modernas

```python
from pathlib import Path

cwd = Path.cwd()
home = Path.home()

# Crear
Path("carpeta/subcarpeta").mkdir(parents=True, exist_ok=True)

# Listar
for f in Path(".").iterdir():
    if f.is_file():
        print(f.name, f.suffix, f.stat().st_size)

# Glob
for py in Path("src").rglob("*.py"):
    print(py)

# Leer/Escribir
Path("salida.txt").write_text("contenido")
texto = Path("entrada.txt").read_text()
```

### `shutil` — Operaciones de Alto Nivel

```python
import shutil
from pathlib import Path

# Copiar
shutil.copy("origen.txt", "destino.txt")
shutil.copytree("carpeta/", "backup/", dirs_exist_ok=True)

# Mover
shutil.move("temporal.txt", "archivos/")

# Eliminar
shutil.rmtree("carpeta_temporal/")

# Archivos comprimidos
shutil.make_archive("backup", "zip", "mi_carpeta/")
shutil.unpack_archive("backup.zip", "extraido/")
```

### `os` — Operaciones de Sistema

```python
import os

os.environ["API_KEY"]  # Variables de entorno
os.getcwd()            # Directorio actual
os.listdir(".")        # Listar directorio
os.rename("a.txt", "b.txt")
os.remove("temporal.txt")
os.system("echo hola")   # Ejecutar comando shell
```

---

## Tareas Programadas

### `schedule`

```bash
pip install schedule
```

```python
import schedule
import time

def backup():
    print("Haciendo backup...")
    shutil.make_archive("backup", "zip", "datos/")

def limpiar_logs():
    for f in Path("logs").glob("*.log"):
        if f.stat().st_mtime < time.time() - 86400 * 7:  # 7 días
            f.unlink()

schedule.every().day.at("03:00").do(backup)
schedule.every().hour.do(limpiar_logs)
schedule.every().monday.do(backup)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Cron (Linux/macOS)

```bash
# crontab -e
0 3 * * * /usr/bin/python3 /home/user/scripts/backup.py
*/30 * * * * /usr/bin/python3 /home/user/scripts/check_status.py
```

---

## Automatización de Correos

```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Cuerpo del mensaje")
msg["Subject"] = "Asunto"
msg["From"] = "tu@email.com"
msg["To"] = "destino@email.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("tu@email.com", "contraseña")
    server.send_message(msg)
```

> ⚠️ Usa variables de entorno o un gestor de secretos para las credenciales.

---

## Proyectos de Automatización

| Proyecto                      | Librerías                            |
|-------------------------------|--------------------------------------|
| Renombrador masivo de archivos| `pathlib`, `re`                      |
| Backup automático             | `shutil`, `schedule`, `pathlib`      |
| Monitor de sistema            | `psutil`, `rich`                     |
| Web scraper                   | `httpx`, `beautifulsoup4`, `selenium`|
| Bot de Telegram               | `python-telegram-bot`                |
| Descargador de videos         | `yt-dlp`                             |

---

---
## 🎯 Ruta completa

La ruta Automatización se ha expandido. Consulta [`32-automatizacion-cli/README.md`](32-automatizacion-cli/README.md) para el plan detallado.

---

## Véase también

- [24-pathlib-os](../04-ecosistema/24-pathlib-os.md) — `pathlib`, `os`, `shutil`
- [29-web](./29-web.md) — APIs y webhooks
- [33-gui](./33-gui.md) — Interfaces gráficas
- [32-automatizacion-cli/README.md](32-automatizacion-cli/README.md) — Ruta Automatización completa
