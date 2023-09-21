import os
import subprocess
import time

def send_files_with_nc(folder_path, remote_ip, remote_port):
    """
    Send all files from a folder to a remote destination using nc.
    :param folder_path: Path to the folder containing the files.
    :param remote_ip: IP address of the remote machine.
    :param remote_port: Port number on the remote machine.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            cmd = ["nc", remote_ip, str(remote_port), "<", file_path]
            subprocess.call(" ".join(cmd), shell=True)
            print(f"Sent {file_path} to {remote_ip}:{remote_port}")
            time.sleep(1)  # Add a delay between sending files, if needed.

if __name__ == "__main__":
    # Replace these values accordingly
    FOLDER_PATH = "/path/to/your/folder"
    REMOTE_IP = "192.168.1.100"
    REMOTE_PORT = 1234

    send_files_with_nc(FOLDER_PATH, REMOTE_IP, REMOTE_PORT)
