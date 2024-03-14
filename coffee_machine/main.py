import inquirer
import os

# Program Objective -----------------------------------------------
# 1. Print Report
# "What would you like? (espresso/latte/cappuccino):
# input "report" will print report of the machine current state
# water: 300ml, milk: 200ml, coffee: 100g, money: 0

# 2. Check if the resources sufficient when user order a drink
# "Please insert coins."
# "How many quarters?:"
# "How many dimes?:"
# "How many pennies?:"
# "Here is $[x.xx] in change."

# 3. Process coins
# 4. Check transaction successful
# 5. Make coffee
# "Here is your latte ☕️ Enjoy!"
# If not enough resource: "Sorry there is not enough [resource]"
# If not enough money to cover the drink: "Sorry that's not enough money. Money refunded"

# All coffee type
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

# Coffee machine started with
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Coin operated values
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

# Report of the machine current state
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    # print(f"Money: ${resources['money']}")

# Turn off machine
def turn_off():
    print("Machine turned off")
    exit()

# Calculating coins value
def calculate_input_coins():
    total_value = 0
    for coin, value in coins.items():
        num_coins = int(input(f"How many {coin}?:"))
        total_value += num_coins * value
    resources["money"] = total_value
    return total_value

# Check if the resources sufficient when user order a drink
def check_resources(drink):
    for item, quantity in MENU[drink]["ingredients"].items():
        if resources[item] < quantity:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# Check transaction successful
def transaction_successful(drink_cost, user_inserted_value):
    if user_inserted_value >= drink_cost:
        change = round(user_inserted_value - drink_cost, 3)
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    
# Making coffee
def make_coffee(drink):
    resources_available = check_resources(drink)
    if (resources_available):
        print(f"{drink.capitalize()} costs ${MENU[drink]['cost']:.2f}")
        print("Please insert coins.")
        drink_cost = MENU[drink]["cost"]
        user_inserted_value = calculate_input_coins()
        print(f"Total inserted: ${user_inserted_value:.2f}")
        transaction = transaction_successful(drink_cost, user_inserted_value)
    else:
        print("Sorry, not enough resources")

# Prompt for user input
def machine_prompt():
    # user_input = input("What would you like? (espresso/latte/cappuccino):")
    questions = [ inquirer.List('drink', message="What would you like?", choices=['espresso', 'latte', 'cappuccino', 'report', 'off'],), ]
    answer = inquirer.prompt(questions)["drink"]
    return answer

def main():
    user_selection = machine_prompt()
    if user_selection in MENU:
        make_coffee(user_selection)
    elif user_selection == "report":
        print_report()
    elif user_selection == "off":
        turn_off()
        
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
