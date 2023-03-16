# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):

    counting = 0
    dictionary = {}

    for rol in dice:
        dictionary[rol] = dice.count(rol)

    for digit in dictionary:
        if dictionary[digit] >= 3:
            counting += 1000 if digit == 1 else digit*100
            dictionary[digit] -= 3
        counting += 100 * \
            dictionary[digit] if digit == 1 else 50 * \
            dictionary[digit] if digit == 5 else 0

    return counting


""" 
This was first attemp which work but awful solution :)
    counting = 0
    dictionary = {}

    for rol in dice:
        dictionary[rol] = dice.count(rol)


    for digit in dictionary:
        if dictionary[digit] >= 3:
            if digit != 1:
                counting += digit*100
                dictionary[digit] -= 3
                if digit == 1:
                    counting += dictionary[digit]*100
                elif digit == 5:
                    counting += dictionary[digit]*50
            else:
                counting += 1000
                dictionary[digit] -= 3
                if digit == 1:
                    counting += dictionary[digit]*100
        elif digit == 1:
            counting += dictionary[digit]*100
        elif digit == 5:
            counting += dictionary[digit]*50

    return counting
"""
