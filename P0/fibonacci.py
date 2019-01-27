print("Printing the n first terms of the fibonacci series")

# Parameter N
N = 10

# Fibonacci list. Initially it containss the first two terms
fibo = [1, 1]

for i in range(2, N):
    # Calculate the actual term: the sum of the two previous
    # Insert the new term in the list
    fibo.append(fibo[i-1] + fibo[i-2])

# Print the list
print("The first {} term of the fibonacci serie are:".format(N))
print("{}".format(fibo))
