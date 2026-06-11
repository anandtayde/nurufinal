# 🌐 Neuroblink: The Complete Forensic Documentation (FULL BREAKDOWN)

This guide provides an exhaustive, end-to-end breakdown of the **Neuroblink Deepfake Detection System**, covering the ecosystem from the UI layer down to the mathematical feature extractors and ML inference.

---

## 🏗️ 1. High-Level System Architecture

Neuroblink operates as a decoupled **Client-Server** ecosystem:

- **Frontend (Next.js/React)**: Handles file ingestion, UI state management, and data visualization. Communicates via RESTful APIs.
- **Backend (FastAPI/Python)**: A high-performance forensic engine that runs CPU-optimized computer vision pipelines.
- **Forensic Core**: A set of specialized analyzers that compute 212 distinct signals derived from physiological and geometric cues.
- **Inference Layer**: A Scikit-Learn based Gradient Boosting model that weights features to produce a final authenticity score.

---

## 🧬 2. The 212-Feature Forensic Pipeline

The system doesn't just look for "fakes"; it measures **212 specific signals** across 9 forensic domains. These signals are extracted for every 3 frames and then statistically aggregated.

### Domain Breakdown:
1.  **Ocular Dynamics (13 features)**: EAR sequences, blink count, regularity, and completeness.
2.  **Spatial Integrity**: Sharpness variance and high-frequency energy (detects GAN blurring).
3.  **Surface Texture**: LBP Entropy and noise level statistics (identifies synthetic skin).
4.  **Geometric Symmetry**: Left-right facial symmetry consistency.
5.  **Head Pose (3 features)**: Yaw, Pitch, and Roll angles via `solvePnP`.
6.  **Temporal Consistency**: Jitter and trend metrics for pose and EAR (detects frame-to-frame stitching).
7.  **Mouth Dynamics**: Mouth Aspect Ratio (MAR) and corner asymmetry.
8.  **Motion (Optical Flow)**: Density and direction entropy of movement across the face.
9.  **Color consistency**: Skin-tone ratios and hue consistency across regions.

---

## ⚙️ 3. Minute-Level Execution Chain (Step-by-Step)

When you click **Analyze Video**, the following happens sequentially:

### **Phase 1: Ingestion (0s - 1s)**
- **Method**: `POST /detect` in `main.py`.
- **Action**: FastAPI receives the video file, validates it, and saves it to a temporary path.

### **Phase 2: Decoding & Tracking (1s - 2.5s)**
- **Class**: `FeatureExtractor` in `feature_extractor.py`.
- **Action**: Uses `OpenCV` to stream frames. `MediaPipe` tracks the face and generates the 468-point 3D landmark mesh.
### **Phase 3: Analysis (2.5s - 4.5s)**
- **Class**: `EyeAnalyzer` in `eye_analyzer.py`.
  - **Function**: `calculate_blink_features`. Applies a **3-frame median filter** to kill noise.
- **Class**: `FacialDynamicsAnalyzer` in `facial_dynamics_analyzer.py`.
  - **Function**: `analyze_frame`. Runs FFTs for artifacts, LBPs for texture, and Farneback flow for motion.

### **Phase 4: Synthesis & Prediction (4.5s - 6.5s)**
- **Function**: `_aggregate_dynamics`. Converts per-frame data into video-level statistical summaries.
- **Class**: `DeepfakeClassifier` in `classifier.py`.
  - **Action**: Scales the 212-feature vector and runs the Gradient Boosting inference.

### **Phase 5: Reporting (6.5s - 8.0s)**
- **Action**: JSON result returned to the Next.js frontend.
- **UI**: `ResultDisplay.tsx` renders the forensic metrics and final verdict.

---

## 📁 4. Core Function-Level Reference

### A. `feature_extractor.py` (The Director)
- **`extract_video_features`**: Coordinates frame processing and component hand-offs.
- **`_calc_ear`**: Geometric EAR calculation based on 6-point eye landmarks.
- **`_aggregate_dynamics`**: Merges per-frame data into video-level summaries (Mean, Std, Median, etc.).

### B. `eye_analyzer.py` (The Ocular Engine)
- **`calculate_blink_features`**: Filters EAR time-series and calculates 13 blink metrics.
- **`_adaptive_threshold`**: Calculates dynamic blink barriers based on the video's baseline.

### C. `facial_dynamics_analyzer.py` (The Forensic Lab)
- **`_edge_artifact_features`**: Computes `cv2.Laplacian` variance to identify synthetic blurring.
- **`_compute_lbp`**: Custom Local Binary Patterns for identifying GAN-generated skin textures.
- **`_head_pose_features`**: Map 2D landmarks to 3D head models using `cv2.solvePnP`.
- **`compute_temporal_features`**: Calculates "jitter" (standard deviation of frame differences).

### D. `classifier.py` (The Judge)
- **`train` / `predict`**: Performs robust scaling and missing value handling before classification.
- **`get_feature_importance`**: Provides the mathematical weight of each forensic clue.

---

## 👨‍💻 5. Summary of Innovation

While traditional deepfake detectors look for blurred pixels, **Neuroblink** looks for **physiological inconsistencies**. By measuring 212 distinct points of data—including how an eye blinks and how skin reflects light—the system creates a comprehensive forensic profile that AI synthesis cannot easily mimic.

---
