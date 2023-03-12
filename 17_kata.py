# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python

def longest_palindrome(s):
    if len(s) > 1:
        empty_list = []
        for i in range(len(s)-1):
            for j in range(len(s)+1):
                text = s[i:j]
                if text == text[::-1]:
                    empty_list.append(text)
        if len(empty_list) != 0:
            return max(len(x) for x in empty_list)
    elif len(s) == 1:
        return 1
    return 0 
