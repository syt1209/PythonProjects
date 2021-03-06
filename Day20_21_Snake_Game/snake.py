from turtle import Turtle
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, snake_length=3, starting_pos=(0, 0)):
        """ Pass in snake length (default at 3 segments) and starting position (default at (0, 0)) """
        self.total_segments = snake_length
        self.pos = starting_pos
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.secondtail = self.segments[-2]

    def create_snake(self):
        for segment_id in range(self.total_segments):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.fillcolor("white")
            new_segment.pencolor("orange")
            new_segment_x = self.pos[0] - segment_id * 20
            new_segment.setpos(new_segment_x, 0)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.fillcolor("white")
        new_segment.pencolor("orange")
        new_segment_x = self.tail.xcor() + (self.tail.xcor() - self.secondtail.xcor())
        new_segment_y = self.tail.ycor() + (self.tail.ycor() - self.secondtail.ycor())
        new_segment.setpos(new_segment_x, new_segment_y)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_pos = self.segments[seg_num-1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]