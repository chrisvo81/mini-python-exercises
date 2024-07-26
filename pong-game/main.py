from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()