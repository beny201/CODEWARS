# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python
def find_missing(y):
    empty_list = []
    # Searching pattern
    pattern = (y[-1]-y[0])/len(y)
    empty_list.append(pattern)
    for index in range(len(y)-1):
        if y[index] != y[index+1]-empty_list[0]:
            return (y[index]+empty_list[0])
