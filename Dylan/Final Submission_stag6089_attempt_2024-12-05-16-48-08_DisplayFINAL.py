def winner(playerHand,compHand):
    #displays the winner of the game
    if len(playerHand) == 0:
        print('You Lose')
        print('Computer Wins!!!')
    elif len(compHand) == 0:
        print('You Won!!!')
        print('Computer Loses')

    return None

