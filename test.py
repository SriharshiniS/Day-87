import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "text": "This product is amazing"
}

try:
    response = requests.post(url, json=data)
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)