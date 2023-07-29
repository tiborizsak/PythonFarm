#from scapy.all import Ether, ARP, srp
import scapy.all as scapey

def szken(ip, interface):
    ether = scapey.Ether()
    arp = scapey.ARP(pdst=ip)
    answer, _ = srp(ether/arp, iface=interface, timeout=1, verbose=0)
    print(answer.summary())

szken("192.168.0.1", "wlan0")  # replace "eth0" with your interface name

