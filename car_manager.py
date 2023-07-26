from turtle import Turtle 
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
X = 300
STARTING_POSITIONS = [(X, -225), (X, -200), (X, -175), (X, -150), (X, -125), (X, -100), (X, -75), (X, -50), (X, -25),
                      (X, 0), (X, 25), (X, 50), (X, 75), (X, 100), (X, 125), (X, 150), (X, 175), (X, 200), (X, 225)]

class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.INCREASE_SPEED = 0

    def create_cars(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(random.choice(STARTING_POSITIONS))
        self.all_cars.append(new_car)    
    
    def move(self):
        for new_car in self.all_cars:
            new_car.backward(STARTING_MOVE_DISTANCE + self.INCREASE_SPEED)

    def level_up(self):
        self.INCREASE_SPEED += 5


        
    
