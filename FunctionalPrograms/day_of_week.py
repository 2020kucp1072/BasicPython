'''
    @Author: VEMULA DILEEP
    @Date: 17-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 11:26
    @Title : To calculate the day of the week for a given date.
'''

def day_of_week(m, d, y):
    """
    Calculates the day of the week for a given date using Zeller's Congruence formula.
    
    Parameters:
    m (int): Month (1 = January, 2 = February, ..., 12 = December).
    d (int): Day of the month.
    y (int): Year.
    
    Returns:
    int: The day of the week (0 = Sunday, 1 = Monday, ..., 6 = Saturday).
    """
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    return d0

def main():
    """
    Main function to take user input and calculate the day of the week.
    """
    m = int(input("Enter month (1-12): "))
    d = int(input("Enter day: "))
    y = int(input("Enter year: "))

    if m < 1 or m > 12 or d < 1 or d > 31:
        print("Invalid date. Please enter valid values.")
    else:
        day = day_of_week(m, d, y)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(f"The day of the week is: {days[day]}")

if __name__ == "__main__":
    main()
