# Snake Water Gun Game

import random

def game_win(user, computer): # function to decide the winner
    if user == computer: # draw condition
        return None 

    # Snake vs Water
    if user == "s" and computer == "w": # user wins
        return True
    if user == "w" and computer == "s": # computer wins
        return False
    
    # Water vs Gun
    if user == "w" and computer == "g": # user wins
        return True
    if user == "g" and computer == "w": # computer wins
        return False
    
    # Gun vs Snake
    if user == "g" and computer == "s": # user wins
        return True
    if user == "s" and computer == "g": # computer wins
        return False

rand_no = random.randint(1, 3) # generates random number between 1 and 3

print("Computer's turn: Snake(s), Water (w), Gun (g)") # prompt for computer choice
if rand_no == 1: # computer chooses Snake
    computer = "s"
elif rand_no == 2: # computer chooses Water
    computer = "w"
else: # computer chooses Gun
    computer = "g"


user = input("Your turn: Snake(s), Water (w), Gun (g): ").lower() # prompt for user choice and .lower() to handle case sensitivity
if user not in ["s", "w", "g"]: # input validation for user choice
    print("Invalid input! Please choose s, w, or g.") # error message for invalid input
    exit() # exits the program if user input is invalid

result = game_win(user, computer) # Returns True if you win, False for lose, None for draw
choices = {"s": "Snake", "w": "Water", "g": "Gun"} # dictionary to map user input to full names for display
print(f"You chose: {choices[user]}")
print(f"Computer chose: {choices[computer]}")


if result is None: # draw condition
    print("Its a draw!")

elif(result): # user wins condition
    print("You win!")
else: # user loses condition
    print("You lose!")