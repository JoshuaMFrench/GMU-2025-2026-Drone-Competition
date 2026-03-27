# Shape Detection Drone Controller

A computer vision challenge where your model must detect **shape color combinations** and trigger drone movement **only on circles**, ignoring triangles and squares entirely.

---

## Overview

Build a vision pipeline that:
- Detects **all shape color combinations** individually (e.g., red circle, blue triangle, green square)
- **Triggers drone movement** when a circle is detected
- **Ignores** triangles and squares
- Works in real time from a drone camera feed

---

## Expected Behavior

See the drone in action:

| View | Link |
|------|------|
| Human-View (drone perspective) | [Watch on YouTube](https://youtube.com/shorts/lY-6Xi5-xPc?feature=share) |
| Laptop-View | *(link coming soon)* |

The drone detects all shapes and logs/displays them, but **only moves** in response to circles.

---

## Circle Response Behavior

Each circle color maps to a specific sequence of drone movements. When a circle is detected, the drone must execute the full movement sequence before resuming detection. Each movement sequence will result in the drone ending roughly where it started.

| Circle Color | Movement Sequence |
|--------------|-------------------|
| Green | Up, Down, Up |
| Yellow | Forward, Back, Forward |
| Purple | Right, Left, Right |

Once **all three circle colors have been detected**, the drone executes a **flip**.

```
on detect("green circle"):
    drone.up() -> drone.down() -> drone.up()
    green_detected = True

on detect("yellow circle"):
    drone.forward() -> drone.back() -> drone.forward()
    yellow_detected = True

on detect("purple circle"):
    drone.right() -> drone.left() -> drone.right()
    purple_detected = True

if (green_detected & yellow_detected & purple_detected):
    drone.flip()
```

Triangles and squares of any color must be detected and logged, but must **never** trigger any movement.

---

## Dataset

Download the raw image data from the provided folders. Each image contains one or more shapes with distinct color-shape combinations.

Included:
- Raw image data (for training your own model from scratch)
- YOLOv8-format labels (pre-annotated bounding boxes and class labels)

---

## Model Requirements

You are **free to use any computer vision approach**, including but not limited to:

- Training your own **YOLOv8** model using the provided labels
- Using a **pre-trained model** with custom fine tuning
- Using **classical CV** techniques (e.g., OpenCV contour detection with color masking)
- Any other detection framework you prefer

The only hard requirement: **each shape color combination must be detected individually** (e.g., "red circle" and "blue circle" are distinct classes).

---

## Getting Started

1. Download the dataset from the provided folder links
2. Choose your model or approach
3. Train or configure your detector on the shape color classes
4. Integrate detection and drone control 
5. Test against the expected behavior

---

## Evaluation Criteria

| Criteria | Notes |
|----------|-------|
| Detects all shape-color combinations | Required |
| Correct movement sequence per circle color | Required |
| Flip executed after all three circles detected | Required |
| Drone ignores triangles and squares | Required |

---

## Questions?

Open an issue or reach out to the challenge organizers.
