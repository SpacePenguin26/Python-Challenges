
#  Challenge 10
#  The program asks the user to input the number of letters in the alphabet. The program must then output whether they got it correct or incorrect.

def Challenge_10():

  answer = int(input("How many letters are there in the Latin alphabet?: "))

  if answer == 26:
    print("\nCorrect! You must be a genious!")

  elif answer == 1 or -1:
    print(f"\nAre you sure? You must have {answer} braincell!")

  else:
    print(f"\nAre you sure? You must have {answer} braincells!")
