# https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python


def kebabize(st):
    new_word = ""
    for char in st:
        if char.isupper():
            new_word += "-" + char
        elif char.isalpha():
            new_word += char
    if len(new_word) > 1 and new_word[0] == "-":
        return new_word[1:].lower()
    return new_word.lower()
