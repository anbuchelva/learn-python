import turtle as turtle_module
import random

screen = turtle_module.Screen()
screen.setup(width=1000, height=400)
is_race_on = False

colors = ["purple", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

f = turtle_module.Turtle()
f.hideturtle()
f.speed(0)
f.pu()
f.goto(480, -500)
f.pd()
f.goto(480, 500)

y = 150
for color in colors:
    new_turtle = turtle_module.Turtle("turtle")
    new_turtle.speed(10)
    new_turtle.penup()
    new_turtle.goto(x=-460, y=y)
    y = int(y - 50)
    new_turtle.color(color)
    all_turtles.append(new_turtle)


user_input = screen.textinput("Make your bet", "Which turtle will will the race? "
                                               "purple / indigo / blue / green / yellow / orange / red").lower()

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 460:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_input:
                print(f"You have won!, The {winning_color} is the winning turtle.")
            else:
                print(f"You have lost!, The {winning_color} is the winning turtle.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
