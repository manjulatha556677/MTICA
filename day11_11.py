sample_dict={
    "name":"manju",
    "age":25,
    "salary":8000,
    "city":"newyork"}
keys={"name","salary"}

res=dict()
for k in keys:
    res:update({k:sample_dict[k]})
print(res)
