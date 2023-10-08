
#  Challenge 6
#  The program asks the user to input two numbers. The program will then output: 
#  - The two numbers added together followed by… 
#  - The two numbers multiplied together. 

def Challenge_06():

  print("Want to add 2 numbers together?\nThen multiply those same numbers?\n")
  num1 = int(input("What is your first number?: "))
  num2 = int(input("What is your second number?: "))
  
  total = (num1 + num2)
  product = (num1 * num2)
  
  print("\nYour total is:", total)
  print("Your product is:", product)