#merge 2 python distonaries into one

dict1={'Ten':10,'Twenty':20,'Thirty':30}
dict2={'Therty':30,'fourty':40,'Fifty':50}

dict3={**dict1,**dict2}
print(dict2)