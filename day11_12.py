sample_dict={
    "name":"manju",
    "age":25,
    "salary":8000,
    "city":"newyork"}
keys={"name","salary"}

d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
        
print(d)

      
