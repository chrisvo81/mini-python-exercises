from turtle import Turtle, Screen

positions = [(0,0), (-20,0), (-40,0)]

def setup_snake():
    for pos in positions:
        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(pos)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    setup_snake()

    screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
