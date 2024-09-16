def prime_factors(N):
    """
    Computes the prime factorization of N using brute force.
    
    Parameters:
    N (int): The number to find prime factors for.
    
    Returns:
    List[int]: A list of prime factors.
    """
    i = 2
    factors = []
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N //= i
        i += 1
    if N > 1:
        factors.append(N)
    return factors

# Main
N = int(input("Enter a number to find its prime factors: "))
if N > 1:
    print(f"Prime factors of {N}: {prime_factors(N)}")
else:
    print("Enter a number greater than 1.")
