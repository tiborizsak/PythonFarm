import re

disk = 'sdc'

# Define the file path
file_path = '/home/tizsak/OI_data/bundles/CR-59132/info/self/core/iostat.out.txt'

# Open and read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Initialize a variable for the timestamp
timestamp = None

# Create a regex pattern for the timestamp
pattern = re.compile(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2} (AM|PM)")

# Iterate through the lines
for line in lines:
    # If the line matches the timestamp format
    if pattern.match(line.strip()):
        timestamp = line.strip()
    elif line.startswith(disk):
        print(timestamp)
        print(line.strip())