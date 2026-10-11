"""YOLOv8-based fish detector. Wraps ultralytics so the rest of the code
only deals with plain Python data, not YOLO-specific objects."""

from dataclasses import dataclass

from ultralytics import YOLO

from config import settings


@dataclass
class Detection:
    x1: int
    y1: int
    x2: int
    y2: int
    confidence: float
    center_x: int
    center_y: int


class FishDetector:
    def __init__(self, model_path=settings.MODEL_PATH,
                 confidence=settings.CONFIDENCE_THRESHOLD):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame) -> list[Detection]:
        """Run inference on one BGR frame, return a list of Detections."""
        results = self.model(frame, conf=self.confidence, verbose=False)[0]

        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            detections.append(
                Detection(int(x1), int(y1), int(x2), int(y2), conf, cx, cy)
            )
        return detections
