number=0
total=0
while True:
          x=input("enter a numner > ")
          if x=="done":
                    break
          try:
                    xval=int(x)
          except:
                    print("that is not valid")
                    continue
          total=total+1
          number=number+xval
print(total)
print(number)
