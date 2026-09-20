# Week 7

**Goal this week:**To control the rover using the Raspberry Pi instead of the ESP's Wi-Fi, create the control website on the Pi, and test the wheels, ultrasonic sensor, and fish tracking together.

## What we did

After last week's testing, our main goal was to make the Raspberry Pi the main control system for the rover.
We first tried to connect the ESP and Raspberry Pi to the same Wi-Fi network so that they could communicate wirelessly.
However, this did not work as expected. The ESP was only working properly when it was connected to the laptop.
After trying different ways to make the Wi-Fi connection work, we decided not to spend more time on that approach.
Instead, we decided to connect the NodeMCU/ESP to the Raspberry Pi using USB.
We then uploaded the required code to both the ESP and Raspberry Pi so that the Pi could send commands to control the rover's wheels.
We also decided to create the local control website on the Raspberry Pi itself, instead of hosting it through the ESP. This was expected to make the control system more usable and reduce the lag we faced earlier.
Once the connection was ready, we first tested the wheels and motor movements from the Raspberry Pi.
After confirming that the wheels were responding correctly, we connected the ultrasonic sensor and tested it separately.
We then tested our fish-tracking system using the Raspberry Pi camera and the trained model.
The wheel control, ultrasonic sensor, and fish tracking were all working successfully when tested separately.
This was an important step because all the individual parts of the project were now working. The next challenge was to bring everything together into one complete system.

## Problems and blockers

The ESP and Raspberry Pi could not communicate properly through the same Wi-Fi network.
We found that the ESP worked only when connected to the laptop, so we dropped the wireless approach for now.
We switched to a USB connection between the Pi and ESP.
Another major problem appeared with the power supply.
Earlier, we were using three batteries of 3.75 V each, giving us around 11.25 V nominally.
After changing the wheels and motors, the new setup required much more power.
The batteries were getting drained in around 5 minutes of operation.
We tried different batteries, but they were also getting drained quickly.
Our measured requirement was around 14 V, 2 A, so we realised that we needed a proper power source capable of supplying enough current for the new motors.
Because of the power problem, we could not continuously test the complete system using the batteries.

## Decisions

We decided to use USB communication between the Raspberry Pi and ESP/NodeMCU instead of relying on Wi-Fi communication for now.
We moved the local control website to the Raspberry Pi to make the control system more usable.
We decided that the wheels, ultrasonic sensor, and fish tracking would first be tested separately before integrating them.
For testing, we temporarily used an external power supply instead of the batteries so that we could continue testing the wheels and tracking system.
We also decided to find a suitable battery/power source that can handle the rover's higher power requirement.

## Next week

Find a suitable battery that can provide enough voltage and current for the new motors.
Integrate the wheel control, ultrasonic sensor, camera, and fish tracking into one system.
Make the rover respond automatically to the fish's movement.
Test the complete system with the aquarium and fish.

## Links

- Code:
- Photos / CAD:
