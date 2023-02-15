#https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python


def xo(s):
    #checking if o and x are in str.
    if s.lower().count("o") == s.lower().count("x") == 0:
        return True
    #counting 
    if s.lower().count("o") == s.lower().count("x"):
        return True
    return False

