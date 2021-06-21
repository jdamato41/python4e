# this assigns a letter grade based on percentage
def grade(pg):
              if pg>=90:
                            print("A")
              elif pg>=80:
                            print("B")
              elif pg>=70:
                            print("C")              
              elif pg<70:
                            print("too bad")
pg=input("enter your perntage")
pg=int(pg)
grade(pg)