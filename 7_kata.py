# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python


def multiplication_table(size):
    # Empty list for main
    list1 = []
    for x in range(size):
        # Creating sublists
        list1.append([])
        for numbers in range(1, size+1):
            list1[x].append(numbers*(x+1))
    return list1
