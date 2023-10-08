
#  Challenge 7
#  Write an algorithm that:
#  - Asks the user for the distance (in metres). 
#  - Asks the user for the time in seconds that a journey was completed in. 
#  - Calculates and outputs the average speed using a function.  

def Challenge_07():

  print("You want to know how fast you were going?")
  distance =  int(input("How far did you travel? (metres): "))
  time =      int(input("How long were you travelling for? (seconds): "))
  
  speed = (distance/time)
  
  print (f"\nYou were travelling at {speed} metres per second (m/s)")   