# This is an infinite loop that has a breakout key
number=0
total=0
while True:
          x=input('enter a number')
          if x=='end':
                    break
          try:
                    xval=int(x)
          except:
                    print('that is not valid input')
                    continue
          total=total+1
          number=number+xval
print(total)
print (number)
print(' ')
#this a for loop
numbers=(2,3,4,5)
for num in numbers:
          print(num)