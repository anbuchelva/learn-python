# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
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