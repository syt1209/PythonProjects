from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

  def __init__(self, car_manager):
    super().__init__()
    self.penup()
    self.color("black")
    self.shape("turtle")
    self.setheading(90)
    self.new_level()
    self.level = 1
    self.car_manager = car_manager

  def move_up(self):
    self.forward(MOVE_DISTANCE)
    if(self.ycor() >= FINISH_LINE_Y):
      self.new_level()
      self.level += 1
      self.car_manager.speedup()
  
  def new_level(self):
    self.goto(STARTING_POSITION)

