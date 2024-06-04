from turtle import Turtle, Screen


def move_forward(turtle):
    turtle.forward(10)


def move_backward(turtle):
    turtle.backward(10)


def turn_left(turtle):
    turtle.left(10)


def turn_right(turtle):
    turtle.right(10)


def clear(turtle):
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def main():
    tim = Turtle()
    screen = Screen()

    screen.listen()
    screen.onkey(key='w', fun=lambda: move_forward(tim))
    screen.onkey(key='s', fun=lambda: move_backward(tim))
    screen.onkey(key='a', fun=lambda: turn_left(tim))
    screen.onkey(key='d', fun=lambda: turn_right(tim))
    screen.onkey(key='c', fun=lambda: clear(tim))

    screen.exitonclick()


if __name__ == '__main__':
    main()

