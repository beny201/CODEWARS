# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/train/python


def hamming(a, b):
    count = 0
    for char_a, char_b in zip(a, b):
        if char_a != char_b:
            count += 1
    return count
