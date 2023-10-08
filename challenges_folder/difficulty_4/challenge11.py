
#  Challenge 11
#  The program asks the user to input two numbers. It will then output the larger of these two numbers.  

def Challenge_11():

  print("So you want to compare two numbers?")
  number1 = int(input("What is your first number?: "))
  number2 = int(input("What is your second number?: "))

  if number1 < number2:
    print(f"\n{number2} is the bigger number!")

  else:
    print(f"\n{number1} is the bigger number!")