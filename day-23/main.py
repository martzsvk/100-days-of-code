from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time


# setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing game")
screen.tracer(0)

# initializing classes
player = Player()
car = Car()
scoreboard = Scoreboard()


# moving player
screen.listen()
screen.onkeypress(player.move_forward, "w")

car_speed = 0.1

playing = True
while playing:
    screen.update()
    time.sleep(car_speed)
    car.make_car()
    car.car_move()

    # detect collision with car
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 20:
            scoreboard.game_over()
            playing = False

    # detect if player is out of bounds
    if player.ycor() > 295:
        scoreboard.level_up()
        player.level_up_player()
        car.level_up_cars()
        car_speed -= 0.01

    # player wins if he successfully completed level 10
    if scoreboard.level == 11:
        scoreboard.win()
        playing = False


screen.exitonclick()