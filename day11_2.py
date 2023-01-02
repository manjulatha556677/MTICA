Months={1:'January',2:'Febreary',3:'March',4:'April',5:'May',6:'Jane',7:'July',8:'August',
       9:'September',10:'Octomber',11:'November',12:'December'}
n=int(input())
for count in range(n):
    mn=int(input())
    if mn>=1 and mn<=12:
       print(Months[mn])

else:
    print("invalid")
