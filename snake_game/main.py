from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

with open("file.txt", mode="w") as file:
    file.write("scs!")
    # print(file.read())

# Create and setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snack game")
screen.tracer(0)

# TODO 1: Create Snake with 3 square
# Create snake with  3 block
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# TODO 2: Process snake movement
game_is_on = True

while game_is_on:
    # screen.update()
    time.sleep(1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        print('Game Over')
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
