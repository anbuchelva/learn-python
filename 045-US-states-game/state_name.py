from turtle import Turtle


class State_Name(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def update_state_name(self, name, x, y):
        self.goto(x=x, y=y)
        self.write(name, align="left", font=("center", 10, "normal"))




