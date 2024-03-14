import os

def clear_terminal():
  if os.name == 'nt':  # If the operating system is Windows
    os.system('cls')
  else:  # If the operating system is not Windows (e.g., Linux or Mac)
    os.system('clear')

# Now you can clear the terminal by calling this function
clear_terminal()