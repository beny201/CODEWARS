# https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python


def camel_case(sentence):
    return "".join([word.capitalize() for word in sentence.split()])
