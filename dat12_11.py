class Student:
     college='MTICA'
     course='MCA'
    
     def __init__(self,name,rollno):
         self.name=name
         self.rollno=rollno
     def displayStudent(self):
         print('name:'+self.name.title()+'\nroll.no:'\
               +str(self.rollno))
         print('college:'+self.college+'\nCourse:'+self.course)

for i in range(2):
    n=input()
    r=int(input())
    obj=Student(n,r)
    obj.displayStudent()
        

      
    
