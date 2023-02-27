# https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python

def number_of_pairs(input):
    # Counting colors
    dic = {}
    for x in input:
        dic[x] = input.count(x)
    # Searching over dictionary if we have at least 2 same colors
    return sum([int(dic[y] / 2) for y in dic if dic[y] > 1])
