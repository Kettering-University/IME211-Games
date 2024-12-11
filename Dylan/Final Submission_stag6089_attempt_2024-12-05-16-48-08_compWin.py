def compwin(playerHand,compHand,war):
    # removes played card from player and add it to the back of compHand
    compHand.append(playerHand.pop(0))
    compHand.append(compHand.pop(0))
    compHand += war
    # resets war so cards are not readied if there is more than one war in a game
    war = []
    # Add the war list to the comp list
    print("\nTHE COMPUTER WINS THIS HAND")
    #prints number of cards left
    print('YOU HAVE', len(playerHand), 'CARDS LEFT')
    print('THE COMPUTER HAS', len(compHand), 'CARDS LEFT')
    return war