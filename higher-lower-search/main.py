from art import logo, vs
from game_data import data
from random import choice
from replit import clear

STARTING_SCORE = 0

def pick_random_account():
  return choice(data)

def compare_followers(followers_a, followers_b):
  return 'A' if followers_a > followers_b else 'B'

def print_versus(account_a, account_b):
  print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
  print(vs)
  print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
  

def main():
  print(logo)
  score = STARTING_SCORE
  game_over = BEGINING_GAME
  account_a = pick_random_account()
  account_b = pick_random_account()

  while account_b == account_a:
    account_b = pick_random_account()
  
  while not game_over:
    print_versus(account_a, account_b)
    guess = input("Who has more followers? Type 'A' or 'B': ")
    winner = compare_followers(int(account_a['follower_count']), int(account_b['follower_count']))
    
    if guess == winner:
      score += 1
      account_a = account_b
      account_b = pick_random_account()
      clear()
      print(f"You're right! Current score: {score}.")
    else:
      game_over = True
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")

main()
