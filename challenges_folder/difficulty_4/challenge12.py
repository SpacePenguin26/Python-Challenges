
#  Challenge 12
#  Write an algorithm that:
#  - Generates a random number between 1 and 10. 
#  - It must then ask the user to guess this number.  
#  - If they guess it correctly it should display ‘Correct’ 
#  - Otherwise, display ‘Not what I was thinking’

def Challenge_12():

  import random
  
  # Generate a random number between 1 and 10
  random_number = random.randint(1, 10)
  
  # Ask the user to guess the number
  user_guess = int(input("Guess the number (between 1 and 10): "))
  
  # Check if the user's guess is correct
  if user_guess == random_number:
      print("\nThat is Correct!! How did you know??")
  else:
      print(f"\nSorry! That's not what I was thinking. The correct number was {random_number}")
