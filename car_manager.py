import turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_increment = MOVE_INCREMENT

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            tim = turtle.Turtle('square')
            tim.shapesize(stretch_wid=1, stretch_len=2)
            tim.color(random.choice(COLORS))
            tim.penup()
            new_y = random.randint(-250, 250)
            tim.goto(300, new_y)
            self.all_cars.append(tim)

    def move(self):
        for cars in self.all_cars:
            cars.bk(self.move_increment)

    def increase_Speed(self):
        self.move_increment += MOVE_INCREMENT
        self.move()




