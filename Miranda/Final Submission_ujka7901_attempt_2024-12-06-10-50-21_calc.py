#defining calc page
def calculate_winnings(bankroll, bets, winning_number, winning_color, winning_third):

#for loop to calculate user winnings based off of bet amount and what they placed it on
    for bet in bets:
        if bet[0] == winning_color:
            print(f"You won ${bet[1]:.2f} on {winning_color}.")
            bankroll = bankroll + bet[1] * 2
        elif bet[0] == winning_number:
            print(f"You won ${bet[1]*35:.2f} on {winning_number}.")
            bankroll = bankroll + bet[1] * 36
        elif bet[0] == winning_third:
            print(f"You won ${bet[1]*2:.2f} on {winning_third}.")
            bankroll = bankroll + bet[1] * 3

    return bankroll
