import time
from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
player = Player()

car_list = []
loop_count = 0

screen.listen()
screen.onkey(player.move, "Up")

is_game_on = True
while is_game_on:
    loop_count += 1
    if loop_count % 6 == 0:
        new_car = Cars()
        new_car.increase_speed(scoreboard.score)
        car_list.append(new_car)

    for car in car_list:
        car.move()
        if car.distance(player) < 25:
            scoreboard.game_over()
            is_game_on = False

    time.sleep(0.1)
    screen.update()

    if player.level_up():
        new_car = []
        screen.update()
        scoreboard.update_score()
        player.level_up()

screen.exitonclick()
