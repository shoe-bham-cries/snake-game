from turtle import Turtle

import snake

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        snake_part = Turtle(shape='square')
        snake_part.penup()
        snake_part.color("white")
        snake_part.goto(position)
        self.snake_body.append(snake_part)

    def reset_snake(self):
        for i in self.snake_body:
            i.goto(999,999)
        self.snake_body.clear()
        self.create_snake()

    def move(self):
        #               Range:       Start,        Stop, Step
        for part in range((len(self.snake_body) - 1), 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            coor = (new_x, new_y)
            self.snake_body[part].goto(coor)
        self.snake_body[0].forward(20)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def extend(self):
        self.add_part(self.snake_body[-1].position())
