def find_largest(a, b, c):
    """
    Finds the largest among three numbers.
    
    Parameters:
    a (int): First number.
    b (int): Second number.
    c (int): Third number.
    
    Returns:
    int: The largest number.
    """
    return max(a, b, c)

# Main
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print(f"The largest number is {find_largest(a, b, c)}.")
