# 🚀 ML Model Deployment Project – Sentiment Analysis API

## 📌 Project Overview

This project demonstrates **end-to-end Machine Learning deployment** using a Sentiment Analysis model.
It covers **training → API → Docker → Cloud → Monitoring → Retraining**.

---

# 🧠 20 TASKS – COMPLETE WORKFLOW

---

## ✅ 1. Train ML Model

* Use inbuilt dataset in `train.py`
* Algorithm: Logistic Regression

```bash
python train.py
```

---

## ✅ 2. Evaluate Model Performance

* Accuracy printed in console
* Uses `accuracy_score`

---

## ✅ 3. Save Model

* Model saved using `joblib`

```python
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
```

---

## ✅ 4. Create Flask App

* API created using Flask (`app.py`)

---

## ✅ 5. Load Model in API

```python
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
```

---

## ✅ 6. Define API Endpoint

```python
@app.route("/predict", methods=["POST"])
```

---

## ✅ 7. Test API Locally

```bash
python app.py
```

---

## ✅ 8. Handle JSON Input/Output

Input:

```json
{"text": "I love this product"}
```

Output:

```json
{
  "prediction": "Positive"
}
```

---

## ✅ 9. Create Dockerfile

* Containerize application

---

## ✅ 10. Build Docker Image

```bash
docker build -t sentiment-api .
```

---

## ✅ 11. Run Docker Container

```bash
docker run -p 5000:5000 sentiment-api
```

---

## ✅ 12. Push to Cloud Registry

* Example: Docker Hub

```bash
docker tag sentiment-api username/sentiment-api
docker push username/sentiment-api
```

---

## ✅ 13. Deploy on Cloud Service

* Use Render / AWS / Azure
* Connect GitHub repository

---

## ✅ 14. Expose API Publicly

* Get public URL from cloud platform

---

## ✅ 15. Send Test Requests

```bash
curl -X POST https://your-api-url/predict \
-H "Content-Type: application/json" \
-d "{\"text\":\"Amazing product\"}"
```

---

## ✅ 16. Monitor Latency & Accuracy

* Measure response time
* Track prediction performance

---

## ✅ 17. Detect Data Drift

```python
def check_drift(text):
    return "Drift" if len(text) > 200 else "No Drift"
```

---

## ✅ 18. Automate Retraining

* Use new dataset (`new_data.csv`)
* Trigger retraining script

---

## ✅ 19. Log Predictions & Errors

```python
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
```

---

## ✅ 20. Document Workflow

* This README explains full pipeline
* Covers development → deployment → monitoring

---

# 📁 Project Structure

```
ml_deployment_project/
│
├── train.py
├── app.py
├── test_api.py
├── requirements.txt
├── Dockerfile
├── model.pkl
├── vectorizer.pkl
└── README.md
```

---

# ⚙️ Setup Instructions

## 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Run Project

```bash
python train.py
python app.py
```

---

## 🔹 Test API

```bash
python test_api.py
```

---

# 🐳 Docker Setup

```bash
docker build -t sentiment-api .
docker run -p 5000:5000 sentiment-api
```

---

# ☁️ Deployment (Render)

1. Push code to GitHub
2. Connect repo to Render
3. Start command:

```bash
python app.py
```

---

# 🎯 Key Features

✔ Inbuilt dataset (no CSV required)
✔ End-to-end ML pipeline
✔ REST API using Flask
✔ Dockerized application
✔ Cloud deployment ready
✔ Logging + Drift detection
✔ Retraining pipeline

---

# 🧑‍💻 Author

**Your Name**

---

# ⭐ Conclusion

This project demonstrates a **complete production-ready ML deployment workflow**, covering all essential steps from model building to monitoring and maintenance.

---
