import time as t
def war(playerHand,compHand,war):
    print("WAR!!!!")
    print('BURN ONE CARD!!!')
    t.sleep(1)
    print('BURN A SECOND CARD!!!')
    t.sleep(1)
    print('BURN A THIRD CARD!!!')
    t.sleep(1)
    # repeat 4 times to burn cards and move them to list war
    for i in range(4):
        #check if there are enough cards for war
        if len(playerHand) == 0 or len(compHand) == 0:
            break
        #adds the 3 burned cards from each player to the empty war list
        war.append(playerHand.pop(0))
        war.append(compHand.pop(0))
        # prints number of cards left
    print('YOU HAVE', len(playerHand), 'CARDS LEFT')
    print('THE COMPUTER HAS', len(compHand), 'CARDS LEFT')
    return None