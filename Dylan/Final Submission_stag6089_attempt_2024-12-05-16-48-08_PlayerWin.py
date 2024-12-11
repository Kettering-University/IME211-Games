def playerwin(playerHand,compHand,war):
    #removes played card from computer and add it to the back of playerHand
    playerHand.append(compHand.pop(0))
    playerHand.append(playerHand.pop(0))
    #adds cards from war to the back of the winners deck
    playerHand += war
    #resets war so cards are not readied if there is more than one war in a game
    war = []
    print("\nYOU WON THIS HAND")
    # prints number of cards left
    print('YOU HAVE',len(playerHand),'CARDS LEFT')
    print('THE COMPUTER HAS', len(compHand), 'CARDS LEFT')
    return war