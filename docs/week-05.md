# Week 5

**Goal this week:**

## What we did

Our next step was to bring the Raspberry Pi into the project because it would handle the camera and fish-tracking system.
We connected to the Raspberry Pi remotely using SSH through PowerShell. This allowed us to access and work on the Pi from our laptop.
Before starting fish tracking, we first needed to make sure that the Raspberry Pi camera was working properly.
We tested the camera using different camera commands and test programs, including rpicam-hello, and checked whether it could capture images and video correctly.
After testing and fixing the initial camera-related issues, we confirmed that the camera was working properly.

Starting the fish tracking
Once the camera was ready, we started working on the main part of the project — detecting and tracking the fish.
Our first approach was to use YOLO (You Only Look Once) for object detection.
Before training our own model, we tested the camera and detection with the available setup.
We noticed an unexpected problem: even though our fish was red, the camera/detection output was showing the fish as dark blue.
The system also detected people as blue, which made it difficult to clearly distinguish the fish from other objects in the camera view.
This became one of our main challenges because simply relying on colour was not giving us reliable fish detection.
We therefore decided that we needed to train the model specifically for our fish and our aquarium setup.

We started collecting images of our fish from different positions and conditions.
We manually labelled more than 1000 images, marking the fish in each image so that YOLO could learn what our fish looked like.
The labelling process took a lot of time because every image had to be checked carefully and the fish had to be marked correctly.
We included images where the fish was in different positions and parts of the aquarium so that the model would not only recognise it in one particular location.
After preparing the dataset, we trained the YOLO model using our labelled images.
We then tested the trained model with new images and camera footage.
We repeatedly checked the results and improved the training wherever the detection was not accurate enough.
After several rounds of testing and training, the model became much better at recognising our fish specifically.
This gave us a reliable starting point for the next stage, where we would use the fish's position to understand its movement and control the rover.

## Problems and blockers

Setting up SSH access to the Raspberry Pi was one of the first steps we had to get working.
We had to test the camera before beginning the tracking work.
The camera/detection system did not represent the fish's actual red colour correctly and showed the fish as dark blue.
It also detected people as blue, making simple colour-based detection unreliable.
We therefore had to move towards a trained object-detection model.
Creating a good dataset required manually labelling 1000+ images, which was time-consuming.
The first model was not perfect, so we had to test and improve it repeatedly.

## Decisions

We decided to use the Raspberry Pi for the camera and computer-vision part.
We chose YOLO as our first approach for fish detection.
Because the initial detection and colour representation were unreliable, we decided to train our own model.
We manually labelled 1000+ images to make the model more familiar with our specific fish and setup.

## Next week

Track the position of the fish using the trained model.
Determine whether the fish is moving left, right, forward or backward.
Convert the detected movement into rover movement commands.
Start connecting the Raspberry Pi tracking system with the ESP32 motor-control system.

## Links

- Code: # Check whether the Raspberry Pi camera is detected
rpicam-hello

# Display the camera preview for 5 seconds
rpicam-hello -t 5000

# Capture an image
rpicam-still -o test.jpg

# Capture an image after a 2-second delay
rpicam-still -t 2000 -o test.jpg

# Record a 10-second video
rpicam-vid -t 10000 -o test.h264

from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolo11n.pt")

# Train the model using our fish dataset
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="fish_tracking"
)

# Test the trained model
results = model.predict(
    source="test.jpg",
    conf=0.5
) 
path: /home/pi/fish_dataset

train: images/train
val: images/val

names:
  0: fish
- Photos / CAD:
