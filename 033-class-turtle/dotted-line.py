import turtle 

tim = turtle.Turtle()
tim.color("Teal")
tim.shape("turtle")
for _ in range(15):
  tim.pendown()
  tim.forward(10)
  tim.penup()
  tim.forward(10)
