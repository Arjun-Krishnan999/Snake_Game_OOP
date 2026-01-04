from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        with open(file="data.txt", mode="r") as data:
            self.high_score=int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, 'center', ('Arial', 15, 'normal'))

    def add_score(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",False,"center",('Arial', 35, 'normal'))