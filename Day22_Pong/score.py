from turtle import Turtle


FONT = ("Courier", 80, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score2, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.score1, align="center", font=FONT)

    def score_one(self):
        self.score1 += 1

    def score_two(self):
        self.score2 += 1

