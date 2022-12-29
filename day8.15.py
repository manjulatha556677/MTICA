def printseriesIncreasing(ch,n):
    for i  in range(1,n+1,1):
        print(ch*i)
        return None
def printSeriesIncreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
        return None
inpch=input("enter a charecter:")
inpNum=int(input("enter a number:"))
printseriesIncreasing(inpch,inpNum)
print('-'*40)
printseriesIncreasing(inpch,inpNum)
               
        
    
