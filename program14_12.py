class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employee{0}:".format(Employee.empCount))
    def displayEmployee(self):
        print("Name: ",self.name,  ",salary:",
              self.salary)
emp1=Employee("Nikhil",9999)
emp1.displayEmployee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))
setattr(emp1,'salary',7000)
print("Modifide salary",getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','Manager')
print(hasattr(emp1,'desg'))
print("Added Attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')
print("is salary an attribute:",hasattr(emp1,'salary'))
