from turtle import Turtle

INIT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in INIT_POSITIONS:
            snake = Turtle(shape='square')
            snake.color('white')
            snake.penup()
            snake.goto(pos)
            self.segments.append(snake)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading != 180:
            self.head.setheading(0)
