from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle(-350, 0)
score = Score()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_on = True
sleep = 2
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce *= -1
        ball.move_speed *= 0.9
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.x_bounce *= -1
        ball.move_speed *= 0.9
    # paddle1 miss
    if ball.xcor() > 380:
        ball.reset()
        score.score_two()
    # paddle2 miss
    if ball.xcor() < -380:
        ball.reset()
        score.score_one()
    ball.move()
    score.update()

screen.exitonclick()
