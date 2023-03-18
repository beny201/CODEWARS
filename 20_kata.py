# https://www.codewars.com/kata/55c6126177c9441a570000cc

import re


def order_weight(strng):

    cleaned_string = re.findall(r"\d+", strng)
    cleaned_string = sorted(cleaned_string)

    def sum_of_digit(digits):
        separated = list(digits)
        return sum(int(digit) for digit in separated)

    return " ".join(sorted(cleaned_string, key=sum_of_digit))
