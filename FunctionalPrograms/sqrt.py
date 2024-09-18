'''
    @Author: VEMULA DILEEP
    @Date: 17-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:25
    @Title : Python program to find the sqrt of a number using newton methd

'''


class Util:
    @staticmethod
    def sqrt(c):
        """ 
    
        Description :
            This function is used to find the sqrt
        Parameters :
            c : number whose sqrt will be found

        Return :
            It returns the sqrt of the given number

        """

        if c < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        if c == 0:
            return 0.0
        
        epsilon = 1e-15  
        t = c  
        
        
        while abs(t - c / t) > epsilon * t:
            t = (t + c / t) / 2.0  
        
        return t

    @staticmethod
    def main():
        c = float(input("Enter a non-negative number to compute its square root: "))
    
        result = Util.sqrt(c)
        print(f"The square root of {c} is approximately: {result}")


if __name__ == "__main__":
    Util.main()