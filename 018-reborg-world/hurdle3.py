# https://reeborg.ca/reeborg.html
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.

def jump():
    #move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()