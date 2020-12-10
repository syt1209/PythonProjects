from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(10)
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        self.score_text = "Score: " + str(self.score)

    def display(self):
        self.write(self.score_text, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.score_text = "Score: " + str(self.score)

    def game_over(self):
        self.pencolor("red")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
