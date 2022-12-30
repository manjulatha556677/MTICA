def printMonth(dn):
  if(dn==1):
        return"sunday"
  elif(dn==2):
       return"Monday"
  elif(dn==3):
       return"Tuesday"
  elif(dn==4):
       return"Wednesday"
  elif(dn==5):
      return "Thursday"
  elif(dn==6):
      return "Friday"
  elif(dn==7):
      return"Saturday"
 
  else:
     mn="Invalid"


for i in range(7):
   inpNum=int(input())
   print(printMonth(inpNum))
