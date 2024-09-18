'''
    @Author: VEMULA DILEEP
    @Date: 17-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:21
    @Title : Python program to convert from fahrenheit

'''

def monthly_payment(P,R,Y):
    """
    Description:
        Funtion to calculate monthly payment to be done for P principal amount at R rate in Y years
    Parameters:
        p : principel amount
        r : rate of interest
        y : time period
    Returns:
        It will return the monthly payment to be done

    """
    r = R/(12*100)
    pay = (P*r)/(1-(1/(1+r)**(12*Y)))
    return pay

def main():
    p = int(input("Enter amount: "))
    r = int(input("Enter rate: "))
    y = int(input("Enter year: "))

    pay = monthly_payment(p,r,y)

    print(f"Monthly payment to be done is {pay}")

if __name__=="__main__":
    main()