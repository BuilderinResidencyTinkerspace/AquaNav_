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
