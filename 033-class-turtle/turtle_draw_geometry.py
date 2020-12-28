from turtle import Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("purple")

for _ in range(4):
  timmy_the_turtle.forward(100)
  timmy_the_turtle.right(90)

timmy_the_turtle.circle(100)

for _ in range(3):
  timmy_the_turtle.forward(100)
  timmy_the_turtle.left(120)
timmy_the_turtle.right(90)

for _ in range(6):
  timmy_the_turtle.forward(100)
  timmy_the_turtle.right(60)
