from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")
WIDTH = 0.2
LENGTH = 0.5

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-75, 180)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(75, 180)
        self.write(self.r_score, align=ALIGN, font=FONT)
        self.half_line()


    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def half_line(self):
        self.shape("square")
        self.shapesize(WIDTH,LENGTH)
        self.color("white")
        self.showturtle()
        self.goto(0, 285)
        self.setheading(270)
        for _ in range(28):
            self.pendown()
            self.stamp()
            self.penup()
            self.forward(20)











    