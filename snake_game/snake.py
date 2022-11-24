from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_DEGREE = [0, 90, 180, 270]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # screen.update()
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            # time.sleep(1)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == MOVE_DEGREE[3]:
            self.head.setheading(MOVE_DEGREE[1])

    def down(self):
        if not self.head.heading() == MOVE_DEGREE[1]:
            self.head.setheading(MOVE_DEGREE[3])

    def left(self):
        if not self.head.heading() == MOVE_DEGREE[0]:
            self.head.setheading(MOVE_DEGREE[2])

    def right(self):
        if not self.head.heading() == MOVE_DEGREE[2]:
            self.head.setheading(MOVE_DEGREE[0])
