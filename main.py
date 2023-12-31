import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0) # turn off the tracer. 

player = Player() 
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1) # 화면이 0.1초마다 업데이트된다
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    
    if player.finish_line():
        player.goto(0, -280)
        car_manager.level_up()
        scoreboard.update_score()
        
screen.exitonclick()

