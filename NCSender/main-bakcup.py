import os
import subprocess
import time

def send_files_with_nc(directory_path, remote_host, remote_port):
    # List all files in the specified directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Iterate through each file and send it using nc (netcat)
    for file in files:
        file_path = os.path.join(directory_path, file)
        print(f"Sending {file_path} to {remote_host}:{remote_port}...")

        try:
            # The '-q 10' option makes nc quit 10 seconds after EOF
            result = subprocess.call(['nc', '-q', '10', remote_host, str(remote_port)], stdin=open(file_path, 'rb'))

            if result != 0:
                print(f"Error sending {file_path}.")
            else:
                print(f"Sent {file_path} successfully.")
        except subprocess.TimeoutExpired:
            print(f"Timeout expired for {file_path}. Moving to next file.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Replace these values accordingly
    FOLDER_PATH = "./msgsrc"
    REMOTE_IP = "172.16.0.12"
    REMOTE_PORT = 514

    send_files_with_nc(FOLDER_PATH, REMOTE_IP, REMOTE_PORT)
