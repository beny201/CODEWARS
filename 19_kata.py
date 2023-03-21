# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):

    outcome = 0
    qty_of_rolls = {}

    for roll in dice:
        qty_of_rolls[roll] = dice.count(roll)

    for dice_result, result_occurrence in qty_of_rolls.items():
        if result_occurrence >= 3:
            outcome += 1000 if dice_result == 1 else dice_result*100
            result_occurrence -= 3
        if dice_result == 1:
            outcome += result_occurrence * 100
        if dice_result == 5:
            outcome += result_occurrence * 50

    return outcome


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
