# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python


def rot13(message):
    chr_range = {
        "lower": (97, 122),
        "upper": (65, 90)
    }

    coded_sentence = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                char_range = chr_range["upper"]
            else:
                char_range = chr_range["lower"]

            unicode_char = ord(char)

            if unicode_char + 13 > char_range[1]:
                unicode_char = char_range[0] + \
                    (unicode_char + 12) - char_range[1]
                coded_char = chr(unicode_char)
                coded_sentence += coded_char
            else:
                coded_char = chr(unicode_char + 13)
                coded_sentence += coded_char
        else:
            coded_sentence += char

    return coded_sentence
