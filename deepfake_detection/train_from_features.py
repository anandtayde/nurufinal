#!/usr/bin/env python3
"""
train_from_features.py
Trains the Deepfake Detection model using pre-extracted .npz features.
Bypasses the requirement for original video files.
"""

import os
import sys
import json
import time
import numpy as np
from typing import List, Dict, Tuple
import re

# Add src to path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from classifier import DeepfakeClassifier

def get_label_from_filename(filename: str) -> int:
    """
    Heuristic for labeling based on common dataset naming conventions
    0 = Real, 1 = Fake
    """
    # Pattern 1: idX_idY... is typically a swap (Fake)
    if re.search(r"id\d+_id\d+", filename):
        return 1
    
    # Pattern 2: idX_... (without second id) is typically an actor (Real)
    if re.search(r"^id\d+(_|\.)", filename):
        return 0
    
    # Pattern 3: digits only (e.g., 000.npz) are typically original clips (Real)
    if re.match(r"^\d+\.npz$", filename):
        return 0
    
    # Pattern 4: underscore pairs (e.g., 01_02.npz) often represent source_target (Fake)
    if re.match(r"^\d+_\d+", filename):
        return 1
        
    # Default: If it has descriptive names but no obvious 'swap' signatures, treat as Real
    # e.g., '01__exit_phone_room.npz'
    return 0

def main():
    feature_dir = "features"
    model_path = "models/classifier.pkl"
    report_path = "training_report_new.json"
    
    print("\n🚀 Starting Feature-Only Training")
    print("=" * 60)
    
    if not os.path.exists(feature_dir):
        print(f"❌ Error: Feature directory '{feature_dir}' not found.")
        sys.exit(1)
        
    files = [f for f in os.listdir(feature_dir) if f.endswith(".npz")]
    if not files:
        print(f"❌ Error: No .npz files found in '{feature_dir}'.")
        sys.exit(1)
        
    print(f"📂 Found {len(files)} feature files.")
    
    features_list = []
    labels = []
    
    print("📥 Loading features and assigning labels...")
    for i, f in enumerate(files, 1):
        if i % 500 == 0:
            print(f"   Processed {i}/{len(files)} files...")
            
        path = os.path.join(feature_dir, f)
        try:
            data = np.load(path, allow_pickle=True)
            # Handle different cache versions
            if "features" in data:
                feats = data["features"].item()
            else:
                # Fallback if saved differently
                feats = data.item() if hasattr(data, "item") else dict(data)
                
            label = get_label_from_filename(f)
            
            features_list.append(feats)
            labels.append(label)
        except Exception as e:
            print(f"   ⚠️  Failed to load {f}: {e}")
            
    if not features_list:
        print("❌ Error: No valid features loaded.")
        sys.exit(1)
        
    # Stats
    real_count = labels.count(0)
    fake_count = labels.count(1)
    print(f"\n📊 Dataset Analysis:")
    print(f"   Total Samples: {len(labels)}")
    print(f"   Real (0): {real_count}")
    print(f"   Fake (1): {fake_count}")
    
    # Train
    print(f"\n🤖 Training Gradient Boosting model...")
    clf = DeepfakeClassifier(model_type="gradient_boosting")
    
    t0 = time.time()
    results = clf.train(features_list, labels)
    duration = time.time() - t0
    
    # Save
    clf.save_model(model_path)
    
    # Report
    report = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_samples": len(labels),
        "real_samples": real_count,
        "fake_samples": fake_count,
        "results": results,
        "training_duration_sec": duration
    }
    
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
        
    print("\n" + "=" * 60)
    print("🎉 TRAINING COMPLETED SUCCESSFULLY!")
    print(f"🎯 Accuracy: {results['accuracy']:.4f}")
    print(f"💾 Model saved to: {model_path}")
    print(f"📄 Report saved to: {report_path}")

if __name__ == "__main__":
    main()
