import sys
import os

print(f"Python: {sys.version}")
print(f"Executable: {sys.executable}")

try:
    import mediapipe
    print(f"mediapipe path: {mediapipe.__path__}")
    print(f"mediapipe version: {mediapipe.__version__}")
except Exception as e:
    print(f"Failed to import mediapipe: {e}")

try:
    from mediapipe.python.solutions import face_mesh
    print("Successfully imported face_mesh via mediapipe.python.solutions")
except ImportError as e:
    print(f"ImportError (python.face_mesh): {e}")

try:
    import mediapipe.solutions.face_mesh
    print("Successfully imported face_mesh via mediapipe.solutions")
except ImportError as e:
    print(f"ImportError (solutions.face_mesh): {e}")
except Exception as e:
    print(f"Other error: {e}")
