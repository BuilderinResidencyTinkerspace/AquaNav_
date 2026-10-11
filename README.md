# AquaNav — Milestone 1

Camera → YOLO fish detection → bounding box → fish center → live web stream.

## Setup (Raspberry Pi 5, Raspberry Pi OS)

Uses system Python (3.11 on Bookworm), not a standalone 3.13 install —
`picamera2` doesn't have reliable 3.13 wheels yet and is a system package
tied to libcamera.

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv python3-picamera2 --no-install-recommends

python3 -m venv --system-site-packages ~/aquanav-venv
source ~/aquanav-venv/bin/activate

pip install ultralytics flask opencv-python-headless numpy
```

## Reuse your existing model

Copy your teammate's checkpoint in, then audit it:

```bash
python check_model.py /path/to/best.pt
```

This prints the class names/count. Update `FISH_CLASS_NAME` in
`config/settings.py` if needed, then:

```bash
cp /path/to/best.pt vision/models/best.pt
```

## Test one subsystem at a time

```bash
python test_camera.py      # Stage 1: camera only, saves stage1_test_frame.jpg
python test_detection.py   # Stage 2: camera + YOLO, prints to terminal
python main.py              # Stage 3: full pipeline + live web stream
```

For Stage 3, open `http://<raspberry-pi-ip>:5000` in a browser on the same
network.

## Structure

```
AquaNav/
├── camera/
│   └── camera_stream.py     # Picamera2 wrapper
├── vision/
│   ├── fish_detector.py     # YOLO wrapper, returns Detection objects
│   ├── visualizer.py        # draws boxes/centers on frames
│   └── models/best.pt       # your trained checkpoint (not included)
├── web/
│   └── stream_server.py     # Flask MJPEG server
├── config/
│   └── settings.py          # all tunable constants
├── check_model.py           # one-off model audit script
├── test_camera.py           # Stage 1 test
├── test_detection.py        # Stage 2 test
└── main.py                  # Stage 3 — full Milestone 1 pipeline
```

Delete `test_camera.py`, `test_detection.py`, and `check_model.py` once
you've moved past Milestone 1 — they're scaffolding, not part of the
running system.
