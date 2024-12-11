import time as t
import PlayerWin as p
import compWin as c
import war as w
def score_cards(playerHand, compHand):
    #Face values of the cards
    cards = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN", "EIGHT","NINE","TEN","JACK","KING","QUEEN","ACE"]
    #creates empty list for war
    war = []
    #while both hands are not empty
    while len(playerHand) != 0  and len(compHand) != 0:
        #Prints card face value
        print("Player Card:",cards[playerHand[0]-2])
        print("Computer Card:",cards[compHand[0]-2])

        # Player wins
        if playerHand[0] > compHand[0]:
            war = p.playerwin(playerHand, compHand, war)

        # Computer wins
        elif playerHand[0] < compHand[0]:
            war = c.compwin(playerHand,compHand,war)

        # WAR
        elif playerHand[0] == compHand[0]:
            w.war(playerHand, compHand, war)

        #divides up rounds
        print("--------------------------------------")

        input("Press ENTER to play your next card: ")
        print()
    return playerHand, compHand








