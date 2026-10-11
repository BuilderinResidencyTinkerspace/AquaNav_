"""Thin wrapper around Picamera2 so the rest of the codebase never talks to
the camera driver directly."""

from picamera2 import Picamera2

from config import settings


class CameraStream:
    def __init__(self, resolution=settings.CAMERA_RESOLUTION):
        self.picam2 = Picamera2()
        cam_config = self.picam2.create_preview_configuration(
            main={"size": resolution, "format": "RGB888"}
        )
        self.picam2.configure(cam_config)

    def start(self):
        self.picam2.start()

    def stop(self):
        self.picam2.stop()

    def get_frame(self):
        """Return one frame as a numpy array (H, W, 3) in RGB order."""
        return self.picam2.capture_array()
