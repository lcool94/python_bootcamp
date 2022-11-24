from turtle import Turtle, Screen
import random

screen = Screen()
colours = ["red", "yellow", "pink", "purple", "black", "blue"]

screen.setup(500, 400)
goal_x = 225
list_turtle = []


def create_turtles():
    start_y = -120
    for number in range(6):
        list_turtle.append(Turtle())
        list_turtle[number].shape("turtle")
        list_turtle[number].color(colours[number])
        list_turtle[number].penup()
        list_turtle[number].goto(-225, start_y)
        start_y += 50


create_turtles()
your_bet = screen.textinput("Your bet", "Who's win? ")
print(your_bet)
is_on = True
while is_on:
    for turtle in list_turtle:
        if turtle.xcor() > goal_x:
            if turtle.pencolor() == your_bet:
                print(f"you won. The {your_bet} turtle is winner.")
            else:
                print(f"you lost. The {turtle.pencolor()} turtle is winner.")

            is_on = False
        range_distance = random.randint(0, 10)
        turtle.forward(range_distance)

screen.exitonclick()
