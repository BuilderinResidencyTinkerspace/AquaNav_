"""Central configuration for AquaNav. Edit values here instead of scattering
magic numbers through the codebase."""

# --- Camera ---
CAMERA_RESOLUTION = (640, 480)   # keep low for real-time inference on Pi 5
CAMERA_FRAMERATE = 30

# --- YOLO model ---
MODEL_PATH = "vision/models/best.pt"
CONFIDENCE_THRESHOLD = 0.5
FISH_CLASS_NAME = "fish"         # set this from the Stage 0 model audit

# --- Web stream ---
WEB_HOST = "0.0.0.0"
WEB_PORT = 5000
