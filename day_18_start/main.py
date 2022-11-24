import turtle as t
import random

james = t.Turtle()
# james.shape("circle")
t.colormode(255)
# james.pensize(5)
james.speed(0)

colours = ["white", "cornflower blue", "coral", "indigo", "magenta", "gold", "lime", "cyan", "old lace",
           "medium slate blue", "rosy brown", "medium purple"]


# # write square
# for _ in range(4):
#     james.forward(100)
#     james.right(90)


# #write dash line
# for _ in range(10):
#     james.forward(10)
#     james.penup()
#     james.forward(10)
#     james.pendown()


# write shape
# d = 50
# for number in range(3, 20):
#     degree = 360 / number
#     for _ in range(number):
#         james.right(degree)
#         james.forward(d)

def turn_left(distance):
    james.left(90)
    james.forward(distance)


def turn_right(distance):
    james.right(90)
    james.forward(distance)


def straight(distance):
    james.forward(distance)


def back(distance):
    james.backward(distance)


def direction(distance):
    number = random.randint(0, 3)
    if number == 0:
        straight(distance)
    elif number == 1:
        back(distance)
    elif number == 2:
        turn_left(distance)
    else:
        turn_right(distance)


# # random move
# while 3 > 2:
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     james.pencolor(tup)
#     direction(10)


# draw circle
for number in range(0, 361, 5):
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    james.pencolor(tup)
    james.circle(100)
    james.setheading(number)
    james.circle(100)

screen = t.Screen()
screen.exitonclick()
