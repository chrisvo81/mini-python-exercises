from art import rock, paper, scissors
import random

shapes = [rock, paper, scissors]
valid_choices = [0, 1, 2]
game_over = False

while (game_over != True):
  user = int(
    input(
      "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"
    ))

  if user in valid_choices:
    comp = random.randint(0, 2)
    print(shapes[user])

    print("\nComputer chose:")
    print(shapes[comp])

    if comp == user:
      print("It's a tie")
    elif (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
      print("You win")
      game_over = False
    else:
      print("You lose")
      game_over = True
  else:
    print("Invalid choice. Please choose a number between 0 and 2")

print("Game over")