class Organization:
   def __init__(self):
      self.inner1 = self.Department1()
      self.inner2 = self.Department2()
        
   def showName(self):
      print("Organization Name: Tutorials Point") 

   class Department1:
      def displayDepartment1(self):
         print("In Department 1")
            
   class Department2:
      def displayDepartment2(self):
         print("In Department 2")


outer = Organization() 
outer.showName()  
inner1 = outer.inner1 
inner1.displayDepartment1() 
inner2 = outer.inner2 
inner2.displayDepartment2() 