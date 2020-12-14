import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
turtle = Player(car_manager)
scoreboard = Scoreboard(turtle)
screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()

  car_manager.new_car()
  car_manager.move_cars()
  scoreboard.update()

  for car in car_manager.cars:
    if car.distance(turtle) <= 20:
      game_is_on = False
      scoreboard.gameover()

