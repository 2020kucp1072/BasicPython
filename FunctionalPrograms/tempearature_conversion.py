'''
    @Author: VEMULA DILEEP
    @Date: 17-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 11:35
    @Title : Convert temperature between Celsius and Fahrenheit.
'''

def celsius_to_fahrenheit(celsius):
    """
    Converts temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts temperature from Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

def main():
    """
    Main function to take user input and perform temperature conversion.
    """
    choice = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ").upper()

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
