def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    
    Parameters:
    year (int): The year to check.
    
    Returns:
    bool: True if it's a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Main
year = int(input("Enter a 4-digit year: "))
if len(str(year)) == 4:
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Please enter a valid 4-digit year.")
