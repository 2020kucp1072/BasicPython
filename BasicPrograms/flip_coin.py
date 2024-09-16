import random

def flip(n):
 
    """
    Simulates flipping a coin n times and calculates the percentage of heads and tails.
    
    Parameters:
    n (int): Number of times to flip the coin.
    
    Returns:
    None
    """
    heads =0
    tails =0
    
    for i in range(n):
        if random.random()<0.5:
            tails+=1
        else:
            heads+=1
    heads_percentage = (heads)*100/n
    tails_percentage = (tails)*100/n

    return heads_percentage,tails_percentage  


#main

n =int(input("enter number of flips"))

if n>0:
   x,y = flip(n)
   
  
   print(f"Heads: {x}%")
   print(f"Tails: {y}%") 
   print(y)

else :
    print("enter a positive number")