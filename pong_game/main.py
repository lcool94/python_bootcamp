from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Games")
screen.tracer(0)

# Create Paddle
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

# Create Ball
ball = Ball()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")
game_is_on = True
print(r_paddle.paddle.xcor())
print(r_paddle.paddle.ycor())
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with top and bot
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle.paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle.paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380 or ball.xcor() < -380:
        game_is_on = False


screen.exitonclick()
