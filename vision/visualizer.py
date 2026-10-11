"""Draws detection boxes and centers onto a frame for the live web view."""

import cv2


def draw_detections(frame, detections):
    for d in detections:
        cv2.rectangle(frame, (d.x1, d.y1), (d.x2, d.y2), (0, 255, 0), 2)
        cv2.circle(frame, (d.center_x, d.center_y), 5, (0, 0, 255), -1)
        label = f"{d.confidence:.2f}"
        cv2.putText(frame, label, (d.x1, max(d.y1 - 8, 0)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
