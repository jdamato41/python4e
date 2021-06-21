num=0
total=0# needed to initialze these variable
while True:
          sval=input("enter a number-  ")
          if sval=="done":
                    break
          try:
                    fval=int(sval)
          except:
                    print("not valid")
                    continue#needed this continue
          print(sval)
          num=num+1#missed this
          total=total+fval#missed this
print("count" ,num, "total ",total, "average ", total/num)
print("goodbye")
         
          
