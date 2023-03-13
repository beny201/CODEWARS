# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python

def longest_palindrome(s):
    string_length = len(s)
    if string_length > 1:
        list_of_matches = []
        for i in range(string_length-1):
            for j in range(string_length+1):
                text = s[i:j]
                if text == text[::-1]:
                    list_of_matches.append(text)
        if len(list_of_matches) != 0:
            return max(len(x) for x in list_of_matches)
    elif len(s) == 1:
        return 1
    return 0
