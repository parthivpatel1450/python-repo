class Employee:

   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      
      Employee.empCount += 1
      print ("Name:", self.__name, ", Age: ", self.__age)
      
      print ("Employee Count:", Employee.empCount)

e1 = Employee("Bhavana", 24)
print()
e2 = Employee("Rajesh", 26)