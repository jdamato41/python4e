#this is a pay caluclator that deals with overtime
rate=input("enter your hourly rate \n")
rate=float(rate)
hours=input("enter the number of hours worked\n")
hours=float(hours)
if hours >40:
              pay=(hours*rate)+((hours-40)*rate)
              print(pay)
else:
              print(rate*hours)
