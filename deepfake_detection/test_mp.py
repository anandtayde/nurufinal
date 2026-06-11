import sys
try:
    import mediapipe as mp
    print(f"MediaPipe Version: {mp.__version__}")
    import mediapipe.solutions.face_mesh as mp_face_mesh
    print("FaceMesh available")
    import mediapipe.solutions.face_detection as mp_face_detection
    print("FaceDetection available")
except ImportError as e:
    print(f"ImportError: {e}")
except AttributeError as e:
    print(f"AttributeError: {e}")
except Exception as e:
    print(f"Error: {e}")
