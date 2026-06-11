import sys
import os

# Add src to path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, SRC_DIR)

print("Starting ML component load test...")

try:
    print("Importing FeatureExtractor...")
    from feature_extractor import FeatureExtractor
    print("Importing DeepfakeClassifier...")
    from classifier import DeepfakeClassifier

    print("Initializing FeatureExtractor...")
    fe = FeatureExtractor()
    print("✅ FeatureExtractor initialized")

    print("Initializing DeepfakeClassifier...")
    cl = DeepfakeClassifier()
    print("✅ DeepfakeClassifier initialized")

    model_file = os.path.join(BASE_DIR, "models", "classifier.pkl")
    if os.path.exists(model_file):
        print(f"Loading model from {model_file}...")
        cl.load_model(model_file)
        print("✅ Model loaded successfully")
    else:
        print(f"❌ Model file not found: {model_file}")

except Exception as e:
    import traceback
    print(f"❌ Error: {e}")
    traceback.print_exc()

print("Test complete.")
