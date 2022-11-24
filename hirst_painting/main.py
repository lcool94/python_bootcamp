import random

import colorgram
import turtle as t

james = t.Turtle()
t.colormode(255)
james.pensize(20)
james.hideturtle()
james.speed(0)

# set first position
james.penup()
james.goto(-225, -225)
james.pendown()

# james.pensize(20)


# colors = colorgram.extract("dot.jpg", 100)
# list_color_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb_color = (r, g, b)
#     list_color_rgb.append(new_rgb_color)
# print(list_color_rgb)

colours = [(250, 249, 249), (219, 210, 93), (231, 135, 158), (125, 81, 121), (237, 57, 137), (1, 105, 141),
           (238, 80, 59), (48, 189, 175), (124, 208, 243), (244, 252, 249), (252, 244, 249), (242, 248, 252),
           (126, 199, 229), (94, 191, 180), (235, 163, 187), (221, 131, 118), (6, 91, 114), (143, 218, 210),
           (247, 165, 156), (80, 147, 165), (191, 74, 58), (134, 202, 250)]

distance = 50


# draw dot
def draw_dot():
    color = random.choice(colours)
    james.pencolor(color)
    james.dot()


def move(m_distance):
    james.penup()
    james.forward(m_distance)
    james.pendown()


def back_head(index):
    if index % 2 == 0:
        james.setheading(0)
    else:
        james.setheading(180)


def go_up(gu_distance, index):
    james.setheading(90)
    move(gu_distance)
    back_head(index+1)
    move(gu_distance)


def draw_picture():
    for number in range(10):
        back_head(number)
        for _ in range(10):
            draw_dot()
            move(distance)
        go_up(distance,number)



draw_picture()

screen = t.Screen()
screen.exitonclick()
