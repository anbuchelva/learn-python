import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed(10)
tim.shape("arrow")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def move_a_step():
    direction = random.choice(directions)
    tim.setheading(direction)
    tim.color(random.choice(random_color()))
    tim.forward(20)


for _ in range(400):
    move_a_step()

screen = t.Screen()
screen.exitonclick()




