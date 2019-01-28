from pathlib import Path

# Name of the file with the DNA sequence
DNA_FILE = "dna.txt"

# We create a file descriptor by providing the PATH
# "./" means the current folder
file = Path("./{}".format(DNA_FILE))

# Print the filename
print("File to be read: {}".format(file))

# Read the data on the file
data = file.read_text()

# Initialize the bases counters

a = 0
t = 0
c = 0
g = 0
unk = 0  # This is for the unknows characters in the string

# Read the string characters and count the bases found
for b in data:
    if b == 'A':
        a += 1
    elif b == 'T':
        t += 1
    elif b == 'C':
        c += 1
    elif b == 'G':
        g += 1
    else:
        unk += 1  # Unknow character

# Show the informacion
print("Total length: {}".format(len(data)))

# Print the results
print("A: {}".format(a))
print("T: {}".format(t))
print("C: {}".format(c))
print("G: {}".format(g))
print("Unknow characters: {}".format(unk))
