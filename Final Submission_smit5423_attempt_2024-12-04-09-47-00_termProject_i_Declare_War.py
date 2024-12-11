import random
import sys

# List needed for the Game
cards = list(range(2,15))*4
random.shuffle(cards)
playerList = cards[0:25]
computerList = cards[26:-1]
war = []

# Game introduction and asking to play
print('Lets play I Declare War!')
print('')
print('Just press Enter and and the game will do the rest!')
print('')

# Comparing the first number in the Players and Computers deck
def compare_cards(comparison_int):

    # Helps the Display
    if playerList[comparison_int] == computerList[comparison_int]:
        print('That was War!')

    elif playerList[comparison_int] > computerList[comparison_int]:
        print('You toke the last round!')

    elif playerList[comparison_int] < computerList[comparison_int]:
        print('Computer toke the last round!')
    else:
        print('')

# Comparing the first number in the Players and Computers deck pt.2
    if playerList[comparison_int] > computerList[comparison_int]:
        playerList.append(computerList.pop(comparison_int))

    # If the cards are the same value
    elif playerList[comparison_int] == computerList[comparison_int]:


        # Remove first 4 cards from player and computer and keep in temporary war list
        for i in range(0,4):
            war.append(playerList.pop(0))
            war.append(computerList.pop(0))

        compare_cards(0)

    else:
        computerList.append(playerList.pop(0))
        computerList.extend(war)
        war.clear()


# Lets the game loop and such
while not (len(playerList) == 0 or len(computerList) == 0):
    compare_cards(0)

    random.shuffle(playerList)
    random.shuffle(computerList)

# Display
    print('Your card:', playerList[0])

    print('Computers card:', computerList[0])

    input()

# Declares the winner of the game
if len(playerList) == 0:
    print('Game over, Computer Wins!')
    sys.exit()

elif len(computerList) == 0:
    print('Game over, You Won!')
    sys.exit()




