from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("sssnnnnaaaaakkkkke")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
scoreboard.update_score()
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.add_tail()

    # Detect collision with walls.
    if snake.head.xcor() >= 310 or snake.head.xcor() <= -310 or snake.head.ycor() >= 310 or snake.head.ycor() <= -310:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()
screen.exitonclick()
