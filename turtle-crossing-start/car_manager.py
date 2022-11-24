import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand = random.randint(1, 6)
        if rand == 1:
            car = Turtle("square")
            car.shapesize(1, 2, 3)
            car.penup()
            car.goto(300, random.randint(-265, 265))
            car.setheading(180)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def level_up(self):
        self.speed += STARTING_MOVE_DISTANCE
