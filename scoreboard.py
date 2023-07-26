from turtle import Turtle

FONT = ("Courier", 17, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-230, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-220, 260)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font = FONT)

        
    
