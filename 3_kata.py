#https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python
 
# damn few hours

def solve(arr):
    def myF(char):
        return arr.count(char)
    sorted_list = sorted(arr)
    sorted_by_count = sorted(sorted_list, key = myF,reverse=True)
    return sorted_by_count