# 📝 Ejercicios — 04 Ecosistema

---

## 23 — Archivos y persistencia

### Ejercicio 23.1 — Notas en JSON
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: json, open, with
- **Criterio de éxito**: Programa de notas que guarda/lee en `notas.json`. CRUD completo con persistencia.

### Ejercicio 23.2 — CSV a SQLite
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: csv, sqlite3
- **Criterio de éxito**: Leer CSV de estudiantes, crear BD SQLite con tabla, insertar datos y permitir consultas.

### Ejercicio 23.3 — Backup automático
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: shutil, datetime, pathlib, zipfile
- **Criterio de éxito**: Script que comprime un directorio en .zip con nombre con fecha, mantiene solo últimos 5 backups.

---

## 24 — pathlib y os

### Ejercicio 24.1 — Organizador de archivos
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: Path, glob, shutil
- **Criterio de éxito**: Script que organiza ~/Downloads en carpetas: Imágenes, Documentos, Videos, Otros según extensión.

### Ejercicio 24.2 — Árbol de directorios
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: Path, rglob, recursión
- **Criterio de éxito**: Función `mostrar_arbol(ruta)` que imprime árbol jerárquico con indentación.

### Ejercicio 24.3 — Watcher de cambios
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: os.stat, hashlib, time.sleep
- **Criterio de éxito**: Script que monitorea un directorio cada 5s y muestra qué archivos cambiaron (por hash).

---

## 25 — Testing

### Ejercicio 25.1 — Tests de calculadora
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: pytest, assert
- **Criterio de éxito**: Batería de tests para funciones matemáticas. Incluir casos normales, borde y error.

### Ejercicio 25.2 — Fixtures + parametrize
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: @pytest.fixture, @pytest.mark.parametrize
- **Criterio de éxito**: Tests para clase `Usuario` con fixture que crea instancia. Parametrize para múltiples casos.

### Ejercicio 25.3 — Mock de API
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: unittest.mock, pytest-mock
- **Criterio de éxito**: Función que llama a API externa. Testear con mock para no hacer llamadas reales.

---

## 26 — Tooling

### Ejercicio 26.1 — Configurar proyecto
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: pyproject.toml, ruff, mypy
- **Criterio de éxito**: Crear pyproject.toml con ruff y mypy configurados. Ejecutar ambos sobre un archivo con errores.

### Ejercicio 26.2 — pre-commit hook
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: pre-commit, .pre-commit-config.yaml
- **Criterio de éxito**: Configurar pre-commit con hooks de ruff y trailing-whitespace. Verificar que rechaza código sucio.

### Ejercicio 26.3 — CI/CD básico
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: GitHub Actions, YAML
- **Criterio de éxito**: Workflow de GitHub Actions que ejecuta ruff, mypy, pytest en cada push.

---

## 27 — Logging y debugging

### Ejercicio 27.1 — Logger configurable
- **Dificultad**: 🟢 Fácil
- **XP**: 10 (+5 first try)
- **Prerrequisitos**: logging, niveles
- **Criterio de éxito**: Script con 4 niveles de log. Configurable por variable de entorno LOG_LEVEL.

### Ejercicio 27.2 — Debug con pdb
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: pdb, breakpoint()
- **Criterio de éxito**: Función con bug intencional. Documentar el proceso de debugging paso a paso con pdb.

### Ejercicio 27.3 — Profiler
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: time, cProfile, pstats
- **Criterio de éxito**: Comparar rendimiento de 3 implementaciones del mismo problema. Identificar cuellos de botella con profile.

---

## 28 — Packaging

### Ejercicio 28.1 — Paquete simple
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: pyproject.toml, src layout
- **Criterio de éxito**: Crear paquete instalable con `pip install -e .`. Una función que se importa correctamente.

### Ejercicio 28.2 — CLI con entry point
- **Dificultad**: 🟡 Medio
- **XP**: 25 (+5 first try)
- **Prerrequisitos**: scripts, entry_points, argparse
- **Criterio de éxito**: Paquete con CLI entry point. `mi-comando --help` funciona después de pip install.

### Ejercicio 28.3 — Publicar en TestPyPI
- **Dificultad**: 🔴 Difícil
- **XP**: 50 (+5 first try)
- **Prerrequisitos**: build, twine, TestPyPI
- **Criterio de éxito**: Paquete completo con README, LICENSE, versión. Publicado en TestPyPI. Instalable desde ahí.
