def fibonacci(n):
    """
    Calculate a list with the n first terms of the fibonacci series
    :param n: Number of total fibonacci term in the list
    :return: the list with the fibonacci series
    """
    # Initial fibonacci list
    fibo = [1, 1]

    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo


# Main program

nterms = int(input("Introduce the number of terms to sum (n): "))

# Get the fibonacci series to sum
fibo_serie = fibonacci(nterms)

total_sum = 0
for term in fibo_serie:
    total_sum += term

print("Fibonacci series: {}".format(fibo_serie))
print("The sum of the {} terms is: {}".format(nterms, total_sum))
