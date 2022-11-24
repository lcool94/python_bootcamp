from turtle import Turtle

DISTANCE_MOVE = 20


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.paddle = None
        self.x = x_position
        self.y = y_position
        self.paddles = Turtle("square")
        self.create_paddle()

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.goto(self.x, self.y)
        paddle.color("White")
        paddle.penup()
        paddle.shapesize(5, 1, 0)
        self.paddle = paddle

    def up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + DISTANCE_MOVE)

    def down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - DISTANCE_MOVE)
