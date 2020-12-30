import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(10)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap):
    for angle in range(int(360/gap)):
        tim.color(random_color())
        tim.setheading(angle * gap)
        tim.circle(100)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
