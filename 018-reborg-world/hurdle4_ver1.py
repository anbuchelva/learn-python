# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_up():
    turn_left()
    move()
    turn_right()

def move_straight():
    move()
    turn_right()

move_up_count = 0
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        move_up_count += 1
        move_up()
        # print(move_up_count)
        if front_is_clear():
            move_straight()
            for move_down_count in range(move_up_count):
                move()
            turn_left()
            move_up_count = 0