from picamera2 import Picamera2
import time
import os

# ==============================
# SETTINGS
# ==============================

TOTAL_IMAGES = 1000
INTERVAL = 0.5

SAVE_DIR = "/home/aquanav/AquaNav/fish_dataset"

WIDTH = 640
HEIGHT = 480

# ==============================
# CREATE FOLDER
# ==============================

os.makedirs(SAVE_DIR, exist_ok=True)

# ==============================
# CAMERA
# ==============================

picam2 = Picamera2()

config = picam2.create_still_configuration(
    main={
        "size": (WIDTH, HEIGHT),
        "format": "RGB888"
    }
)

picam2.configure(config)

picam2.start()

time.sleep(2)

print()
print("================================")
print("AquaNav Fish Image Collector")
print("================================")
print()
print(f"Saving to: {SAVE_DIR}")
print(f"Images: {TOTAL_IMAGES}")
print(f"Interval: {INTERVAL} seconds")
print()
print("Starting in 5 seconds...")
print()

time.sleep(5)

# ==============================
# CAPTURE
# ==============================

for i in range(1, TOTAL_IMAGES + 1):

    filename = os.path.join(
        SAVE_DIR,
        f"fish_{i:04d}.jpg"
    )

    picam2.capture_file(filename)

    print(
        f"[{i}/{TOTAL_IMAGES}] "
        f"{filename}"
    )

    time.sleep(INTERVAL)

# ==============================
# FINISH
# ==============================

picam2.stop()

print()
print("================================")
print("DONE!")
print(f"{TOTAL_IMAGES} images captured.")
print(f"Saved in: {SAVE_DIR}")
print("================================")