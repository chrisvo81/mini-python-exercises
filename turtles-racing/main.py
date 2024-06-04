from turtle import Turtle, Screen
import random


rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []


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


def initialize_turtles():
    for i in range(len(rainbow_colors)):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(rainbow_colors[i])
        turtle_setup(new_turtle, i)
        all_turtles.append(new_turtle)


def announce_result(winner, bet):
    if winner == bet:
        print(f"You've won! The {winner} turtle is the winner.")
    else:
        print(f"You've lost! The {winner} turtle is the winner.")


def start_race():
    winning_turtle = None

    while not winning_turtle:
        for turtle in all_turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

            if turtle.xcor() > 230:
                winning_turtle = turtle.pencolor()
                break

    return winning_turtle


def main():
    user_bet = validate_input()

    if user_bet:
        initialize_turtles()
        winning_turtle = start_race()
        announce_result(winner=winning_turtle, bet=user_bet)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=500, height=400)
    main()
    screen.exitonclick()

