seq = input("Introduce the DNA sequence (A,T,C,G): ")

print("Total length: {}".format(len(seq)))

# Initialize the bases counters

a = 0
t = 0
c = 0
g = 0

# Read the string characters and count the bases found
for b in seq:
    if b == 'A':
        a += 1
    elif b == 'T':
        t += 1
    elif b == 'C':
        c += 1
    elif b == 'G':
        g += 1


# Print the results
print("A: {}".format(a))
print("T: {}".format(t))
print("C: {}".format(c))
print("G: {}".format(g))
