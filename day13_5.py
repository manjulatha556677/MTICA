def printadd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMul(a,b):
    return a*b
def printdiv(a,b):
    return a/b
def choice():
    print("+:Addition");print("-:Substraction");
    print("*:Multiplication");print("/:Division");
    print("q:Quite");
    return
colorselect={"+":printadd,"-":printSub,"*":printMul,"/":printdiv}
while True:
    choice()
    selection=input("selection an arthematic operation:")
    if (selection=='q') or selection=="Q":break
    if ((selection=="+") or (selection=="-")or
       (selection=="*") or (selection=="/")):
       n1=int(input("enter first no:"))
       n2=int(input("enter second no:"))

       z=colorselect[selection](n1,n2)
       print(n1,selection,n2,'=',z)
                            
    
    
    
    
        

 
   
