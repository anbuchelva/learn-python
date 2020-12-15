from art import logo
import random

print(logo)
print("Welcome to Guess a number game!")

game_choice = input("choose a level of game 'hard' or 'easy': ")
if game_choice.lower() == "hard":
    options_to_try = 5
elif game_choice.lower() == "easy":
    options_to_try = 10
else:
    print("incorrect option selected")
    options_to_try = 0

number = random.randint(1,100)

def check_number(user_guess, number):
    if user_guess > number:
        return 1        
    elif user_guess < number:
        return -1
    else:
        return 0
        
while options_to_try != 0:
    user_guess = int(input(f"Guess a number between 1 and 100 | no of tries remaining = {options_to_try}): "))
    options_to_try -= 1
    check_result = check_number(user_guess, number)
    if check_result < 0:
        print(f"{user_guess} is too low. Try again!")
    elif check_result > 0:
        print(f"{user_guess} is too high. Try again!")
    else:
        print(f"{user_guess} is the right number!")
        options_to_try = 0