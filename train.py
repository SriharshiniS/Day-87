import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# -----------------------------
# Step 1: Inbuilt Dataset
# -----------------------------
data = {
    "text": [
        "I love this product",
        "This is amazing",
        "Very happy with service",
        "Worst experience ever",
        "I hate this",
        "Not good at all",
        "Excellent quality",
        "Super fast delivery",
        "Terrible product",
        "Will buy again",
        "Absolutely fantastic",
        "Really bad experience",
        "Highly recommended",
        "Waste of money",
        "Loved it so much",
        "Not worth it",
        "Great value",
        "Very disappointing",
        "Best purchase ever",
        "Awful service"
    ],
    "sentiment": [1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Feature Engineering
# -----------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["sentiment"]

# -----------------------------
# Step 3: Train Model
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# -----------------------------
# Step 4: Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# -----------------------------
# Step 5: Save Model
# -----------------------------
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model & Vectorizer saved!")