

sample_dict={
    "name":"'manju"
    "age":25
    "salary":80000
    "city":"hydarabad"}
keys=["name","salary"]
newDict={}
for i in keys:
    newDict[i]sample_dict[i]
print(newDict)

    newDict={i:sample_Dict[i] for i in keys}
print(newDict)
    
