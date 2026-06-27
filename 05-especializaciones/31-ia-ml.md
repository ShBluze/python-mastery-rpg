# 31 — IA & Machine Learning

> `scikit-learn`, `tensorflow`, `pytorch`, `transformers`, `opencv`, `langchain`, pipelines ML.

---

## `scikit-learn` — ML Clásico

```bash
pip install scikit-learn
```

### Pipeline completo

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Datos
iris = load_iris()
X, y = iris.data, iris.target

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluación
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

### Preprocesamiento

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", LabelEncoder()),
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipe, numeric_cols),
    ("cat", categorical_pipe, categorical_cols),
])
```

### Modelos comunes

```python
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
```

---

## `tensorflow` / `keras` — Deep Learning

```bash
pip install tensorflow
```

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(128, activation="relu", input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax"),
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
model.evaluate(X_test, y_test)
```

### CNN (Visión)

```python
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax"),
])
```

---

## `pytorch` — Deep Learning (Dinámico)

```bash
pip install torch
```

```python
import torch
import torch.nn as nn
import torch.optim as optim

class MiRed(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

model = MiRed()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

---

## `transformers` — NLP Moderno (Hugging Face)

```bash
pip install transformers datasets
```

```python
from transformers import pipeline

clasificador = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
resultado = clasificador("I love Python!")
# [{'label': 'POSITIVE', 'score': 0.999}]

generador = pipeline("text-generation", model="gpt2")
generador("Python es", max_length=30)

traductor = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
traductor("Hola mundo")
```

### Fine-tuning

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
from datasets import load_dataset

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

dataset = load_dataset("imdb")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)
```

---

## `opencv` — Visión por Computadora

```bash
pip install opencv-python
```

```python
import cv2

img = cv2.imread("foto.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
detections = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in detections:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite("output.jpg", img)
```

---

## `langchain` — LLM Orchestration

```bash
pip install langchain openai
```

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4")
prompt = ChatPromptTemplate.from_template("Resume este texto: {texto}")

chain = prompt | llm
resultado = chain.invoke({"texto": "..."})
```

---

## Flujo de Trabajo ML

```
1. Recolectar datos
2. Limpiar y explorar (EDA)
3. Feature engineering
4. Split train/test/validación
5. Seleccionar modelo
6. Entrenar
7. Evaluar (métricas)
8. Ajustar hiperparámetros
9. Desplegar (API / batch)
10. Monitorear
```

---

## Proyectos Recomendados

| Proyecto                      | Librerías                              |
|-------------------------------|----------------------------------------|
| Clasificador de spam          | `scikit-learn`, `pandas`               |
| Reconocimiento de dígitos     | `tensorflow` / `pytorch`               |
| Chatbot con RAG               | `langchain`, `chromadb`, `openai`      |
| Detección de objetos          | `opencv`, `yolo` / `detectron2`        |
| Análisis de sentimiento       | `transformers`, `pandas`               |

---

---
## 🎯 Ruta completa

La ruta IA/ML se ha expandido. Consulta [`31-ia-ml/README.md`](31-ia-ml/README.md) para el plan de estudio detallado.

---

## Véase también

- [30-data-science](./30-data-science.md) — `numpy`, `pandas`, `matplotlib`
- [29-web](./29-web.md) — APIs para servir modelos
- [31-ia-ml/README.md](31-ia-ml/README.md) — Ruta IA/ML completa
