from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    is_crashed = False
    while not is_crashed:
        screen.update()
        time.sleep(0.125)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            # print("nom nom nom")
            food.refresh()
            snake.extned()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            is_crashed = True
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments:
            if snake.head.distance(segment) < 10 and segment != snake.head:
                is_crashed = True
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    game_on()
