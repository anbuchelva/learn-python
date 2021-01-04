from turtle import Screen, Turtle
from cars import Cars
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=400, width=800)
screen.tracer(0)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
