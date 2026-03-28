from turtle import Turtle

FONT = ("Times New Roman", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def win(self):
        self.clear()
        self.goto(0, 0)
        self.write("You won", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=FONT)


