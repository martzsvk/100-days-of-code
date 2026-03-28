from turtle import Turtle
import random


# car size
WIDTH = 1
LENGTH = 2
# colors for cars
COLORS = ["blue", "cyan", "darkgrey", "darkred", "gray", "greenyellow", "lavender", "orangered", "navy", "purple", "red",
"royalblue", "seagreen", "tan", "yellowgreen"
]
# moving distance for cars
MOVE_CAR = 5

class Car:
    def __init__(self):
        self.all_cars = []

    def make_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(x=300, y=random.randint(-255, 280))
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(MOVE_CAR)

    def level_up_cars(self):
        for car in self.all_cars:
            self.all_cars.remove(car)
            car.hideturtle()










