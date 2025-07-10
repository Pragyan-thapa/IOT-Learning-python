class Car:
    make = "BMW"
    model = "BMW E9"
    year = 1968
    
    def start_engine(self):
        print("car started")


car1 = Car()
print(car1.make,car1.model,car1.year)

car1.start_engine()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

stu1 = Student("Ajay",12)
stu1.name = "Pritam"
print(stu1.name,stu1.age)
