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
        with open("data.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())
        self.score_text = "Score: " + str(self.score) + " | High Score:" + str(self.high_score)

    def display(self):
        self.clear()
        self.write(self.score_text, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.score_text = "Score: " + str(self.score) + " | High Score:" + str(self.high_score)

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.pencolor("red")
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
