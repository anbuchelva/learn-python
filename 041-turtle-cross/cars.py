from turtle import Turtle, Screen
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(self.random_color())
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.penup()
        self.goto(400, random.randint(-160, 160))

    def random_color(self):
        colors = ["red", "orange", "blue", "purple", "green", "white"]
        color = (random.choice(colors))
        return color

    def move(self):
        # print(self.color)
        self.goto(self.xcor()-10, self.ycor())
