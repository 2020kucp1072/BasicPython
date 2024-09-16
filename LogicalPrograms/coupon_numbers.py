import random

def distinct_coupon_numbers(n):
    """
    Simulates generating distinct coupon numbers and calculates how many random numbers are needed.
    
    Parameters:
    n (int): The number of distinct coupon numbers to generate.
    
    Returns:
    int: The number of random numbers generated to get n distinct coupon numbers.
    """
    distinct_numbers = set()
    random_number_count = 0
    while len(distinct_numbers) < n:
        random_num = random.randint(1, n)
        random_number_count += 1
        distinct_numbers.add(random_num)
    return random_number_count

# Main
n = int(input("Enter the number of distinct coupon numbers: "))
print(f"Total random numbers needed: {distinct_coupon_numbers(n)}")


