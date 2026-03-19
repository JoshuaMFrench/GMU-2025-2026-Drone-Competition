The goal of the Cryptographic Drone Race challenge is to create Python code that allows for a Tello drone to successfully navigate the course.

The challenge will have a series of gates, each with a numbered Apriltag on the left side and an encrypted QR code on the right. Some gates may have two or more encrypted QR codes, but only one will be legitimate.

To complete the challenge, the drone must navigate the entire course in the correct order according to the Apriltags and QR codes (starting from 0).

Each QR code will be encrypted with the same key and algorithm; it is your job to crack the encryption and create code that can decrypt the QR codes in real time.

Each QR code's plaintext will consist of a dictionary with the key being a number (denoting the order of the gates) and the value being the movement command(s) for the Tello.

Once the drone has navigated to the center of the correct gate, it should act on the movement command it gathered from the legitimate QR code before moving onto the next gate.

The last QR code will always contain a land command to end the course.

Grading will be done according to the given rubric.

You are provided with:
1) Skeleton code (optional to use).
2) PDF of the Apriltags (we will be using [Apriltags](https://chaitanyantr.github.io/apriltag.html) of the family "tag16h5" and of 125mm across the diagonal, so please look at the correct size PDF). 
3) An encrypted and plaintext list of all possible movement commands (provided in the two command space files).
4) Three Encrypted QR codes for you to verify the functionality of your code (provided in the three test PNGs).
