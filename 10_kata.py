# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic(value):

    digits = str(value)
    number_of_digits = len(str(value))
    sum_of_number = sum(int(digit) ** number_of_digits for digit in digits)
    return sum_of_number == value
