from turtle import Turtle
SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.move_speed = 0.1
        self.y_bounce = 1
        self.x_bounce = 1

    def move(self):
        new_x = self.xcor() + SPEED*self.x_bounce
        new_y = self.ycor() + SPEED*self.y_bounce
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce *= -1

