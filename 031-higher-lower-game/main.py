# steps to process
###################
# import random
# import art, game data
# generate a random choice from the game data and store it in A
# generate a random choice from the game data and store it in B - both requires a function
# print the dictionary value in a sentance form - needs a function
# compare the followers count betwen A and B
# if the user's selection is correct, loop the game - by moving the B to A and compare it with new list
# if the user's selection is incorrect, quit the game

import random
from art  import logo, vs
from game_data import data
from clear import clear
# print(logo)

def choose_data():
    data_point = random.choice(data)
    return data_point

def person_to_text(person_dict, person):
    person_name = person_dict["name"]
    person_desc = person_dict["description"]
    person_cnty = person_dict["country"]
    person_flwr = person_dict["follower_count"]
    if person == 1:
        print(f"Compare A: {person_name}, a {person_desc}, from {person_cnty}.")
    else:
        print(f"Against B: {person_name}, a {person_desc}, from {person_cnty}.")
    return person_flwr

final_score = 0
person_1_follwers = 0
person_2_follwers = 1
should_continue = True
while should_continue:
    while person_1_follwers != person_2_follwers:
        if final_score == 0:
            person_1_data = choose_data()
            person_1_follwers = person_to_text(person_1_data,1)
            # print(vs)
            person_2_data = choose_data()
            person_2_follwers = person_to_text(person_2_data,2)
            print(f"info: person 1 followers {person_1_follwers} | person 2 followers {person_2_follwers}")
        else:
            person_1_follwers = person_to_text(person_x_data,1)
            person_1_data = person_x_data
            # print(vs)
            person_2_data = choose_data()
            person_2_follwers = person_to_text(person_2_data,2)

    print(f"info: person 1 followers {person_1_follwers} | person 2 followers {person_2_follwers}")
    user_selection = input("Who has more followers? Type 'A' or 'B': ")
    
    if user_selection == "A":
        user_followers = person_1_follwers
        user_data = person_1_data
        other_followers = person_2_follwers
    elif user_selection == "B":
        user_followers = person_2_follwers
        user_data = person_2_data
        other_followers = person_1_follwers        

    if user_followers > other_followers:
        final_score += 1
        print(f"You're right! Current score: {final_score}.")
        person_x_data = user_data
        # print(person_x_data)
        # print(final_score)
        # print("-----------------------------------------------------------------------")
    else:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        should_continue = False