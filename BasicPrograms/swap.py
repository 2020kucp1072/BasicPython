def swap_numbers(a, b):
    """
    Swaps two numbers.
    
    Parameters:
    a (int): First number.
    b (int): Second number.
    
    Returns:
    tuple: Swapped values of a and b.
    """
    a, b = b, a
    return a, b

# Main
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a, b = swap_numbers(a, b)
print(f"After swapping: a = {a}, b = {b}")
