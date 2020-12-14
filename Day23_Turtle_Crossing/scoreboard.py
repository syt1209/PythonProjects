from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

  def __init__(self, player):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.player = player
    self.goto(-280, 250)
  
  def update(self):
    self.clear()
    self.write(f"Level: {self.player.level}", align="left", font = FONT)

  def gameover(self):
    self.goto(0, 0)
    self.write("Game Over", align="center", font=FONT)
