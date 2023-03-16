# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):

    odd_numbers = []
    even_number = []
    for integer in integers:
        if integer % 2 != 0:
            odd_numbers.append(integer)
        else:
            even_number.append(integer)

    return odd_numbers[0] if len(odd_numbers) == 1 else even_number[0]
