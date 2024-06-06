from turtle import Turtle, Screen
from snake import Snake
import time


def setup_screen(screen):
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")


def game_on():
    global is_crashed
    screen = Screen()
    setup_screen(screen)
    screen.tracer(0)

    snake = Snake()

    is_crashed = False
    while not is_crashed:
        screen.update()
        time.sleep(0.15)
        snake.move()

    screen.exitonclick()


if __name__ == '__main__':
    game_on()
