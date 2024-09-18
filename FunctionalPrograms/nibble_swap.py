'''
    @Author: VEMULA DILEEP
    @Date: 18-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 11:28
    @Title : Python program to convert a decimal number to binary, reverse its nibbles, and compute its new decimal value
'''

def binary(num):
    """
        Description :
            This function converts a decimal number to its 8-bit binary representation
        Parameters :
            num: It is the decimal number to be converted
        Return :
            It returns the 8-bit binary form of num as a string
    """
    
    res = ""
    rem = 0
    while(num != 0):
        rem = num % 2
        res = str(rem) + res
        num = num // 2
    
    count = 8 - len(res)
    res = count * '0' + res
    print(res)
    return res


def nibble(num):
    """
        Description :
            This function reverses the nibbles (4-bit groups) of the 8-bit binary representation
            of a decimal number and converts the result back to a decimal number
        Parameters :
            num: It is the decimal number to be processed
        Return :
            It returns the decimal value after reversing the nibbles of the binary representation
    """
    
    bin = binary(num)
    bin_list = list(bin)
    
    for i in range(0, len(bin) // 2):
        c = bin_list[i]
        bin_list[i] = bin_list[len(bin_list) // 2 + i]
        bin_list[len(bin_list) // 2 + i] = c
        
    bin = ''.join(bin_list)
    res = 0
    for i in range(0, 8):
        res = res + pow(2, i) * int(bin[i * -1 - 1])
    
    return res


def main():
    """
        Description :
            The main function reads a number from the user, processes it using the nibble function,
            and prints the result
    """
    num = int(input("Enter the number: "))
    num1 = nibble(num)
    print(num1)

if __name__ == "__main__":
    main()
