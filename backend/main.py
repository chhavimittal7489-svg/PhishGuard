from fastapi import FastAPI

from feature_extractor import extract_features
from treath_intel import check_urlhaus, get_domain_info
from fastapi.middleware.cors import CORSMiddleware
import pickle

from urllib3.util import url

model = pickle.load(open("model.pkl", "rb"))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "PhishGuard API Running"
    }

@app.post("/predict")
def predict(url: str):

    # Extract features
    features = extract_features(url)

    # Threat intelligence lookup
    threat_result = check_urlhaus(url)

    # Perform WHOIS domain forensic lookup
    domain_info = get_domain_info(url)

    prediction = model.predict([features])[0]

    probability = model.predict_proba([features])[0][1]

    prediction_label = "Phishing" if prediction == 1 else "Safe"

    risk_score = round(probability * 100, 2)

    trusted_domains = [
        "google.com",
        "github.com",
        "microsoft.com",
        "wikipedia.org"
    ]

    if any(domain in url for domain in trusted_domains):
        prediction_label = "Safe"
        risk_score = 5

    return {

        "url": url,

        "features": features,

        "prediction": prediction_label,

        "risk_score": risk_score,

        "threat_intelligence": threat_result,

        "domain_info": domain_info
    }

