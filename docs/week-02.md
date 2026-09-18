# Week 2

Goal this week:To find suitable wheels, connect the wheels to the motors and base, and complete the initial motor-control circuit.

## What we did

-We contacted Thomson Electronics to get the wheels we needed.
We decided to use 60 mm mecanum wheels and purchased them.
We then faced a new challenge: connecting the motors to the wheels and the base.
We needed a suitable shaft to connect the motor and wheel, so we decided to 3D print one.
We first tried mounting the motors and wheels onto the shoe rack.
We then had doubts about whether the shoe rack could handle the weight, so we moved towards using the wooden base.
We 3D printed several shafts, with each version differing by a few millimetres.
None of the first versions fitted correctly, so we spent a lot of time doing trial and error.
Finally, we got a shaft with the correct fit for the motor and wheel.
After solving the mechanical connection, we prepared the electronics using:
ESP32
2 motor drivers
4 motors
1 breadboard
3 batteries, each 3.75 V
We completed the initial connections between these components.
However, we accidentally connected the batteries directly without using a buck converter, which caused the ESP32 to crash due to the excessive voltage supplied to it.

## Problems and blockers

Finding the correct wheels took some searching.
The motor and mecanum wheel needed a custom shaft to connect them properly.
Several 3D-printed shaft designs failed because they were slightly different in size.
We had doubts about the strength of the shoe rack and moved towards the wooden base.
The ESP32 was damaged/crashed after we connected the battery supply incorrectly without a buck converter.

## Decisions

We decided to use 60 mm mecanum wheels.
We decided to use 3D-printed shafts to connect the motors and wheels.
After several attempts, we finalised the shaft with the correct fit.
We decided to replace the damaged ESP32 and redo the connections properly with the correct power supply.

## Next week

Get a new ESP32.
Redo the motor-driver and motor connections.
Use a buck converter to provide the correct voltage to the ESP32.
Test the motors and wheels safely.

## Links

- Code:
- Photos / CAD:<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/adf1c08a-e3a6-4a01-aff5-ffd114313915" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/4b4d160c-843f-44df-9843-781d67ec0070" />

<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/29aa1b4a-c678-4e8d-9fc3-dae1885cdf66" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/13fea29d-3efd-4473-be34-5e94ee876d9a" />
<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/10018e21-7715-4759-b7ee-8e2eaca5ada9" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/6f48c0f0-5311-48b0-a916-2f71a439a9e7" />






