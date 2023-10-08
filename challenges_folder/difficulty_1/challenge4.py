# --- Challenge 4 ---
# This program asks the user to input their first name and then their surname.
# It then outputs the user's first name and then their surname on the same line.

def Challenge_04():
  
  print("Oh hey!")  # Print a greeting message to the user

  # Ask the user to input their first name and store it in the 'name' variable
  name = input("What's your name?: ")
  # Ask the user to input their surname and store it in the 'surname' variable
  surname = input("What's your surname?: ")

  # Print a greeting message with the user's first name and surname
  print(f"\nHello, {name} {surname}")
