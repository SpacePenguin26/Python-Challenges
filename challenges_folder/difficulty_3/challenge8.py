
#  Challenge 8
#  The program asks the user to input how many minutes and texts they have used in the last month and then outputs the total cost of the bill. This is calculated by working out:
#  - The total cost of the minutes (at £0.10 per minute) and…. 
#  - Adding this to the total cost of the texts (at £0.05 per text) and…. 
#  - Adding on an additional monthly charge of £10.00. 

def Challenge_08():
  print("During the past month,")
  
  minutes = int(input("How many minutes have you used?: "))
  text =    int(input("How many texts have you sent?: "))
  
  mcost = (minutes*0.10) 
  tcost = (text*0.05)
  monthlyCharge = 10
  
  total = (mcost + tcost + monthlyCharge)
  
  print (f"\nYour Monthly Cost is £{total}")