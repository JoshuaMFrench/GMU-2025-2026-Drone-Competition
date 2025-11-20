The goal of the Cryptographic Drone Race challange is to create Python code that allows for the tello drone to sucessfully navigate the corse.

The challange is set up with a series of gates that have a numbered april tag on the left side and an encrypted QR code on the right.
To compleate the challange the drone must navigate the entire corse in the correct order according to the april tags and QR codes (starting from 0).
Each QR code will be encrypted with the same key and alogrythem, it is your job to crack the encryption and create code that can decrypt the QR codes in real time.
Each QR code's plantext will consist of a number (denoting the order of the gates) and a movement command for the tello.
Once the  Drone has navigated to the center of the gate, it should act on the movment command it gathered from the QR code.
The last QR code will always contain a land command.
Grading will be done according to the given rubric.

You are provided with:
1) Skeleton code (optinal to use)
2) PDF of the April tags. 
3) A encrypted, and plaintext list of all possible movement commands
4) Three Encrypted QR codes for you to verify the functinality of your code.
