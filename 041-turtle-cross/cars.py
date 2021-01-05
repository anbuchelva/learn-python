from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.move_distance = 0
        self.move_speed = 0

    def move(self):
        self.move_distance = STARTING_MOVE_DISTANCE + self.move_speed
        self.goto(self.xcor() - self.move_distance, self.ycor())

    def increase_speed(self, level):
        self.move_speed = (level - 1) * MOVE_INCREMENT
