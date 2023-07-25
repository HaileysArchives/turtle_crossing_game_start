from turtle import Turtle 
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
X = -300
STARTING_POSITIONS = [(X, -225), (X, -200), (X, -175), (X, -150), (X, -125), (X, -100), (X, -75), (X, -50), (X, -25),
                      (X, 0), (X, 25), (X, 50), (X, 75), (X, 100), (X, 125), (X, 150), (X, 175), (X, 200), (X, 225)]

class CarManager:
    
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        
        for car in self.all_cars:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car = car
            self.all_cars.append(car)
        
    
