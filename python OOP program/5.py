class Student:
   def __init__(self, name, grade):
      self.__name = name
      self.__grade = grade
      print ("Name:", self.__name, ", Grade:", self.__grade)

# Creating instances 
student1 = Student("Ram", "B")
student2 = Student("Shyam", "C")