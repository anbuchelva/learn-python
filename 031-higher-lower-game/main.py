import random
from art  import logo, vs
from game_data import data
from clear import clear

def person_to_text(person_dict):
    """it converts the dictionary to readble text."""
    person_name = person_dict["name"]
    person_desc = person_dict["description"]
    person_cnty = person_dict["country"]
    return person_name + ", a " + person_desc + ", from " + person_cnty +"."

def check_scores(user_guess,a_followers,b_followers):
    """checks the followers between two set of dictionary"""
    if user_guess == "a":
        user_followers = a_followers
        other_followers = b_followers
    elif user_guess == "b":
        user_followers = b_followers
        # user_data = person_2_data
        other_followers = a_followers
    # print(f"U:{user_followers}, O: {other_followers}")
    if user_followers > other_followers:
        return True
    else:
        return False

should_continue = True
final_score = 0
while should_continue:
    # clear previous contents
    clear()
    # print logo every time
    print(logo)
    if final_score > 0:
        print(f"You're right! Current score: {final_score}.")
        person_a = person_b        
    # choose random dictionary from game data
    else:
        person_a = random.choice(data)

    person_b = random.choice(data)
    while person_a == person_b:
        person_b = random.choice(data)

    print(f"Compare A: {person_to_text(person_a)}")
    print(vs)
    print(f"Against B: {person_to_text(person_b)}")

    # get followers count for each
    a_followers = person_a["follower_count"]
    b_followers = person_b["follower_count"]
    print(f"A: {a_followers}, B: {b_followers}")
    user_guess = input("Who has more followers? Type 'A' or 'B' or 'Q' to quit: ").lower()
    if user_guess == "q":
        break

    # print(check_scores(user_guess,a_followers,b_followers))
    if check_scores(user_guess,a_followers,b_followers):
        final_score += 1
    else:
        print(f"\nSorry, that's wrong. Final score: {final_score}")
        should_continue = False