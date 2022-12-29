def kelvintofahrenheit(Temperature):
    assert (Temperature>0),"coldern than absolute zero at  MTICA"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print(kelvinTopahrenheit(-50))
except Exception as ob:
        print(ob)
try:
    print(kelvinTopahrenheit(273))
except Exception as ob:
        print(ob)
try:
    print(kelvinTopahrenheit(505.78))
except Exception as ob:
        print(ob)
try:
    print(kelvinTopahrenheit(-5))
except Exception as ob:
        print(ob)
print("THANK YOU")
    
