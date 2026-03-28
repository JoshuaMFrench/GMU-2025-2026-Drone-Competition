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
- **Left side** — a numbered Apriltag indicating gate order
- **Right side** — one or more encrypted QR codes

If a gate has **multiple QR codes**, only one is legitimate. Your code must identify and use the correct one.

---

## Apriltags

The course uses Apriltags from the **tag16h5** family, sized **125mm across the diagonal**.

- Tag reference: [https://chaitanyantr.github.io/apriltag.html](https://chaitanyantr.github.io/apriltag.html)
- Make sure to use the correct size PDF when printing

---

## QR Code Encryption

All QR codes on the course are encrypted with the **same key and algorithm**. Your job is to:

1. Crack the encryption using the provided plaintext and encrypted command files
2. Implement a decryption function that runs in real time during the flight

Each decrypted QR code will contain a Python dictionary in the following format:

```python
{
    gate_number: "movement_command"
}
```

Where `gate_number` is an integer denoting the order of that gate, and `movement_command` is a valid Tello instruction.

---

## Flight Logic

The drone should follow this loop for each gate:

```
1. Detect the Apriltag to identify the upcoming gate number
2. Scan and decode the QR code(s) on that gate
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
4. Set up QR code scanning for the right side of each gate
5. Integrate detection, decryption, and Tello movement commands into a single autonomous flight script
6. Test on the ground before flying

---

## Grading

Grading will be done according to the provided rubric. Key areas include:

| Criteria | Notes |
|----------|-------|
| Correct gate ordering | Must follow Apriltag sequence starting from 0 |
| Successful QR decryption | Must identify and decrypt the legitimate QR code per gate |
| Correct movement execution | Drone must act on the command before proceeding |
| Course completion | Drone must land via the final gate's land command |

---

## Video

Here is our [video](https://www.youtube.com/watch?v=GVJd_MzyqwA) illustrating the drone doing the course, operating on only the correct encrypted QR codes associated with the Apriltag for the gate.

## Questions?

Open an issue or reach out to the challenge organizers.
