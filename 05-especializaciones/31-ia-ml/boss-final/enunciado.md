# 👑 Boss Final — Sistema ML Completo

**Ruta**: 🤖 IA/ML | **XP**: 500 | **HP mínimo**: 80

---

## 📖 Historia

Eres un mago de la IA. El reino necesita un sistema de clasificación de texto (spam, sentimientos, categorización de noticias). Entrena un modelo, crea una API de inferencia y despliega.

## 🎯 Requisitos obligatorios

- [ ] Dataset de texto real (spam, sentimientos, o similar)
- [ ] Pipeline de preprocesamiento (tokenización, limpieza, vectorización)
- [ ] Modelo de ML clásico (scikit-learn) y uno de Deep Learning (PyTorch)
- [ ] Comparación de rendimiento entre ambos
- [ ] API de inferencia con FastAPI
- [ ] Pruebas de la API con ejemplos reales
- [ ] Dockerfile para el servicio
- [ ] README con resultados y cómo usar

## 📋 Criterios de éxito

- API responde en < 1s por predicción
- Accuracy ≥ 85% en test set
- Código modular (preprocess, train, predict, api)
- logging de inferencias

## 📦 Stack

- scikit-learn, PyTorch
- Hugging Face Tokenizers
- FastAPI + Uvicorn
- Docker
- MLflow o similar (opcional)
