from clear import clear
from art import logo
import random


def deal_card():
    """will generate a random card from the 'cards' list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """calculates the sum value that is stored in user / computer cards"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0 #blackjack    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)        
    return sum(cards)

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif(computer_score > user_score):
        return "You lose 😤"
    else:
        return "You win 😃"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's frist card: {computer_cards[0]}")

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_new_card = input("Do you want to draw a new card? 'y' to continue 'n' to pass: ")
            if draw_new_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
            else:
                is_game_over = True
        

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a black jack game? 'y' for yes and 'n' for no: " ) == "y":
    clear()    
    play_game()