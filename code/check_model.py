"""One-off script to inspect an existing YOLO checkpoint before reusing it.

Usage:
    python check_model.py path/to/best.pt
"""

import sys

from ultralytics import YOLO

if len(sys.argv) != 2:
    print("Usage: python check_model.py path/to/best.pt")
    sys.exit(1)

model = YOLO(sys.argv[1])

print("Class names:", model.names)
print("Number of classes:", len(model.names))
print("Model task:", model.task)
