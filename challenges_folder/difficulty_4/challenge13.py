
#  Challenge 13
#  A company calculates holiday allowance for employees. 
#  The company gives each employees 28 days holiday each year. Holidays are awarded based on the following rules: 
#  1. Full time employees who work 5 days a week get 28 days holiday a year 
#  2. Part time employees get a proportion of holiday allowance based on how many days they work, e.g. An employee who works 1 day a week would only get 1/5th of the holidays allowed.

def Challenge_13():
  # Input employee type and days worked per week
  employee_type = input("Enter employee type (full-time or part-time): ").lower()
  days_worked_per_week = int(input("Enter days worked per week: "))
  
  # Define the total holiday allowance for a full-time employee
  full_time_allowance = 28
  
  if employee_type == "full-time":
      holiday_allowance = full_time_allowance
  elif employee_type == "part-time":
      if days_worked_per_week <= 0:
          holiday_allowance = 0
      elif days_worked_per_week >= 5:
          holiday_allowance = full_time_allowance
      else:
          # Calculate proportionate allowance for part-time employees
          proportionate_allowance = (days_worked_per_week / 5) * full_time_allowance
          holiday_allowance = proportionate_allowance
  else:
      holiday_allowance = 0  # Invalid employee type
  
  # Print the holiday allowance
  if holiday_allowance > 0:
      print(f"Holiday allowance: {holiday_allowance} days")
  else:
      print("Invalid input or no holiday allowance for this employee type.")
