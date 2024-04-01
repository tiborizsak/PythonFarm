import socket

# Configuration
syslog_server_ip = 'syslog-ng.server.ip'  # Replace with your syslog-ng server IP
syslog_server_port = 514  # The TCP port your syslog-ng server is listening on
message_template = "<14>Test message from {} - count {}"
next_ip = '172.16.0.200'  # Example IP, replace with the actual IP you're working with

# Function to send syslog message over TCP
def send_syslog_message(ip, count):
    message = message_template.format(ip, count)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((syslog_server_ip, syslog_server_port))
        sock.sendall(message.encode('utf-8'))

# Main loop to send a set of messages
for count in range(1, 6):  # Adjust the range as needed for your tests
    send_syslog_message(next_ip, count)
    print(f"Sent message {count} from IP {next_ip}")

print("Finished sending messages.")
