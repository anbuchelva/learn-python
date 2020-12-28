import turtle 
import random as r

tim = turtle.Turtle()
color = ["vilot", "blue", "green", "yellow", "orange", "red"]

def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

for shape in range(3,11):
  tim.color(r.choice(color))
  draw_shape(shape)
