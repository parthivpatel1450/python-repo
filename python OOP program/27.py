class Organization:
   def __init__(self):
      self.inner = self.Department()

   def showName(self):
      print("Organization Name: Tutorials Point")

   class Department:
      def __init__(self):
         self.innerTeam = self.Team1()

      def displayDep(self):
         print("In Department")

      class Team1:
         def displayTeam(self):
            print("Team 1 of the department")

outer = Organization()  
outer.showName()  

inner = outer.inner  
inner.displayDep()  

innerTeam = inner.innerTeam  
innerTeam.displayTeam() 