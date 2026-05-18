# PhishGuard

PhishGuard is an ML-powered phishing URL detection system designed to identify malicious and suspicious websites in real time using Machine Learning and Cyber Threat Intelligence integration.

The system combines handcrafted URL feature extraction, a Random Forest classification model, WHOIS-based domain forensics, and threat intelligence lookups to analyze URLs and generate risk assessments. It also includes a FastAPI backend, a web-based analyst dashboard, and a browser extension for real-time website scanning.

## Features

* Real-time phishing URL detection
* Random Forest Machine Learning model
* URL feature extraction pipeline
* WHOIS domain intelligence lookup
* URLhaus threat intelligence integration
* FastAPI REST API backend
* Interactive frontend dashboard
* Browser extension for live website scanning

## Tech Stack

* Python
* FastAPI
* scikit-learn
* Random Forest Classifier
* HTML/CSS/JavaScript
* Browser Extension APIs
* URLhaus API
* python-whois

## System Architecture

Browser Extension / Dashboard
↓
FastAPI Backend
↓
Feature Extraction
↓
Random Forest ML Model
↓
Threat Intelligence APIs + WHOIS
↓
Risk Analysis & Detection Result

## How to Run

### Backend

```bash
cd backend
uvicorn main:app --reload
```

### Frontend

Open `frontend/index.html` in browser.

### Browser Extension

1. Open `chrome://extensions`
2. Enable Developer Mode
3. Click "Load Unpacked"
4. Select the `extension` folder

## Future Scope

* Deep learning-based phishing detection
* Email phishing analysis
* QR code phishing detection
* Cloud deployment
* Real-time blacklist synchronization

## Disclaimer

This project is a prototype developed for educational and hackathon purposes.

## Note
Large dataset files and serialized model weights are excluded from this repository due to GitHub file size limitations. The repository includes the complete model training pipeline (`train_model.py`) and feature extraction logic required to reproduce the trained model.
