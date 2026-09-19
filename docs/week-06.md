# Week 6

Goal this week:To move from controlling the rover through the ESP32's own Wi-Fi website to controlling it through the Raspberry Pi, so that the control system would be smoother and less laggy.
## What we did

In the previous weeks, we had already connected the vehicle, placed the aquarium on it, and successfully tested its movement.
At that stage, the rover was being controlled using an ESP32, which created its own Wi-Fi network and hosted a local website for controlling the vehicle.
Although the vehicle was working, the local website was lagging and the controls were not responding as smoothly as we wanted.
We discussed how we could improve this, and Shan suggested moving the control system to the Raspberry Pi.
Our plan was to keep the Raspberry Pi and ESP on the same Wi-Fi network and use the Raspberry Pi as the main control point.
Before making this change, we had to make sure the ESP side was working properly.
We faced an issue where, when the ESP32 was disconnected from the laptop, its Wi-Fi connection/local website would also stop working properly.
We also had trouble uploading the required code to our previous ESP32.
To continue testing, we got a NodeMCU and made the required motor-driver and power connections.
We uploaded the motor-control code to the NodeMCU and successfully enabled its Wi-Fi.
After that, we tested the vehicle again and confirmed that the wheels and motors were working.
We then continued troubleshooting the original ESP32 because we still needed to understand why its Wi-Fi and programming setup was not working as expected.
During this troubleshooting, another problem appeared: the USB port of the ESP32 was damaged.
The ESP32 itself could still power on and work, but the USB port could no longer be used to upload new code.
Because of this, we could not continue programming that ESP32 normally.
So, this week became less about the final Pi control and more about getting the ESP side stable enough to make the transition.

## Problems and blockers

The ESP32's local control website had noticeable lag.
The ESP32's Wi-Fi/local website did not behave as expected when disconnected from the laptop.
We were unable to upload new code to the previous ESP32.
During troubleshooting, the ESP32's USB port was damaged, preventing further code uploads.
We therefore had to use a NodeMCU to continue the motor and Wi-Fi testing.

## Decisions

The ESP32's local control website had noticeable lag.
The ESP32's Wi-Fi/local website did not behave as expected when disconnected from the laptop.
We were unable to upload new code to the previous ESP32.
During troubleshooting, the ESP32's USB port was damaged, preventing further code uploads.
We therefore had to use a NodeMCU to continue the motor and Wi-Fi testing.

## Next week

Connect the Raspberry Pi and ESP/NodeMCU to the same Wi-Fi network.
Create a control system on the Raspberry Pi.
Send movement commands from the Pi to the ESP.
Test forward, backward, left, right, U-turn and stop commands.
Work towards replacing the laggy ESP-hosted website with the Raspberry Pi-based control system.

## Links

- Code:
- Photos / CAD:
