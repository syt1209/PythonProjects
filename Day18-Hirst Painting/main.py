
import colorgram
import random
import turtle as t

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim = t.Turtle()
ts = t.Screen()
ts.colormode(255)
ts.screensize(420, 420)
ts.bgcolor(rgb_colors[0])  # use the first color as the background
# 29 dot colors for painting
rgb_colors.pop(0)

# Move tim to starting point
tim.setheading(90)
tim.penup()
tim.forward(180)
tim.left(90)
tim.forward(180)

for row in range(10):
    tim.setheading(0)
    for column in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(40)
    tim.right(90)
    tim.forward(40)
    tim.right(90)
    tim.forward(400)

ts.exitonclick()
