from turtle import Turtle, Screen


rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def validate_input():
    error_message = ""

    while True:
        user_bet = screen.textinput(title="Make your bet",
                                    prompt=f"{error_message}Which turtle will win the race? Enter a color: ").lower()
        if user_bet in rainbow_colors:
            return user_bet
        else:
            error_message = "! Invalid color ! Valid colors: red, orange, yellow, green, blue, indigo, violet\n\n"


def turtle_setup(turtle, index):
    position = -50 + (index * 30)
    turtle.penup()
    turtle.goto(x=-230, y=position)


def main():
    user_bet = validate_input()
    print(user_bet)
    for i in range(len(rainbow_colors)):
        turt = Turtle(shape='turtle')
        turt.color(rainbow_colors[i])
        turtle_setup(turt, i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=500, height=400)
    main()
    screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
