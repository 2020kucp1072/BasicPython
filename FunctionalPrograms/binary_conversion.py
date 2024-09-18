'''
    @Author: VEMULA DILEEP
    @Date: 17-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:34
    @Title : Python program to find day of a week of a particular date

'''


def decimal_to_binary(num):
    """
        Description :
            This function is used to binary representation of a decimal number
        Parameters :
            num: It is the deciml number
        Return :
            It returns the binary form of num
    """

    ans = ''
    while(num>0):
        rem = num%2
        ans = str(rem)+ans
        num = num//2

    zero_to_add = 32-len(ans)
    ans = '0'*zero_to_add+ans
    return ans

def main():
    num = int(input("Enter a number: "))
    ans = decimal_to_binary(num)
    print(f"Binary of {num} is {ans}")

if __name__=="__main__":
    main()