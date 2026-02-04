class employee:
    emp_count=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.emp_count +=1
    
    def displaycount(self):
        print(f"total employee {employee.emp_count}")

    def displayemployee(self):
        print("name : ", self.name, "salary : ", self.salary)

emp1=employee("parthiv",3000)
emp2=employee("soham",6000)

emp1.displayemployee()
emp2.displayemployee()

print(f"total employee {employee.emp_count}")

print(getattr(emp1,'salary'))
print(hasattr(emp1,'age'))
setattr(emp1,'age',20)
print(emp1.age)

delattr(emp1,'age')
print(emp1.age)