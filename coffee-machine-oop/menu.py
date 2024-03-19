class MenuItem:
  def __init__(self, name, cost, water, coffee, milk):
    self.name = name
    self.cost = cost
    self.ingredients = {
      "water": water,
      "coffee": coffee,
      "milk": milk
    }

class Menu:
  """Models the menu with drinks"""
  def __init__(self):
    self.menu = [
      MenuItem(name="espresso", cost=1.5, water=50,coffee=18, milk=0),
      MenuItem(name="latte", cost=2.5, water=200, coffee=24,milk=150),
      MenuItem(name="cappuccino", cost=3.0, water=250, coffee=24, milk=100)
    ]
    
  def get_items(self):
    """Return all the names of avaialble menu items"""
    options = ""
    for item in self.menu:
      options += f"{item.name}/"
    return options

  def find_drink(self, order_name):
    """Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None"""
    for item in self.menu:
      if item.name == order_name:
        return item
    print("Sorry that item is not available.")