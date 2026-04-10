# Cryptographic Drone Race

A Python programming challenge where you build autonomous navigation code for a Tello drone to complete an encrypted gate course, without any human input during the run.

---

## Overview

The drone must navigate a series of physical gates arranged in a **U-shaped course**. Each gate is identified by an Apriltag and carries an encrypted QR code containing movement instructions. Your code must detect, decrypt, and act on these instructions in real time to guide the drone through the course in the correct order.

---

## Course Layout

The gates are arranged in a **U shape**. The drone starts at the open end of the U, travels down one side, rounds the bottom, and returns up the other side to finish. Gates must be navigated in order from 0 to the last gate — following the U-shaped path, not cutting across it.

---

## Gate Structure

Each gate consists of:
- A numbered Apriltag indicating gate order (always on the **left** side)
- One or more encrypted QR codes (may be on **either** side)

If a gate has **multiple QR codes**, only **one** is legitimate. Your code must identify and use the correct one.

---

## Apriltags

The course uses Apriltags from the **tag16h5** family, sized **125mm across the diagonal**.

- Tag reference: [https://chaitanyantr.github.io/apriltag.html](https://chaitanyantr.github.io/apriltag.html)
- Make sure to use the correct size PDF when printing

You may choose to use or not use the Apriltags, as they are just to navigate the drone to the center of the gate.

---

## QR Code Encryption

All QR codes on the course are encrypted with the **same key and algorithm**. Your job is to:

1. Crack the encryption using the provided plaintext and encrypted command files
2. Implement a decryption function that runs in real time during the flight

Each decrypted QR code will contain a Python dictionary in the following format:

```python
{
    gate_number: ["movement_command", "movement_command"}
}
```

Where `gate_number` is an integer denoting the order of that gate, and `movement_command` is a valid Tello instruction.

Instructions are stored within an ordered list, starting from the first commmand to be executed. 

Some commands have a number associated, which are formatted like following:

```python
    "movement_command number" <-- Delineated by a space character
```

Other commands do **not** have a number associated, which are formatted like following:

```python
    "movement_command"
```

Your code **must** be able to handle both cases. Please reference the [DJI Tello documentation](https://djitellopy.readthedocs.io/en/latest/tello/#djitellopy.tello.Tello.move_back) and our command space text file for any questions about the commands or command structure.

---

## Flight Logic

The drone should follow this loop for each gate:

```
1. Detect the Apriltag (or otherwise identify the gate) to identify the upcoming gate number
2. Scan for the QR code(s) on that gate
3. Decrypt the QR code(s) and identify the legitimate one
4. Fly to the center of the gate
5. Execute the movement command from the decrypted QR code
6. Proceed to the next gate
```

The course starts at gate **0**. The **last gate** and **incorrect gates** will always contain a **land command** to end the run.

---

## Provided Files

| File | Description |
|------|-------------|
| Skeleton code | Optional starting framework for your solution |
| Apriltag PDF | Printable tags (tag16h5 family, 125mm diagonal) |
| Command files (x2) | One plaintext and one encrypted list of all possible movement commands |
| Test PNGs (x3) | Three encrypted QR codes to verify your decryption implementation before the live run |

Use the plaintext and encrypted command files together to reverse-engineer the encryption scheme. Use the three test QR codes to validate that your decryption pipeline works correctly before attempting the course.

---

## Getting Started

1. Study the plaintext and encrypted command files to reverse the encryption algorithm
2. Implement a decryption function and verify it against the three test QR codes
3. Set up Apriltag detection to read gate order from the left side of each gate
4. Set up QR code scanning for each gate
5. Integrate detection, decryption, and Tello movement commands into a single autonomous flight script
6. Test on the ground before flying

---

## Grading

Grading will be done according to the provided rubric. Key areas include:

| Criteria | Notes |
|----------|-------|
| Correct gate ordering | Must follow Apriltag sequence starting from 0 |
| Successful QR decryption | Must identify and decrypt the legitimate QR code per gate |
| Correct movement execution | Drone must act on the QR command(s) before proceeding |
| Course completion | Drone must land via the final gate's land command |

For more in-depth information about this challenge, please view our [competition description document](https://docs.google.com/document/d/1TKOaak7x9xW8TqyNmZzIPVmJ_aiLyp3A-kBdy1dTi-A/edit?usp=sharing) for a breakdown of the points and such.

---

## Video

Here is our [video](https://www.youtube.com/watch?v=GVJd_MzyqwA) illustrating the drone doing the course, operating on only the correct encrypted QR codes associated with the Apriltag for the gate.

## Questions?

Open an issue or reach out to the challenge organizers.
