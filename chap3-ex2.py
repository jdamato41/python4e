#this program will calculate by given the rate and hours, it also does overtime
hours=input("Enter the hours worked \n")
try:
              hours=float(hours)
              print("You entered:", hours)
              ot=hours-40
              print(ot)
except:
              print("you need to enter a number")
rate=input("Enter your hourly rate of pay\n")
try:
              rate=float(rate)
              print ("You entered an hourly rate of", rate)
""" except:
              print("You must enter a number")
if hours>40:
              print("over40")
              #pay=(hours*rate)+(ot)*(rate*1.5))
else:
              pay=(hours*rate) """
print("you have", hours,"and",hours-40,"overtime")
print(pay, "is the amount of pay you will receive")
              