# 30 — Data Science & Análisis de Datos

> `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `jupyter`, ETL, visualización.

---

## `numpy` — Computación Numérica

```bash
pip install numpy
```

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr * 2  # Vectorización: [2, 4, 6, 8, 10]

matrix = np.array([[1, 2], [3, 4]])
matrix @ matrix  # Producto matricial

np.zeros((3, 4))
np.ones((2, 3))
np.random.randn(1000)  # Distribución normal
np.linspace(0, 1, 10)  # 0, 0.111, 0.222, ...
```

### Operaciones clave

```python
arr.sum()
arr.mean()
arr.std()
arr.max()
arr.argmax()
np.unique(arr)
arr.reshape((5, 1))
```

---

## `pandas` — Manipulación de Datos

```bash
pip install pandas
```

### Estructuras básicas

```python
import pandas as pd

# Series (1D)
s = pd.Series([1, 3, 5, None, 9], index=["a", "b", "c", "d", "e"])

# DataFrame (2D) — tabla
df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Carlos"],
    "edad": [25, 30, 35],
    "ciudad": ["Madrid", "Barcelona", "Valencia"],
})
```

### Lectura/Escritura

```python
df = pd.read_csv("datos.csv")
df = pd.read_json("datos.json")
df = pd.read_excel("datos.xlsx", sheet_name="ventas")
df = pd.read_sql("SELECT * FROM usuarios", conexion)

df.to_csv("limpio.csv", index=False)
df.to_parquet("datos.parquet")
```

### Exploración

```python
df.head(10)
df.info()
df.describe()
df["columna"].value_counts()
df.isna().sum()
df.shape
df.columns
df.dtypes
```

### Filtrado y transformación

```python
# Filtrar
df[df["edad"] > 30]
df.query("edad > 30 and ciudad == 'Madrid'")

# Seleccionar columnas
df[["nombre", "edad"]]
df.loc[0:5, ["nombre", "edad"]]

# Crear columnas
df["edad_doble"] = df["edad"] * 2
df["categoria"] = df["edad"].apply(lambda x: "joven" if x < 30 else "adulto")

# Agrupar
df.groupby("ciudad")["edad"].agg(["mean", "count"])
df.pivot_table(index="ciudad", columns="categoria", values="edad", aggfunc="mean")
```

### Limpieza

```python
df.dropna()
df.fillna({"edad": df["edad"].median()})
df.drop_duplicates()
df.rename(columns={"old": "new"})
```

---

## `matplotlib` — Visualización

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt

# Líneas
plt.plot([1, 2, 3], [4, 5, 6], label="serie A")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Título")
plt.legend()
plt.show()

# Barras
plt.bar(["A", "B", "C"], [10, 20, 15])

# Dispersión
plt.scatter(x, y, c=colores, alpha=0.5)

# Histograma
plt.hist(datos, bins=30, edgecolor="black")

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
```

---

## `seaborn` — Visualización Estadística

```bash
pip install seaborn
```

```python
import seaborn as sns

# Datos de ejemplo
df = sns.load_dataset("iris")

sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
sns.boxplot(data=df, x="species", y="petal_length")
sns.heatmap(df.select_dtypes("number").corr(), annot=True, cmap="coolwarm")
sns.pairplot(df, hue="species")
sns.displot(df, x="sepal_length", kind="kde")
```

---

## `scipy` — Ciencia y Computación Técnica

```bash
pip install scipy
```

```python
from scipy import stats, optimize

# Estadística
stats.ttest_ind(grupo_a, grupo_b)  # T-test
stats.norm.pdf(x, loc=0, scale=1)  # PDF normal
stats.pearsonr(x, y)               # Correlación

# Optimización
result = optimize.minimize(lambda x: x**2 + 10, x0=5)

# Señales
from scipy import signal
filtered = signal.medfilt(ruidosa, kernel_size=3)
```

---

## Jupyter Notebook / JupyterLab

```bash
pip install jupyterlab
jupyter lab
```

```python
# Celdas mágicas útiles
%matplotlib inline  # Mostrar plots inline
%timeit funcion()   # Medir tiempo
%debug              # Post-mortem debugger
!pip install pandas # Ejecutar shell
```

---

## Flujo ETL Típico

```python
import pandas as pd

# Extract
df = pd.read_csv("ventas_raw.csv")

# Transform
df = df.dropna(subset=["total"])
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month
df["total_limpio"] = df["total"].clip(lower=0)
resumen = df.groupby("mes").agg(
    ventas=("total_limpio", "sum"),
    transacciones=("id", "count"),
).reset_index()

# Load
resumen.to_sql("ventas_resumen", conexion, if_exists="replace")
```

---

## Proyectos Recomendados

| Proyecto                          | Librerías                           |
|-----------------------------------|-------------------------------------|
| Análisis de ventas                | `pandas`, `matplotlib`, `seaborn`   |
| Predicción de precios             | `numpy`, `pandas`, `scikit-learn`   |
| Dashboard interactivo             | `pandas`, `plotly` / `dash`         |
| Procesamiento de imágenes         | `numpy`, `scipy`, `opencv-python`   |
| Análisis de series temporales     | `pandas`, `statsmodels`             |

---

---
## 🎯 Ruta completa

La ruta Data Science se ha expandido. Consulta [`30-data-science/README.md`](30-data-science/README.md) para el plan de estudio detallado.

---

## Véase también

- [31-ia-ml](./31-ia-ml.md) — Machine Learning & Deep Learning
- [23-archivos-persistencia](../04-ecosistema/23-archivos-persistencia.md) — Carga de datos
- [30-data-science/README.md](30-data-science/README.md) — Ruta Data Science completa
