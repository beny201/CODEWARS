# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python
def find_missing(y):
    # Searching pattern
    pattern = (y[-1] - y[0])/len(y)
    for index in range(len(y) - 1):
        if y[index] != y[index + 1] - pattern:
            return y[index] + pattern
