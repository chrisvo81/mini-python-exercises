from turtle import Turtle, Screen
import colorgram
import random


def filtered_colors(colors):
    colors_list = []
    for color in colors:
        r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
        # check if not near white or near black
        if not ((r > 200 and g > 200 and b > 200) or (r < 50 and g < 50 and b < 50)):
            colors_list.append(color)
    return colors_list


def randomize_color(colors):
    color = random.choice(colors)
    r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
    new_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return new_color


def painting_dots(turtle):
    colors = filtered_colors(colorgram.extract('color-chart.jpg', 30))
    for _ in range(10):
        turtle.pd()
        turtle.dot(20, randomize_color(colors))
        turtle.pu()
        turtle.fd(50)


def set_starting_position(turtle):
    turtle.pu()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)


def set_backup_position(turtle):
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


def main():
    # Setting Screen
    screen = Screen()

    # Setting turtle
    turtle = Turtle()
    turtle.speed('fastest')

    # Set color
    set_starting_position(turtle)
    for _ in range(10):
        painting_dots(turtle)
        set_backup_position(turtle)

    # Wait for a mouse click to close the window
    screen.exitonclick()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
