# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import random
import turtle as t

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()


def paint_dots(gap, row, col):
    start_x = -1 * col * gap / 2
    start_y = -1 * row * gap / 2
    for v_position in range(row):
        tim.goto(start_x, start_y + (v_position * gap))
        for h_position in range(col):
            tim.forward(gap)
            tim.dot(20, random.choice(color_list))


paint_dots(30, 20, 30)
screen.exitonclick()
