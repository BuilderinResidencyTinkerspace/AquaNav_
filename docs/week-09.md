# Week 9

**Goal this week:**
This was the last week of the Builder-in-Residence (BIR) program. Since we had improved the fish tracking in the previous week, our main goal this week was to make the rover's movement more accurate and reliable based on the fish's position.
## What we did
We first tried a basic movement model where the rover would simply follow the fish's movement. For example, if the fish moved forward, the wheels would move forward.
After testing this approach, we wanted to make the movement more accurate using OpenCV.
We divided the camera frame into four grids:
Top-left
Top-right
Bottom-left
Bottom-right
We also kept a center area for the fish.
The idea was that when the fish comes into the center area, the aquarium should stop moving.
When the fish moves into one of the four grids, the rover would move according to that grid.
We wrote the code for this strategy and tested it with the rover. The basic grid-based movement worked.
However, we noticed another problem. If the fish stayed outside the center area, the rover would keep moving continuously and would not stop.
We discussed this and came up with another approach.
The new idea was to make the rover move for around 5–8 seconds when the fish is outside the center, and then stop.
After stopping, the rover would wait for around 10 seconds before moving again.
This cycle would continue until the fish either stopped moving or came back to the center.
We tested this strategy, and it worked well. We decided to go with this approach for the final movement logic.

## Problems and blockers

The basic movement model was too simple and was not accurate enough.
Continuous movement created a problem when the fish remained outside the center area.
We needed a way to prevent the rover from continuously moving without giving the fish time to change its position.
We solved this by adding movement and stopping intervals to the control logic.

## Decisions

We decided to divide the camera frame into four grids with a center area for more accurate movement.
The rover would stop when the fish reached the center.
When the fish was outside the center, the rover would move according to its grid.
We added a 5–8 second movement period followed by a 10-second stopping period.
After testing, we decided to use this as our final movement strategy.

## Next week

Although the BIR program ends this week, we have an idea to continue developing the project and make it more useful in real-life situations.
We are planning to add a Guided Mode to the rover.
The idea is to make the rover work more like a guide robot in a shopping mall, such as the type of robot used to help people find places.
We are thinking of using LiDAR to map the entire area so that the rover can understand its surroundings and know where different locations are.
A screen or voice-control system could be added so that a person can tell the rover where they want to go.
The rover could then use the map and its navigation system to guide the person to that location.
This would be our next step in taking the project beyond fish tracking and exploring how the same rover could be used as a useful navigation and guidance robot.

## Links

- Code:
- Photos / CAD:
