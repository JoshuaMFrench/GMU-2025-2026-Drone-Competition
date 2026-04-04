🚁 Drone Swarm Hacking Challenge

A hands-on cybersecurity challenge demonstrating how insecure IoT devices (DJI Tello drones) can be compromised over a local network using ARP spoofing and command injection.

📌 Overview

This project simulates a drone swarm operating on a shared Wi-Fi network and demonstrates how a malicious actor can:

Intercept communication using ARP spoofing (MITM attack)

Isolate a drone from the swarm

Inject malicious commands to take control

This challenge is designed for students to explore real-world network vulnerabilities in IoT systems.

💥💥💥
Python script materials were sourced from Steven J Antezana - George Mason University
💥💥💥

🎯 Objectives

Participants must:

Successfully hijack at least one drone in the swarm

Execute up to two attacker-controlled commands after takeover

(Advanced) Repeat the attack on a second drone

🧠 Learning Outcomes

Understand ARP spoofing and MITM attacks

Analyze unsecured network communication

Execute command injection attacks

Observe real-time behavior of compromised IoT devices

🧰 Requirements

Hardware

2x DJI Tello drones

1x Router (shared network)

1–2x Laptops (controller + attacker)

Software

Python 3.x

djitellopy library

Provided scripts in this repository

-----------------------------------------------------
⚙️ Setup - THIS WILL BE DONE FOR YOU AT GEORGE MASON

1. Connect Drones to the Router (Station Mode)

By default, Tello drones broadcast their own Wi-Fi.

2. Configure Static IP Addresses

Use router DHCP reservations

Assign each drone a fixed IP address

-----------------------------------------------------

4. Update Scripts

Before running anything, configure:

DRONE_IP = "192.168.X.X"

DRONE_MAC = "XX:XX:XX:XX:XX:XX"

ATTACKER_IP = "192.168.X.X"

Incorrect values will cause the attack to fail

🚀 Execution Flow

Step 1 — Start the Swarm

Run the swarm script

Expected behavior:

Drones take off

Execute synchronized movements

Land together

Step 2 — Launch ARP Spoofing Attack

While the swarm is taking off, this is your window to run your ARP poisoning script.

This creates a man-in-the-middle attack between the controller and target drone.

Step 3 — Inject Commands (Takeover)

After spoofing is active run your spoofing commands.

This sends attacker-controlled commands to the drone

---------------------------------------------------------
✅ Success Criteria

A successful attack will result in:

One drone breaking from swarm behavior

The second drone continuing normally

The compromised drone executing attacker commands

🧠 Scoring System

Task	                                 Points

Hack 1 drone	                         4

Execute 1 command	                     +2

Execute 2 commands	                   +4

Hack both drones	                     up to 16 total

----------------------------------------------------------

⚠️ Known Issues

Drones may not always connect reliably to the router

Swarm execution may fail depending on connectivity

Reconnection may be required between attempts

💡 Tips for Success

Start by targeting one drone only

Verify IP/MAC addresses before attacking

Timing is critical — launch attack during swarm execution

If nothing happens, debug your network configuration

-----------------------------------------------------------

🧪 Example Attack Flow

Swarm starts normally

Attacker launches ARP spoofing

One drone stops responding to swarm commands

Attacker injects new commands

Drone follows attacker instead of controller

------------------------------------------------------------

🔐 Disclaimer

This project is for educational purposes only.

Do not use these techniques on networks or devices you do not own or have explicit permission to test.

------------------------------------------------------------

👤 Author

Travis Hannam

Cyber Security Engineering

George Mason University

