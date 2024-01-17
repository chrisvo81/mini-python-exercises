from random import randint

#Number Guessing Game Objectives:
logo = '''
 ______     __  __     ______     ______     ______     __   __     __  __     __    __     ______     ______     ______    
/\  ___\   /\ \/\ \   /\  ___\   /\  ___\   /\  ___\   /\ "-.\ \   /\ \/\ \   /\ "-./  \   /\  == \   /\  ___\   /\  == \   
\ \ \__ \  \ \ \_\ \  \ \  __\   \ \___  \  \ \___  \  \ \ \-.  \  \ \ \_\ \  \ \ \-./\ \  \ \  __<   \ \  __\   \ \  __<   
 \ \_____\  \ \_____\  \ \_____\  \/\_____\  \/\_____\  \ \_\\"\_\  \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_____/   \/_/  \/_/   \/_____/   \/_____/   \/_/ /_/ 
'''
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


## function check answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
        return False
    elif guess < answer:
        print("Too low")
        return False
    else:
        print(f"You got it! The answer was {answer}")
        return True


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if difficulty == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    correct_number = randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    print(f"Pssst, the correct answer is {correct_number}")

    attempts = set_difficulty()
    print(f"You have {attempts} attempts remaining to guess the number.")

    is_correct_answer = False
    while not is_correct_answer and attempts != 0:
        guess = int(input("Make a guess: "))
        is_correct_answer = check_answer(guess, correct_number)
        attempts -= 1
        if not is_correct_answer and attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")

    if not is_correct_answer and attempts == 0:
        print("You've run out of guesses, you lose.")


game()