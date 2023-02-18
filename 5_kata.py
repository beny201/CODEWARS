#https://www.codewars.com/kata/58f6000bc0ec6451960000fd/train/python

def sel_reverse(arr,l):
    if l>0 and len(arr) > l:
        qty = len(arr)
        new_list = [(arr[i:i+l])[::-1] for i in range(0,qty,l)]
        flat_list = [x for sublist in new_list for x in sublist ]
        return flat_list
    elif l>0 and len(arr) < l:
        return arr[::-1]
    else:
        return arr
    

