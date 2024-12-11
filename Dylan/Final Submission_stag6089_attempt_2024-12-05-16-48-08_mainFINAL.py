import random
import dealingFINAL as deal
import scoreCards as sc

import DisplayFINAL as f

# suit = [1, 2, 3, 4]
#DECK SHUFFLING
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
random.shuffle(deck)
#starts the game
start = input("Do You Want To Play War? (Y/N): ").upper()
if start == 'Y':
    # FUNCTIONS
    playerHand, compHand = deal.dealing(deck)
    playerHand, compHand = sc.score_cards(playerHand, compHand)
    f.winner(playerHand, compHand)
else:
    while start != 'Y':
        print('Boring')
        start = input("ARE YOU SURE? (Y/N): ").upper()



