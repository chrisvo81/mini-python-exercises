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
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Coffee machine started with
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Coin operated values
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Coffee Machine!')
