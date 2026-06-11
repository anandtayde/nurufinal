import os
import sys
import pickle
import traceback

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

try:
    print("--- Debug Load Start ---")
    model_path = os.path.join('models', 'classifier.pkl')
    print(f"Loading from: {model_path}")
    
    with open(model_path, 'rb') as f:
        state = pickle.load(f)
        
    print("Pickle load successful!")
    print(f"Keys: {state.keys()}")
    print(f"Model type: {state.get('model_type')}")
    print(f"Is trained: {state.get('is_trained')}")
    
    from classifier import DeepfakeClassifier
    clf = DeepfakeClassifier()
    clf.load_model(model_path)
    print("DeepfakeClassifier.load_model successful!")
    
except Exception as e:
    print("\n--- ERROR DURING LOAD ---")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    traceback.print_exc()
    sys.exit(1)
