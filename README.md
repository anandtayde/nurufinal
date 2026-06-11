<div align="center">

# 🧠 NeuroBlink

### AI-Powered Deepfake Detection & Facial Behavior Analysis Platform

Detect deepfakes, analyze facial dynamics, track eye movements, and generate intelligent reports using Machine Learning and Computer Vision.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![License](https://img.shields.io/badge/License-MIT-blue)

</div>

---

# 📖 Overview

NeuroBlink is an AI-powered deepfake detection and facial behavior analysis system designed to identify manipulated videos and extract meaningful facial insights.

The platform combines Computer Vision, Machine Learning, and Behavioral Analytics to evaluate video authenticity through:

- Deepfake detection
- Eye movement tracking
- Facial expression analysis
- Facial dynamics monitoring
- Landmark detection
- Feature extraction
- Automated report generation

The project consists of a Python-based ML backend and a modern Next.js frontend dashboard.

---

# ✨ Key Features

## 🎭 Deepfake Detection

Detect AI-generated or manipulated facial content using trained machine learning models.

## 👁️ Eye Movement Analysis

Analyze blinking patterns and eye behavior for authenticity verification.

## 😀 Facial Expression Recognition

Track and classify facial expressions across video frames.

## 📍 Facial Landmark Detection

Identify key facial points for accurate motion analysis.

## 📈 Feature Extraction Pipeline

Extract behavioral and visual features from videos for classification.

## 📊 Automated Reports

Generate detailed analysis reports with visual insights.

## ⚡ Real-Time Processing

Fast video analysis pipeline optimized for performance.

---

# 🏗️ System Architecture

```text
Video Input
     │
     ▼
Face Detection
     │
     ▼
Landmark Detection
     │
     ▼
Feature Extraction
     │
     ▼
 ┌─────────────┬──────────────┬─────────────┐
 │ Eye Analysis│ Expressions  │ Dynamics    │
 └─────────────┴──────────────┴─────────────┘
               │
               ▼
      ML Classification
               │
               ▼
      Deepfake Prediction
               │
               ▼
         Report Generation
```

---

# 📂 Project Structure

```text
Dipex-2026-Neuroblink
│
├── deepfake_detection
│
├── models
│   ├── classifier.pkl
│   └── trained_classifier.pkl
│
├── reports
│
├── src
│   ├── classifier.py
│   ├── eye_analyzer.py
│   ├── face_detector.py
│   ├── facial_dynamics_analyzer.py
│   ├── feature_extractor.py
│   ├── landmark_detector.py
│   ├── migrate_features.py
│   └── main.py
│
├── utils
│   ├── video_utils.py
│   └── visualization.py
│
├── frontend
│   ├── src
│   ├── public
│   ├── app
│   └── package.json
│
├── server.py
├── train.py
├── predict.py
├── validate_model.py
└── requirements.txt
```

---

# 🛠️ Tech Stack

## Backend

- Python
- OpenCV
- NumPy
- Pandas
- Scikit-Learn
- Pickle Models

## Computer Vision

- Face Detection
- Facial Landmark Detection
- Feature Extraction
- Motion Analysis

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

## Development Tools

- Git
- GitHub
- VS Code

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/anandtayde/nurufinal.git
cd nurufinal
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Backend

```bash
python server.py
```

or

```bash
python src/main.py
```

---

# 🌐 Running Frontend

```bash
cd frontend

npm install

npm run dev
```

Application:

```text
http://localhost:3000
```

---

# 📊 Machine Learning Pipeline

### Training

```bash
python train.py
```

### Validation

```bash
python validate_model.py
```

### Prediction

```bash
python predict.py
```

---

# 📸 Results

The system generates:

- Deepfake classification results
- Feature importance analysis
- Eye movement metrics
- Facial dynamics reports
- Visual analytics dashboards

Generated reports are stored inside:

```text
reports/
```

---

# 🔮 Future Enhancements

- Real-time webcam analysis
- Advanced deepfake transformers
- Emotion intelligence dashboard
- Cloud deployment
- Mobile support
- Multi-face tracking

---

# 👨‍💻 Author

## Anand Tayade

🌐 Portfolio: https://anandtayde.in

💼 LinkedIn: https://www.linkedin.com/in/anandtayde

📧 Email: anandtayade2004@gmail.com

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
