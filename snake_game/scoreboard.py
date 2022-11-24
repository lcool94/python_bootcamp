from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align="center", font="arial")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", move=False, align="center", font="arial")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
