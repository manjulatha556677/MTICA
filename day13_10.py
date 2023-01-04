def squares(x=0):
    while x<10:
        x=x+1
        yield x*x
yieldelist=[i for i in squares()]
print(yieldelist)
