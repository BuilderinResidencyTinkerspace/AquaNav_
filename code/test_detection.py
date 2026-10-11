"""Stage 2 test: run detection on 10 live frames and print results to the
terminal (no web server involved). Delete once Stage 2 passes."""

import time

import cv2

from camera.camera_stream import CameraStream
from vision.fish_detector import FishDetector

cam = CameraStream()
detector = FishDetector()
cam.start()

for i in range(10):
    frame = cam.get_frame()
    bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    start = time.time()
    detections = detector.detect(bgr)
    elapsed = time.time() - start

    print(f"Frame {i}: {len(detections)} detection(s), "
          f"{elapsed*1000:.0f} ms inference")
    for d in detections:
        print(f"  -> center=({d.center_x},{d.center_y}) conf={d.confidence:.2f}")

cam.stop()
