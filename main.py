from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from fileu import Fileu
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game by Miki")
screen.tracer(0)

fileu = Fileu()

scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # coliziune cu peretii sus si jos
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce()

    #coliziune cu paleta dreapta
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.deflect()

    #coliziune cu paleta stanga
    if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.deflect()

    #coliziunce afara
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
