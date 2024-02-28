import os

# The name of the file to manipulate
filename = "example_file.txt"

# Writing to a file (creating a new one or overwriting an existing one)
with open(filename, "w") as file:
    file.write("Hello, world!\n")
    file.write("This is an example file.\n")

# Reading from the file and printing its contents
with open(filename, "r") as file:
    lines = file.readlines()
    print("Current contents of the file:")
    for line in lines:
        print(line, end="")

# Appending text to the file
with open(filename, "a") as file:
    file.write("Here's a new line added to the file.\n")

# Reading from the file again to show the appended text
with open(filename, "r") as file:
    print("\nContents of the file after appending text:")
    print(file.read())

# Removing the file
os.remove(filename)
print(f"\nThe file '{filename}' has been removed.")

fajlname = 'valamiizgalmasfilename.txt'
belehanyomszoveg = 'Lorem Ipsum doloret aleat iacta es.\n '

with open(fajlname, "a") as file:
    file.write(belehanyomszoveg)
    file.close()

# Copy, move, delete files

import shutil

shutil.copy('mit', 'hova') # renaming is also possible this way like in linux

shutil.move('mit', 'hova')

shutil.copytree('melyikmappat', 'hova') # copy folders with subfolders

shutil.rmtree('melyikmappat') # Remove directory

os.unlink('melyikfilet') # Remove file

# Walk directory
# import os

for foldername, subfolders, filename in os.walk('/home/tizsak'):
    print(foldername)
    print(subfolders)
    print(filename)

