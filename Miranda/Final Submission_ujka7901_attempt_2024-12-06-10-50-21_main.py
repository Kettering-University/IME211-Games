# import of all pages of code
from display import play_again
from inputs import input_menu
from winning_value import winning_values
from calc import calculate_winnings
from instructions import print_instructions

#defining main page
def main():
    bankroll = 1000
    print_instructions()
    game_over = False

#while loop to keep game going or end game based on user option
    while bankroll > 0 and game_over == False:
        bankroll, bets = input_menu(bankroll)
        winning_number, winning_color, winning_third = winning_values(bets)
        bankroll = calculate_winnings(bankroll, bets, winning_number, winning_color, winning_third)
        game_over = play_again(bankroll)

    print("Thanks for playing!")

if __name__ == '__main__':
    main()