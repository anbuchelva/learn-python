import random

user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gestures = [rock, paper, scissors]

computer_selection = random.randint(0,2)

if user_selection > 2 or user_selection < 0:
    print("Invalid number, try again!")
else:
    print("You have chosen:")
    print(gestures[user_selection])
    print("Computer chose:")
    print(gestures[computer_selection])

    if user_selection == 0:
        if computer_selection == 0:
            print("Draw")
        elif computer_selection == 1:
            print("You lose!")
        else:
            print("You win!")

    if user_selection == 1:
        if computer_selection == 0:
            print("You win!")
        elif computer_selection == 1:
            print("Draw!")
        else:
            print("You lose!")

    if user_selection == 2:
        if computer_selection == 0:
            print("You lose!")
        elif computer_selection == 1:
            print("You win!")
        else:
            print("Draw!")