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


first_num = int(input("What's the first number?\n"))

print('\n'.join(operators.keys()))

operator = validate_operator_input()

second_num = int(input("What's the next number?\n"))

result = operators[operator](first_num, second_num)

print(f"{first_num} {operator} {second_num} = {result}")