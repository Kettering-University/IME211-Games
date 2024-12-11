import determinechoice
import random

# Variables
attempts = 3
coins = 0
power_ups = 1

# Function that evaluates user choice and computer choice, determines a winner
def selections(user_choice, computer_choice):
    global coins
    global power_ups
    if user_choice == computer_choice:
        print("It's a draw!")     # Display that it's a draw if the user choice is the same as the computer's choice
    elif (user_choice == "Rock", computer_choice == "Scissors") or \
        (user_choice == "Paper", computer_choice == "Rock") or \
        (user_choice == "Scissors", computer_choice == "Paper"):
            print("You win! 1 Coin Earned!") # Display that you beat the computer and gained one coin.
            coins += 1
            power_ups += 1
    else:
        print("Computer wins. No coins earned.")
        adjust_attempts()
    return()

# Function that adjusts the number of attempts you have
def adjust_attempts():
    global attempts
    attempts -= 1
    print(f"{attempts} attempts remaining.") # Take away one attempt per attempt
    return None

# Function that adjusts the number of power ups you have (start with 1)
def adjust_power_ups(computer_choice, power_ups):
    print(f"Power up! Computer uses {computer_choice}!") # Function reveals what computer picked
    power_ups -= 1
    if power_ups == 0:
        print("You have no power ups :(")
    return None

# Loop that runs the game
while attempts > 0:
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"You have {coins} coins, and {power_ups} power-ups.")
    if power_ups > 0:
        use_powerup = input("A power up reveals what the computer picked! Would you like to use a power up? ")
        if use_powerup == "Y":
            adjust_power_ups(computer_choice, power_ups)   # Functions in this code are used in this loop
            user_choice = determinechoice.determine_choice()
            selections(user_choice, computer_choice)
    if attempts == 0:
            print(f"Game over! You finished with {coins} coins.")    # Display game over


