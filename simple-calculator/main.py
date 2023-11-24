from art import logo

print(logo)

def add(num1, num2):
  return num1 + num2

def minus(num1, num2):
  return num1 - num2

def multi(num1, num2):
  return num1 * num2

def div(num1, num2):
  return num1 / num2

operators = {
  "+": add,
  '-': minus,
  '*': multi,
  '/': div
}
def validate_operator_input():
  while True:
    user_input = input("Pick an operation:\n")
    if user_input in operators.keys():
      return user_input
    else:
      print("Invalid operator. Please enter a valid operator.")

def validate_cont_input(user_input):
  while user_input.lower() not in ['y', 'n']:
    print("Invalid input. Please enter 'y' or 'n'.")
    user_input = input()
  return user_input.lower()

def numeric_input(user_input):
  try:
    # Try to convert the input to a float
    num = float(user_input)
    print(f"{num} is a valid float.")
  except ValueError:
    # If both conversions fail, it's not a number
    print(f"'{user_input}' is not a valid number.")


first_num = numeric_input(input("What's the first number?\n"))

cont_cal = True

while cont_cal:
  print('\n'.join(operators.keys()))
  operator = validate_operator_input()

  second_num = numeric_input(input("What's the next number?\n"))

  result = operators[operator](first_num, second_num)
  print(f"{first_num} {operator} {second_num} = {result}")

  first_num = result

  user_input = input("Would you like to do another calculation? (y/n)\n")
  cont_cal = validate_cont_input(user_input) == 'y'

print("Thanks for using the calculator!")
