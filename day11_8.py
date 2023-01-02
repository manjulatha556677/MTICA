 #initialize dictonary with default values

employees=['manju','anju','arun']
defaults={"destination":"developer","salary":80000}

data=dict.fromkeys(employees,defaults)
print(data)
print(data["manju"])
