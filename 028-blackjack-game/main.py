from art import logo
from clear import clear
import random

deck = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

# def random_card():
#     return list(random.choice(deck))

def check_ace(sum_value,list_name):
    if sum_value > 21:
        replace_ace = False
        card = 0        
        while not replace_ace:
            if list_name[card] == 11:                    
                list_name[card] = 1
                replace_ace = True
            card += 1
            if card == len(list_name):
                replace_ace = True
    sum_value = sum(list_name)    
    return sum_value
                        
should_continue = True
while should_continue:    
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()
    if play_game == "y":
        print(logo)
        user_value = []
        for _ in range(2):
            user_value += random.choices(deck)
        # user_value = [11,11]
        user_value_sum = sum(user_value)
        user_value_sum = check_ace(user_value_sum,user_value)        
        print(f"Your cards: {user_value}, current score: {user_value_sum}")
        
        computer_value = []
        computer_value += random.choices(deck)
        computer_value_sum = sum(computer_value)        
        print(f"Computer's first cards {computer_value}")
        
        get_another_card = True
        while get_another_card:
            another_card_bool = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card_bool == "y":
                user_value.append(random.choice(deck))
                user_value_sum = sum(user_value)
                user_value_sum = check_ace(user_value_sum,user_value)
                if user_value_sum > 21:                    
                    print(f"Your cards: {user_value}, current score: {user_value_sum}")
                    print("You are busted. Computer won! 👎")
                    break
                print(f"Your cards: {user_value}, current score: {user_value_sum}")
                print(f"Computer's first cards {computer_value}")
            elif another_card_bool == "n":
                get_another_card = False
                print(f"Your final hand: {user_value}, final score: {user_value_sum}")                
                while computer_value_sum < 17:
                    computer_value.append(random.choice(deck))
                    computer_value_sum = sum(computer_value)
                    computer_value_sum = check_ace(computer_value_sum,computer_value)                
                print(f"Computer's final hand: {computer_value}, final score: {computer_value_sum}")
                if user_value_sum > 21:
                    print("You are busted. Computer won! 👎")
                elif computer_value_sum > 21:
                    print("Computer is busted, you won! 👍")
                elif user_value_sum == computer_value_sum:
                    print("Its a draw! 🙃")
                elif user_value_sum > computer_value_sum:
                    print("You won! 👍")
                else:
                    print("Computer won! 👎")    
            else:
                print("Invalid Input, try again!")

    elif play_game == "n":
        should_continue = False
    else:
        print("Invalid Input, try again!")