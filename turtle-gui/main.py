from turtle import Turtle, Screen
from tk_colors import tk_color
import random


def create_turtle(input_colour='red'):
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.color(input_colour)
    return turtle


def forward_dash_line(turtle, num_dashes=15, dash_length=10):
    for _ in range(num_dashes):
        turtle.forward(dash_length)
        turtle.pu()
        turtle.forward(dash_length)
        turtle.pd()


def draw_square(turtle, turn_direction='right'):
    for _ in range(4):
        if turn_direction == 'right':
            turtle.right(90)
        else:
            turtle.left(90)
        turtle.forward(100)


def draw_pentagon(turtle, num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


def randomize_tk_color():
    chosen_color = random.choice(tk_color)
    return chosen_color


def random_rgb_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rand_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return rand_color


def random_walk(turtle):
    direction = [0, 90, 180, 270]
    turtle.pensize(15)
    turtle.speed('fastest')
    for _ in range(200):
        turtle.setheading(random.choice(direction))
        turtle.forward(random.randint(0, 80))
        # turtle.color(randomize_tk_color())
        turtle.color(random_rgb_color())


def make_spirograph(turtle):
    for _ in range(0, 72):
        turtle.speed('fastest')
        turtle.circle(100)
        turtle.left(5)
        turtle.color(random_rgb_color())


# Better function for making spirograph
def make_spirograph_2(turtle, gap_size):
    for _ in range(int(360 / gap_size)):
        turtle.speed('fastest')
        turtle.circle(100)
        turtle.color(random_rgb_color())
        turtle.setheading(turtle.heading() + gap_size)


def main():
    # Use a breakpoint in the code line below to debug your script.
    timmy = create_turtle('green')
    # forward_dash_line(timmy)

    # tommy = create_turtle()
    # draw_square(tommy, 'left')

    # for shape_side_n in range(3, 11):
    #     draw_pentagon(timmy, shape_side_n)
    #     timmy.color(randomize_tk_color())

    # random_walk(timmy)

    # make_spirograph(timmy)
    make_spirograph_2(timmy, 5)

    screen = Screen()
    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
