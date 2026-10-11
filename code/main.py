"""Milestone 1: Camera -> YOLO fish detection -> bounding box -> fish
center -> live web stream.

Run this, then open http://<pi-ip>:5000 in a browser on the same network.
"""

import threading

import cv2

from camera.camera_stream import CameraStream
from config import settings
from vision.fish_detector import FishDetector
from vision.visualizer import draw_detections
from web.stream_server import run_server, update_frame


def main():
    camera = CameraStream()
    detector = FishDetector()

    camera.start()
    print("Camera started. Web server: "
          f"http://{settings.WEB_HOST}:{settings.WEB_PORT}")

    server_thread = threading.Thread(
        target=run_server, args=(settings.WEB_HOST, settings.WEB_PORT),
        daemon=True,
    )
    server_thread.start()

    try:
        while True:
            frame = camera.get_frame()  # RGB
            bgr_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            detections = detector.detect(bgr_frame)
            annotated = draw_detections(bgr_frame, detections)

            if detections:
                d = detections[0]
                print(f"Fish center: ({d.center_x}, {d.center_y}) "
                      f"conf={d.confidence:.2f}")

            update_frame(annotated)

    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        camera.stop()


if __name__ == "__main__":
    main()
