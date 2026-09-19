# Week 4

Goal this week:To build a stronger rover base, make the wheels work, and test whether the vehicle could carry the aquarium.

## What we did

We realised that the 60 mm mecanum wheels could not handle the weight of the setup properly.
We thought of using two mecanum wheels along with a caster wheel to provide better support.
We searched several shops for a suitable caster wheel, but could not find one.
During a random conversation with Jayasurya and Shan, we discussed how an aluminium frame would give the rover better support and grip.
Jayasurya helped us by giving us an aluminium frame/base that he had made for a college event two years ago.
We connected the motors and wheels to the aluminium frame.
Since the earlier 60 mm mecanum wheels were not suitable for the weight, we got another set of four wheels and connected them to the motors.
We connected the ESP32, two motor drivers, four motors and battery and tested the setup.
The motors and wheels worked successfully.
We uploaded code to control the rover to move forward, backward, left, right, U-turn and stop.
All the basic movements worked.
We then created a local-host control website to control the rover wirelessly.
The website worked and we were able to control the vehicle from it.
Finally, we placed the aquarium on the rover base to check whether it could carry the weight and still move.
The rover successfully carried the aquarium and moved.

## Problems and blockers

The 60 mm mecanum wheels were not able to properly support the weight.
We could not find a suitable caster wheel despite searching several shops.
We needed a stronger frame to support the aquarium and the components.

## Decisions

We decided to move away from the original 60 mm mecanum-wheel setup.
We used the aluminium frame provided by Jayasurya.
We replaced the earlier wheels with another set of four wheels.
We decided to control the rover using an ESP32 and a local-host website.

## Next week

Improve the rover's mechanical setup.
Work on the Raspberry Pi and camera.
Start testing object/fish detection and tracking.
Plan how the rover can respond automatically to the detected movement.

## Links

- Code:
- Photos / CAD:<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/304066d2-7c20-4b67-895c-f085f806633e" />
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/0ea31927-4aef-4837-a94e-9383c33c9409" />


