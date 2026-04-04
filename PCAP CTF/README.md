#  PCAP CTF
 
---
 
##  Overview
 
You have been given a PCAP (Packet Capture) file containing network traffic recorded from a live system. Hidden within this traffic is a video stream that was being transmitted over the network. Your mission is to reconstruct the video from the raw packet data and find the flag concealed within it.
 
## Objective

- Analyze the provided PCAP file using Wireshark
- Identify and isolate the video stream within the network traffic
- Export and reconstruct the video file from the captured data
- Watch the video and locate the hidden flag
 
##  Background
 
**What is a PCAP file?**
A PCAP file is a recording of raw network traffic. It stores every packet that passed through a network interface during a capture session — including headers, payloads, timestamps, and protocol data.
 
**What is Wireshark?**
Wireshark is a free, open-source network protocol analyzer. It lets you inspect packet contents, filter by protocol, follow data streams, and export reassembled objects (such as files transmitted over HTTP, RTP streams, or raw TCP data) from a capture.
