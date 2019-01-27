def sumn(n):
    """
      Function for adding the numbers from 1 to n
      It returns the sum
    """
    # Variable for storing the partial sum
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i

    # Return the result
    return total_sum


# Define the numbers to sum
N = 100

print("Adding the numbers from 1 to n")
print("The total sum is: {}".format(sumn(N)))
