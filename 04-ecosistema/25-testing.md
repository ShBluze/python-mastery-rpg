# 25 — Testing

> `pytest`, fixtures, parametrize, mock, coverage, property-based testing, TDD.

---

## `pytest` — Básico

```bash
pip install pytest pytest-cov pytest-mock
```

```python
# test_ejemplo.py
def sumar(a, b):
    return a + b

def test_suma_basica():
    assert sumar(2, 3) == 5

def test_suma_negativos():
    assert sumar(-1, 1) == 0
```

```bash
pytest                          # Descubre y ejecuta
pytest -v                       # Verbose
pytest -k "negativos"           # Filtra por nombre
pytest --co                    # Solo recolecta (dry-run)
```

---

## Fixtures — Setup/Teardown Reutilizable

```python
# conftest.py (compartido) o test_archivo.py
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def usuario_basico():
    return {"nombre": "Ana", "email": "ana@test.com", "activo": True}

@pytest.fixture
def db_mock():
    mock = MagicMock()
    mock.obtener_usuario.return_value = {"id": 1, "nombre": "Ana"}
    yield mock
    mock.close.assert_called_once()  # Teardown

def test_usuario_activo(usuario_basico):
    assert usuario_basico["activo"] is True

def test_db_mock(db_mock):
    u = db_mock.obtener_usuario(1)
    assert u["nombre"] == "Ana"
```

### Fixtures con parámetros

```python
@pytest.fixture(params=[1, 2, 3])
def numero(request):
    return request.param

def test_pares(numero):
    assert numero > 0
```

### Scope de fixtures

| Scope | Cuándo se ejecuta |
|-------|-------------------|
| `function` (default) | Cada test |
| `class` | Una vez por clase |
| `module` | Una vez por archivo |
| `session` | Una vez por sesión completa |

```python
@pytest.fixture(scope="session")
def conexion_db():
    conn = crear_conexion_real()
    yield conn
    conn.close()
```

### Fixtures autouse (setup global)

```python
@pytest.fixture(autouse=True)
def limpiar_estado():
    EstadoGlobal.reset()
    yield
    EstadoGlobal.reset()
```

---

## Parametrize — Múltiples Casos

```python
import pytest

@pytest.mark.parametrize("a,b,esperado", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_suma(a, b, esperado):
    assert sumar(a, b) == esperado

# IDs personalizados
@pytest.mark.parametrize("entrada,esperado", [
    ("hola", "HOLA"),
    ("mundo", "MUNDO"),
], ids=["minusculas", "otro"])
def test_upper(entrada, esperado):
    assert entrada.upper() == esperado
```

### Parametrize con fixtures

```python
@pytest.fixture
def cliente_http():
    return HttpClient()

@pytest.mark.parametrize("endpoint,status", [
    ("/users", 200),
    ("/posts", 200),
    ("/inexistente", 404),
])
def test_endpoints(cliente_http, endpoint, status):
    resp = cliente_http.get(endpoint)
    assert resp.status_code == status
```

---

## Mocking — `unittest.mock` / `pytest-mock`

```python
from unittest.mock import Mock, MagicMock, patch, AsyncMock

# Mock simple
mock = Mock()
mock.metodo.return_value = "falso"
assert mock.metodo() == "falso"

# MagicMock (soporta protocolos)
mock = MagicMock()
mock.__len__.return_value = 5
assert len(mock) == 5

# Patch (reemplaza temporalmente)
with patch("modulo.ClaseExterna") as mock_clase:
    mock_clase.return_value.metodo.return_value = "ok"
    from modulo import mi_funcion
    assert mi_funcion() == "ok"

# Patch como decorador
@patch("requests.get")
def test_api(mock_get):
    mock_get.return_value.json.return_value = {"data": 1}
    resp = llamar_api()
    assert resp == {"data": 1}
    mock_get.assert_called_once_with("https://api.example.com")

# AsyncMock (Python 3.8+)
async def test_async():
    mock = AsyncMock()
    mock.fetch.return_value = {"ok": True}
    result = await mock.fetch()
    assert result == {"ok": True}
```

### `mocker` fixture (pytest-mock)

```python
def test_con_mocker(mocker):
    mock = mocker.patch("modulo.dependencia")
    mock.return_value = "mocked"
    
    # Spy (llama original + observa)
    spy = mocker.spy(modulo, "funcion")
    modulo.funcion()
    spy.assert_called_once()
```

---

## Cobertura (`pytest-cov`)

```bash
pytest --cov=mi_paquete --cov-report=term-missing
pytest --cov=mi_paquete --cov-report=html  # Reporte HTML
pytest --cov=mi_paquete --cov-fail-under=80  # Fallar si < 80%
```

