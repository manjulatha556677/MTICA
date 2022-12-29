num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
try:
    res=int(num1)/(num2)#execute with num2=non zero agnd zero
except (ZeroDivisionError,ValueError):
        print("Exception handle by archu")
except Exception is ob:
         print(ob)
else:
    print(num1,'/',num2,'=',res)
finally:
        print('thanks')
    
print("visit again at python class MTICA")
