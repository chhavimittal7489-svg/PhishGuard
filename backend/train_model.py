import re

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:/Users/chhavi mittal/OneDrive/Desktop/phisguard/malicious_phish.csv")

def convert_label(x):

    if x == "benign":
        return 0
    else:
        return 1

df["label"] = df["type"].apply(convert_label)
def extract_features(url):

    features = []

    # URL Length
    features.append(len(url))

    # Dot Count
    features.append(url.count('.'))

    # Hyphen Count
    features.append(url.count('-'))

    # @ Count
    features.append(url.count('@'))

    # Digit Count
    features.append(sum(c.isdigit() for c in url))

    # HTTPS
    features.append(1 if "https" in url else 0)

    # IP Address
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(1 if re.search(ip_pattern, url) else 0)

    # Suspicious Words
    suspicious_words = [
        'login',
        'verify',
        'secure',
        'bank',
        'update',
        'free',
        'bonus'
    ]

    suspicious_count = sum(
        word in url.lower()
        for word in suspicious_words
    )

    features.append(suspicious_count)

    return features

X = df["url"].apply(extract_features).tolist()

y = df["label"]
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.2
)

model = RandomForestClassifier()

model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")

import pickle

pickle.dump(model, open("model.pkl", "wb"))

