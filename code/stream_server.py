"""Minimal Flask MJPEG server — just enough to view the live annotated
feed in a browser. No templates, no extra frameworks."""

import threading

import cv2
from flask import Flask, Response

app = Flask(__name__)

_latest_frame = None
_lock = threading.Lock()


def update_frame(frame):
    """Called by main.py every loop iteration with the newest annotated frame."""
    global _latest_frame
    with _lock:
        _latest_frame = frame.copy()


def _generate():
    while True:
        with _lock:
            if _latest_frame is None:
                continue
            ok, jpeg = cv2.imencode(".jpg", _latest_frame)
        if not ok:
            continue
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n")


@app.route("/")
def index():
    return ("<html><body><h2>AquaNav — Fish Detection</h2>"
            "<img src='/video_feed'></body></html>")


@app.route("/video_feed")
def video_feed():
    return Response(_generate(),
                     mimetype="multipart/x-mixed-replace; boundary=frame")


def run_server(host, port):
    app.run(host=host, port=port, threaded=True, use_reloader=False)
