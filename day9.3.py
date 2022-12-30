def printMonth(dn):
   if(dn==1)
       return "january"
 elif(dn==2)
    return "Febreary"
 elif(dn==3)
    return "March"
 elif(dn==4)
    return "April"
 elif(dn==5)
    return "May"
 elif(dn==6)
    return "June"
 elif(dn==7)
    return "July"
 elif(dn==8)
    return "August"
 elif(dn==9)
    return "September"
 elif(dn==10)
    return "0ctober"
 elif(dn==11)
    return "November"
 elif(dn==12)
   return "December"
else:
    return"Invalid"


for i in range(3):
inpNum=int(input())
print(printMonth(inpNum)
