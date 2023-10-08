# --- Challenge 1 ---
# Design a program which asks the user to input their name, age, and favorite color.

# Define a function called Challenge_01
def Challenge_01():
  
    print("Hello!")  # Print a welcome message

    # Prompt the user to input their name, age, and favorite colour
    name = input("What's your name?: ")
    age = input("How old are you?: ")
    colour = input("What's your favorite colour?: ")

    # Print a message with the provided information, using f-strings
    print(f"\nSorry, your name ({name}), age ({age}), or color ({colour}) cannot be printed.")
