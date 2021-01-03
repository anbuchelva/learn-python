from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("P O N G")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True


def check_winning_status():
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.announce_winner()
        global is_game_on
        is_game_on = False


while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # deduct collision with wall
    if abs(ball.ycor()) >= 280:
        ball.bounce_y()

    # deduct collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # deduct if player misses the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        check_winning_status()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        check_winning_status()
        ball.reset_position()

screen.exitonclick()