```toml
# pyproject.toml
[tool.coverage.run]
source = ["mi_paquete"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
]
```

---

## Property-Based Testing (`hypothesis`)

```bash
pip install hypothesis
```

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_suma_conmutativa(a, b):
    assert sumar(a, b) == sumar(b, a)

@given(st.lists(st.integers()))
def test_ordenar_idempotente(lista):
    assert sorted(sorted(lista)) == sorted(lista)

@given(st.text())
def test_reverse_involutivo(s):
    assert s[::-1][::-1] == s
```

### Estrategias comunes

```python
st.integers(min_value=0, max_value=100)
st.floats(allow_nan=False, allow_infinity=False)
st.text(min_size=1, max_size=50)
st.lists(st.integers(), min_size=0, max_size=10)
st.dictionaries(st.text(), st.integers())
st.datetimes()
st.uuids()
st.emails()
st.ip_addresses()
st.one_of(st.integers(), st.text())  # Unión
st.tuples(st.integers(), st.text())  # Tupla fija
```

---

## Markers — Categorizar Tests

```python
import pytest

@pytest.mark.slow
def test_lento():
    ...

@pytest.mark.integration
def test_con_db():
    ...

@pytest.mark.skip(reason="No implementado")
def test_futuro():
    ...

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requiere 3.10+")
def test_match():
    ...

@pytest.mark.xfail(reason="Bug conocido #123")
def test_bug():
    ...
```

```bash
pytest -m "not slow"           # Excluye lentos
pytest -m "integration"        # Solo integración
pytest -m "slow or integration"
```

---

## Testing Async

```python
import pytest

@pytest.mark.asyncio
async def test_asyncio():
    async def fetch():
        await asyncio.sleep(0.01)
        return "data"
    
    result = await fetch()
    assert result == "data"
```

```bash
pip install pytest-asyncio
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

---

## Testing con Bases de Datos

```python
import pytest
import sqlite3

@pytest.fixture
def db_memoria():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    yield conn
    conn.close()

def test_insert_usuario(db_memoria):
    db_memoria.execute("INSERT INTO users VALUES (1, 'Ana')")
    cursor = db_memoria.execute("SELECT * FROM users")
    assert cursor.fetchone() == (1, 'Ana')
```

---

## Testing CLI (`click`, `typer`)

```python
from click.testing import CliRunner
from mi_cli import main

def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output

def test_cli_comando():
    runner = CliRunner()
    result = runner.invoke(main, ["saludar", "--nombre", "Ana"])
    assert result.exit_code == 0
    assert "Hola Ana" in result.output
```

---

## TDD — Flujo Recomendado

```bash
# 1. Escribir test que falla (RED)
pytest test_nuevo.py::test_feature -v

# 2. Implementar mínimo para pasar (GREEN)
# ... código ...

# 3. Refactorizar manteniendo tests verdes (REFACTOR)
pytest test_nuevo.py -v

# 4. Repetir
```

---

## Estructura Recomendada

```
proyecto/
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       └── modulo.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Fixtures compartidas
│   ├── unit/
│   │   ├── test_modulo.py
│   │   └── test_otro.py
│   ├── integration/
│   │   └── test_api.py
│   └── e2e/
│       └── test_flujo.py
├── pyproject.toml
└── pytest.ini (opcional)
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --strict-markers --strict-config"
markers = [
    "slow: tests lentos",
    "integration: requieren BD/servicios",
    "unit: tests unitarios rápidos",
]
```

---

## Buenas Prácticas

| ✅ Hacer | ❌ Evitar |
|----------|-----------|
| Un assert por test (idealmente) | Múltiples asserts sin relación |
| Nombres descriptivos: `test_que_hace_que_cuando` | `test_1`, `test_funciona` |
| Fixtures para setup compartido | Setup duplicado en cada test |
| `parametrize` para casos similares | Tests duplicados |
| Mock solo dependencias externas | Mock de código propio |
| Tests determinísticos (sin random/time) | Tests flaky |
| Cobertura > 80% en lógica crítica | Cobertura 100% ciega |

---

## 🎯 Ejercicios

Practica testing en [ejercicios.md](./ejercicios.md#25--testing).

**Mini-ejercicio**: Tests para función `es_palindromo(texto)` con pytest. Casos: normal, vacío, con espacios, mayúsculas, números.

---

## Véase también

- [26-tooling](./26-tooling.md) — `ruff`, `mypy` en CI
- [27-logging-debugging](./27-logging-debugging.md) — Debug tests
- [28-packaging](./28-packaging.md) — `pytest` en `pyproject.toml`
- [ejercicios.md](./ejercicios.md) — Práctica recomendada