def calculator():#this function calculated pay
              othours=hours-40#this section calcualted overtime pay
              otrate=rate*1.5
              print("You have overtime hours:",othours, "Your overtime rate is:",otrate, "\n")
              otpay=othours*otrate
              regpay=(hours-othours)*rate
              print("Reg Pay\n",regpay)
              print("Overtime Pay\n",otpay)
              totalpay=otpay+regpay
              print("Total Pay:",totalpay)
hours=input("Enter the number of hours worked:\n")
try:
              hours=float(hours)
except:
              print("you have not entered a number")
rate=input("enter the hourly rate of pay:\n")
try:
              rate=float(rate)
except:
              print("please enter a number\n")
if hours>40:
              calculator()
else:
             regpay=rate*hours# this calculated the regular pay with no overtime
             print("you have no overtime, so your total salary is:",regpay)


