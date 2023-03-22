# https://www.codewars.com/kata/55c6126177c9441a570000cc

import re


def order_weight(strng):

    weights_of_members = sorted(re.findall(r"\d+", strng))

    def sum_of_digits(digits):
        return sum(int(digit) for digit in digits)

    return " ".join(sorted(weights_of_members, key=sum_of_digits))
