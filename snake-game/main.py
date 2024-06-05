from turtle import Turtle, Screen

def setup_snake():
    for i in range(3):
        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(x=-i*20, y=0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    setup_snake()

    screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
