from turtle import Turtle

FORWARD_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        # print(f"x: {self.xcor()}\ny: {self.ycor()}\n")

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
