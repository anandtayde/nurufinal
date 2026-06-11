# 🧠 Neuroblink – Project Overview & Mechanical Working

Neuroblink is a state-of-the-art deepfake detection system designed to protect digital authenticity. It leverages a multi-signal analysis pipeline that combines **physiological cues** (eye blinking) with **forensic facial dynamics** to distinguish between real humans and AI-generated syntheses.

---

## 🚀 Key Features

- **212 Feature Signals**: Real-time extraction of subtle facial behaviors across 9 domains.
- **Adaptive Detection**: Ocular analysis that adjusts to lighting, face size, and skin tone.
- **Machine Learning Core**: High-precision Gradient Boosting classifier trained on forensic datasets ($FF++$, $Celeb-DF$).
- **Explainable Results**: Detailed breakdowns of sharpness, symmetry, and temporal consistency.

---

## 🛠️ System Architecture

### 1. Front-End (Next.js + Framer Motion)
- **Interface**: A premium, "cyber-noir" UI built with glassmorphism and interactive data viz.
- **Upload Flow**: Secure video ingestion with immediate status feedback.
- **Live Mode**: Camera streaming with real-time landmark mesh overlay.

### 2. Back-End (FastAPI + MediaPipe + Scikit-Learn)
- **Processing Engine**: A Python-based microservice that orchestrates the detection pipeline.
- **Computer Vision**: Uses MediaPipe's 468-point face mesh for ultra-precise tracking.
- **classifier**: A Gradient Boosting model that evaluates the fusion of ocular and dynamic features.

---

## 🔄 High-Level Workflow

1. **Ingestion**: User uploads a video or starts the live feed.
2. **Preprocessing**: The system decodes frames and detects the primary subject's face.
3. **Signal Extraction**:
   - **Ocular Path**: Computes Eye Aspect Ratio (EAR) to detect natural vs. synthetic blinks.
   - **Dynamic Path**: Analyzes skin texture, head pose jitter, and boundary flow artifacts.
4. **Classification**: The 212-feature vector is fed into the model to generate a "REAL" or "FAKE" prediction.
5. **Visualization**: Findings are presented with confidence scores and detailed forensic metrics.

---

## 📂 project Structure

- `/frontend`: Next.js web application.
- `/deepfake_detection`: Python backend with feature extractors and model logic.
- `/data`: Storage for training datasets.
- `/models`: Stored pre-trained binary classifiers (.pkl).

---

© 2026 Neuroblink Team · Protecting Digital Authenticity
