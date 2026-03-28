from turtle import Turtle

WIDTH = 1
LENGTH = 5

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
