from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Monospace", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Monospace", 70, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def announce_winner(self):
        self.goto(0, 0)
        if self.l_score == 10:
            self.write("Player on the Left side is the winner", align="center", font=("Monospace", 20, "normal"))
        elif self.r_score == 10:
            self.write("Player on the Right side is the winner", align="center", font=("Monospace", 20, "normal"))
