# Week 8

Goal this week:To improve the fish tracking and start connecting it with the rover's wheel movement.

## What we did

We temporarily borrowed a battery from someone so that we could continue testing the rover while working on the power-supply issue.
Using the temporary battery, we tested the rover with the aquarium and checked the wheel movement.
We tested the fish tracking again and tried to connect the tracking system with the wheel movement.
Initially, we were using YOLO for fish tracking, but after trying it several times and facing different issues, we decided to try OpenCV instead.
With OpenCV, the fish tracking gave us better results, so we continued with this approach.
We then started with a simple movement logic:
If the fish is stationary, the wheels should remain stopped.
If the fish is moving, the wheels should start moving.
We tried connecting this basic fish-movement detection with the wheel-control system.
During testing, the Raspberry Pi kept powering off because the available power supply was not sufficient.

## Problems and blockers

We had several difficulties with the YOLO-based fish tracking, so we changed our approach to OpenCV.
Connecting the fish tracking directly to the wheel movement was more difficult than testing each part separately.
The Raspberry Pi was repeatedly shutting down during testing because of insufficient power.
The temporary battery helped us continue testing, but it was not a permanent solution.
Decisions

## Decisions

We decided to continue with OpenCV for fish tracking because it was giving better results in our tests.
We started with a simple moving/stationary logic before implementing directional movement.
We used a borrowed battery temporarily so that testing could continue while we worked on a proper power solution.

## Next week

We decided to continue with OpenCV for fish tracking because it was giving better results in our tests.
We started with a simple moving/stationary logic before implementing directional movement.
We used a borrowed battery temporarily so that testing could continue while we worked on a proper power solution.

## Links

- Code:
- Photos / CAD:
