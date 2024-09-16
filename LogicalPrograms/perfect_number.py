def is_perfect_number(num):
    """
    Checks if the given number is a perfect number.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect number, otherwise False.
    """
    if num < 2:
        return False
    # divisors = [i for i in range(1, num) if num % i == 0]
    
    divisors =[]
    for i in range(1,num):
        if num%i==0:
            divisors.append(i)
    
    return sum(divisors) == num

# Main
num = int(input("Enter a number to check if it's a perfect number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
