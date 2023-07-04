from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.score_l, align="center", font=("courier", 60, "bold"))
        self.goto(100, 210)
        self.write(self.score_r, align="center", font=("courier", 60, "bold"))

    def l_point(self):
        self.score_l += 1
        self.update()

    def r_point(self):
        self.score_r += 1
        self.update()
