import os
import subprocess
import argparse

MSG_SRC_DIR = "msgsrc"
def send_files_with_nc(directory_path, remote_host, remote_port):
    # List all files in the specified directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Iterate through each file and send it using nc (netcat)
    for file in files:
        file_path = os.path.join(directory_path, file)
        print(f"Sending {file_path} to {remote_host}:{remote_port}...")

        try:
            # The '-q 10' option makes nc quit 10 seconds after EOF
            result = subprocess.call(['nc', '-q', '5', remote_host, str(remote_port)], stdin=open(file_path, 'rb'))

            if result != 0:
                print(f"Error sending {file_path}.")
            else:
                print(f"Sent {file_path} successfully.")
        except subprocess.TimeoutExpired:
            print(f"Timeout expired for {file_path}. Moving to next file.")
        except Exception as e:
            print(f"Error: {e}")


def extract_protocol_streams(protocol, input_file, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get the list of unique stream indices for the protocol
    cmd_get_indices = [
        'tshark', '-r', input_file, '-Y', protocol, '-T', 'fields', '-e', f"{protocol}.stream"
    ]
    result = subprocess.run(cmd_get_indices, capture_output=True, text=True)
    stream_indices = set(result.stdout.splitlines())

    # Extract each stream into a separate file within the output directory
    extracted_files = []
    for index in stream_indices:
        output_file = os.path.join(output_directory, f"{protocol}_stream_{index}.pcap")
        filter_string = f"{protocol} && {protocol}.stream=={index}"

        cmd_extract_stream = [
            'tshark', '-r', input_file, '-Y', filter_string, '-w', output_file
        ]
        subprocess.run(cmd_extract_stream)
        extracted_files.append(output_file)

    print(f"Extracted {len(stream_indices)} {protocol.upper()} streams.")
    for f in extracted_files:
        print(f"Saved stream to {f}")

    return extracted_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process pcap and/or send files using nc.')
    parser.add_argument('-tsharkproc', action='store_true', help='Process pcap file using tshark')
    parser.add_argument('-ncsend', action='store_true', help='Send files using nc')
    parser.add_argument('--pcap', type=str, help='Path to pcap file')
    parser.add_argument('--destip', type=str, default='example.com', help='Destination IP for nc')
    parser.add_argument('--destport', type=int, default=12345, help='Destination port for nc')
    parser.add_argument('--protocol', choices=['udp', 'tcp', 'both'], default='both',
                        help='Protocol to extract streams for (udp/tcp/both)')
    args = parser.parse_args()

    if args.tsharkproc:
        # Check if --pcap is provided when -tsharkproc is used
        if not args.pcap:
            print("Error: You must provide a path to the pcap file using --pcap when using -tsharkproc.")
            exit(1)

        extracted_files = []
        if args.protocol in ['udp', 'both']:
            extracted_files.extend(extract_protocol_streams('udp', args.pcap, MSG_SRC_DIR))
        if args.protocol in ['tcp', 'both']:
            extracted_files.extend(extract_protocol_streams('tcp', args.pcap, MSG_SRC_DIR))

        if args.ncsend:
            for file in extracted_files:
                send_files_with_nc(file, args.destip, args.destport)
    elif args.ncsend:
        send_files_with_nc(MSG_SRC_DIR, args.destip, args.destport)
