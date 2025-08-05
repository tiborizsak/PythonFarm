from scapy.all import sniff

# Init empty dictionary which will be populated with key:value pairs -> {"aa:bb:cc:dd:ee:ff": "192.168.0.1"}
IP_MAC_Map = {}

# Callback function to be invoked on a captured packet
def processPacket(packet):
    src_IP = packet['ARP'].psrc #IMPORTANT! .psrc is layer 3 -> address from the ARP packet itself
    src_MAC = packet['Ether'].src #IMPORTANT! .src is layer 2

    if src_MAC in IP_MAC_Map.keys():
        if IP_MAC_Map[src_MAC] != src_IP : #When referencing src_MAC the value part will be compared thus an ip address
            try:
                old_IP = IP_MAC_Map[src_MAC]
            except:
                old_IP = "unknown"
            message = f"Possible ARP attack detected!!! It is possible that the machine with IP address {str(old_IP)} is pretending to be {str(src_IP)}"
        return message
    else:
        IP_MAC_Map[src_MAC] = src_IP

sniff(count=0, filter="arp", store=0, prn=processPacket)
