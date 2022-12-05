# pt 1
outcomes = {
    'AX': 4, 'AY': 8, 'AZ': 3,
    'BX': 1, 'BY': 5, 'BZ': 9,
    'CX': 7, 'CY': 2, 'CZ': 6
}

with open('inputs/in2.txt', 'r') as file:
    games = [i for i in file.read().strip().replace(' ', '').splitlines()]

outcome1 = 0
for game in games:
    for i in range(0, len(game), 2):
        outcome1 += outcomes[game[i:i+2]]

print(outcome1)
# answer: 12740


# pt 2
def strategizer(game):
    choice = ''
    opp = game[0]
    verdict = game[1]
    if verdict == 'X': # loss
        if opp == 'A':
            choice = 'Z'
        elif opp == 'B':
            choice = 'X'
        elif opp == 'C':
            choice = 'Y'
    elif verdict == 'Y': # draw
        if opp == 'A':
            choice = 'X'
        elif opp == 'B':
            choice = 'Y'
        elif opp == 'C':
            choice = 'Z'
    elif verdict == 'Z': # win
        if opp == 'A':
            choice = 'Y'
        elif opp == 'B':
            choice = 'Z'
        elif opp == 'C':
            choice = 'X'
    return opp + choice
        

outcome2 = 0
for game in games:
    for i in range(0, len(game), 2):
        outcome2 += outcomes[strategizer(game[i:])]

print(outcome2)
# answer: 11980