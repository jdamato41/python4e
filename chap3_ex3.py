# takes the input and checks that it is a float
inputscore=input("enter a decimal amount\n")
try:
              inputscore=float(inputscore)
              print (type (inputscore))
              print("OK")
except:
              print("please enter a score as a number")
 #this section will calculate the letter grade for the inputscore  
if inputscore >=90:
                print("A")
elif inputscore >=80:
              print("B")
elif inputscore >=70:
              print("C")
elif inputscore >=60:
              print ("D")
else:
              print("F")


           
