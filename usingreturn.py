def function1(x,y):
              answer=x+y
              return answer
x=input("a number")
try:
              x=int(x)
except:
              print("not a number)")
y=input("another number")
y=int(y)
answer=function1(x,y)
print (answer)
