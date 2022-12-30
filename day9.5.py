def printDay(dn):
  if(dn==1):
        return"sunday"
  elif(dn==2):
       return"monday"
  elif(dn==3):
       return"tuesday"
  elif(dn==4):
       return"wednesday"
  elif(dn==5):
      return "thursday"
  elif(dn==6):
      return "friday"
  elif(dn==7):
      return"saturday"
  
  else:
     return "Invalid"
    
def printDay1(dn):
  if(dn==1):
        return"sunday"
  elif(dn==2):
       return"monday"
  elif(dn==3):
       return"tuesday"
  elif(dn==4):
       return"wednesday"
  elif(dn==5):
      return "thursday"
  elif(dn==6):
      return "friday"
  elif(dn==7):
      return"saturday"
  
  else:
      return "Invalid"

import time
for i in range(12):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print=((time.time()-start)*1000000)     
    start=time.time()
    print(printDay1(inpNum))
    print=((time.time()-start )*1000000)     

  
   
