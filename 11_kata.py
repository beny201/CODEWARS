# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    matches = [digit for digit in seq if seq.count(digit) % 2 != 0]
    return matches[0]
