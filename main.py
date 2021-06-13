import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
car_manager = CarManager()

scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkeypress(key='Up', fun=player.move_up)
screen.title('Turtle Crossing')

game_is_on = True

speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()
    scoreboard.write_score()
    car_manager.create()
    car_manager.move()
    for cars in car_manager.all_cars:
        if player.distance(cars) < 35:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 270:
        player.go_to_start()
        speed -= 0.01
        scoreboard.update_score()
        car_manager.increase_Speed()




screen.update()
screen.exitonclick()
