def is_prime_number(num):
    """
    Checks if the given number is a prime number.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a prime number, otherwise False.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main
num = int(input("Enter a number to check if it's a prime number: "))
if is_prime_number(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
