def reverse_number(num):
    """
    Reverses the given number.
    
    Parameters:
    num (int): The number to reverse.
    
    Returns:
    int: The reversed number.
    """
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num = num // 10
    return reversed_num

# Main
num = int(input("Enter a number to reverse: "))
print(f"Reversed number: {reverse_number(num)}")
