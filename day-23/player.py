from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=-280)

    def move_forward(self):
        self.forward(10)

    def level_up_player(self):
        self.goto(x=0, y=-280)



