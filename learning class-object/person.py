class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


emp1 = employee("rajan",38,1143)
print(emp1.name,emp1.age,emp1.employee_id)

