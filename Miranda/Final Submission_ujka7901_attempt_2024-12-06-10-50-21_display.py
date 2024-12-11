#defining play again page
def play_again(bankroll):

#printing the users bankroll
    print(f"Your bankroll is ${bankroll}")

#user input if they want to play again
    again = input("Do you want to keep playing (Y/N): ").lower().strip()

#if statement based on user input if they want to play again
    if again == "y":
        game_over = False
    elif again == "n":
        game_over = True

    return game_over