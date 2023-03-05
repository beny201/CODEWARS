# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python


def is_pangram(sentence):

    base_list = list(map(chr, range(97, 123)))

    for base_char in base_list:
        if base_char not in sentence.lower():
            return False
    return True
