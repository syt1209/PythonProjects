from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = list()

for tim_i in range(6):
    tim = Turtle(shape="turtle")
    all_turtles.append(tim)
    tim.color(colors[tim_i])
    tim.penup()
    pos_y = -125 + tim_i*50
    tim.goto(x=-230, y=pos_y)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winner is the {winning_color.upper()} turtle")
            else:
                print(f"You lost... The winning turtle is the {winning_color.upper()} turtle.")


screen.exitonclick()
