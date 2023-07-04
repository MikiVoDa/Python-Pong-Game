from turtle import Turtle

class Fileu(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(0, 310)
        self.setheading(270)
        self.pensize(5)
        while self.ycor() > -310:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
