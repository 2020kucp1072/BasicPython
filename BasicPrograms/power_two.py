def power_of_two(N):
    """
    Prints powers of 2 less than or equal to 2^N.
    
    Parameters:
    N (int): The power value.
    
    Returns:
    None
    """
    for i in range(N+1):
        print(f"2^{i} = {2**i}")

# Main
N = int(input("Enter a value for N (0 <= N < 31): "))
if 0 <= N < 31:
    power_of_two(N)
else:
    print("N should be in the range of 0 to 30.")
