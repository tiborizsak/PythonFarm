ips = []
ports = []
users = []
passwords = []

with open('proxies.out', 'r') as f:   # Replace 'proxies.txt' with your actual file name
    lines = f.readlines()

for line in lines:
    oip, oport, ouser, opassword = line.strip().split(':')
    ips.append(oip)
    ports.append(oport)
    users.append(ouser)
    passwords.append(opassword)

print("IPs: ", ips)
print("Ports: ", ports)
print("Users: ", users)
print("Passwords: ", passwords)
