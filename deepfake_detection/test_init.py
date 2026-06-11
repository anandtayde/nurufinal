import os
import sys

# Add src to path
BASE_DIR = os.getcwd()
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, SRC_DIR)

try:
    print("Testing FeatureExtractor initialization...")
    from feature_extractor import FeatureExtractor
    fe = FeatureExtractor()
    print("✅ FeatureExtractor initialized successfully")
    
    print("Testing DeepfakeClassifier initialization...")
    from classifier import DeepfakeClassifier
    clf = DeepfakeClassifier()
    print("✅ DeepfakeClassifier initialized successfully")
    
    model_path = os.path.join(BASE_DIR, "models", "classifier.pkl")
    if os.path.exists(model_path):
        print(f"Loading model from {model_path}...")
        clf.load_model(model_path)
        print("✅ Model loaded successfully")
    else:
        print(f"❌ Model file not found: {model_path}")
        
except Exception as e:
    import traceback
    print(f"❌ Initialization failed: {e}")
    traceback.print_exc()
