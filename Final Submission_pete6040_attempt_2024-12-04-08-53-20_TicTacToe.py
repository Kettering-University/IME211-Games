from random import choice
import sys

#Tic Tac Toe Game Design
print("Welcome to Tic Tac Toe")

#This variable (board) defines the numbers on the board
board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

turn = 1

def print_board():
    # This function defines the board
    print(" | ".join(board[0:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:9]))

def get_input():
    # This function gathers and checks the input of the user
    choice = int(input("Pick a spot on the board 0-8: "))

    # Checks for invalid numbers and if the board position is already taken
    while choice not in range(0,9) or board[choice] == "X" or board[choice] == "O":
        print("Invalid input")
        choice = int(input("Pick a spot on the board 0-8: "))
    return choice

def check_winner():
    #This function checks if there is a winner as the game progresses
    winners = [[board[0], board[1], board[2]], [board[3], board[4], board[5]], [board[6], board[7], board[8]],
               [board[0], board[3], board[6]], [board[1], board[4], board[7]], [board[2], board[5], board[8]],
               [board[0], board[4], board[8]], [board[2], board[4], board[6]]]
    for winner in winners:
        if winner == ["X", "X", "X"] or winner == ["O", "O", "O"]:
            print("Winner, Great job!")
            sys.exit()


def place_marker():
    #Place marker selection ("X" and "O")
    if turn % 2 == 0:
        board[choice] = "X"
    else:
        board[choice] = "O"


print_board()

# Main loop: 1 for each turn
while turn<=9:
    choice = get_input()
    place_marker()
    print_board()
    turn += 1
    check_winner()
print("Draw!")










