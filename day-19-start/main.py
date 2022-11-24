from turtle import Turtle, Screen

james = Turtle()

screen = Screen()


def move_foward():
    james.forward(10)


def move_back():
    james.back(10)


def move_left():
    james.setheading(james.heading() + 10)


def move_right():
    james.setheading(james.heading() - 10)


def clear():
    james.clear()
    james.penup()
    james.home()
    james.pendown()


screen.listen()

screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
