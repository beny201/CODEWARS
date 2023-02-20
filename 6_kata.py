#https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd/train/python

#Tried to make by functions but took to long time and did not pass on site. I hope that they are okey :) 
# Used dedicated method for it. 

"""def mygcd(x, y):
    min_value = min(x,y)
    return max(value for value in range(min_value,0,-1) if x % value == 0 and y % value ==0)

def mygcd(x, y):
    i = min(x,y)
    while i>0:
        if x % i == 0 and y % i ==0:
            return i
        i -= 1
"""

def mygcd(x, y):
    import math
    return math.gcd(x, y)
