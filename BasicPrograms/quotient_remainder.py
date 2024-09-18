def compute_quotient_remainder(dividend, divisor):
    """
    Computes the quotient and remainder of a division.
    
    Parameters:
    dividend (int): The number to be divided.
    divisor (int): The number by which to divide.
    
    Returns:
    tuple: Quotient and remainder.
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Main
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
quotient, remainder = compute_quotient_remainder(dividend, divisor)
print(f"Quotient: {quotient}, Remainder: {remainder}")
