from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
  def __init__(self):
    self.cars = []
    self.speed = STARTING_MOVE_DISTANCE

  def new_car(self):
    chance = random.randint(0, 10)
    if chance == 0:
      new_car = Turtle()
      new_car.penup()
      new_car.color(random.choice(COLORS))
      new_car.shape("square")
      new_car.shapesize(stretch_wid = 1, stretch_len = 2)
      y_pos = random.randint(-200, 200)
      new_car.goto(-300, y_pos)
      self.cars.append(new_car)
  
  def move_cars(self):
    for car in self.cars:
      car.forward(self.speed)

  def speedup(self):
    self.speed += MOVE_INCREMENT