
def patternprinting(s,n):
    assert(n>=0),'invalid'
    for i in range(n,0,-2):
         print(s*i)
      
s=input()
n=int(input())
try:
    patternprinting(s,n)
except AssertionError as a:
    print(a)
          
