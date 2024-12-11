#defining input page
def input_menu(bankroll):

#defining the numbers, colors, thirds, and user bets
    kind = 0
    bets = []
    option = (1, 2, 3, 4, 5)
    num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31,
        32, 33, 34, 35, 36)
    colors = ("red", "black", "green")
    section = ("first", "second", "third")

#while loop for the user menu options
    while kind < 4:

        print("Game options:")
        print("")
        print("     1) Bet on a number")
        print("     2) Bet on a color")
        print("     3) Bet on a third")
        print("     4) EXIT PROGRAM")
        print("     5) Start game")
        print("")
        print("   Your bankroll is"," $",bankroll, sep="")

#user input of menu options
        kind = int(input("Enter the option you would like to do (1-3 or 4 to EXIT PROGRAM): "))

#while loop if user picks an option out of range
        while kind not in option:
            print("Invalid game option... must be 1-4!")
            kind = int(input("Enter the option you would like to do: "))

#if statements for all the menu options and user inputs for them
        if kind == 1:
            bet_type = int(input("Pick a number: "))
            while bet_type not in num:
                print("This number is not on the game board please choose one between 0-36")
                bet_type = int(input("Pick a number: "))
        elif kind == 2:
            bet_type = input("Pick a color: ").lower().strip()
            while bet_type not in colors:
                print("This color is not on the game board please choose between red, black, and green")
                bet_type = input("Pick a color: ").lower().strip()
        elif kind == 3:
            bet_type = input("Pick a third: ").lower().strip()
            while bet_type not in section:
                print("This third is not on the game board please choose between first, second, and third")
                bet_type = input("Pick a third: ").lower().strip()

# if statement for when the user inputs the exit option
        elif kind == 4:
            print("EXITING THE PROGRAM...")
            print("Thanks for playing!")

            exit()

        elif kind == 5:
            break

#input for user bet amount with restrictions for negative number and too large of bets
        bet_amount = int(input("Place a bet amount: "))
        while bet_amount <= 0:
            print("Invalid bet amount! Please enter a positive number.")
            bet_amount = int(input("Place a bet amount: "))
        if bet_amount <= bankroll:
            bankroll = bankroll - bet_amount
        else:
            print("Not enough money in bankroll, lower bet")
            continue

#added user bets to the bets list defined above
        bets.append([bet_type, bet_amount])

    return bankroll, bets
