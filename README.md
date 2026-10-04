# AquaNav

### A small rover with a simple idea — watch the fish, understand its movement, and move with it.

---

## What is AquaNav?

AquaNav is a four-wheel autonomous rover built around a simple aquarium, where the movement of a fish becomes the input for the robot.

The idea was to make a rover that doesn't just move because someone tells it to move.

Instead, it uses a camera to observe the fish, understand where it is in the aquarium, and make a movement decision based on that position.

The project combines:

**Mechanical Design + Electronics + Computer Vision + Robotics**

into one experimental platform.

---

## Where did the idea come from?

AquaNav didn't start with a fixed design.

During the early stages of the project, we explored several ideas, including an automatic medicine dispenser and a rover-to-drone concept.

Later, we came across a concept of a vehicle responding to fish movement.

That idea caught our attention.

We started asking:

> What if we actually built something like that ourselves?

From there, the project slowly developed into AquaNav.

The first few weeks were mostly about figuring out what the rover should look like, how much weight it could carry, how to move it, and how to make it understand the fish.

---

## The Idea Behind the Robot

The basic concept is simple:

```text
                 CAMERA
                    |
                    v
             +-------------+
             |    FISH     |
             |  TRACKING   |
             +------+------+
                    |
             Fish Position
                    |
                    v
             +-------------+
             |   DECISION  |
             |    LOGIC    |
             +------+------+
                    |
                    v
             +-------------+
             |    MOTOR    |
             |   CONTROL   |
             +------+------+
                    |
                    v
                  ROVER
The camera watches the aquarium.
The vision system determines where the fish is.
The movement logic decides what the rover should do.
The motors then carry out that decision.
Building the Rover
The physical rover went through quite a few changes.
We initially searched for a ready-made base that could carry the aquarium. We tried furniture bases, a shoe rack, plywood and wooden structures.
Some were too weak.
Some were unsuitable.
Some simply didn't work for the size and weight we needed.
Eventually, we got access to an aluminium frame that had previously been made for another college project. This became the foundation of our rover.
We then mounted the motors and wheels and started testing movement.
The Wheel Problem
Choosing wheels turned out to be harder than expected.
We initially bought 60 mm mecanum wheels because they looked suitable for the type of movement we wanted.
But once the aquarium and other components were added, we realised that the wheels were struggling with the load.
We experimented with different wheel arrangements and eventually moved to another wheel setup.
For the motor-wheel connection, we also designed and printed several versions of 3D-printed shafts.
Some were too loose.
Some were too tight.
Some were only a few millimetres away from fitting correctly.
After several attempts, we finally got a working fit.
Building the Aquarium
The aquarium was not just something placed on top of the rover.
Its size and weight directly affected the mechanical design.
We first visited aquarium shops looking for something suitable, but the available options didn't match what we needed.
So we approached a glass workshop and had an aquarium custom-built for our setup.
For testing, we chose a red fighter fish.
Before putting the fish into the aquarium, we cleaned the tank, added water, and allowed the fish to gradually adjust to the new water temperature.
This gave us the environment in which the actual tracking experiments could take place.
Making the Rover Move
The first movement tests were done using an ESP32, motor drivers and four motors.
We programmed the basic movements:
Forward
Reverse
Left
Right
U-turn
Stop
A local webpage was also created so that we could control the rover manually.
This worked, but the website was not as responsive as we wanted.
We then explored different ways of connecting the Raspberry Pi and the motor controller.
We tried Wi-Fi communication.
That didn't work reliably.
We eventually moved toward a USB connection between the Raspberry Pi and NodeMCU/ESP, allowing the Pi to send movement commands.
Power: One of Our Biggest Problems
Getting the motors to move was only half the problem.
We also needed enough power to run the entire system.
During testing, our batteries drained very quickly after changing the motor and wheel setup.
The Raspberry Pi also started shutting down when the available power wasn't enough.
At one point, we borrowed a temporary battery so that we could continue testing instead of stopping the project completely.
Power became one of the biggest lessons of the project:
A robot can have working code and working hardware, but without the right power source, none of it matters.
Teaching the Rover to See the Fish
Once the rover could move, our next challenge was much harder:
How do we make it understand the fish?
We first experimented with YOLO-based detection.
During testing, we noticed strange detection results. The red fish was sometimes represented incorrectly, and other objects could also be detected.
So we decided to build our own dataset.
We manually labelled more than 1000 images using Edge Impulse and trained our own detection model.
We repeated the process several times and improved the results.
But we still wanted something more suitable for our final movement logic.
From YOLO to OpenCV
After many experiments, we changed our approach.
Instead of depending entirely on YOLO, we started using OpenCV for tracking.
This worked better for what we actually needed.
We didn't need the rover to identify everything inside the aquarium.
We mainly needed one piece of information:
Where is the fish right now?
That changed the direction of the project.
Turning Position into Movement
We first tried a very basic idea:
