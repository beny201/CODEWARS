#https://www.codewars.com/kata/59a8570b570190d313000037/train/python

def sum_cubes(n):
    cubed_values = [x**3 for x in range(1+n)]
    return sum(cubed_values)

