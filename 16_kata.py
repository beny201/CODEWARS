# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):

    list_variables = []
    for nr in str(n):
        list_variables.append(int(nr) ** p)
        p += 1
    if sum(list_variables) % n == 0:
        return sum(list_variables) // n
    return - 1
