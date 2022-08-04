import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

# main game loop
while True:
    print('%s Wins, %s Losses, %d Ties' % (wins, losses, ties))

    while True:
        print('Enter r(ock), p(aper), s(cissors), q(uit)')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('you can only choose one')

    # display what the player chose
    if playerMove == 'r':
        print('Rock Vs')
    elif playerMove == 'p':
        print('Paper Vs')
    elif playerMove == 's':
        print('Scissors Vs')

    # display what the computer chose
    randomMove = random.randint(1, 3)
    if randomMove == 1:
        computerMove = 'r'
        print('Rock')
    elif randomMove == 2:
        computerMove = 'p'
        print('Paper')
    elif randomMove == 3:
        computerMove = 's'
        print('Scissors')

    if playerMove == computerMove:
        print('its a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('you win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('you lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose')
        losses = losses + 1

