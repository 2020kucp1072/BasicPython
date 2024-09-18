def harmonic_number(N):
    """
    Computes the Nth harmonic number: 1 + 1/2 + 1/3 + ... + 1/N.
    
    Parameters:
    N (int): The value to calculate the harmonic sum.
    
    Returns:
    float: The Nth harmonic number.
    """
    harmonic_sum = 0
    for i in range(1, N+1):
        harmonic_sum += 1/i
    return harmonic_sum

# Main
N = int(input("Enter the harmonic value N (N != 0): "))
if N != 0:
    print(f"The {N}th harmonic number is {harmonic_number(N)}")
else:
    print("N cannot be 0.")
