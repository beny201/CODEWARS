#https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

def in_array(a1, a2):  
    #finding all possibles words
    match = [word for word in a1 for second_words in a2 if word in second_words]
    #removing duplicated, and sort alphabetical
    return sorted(list(set(match)))

