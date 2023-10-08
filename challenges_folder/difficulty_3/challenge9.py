
#  Challenge 9
#  Write an algorithm that: 
#  - Stores a random first name as a variable. 
#  - Asks the user to input their first name. 
#  - If it is the same as the stored name, outputs 'You’re cool.' 
#  - Otherwise outputs 'Nice to meet you.' 

def Challenge_09():
  
  goodNames = ['Andrew', 'Fin', 'Aaron']

  firstName = input("What is your firstname?: ")

  if firstName == 'Lucas':
    print("\nSupprised you can even reach the keyboard, short boy!")
    
  elif firstName in goodNames:
    print(f"\nYou're a cool guy {firstName}")
    
  else:
    print(f"\nWho even are you {firstName}? You're not cool!")