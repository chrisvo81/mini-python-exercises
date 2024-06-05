import time
from turtle import Turtle, Screen


init_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []


def setup_snake():
    for pos in init_positions:
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(pos)
        segments.append(snake)


def setup_screen(screen):
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")


def game_on():
    global is_crashed
    screen = Screen()
    setup_screen(screen)
    setup_snake()

    is_crashed = False
    while not is_crashed:
        screen.update()
        time.sleep(0.2)

        for seg in range(len(segments)-1, 0, -1):
            new_x = segments[seg - 1].xcor()
            new_y = segments[seg - 1].xcor()
            segments[seg].goto(new_x, new_y)

    screen.exitonclick()


if __name__ == '__main__':
    game_on()
