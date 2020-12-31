import turtle as turtle_module

tim = turtle_module.Turtle()
screen = turtle_module.Screen()
tim.shape("turtle")


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.right(-10)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clear():
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
