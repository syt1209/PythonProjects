import turtle

tim = turtle.Turtle()
tim.setheading(0)
tim_screen = turtle.Screen()
step = 10


def forwards():
    tim.forward(step)


def backwards():
    tim.backward(step)


def counter_clockwise():
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)
    tim.forward(step)


def clock_wise():
    current_heading = tim.heading()
    tim.setheading(current_heading - 10)
    tim.forward(step)


def clear_drawing():
    tim_screen.clearscreen()
    tim.penup()
    tim.home()
    tim.pendown()


tim_screen.listen()
tim_screen.onkey(key="w", fun=forwards)
tim_screen.onkey(key="s", fun=backwards)
tim_screen.onkey(key="a", fun=counter_clockwise)
tim_screen.onkey(key="d", fun=clock_wise)
tim_screen.onkey(key="c", fun=clear_drawing)


tim_screen.exitonclick()