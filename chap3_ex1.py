#this is a pay caluclator that deals with overtime
rate=input("enter your hourly rate")
rate=float(rate)
hours=input("ente the number of hours worked")
hours=float(hours)
if hours >40:
              pay=(hours*rate)+((hours-40)*rate)
              print(pay)
else:
              print(rate*hours)
              