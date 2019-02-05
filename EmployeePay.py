#Made by: Elias Enamorado 
#Purpose: Calculate employee pay based on payrate and amount of hours worked
name_list = ["Mary", "John", "Bob", "Mel", "Jen","Sue", "Ken", "Dave", "Beth", "Ray"]; 

pay_rate=[15,22,35,43,17,29,40,20,37,16.50]

hours_worked=[40,25,4,62,33,45,36,17,37,80]

for name, pay, hours in zip(name_list, pay_rate, hours_worked):
  if hours > 40:
    print(name + " earned $" + str(pay*hours*1.5) + "\n")
  else:
    print(name + " earned $" + str(pay*hours) + "\n")