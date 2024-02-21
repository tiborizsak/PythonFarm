import re
from collections import defaultdict

def parse_log_line(line):
    pattern = r'(\w+\s+\d+\s+\d+:\d+):.*Syslog connection (accepted|closed); fd=\'(\d+)\'.*local=\'AF_INET\(([\d.]+):\d+\)\''
    match = re.search(pattern, line)
    if match:
        return match.groups()
    return None

def process_log_file(file_path):
    connections = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
    active_connections_per_minute = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r') as file:
        for line in file:
            data = parse_log_line(line)
            if data:
                timestamp, status, fd, local_ip = data
                if status == 'accepted':
                    connections[local_ip][timestamp][fd] = True
                elif status == 'closed':
                    connections[local_ip][timestamp][fd] = False

    # Calculate active connections per minute
    for local_ip, timestamps in connections.items():
        for timestamp, fds in timestamps.items():
            active_fds = sum(10 for fd_status in fds.values() if fd_status)
            active_connections_per_minute[local_ip][timestamp] = active_fds

    # Print results
    for local_ip in active_connections_per_minute:
        for timestamp, active_count in sorted(active_connections_per_minute[local_ip].items()):
            print(f"{local_ip} at {timestamp} had {active_count} active connections")

# Example usage
process_log_file('messages-20231021')
