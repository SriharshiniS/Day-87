from flask import Flask, request, jsonify
import joblib
import logging

app = Flask(__name__)

# -----------------------------
# Load Model
# -----------------------------
try:
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except:
    model = None
    vectorizer = None

# -----------------------------
# Logging Setup
# -----------------------------
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route("/")
def home():
    return "✅ Sentiment API is running!"

# -----------------------------
# Drift Detection
# -----------------------------
def check_drift(text):
    if len(text) > 200:
        return "⚠️ Possible drift detected"
    return "No drift"

# -----------------------------
# Prediction API
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if model is None or vectorizer is None:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json()

    if "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data["text"]

    # Transform input
    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)[0]
    result = "Positive" if prediction == 1 else "Negative"

    drift_status = check_drift(text)

    # Log result
    logging.info(f"Input: {text}, Prediction: {result}")

    return jsonify({
        "input": text,
        "prediction": result,
        "drift": drift_status
    })

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)