"""Stage 1 test: confirm the camera captures frames and save one to disk
so you can eyeball it. Delete once Stage 1 passes."""

import cv2

from camera.camera_stream import CameraStream

cam = CameraStream()
cam.start()

frame = cam.get_frame()          # RGB
bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
cv2.imwrite("stage1_test_frame.jpg", bgr)

print("Frame shape:", frame.shape)
print("Saved stage1_test_frame.jpg")

cam.stop()
