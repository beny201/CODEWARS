def card_game(n):
    is_even = lambda n: n % 2 == 0
    players = [0, 0]
    names = ['Alice', 'Bob']
    turn = 0
    print(n, 'cards remaining.')
    while(n > 0):
        if is_even(n) and (not is_even(n // 2) or n <= 4):
            n //= 2
            players[turn] += n
            print(f"{names[turn]} halved the stack.")
        else:
            n -= 1
            players[turn] += 1
            print(f"{names[turn]} drew one card.")
        print(n, 'cards remaining.')
        
        turn = (turn + 1) % 2
    print('Game Over', *[f"{z[0]} has {z[1]} cards" for z in zip(names, players)], sep=', ', end='.\n')
    return players[0]


print(1 % 2) 
print(0 % 2) 
print(3 % 2) 
print(4 % 2) 
print(25 % 2) 
