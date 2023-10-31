# Encapsulation:  Encapsulation refers to the varable (binding data) and the methods into a single unit #

class Student:
    def __init__(self , name , dept , age ):
        self.name = name
        self.dept = dept
        self.age  = age
    def display (self):
        print("name :",self.name,"dept :",self.dept)
    def years (self):
        print("age :",self.age)
stu = Student('dhana','cse',19)
stu.display()
stu.years()