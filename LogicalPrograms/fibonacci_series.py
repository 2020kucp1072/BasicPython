def fibonacci_series(n):
    """
    Generates a Fibonacci series up to n terms.
    
    Parameters:
    n (int): The number of terms in the Fibonacci series.
    
    Returns:
    list: A list containing the Fibonacci series.
    """
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Main
n = int(input("Enter the number of terms for Fibonacci series: "))
print(f"Fibonacci series: {fibonacci_series(n)}")

