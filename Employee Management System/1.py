class EmployeeManagementSystem:
    def __init__(self):
        self.admin_username = "admin"
        self.admin_password = "admin123"


        self.employee={
                        "E101": {
                                "name": "Parthiv",
                                "age": 22,
                                "department": "IT",
                                "salary": 30000
                                }
                        }
    
    def Main_Menu(self):
        while True:
            print("-" * 30)
            print("_ _ _EmployeeManagementSystem_ _ _")
            print("1. Admin Login")
            print("2. Exit")

            n=input("Enter your choice : ")

            if n=="1":
                self.AdminLogin()
            elif n=="2":
                print("Thank you for visit")
                break
            else:
                print("Invalid Choice!")

    def AdminLogin(self):

        for i in range(3):
            Username=input("Enter username : ")
            Password=input("Enter password : ")
            if Username==self.admin_username and Password==self.admin_password:
                print("Login Successful")
                self.AdminMenu()
                return
            else: 
                print("Wrong Username and password!") 
                
        print("Too many attempts. Returning to main menu.")

    def AdminMenu(self):
        while True:
            print("-" * 30)
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            p=input("Enter your choice : ")

            if p=="1":
                self.AddEmployee()
            elif p=="2":
                self.ViewAllEmployees()
            elif p=="3":
                self.SearchEmployee()
            elif p=="4":
                self.UpdateEmployee()
            elif p=="5":
                self.DeleteEmployee()
            elif p=="6":
                print("Thanks for visit")
                break
            else:
                print("Invalid choice")

    def AddEmployee(self): 
        EmployeeID=input("Enter a EmployeeID : ")
        if EmployeeID in self.employee:
            print("Employee already exists")
            return

        Name=input("Enter your Name : ")
        Department=input("Enter your Department : ")
        try:
            Age=int(input("Enter your Age : "))
            Salary=int(input("Enter your salary : "))
        except ValueError:
            print("Please enter valid numbers!")
            return

        if Salary <= 0:
            print("Invalid salary")
            return
        
        self.employee[EmployeeID]={
                                "name": Name,
                                "age": Age,
                                "department": Department,
                                "salary":Salary
                                 }
        print("Employee added successfully!")
        
    def ViewAllEmployees(self):
        if not self.employee:
            print("No employee found")
            return 
        
        for EmployeeID,details in self.employee.items():
            print("-" * 30)
            print(f"employeeID : {EmployeeID}")
            print(f"Name : {details['name']}")
            print(f"Age : {details['age']}")
            print(f"Department : {details['department']}")
            print(f"Salary : {details['salary']}")

    def SearchEmployee(self):
        EmployeeID=input("Enter a EmployeeID : ")
        if EmployeeID not in self.employee:
            print("Employee not found")
            return 
        

        details = self.employee[EmployeeID]

        print("-" * 30)
        print(f"Name: {details['name']}")
        print(f"\nEmployeeID: {EmployeeID}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    
    def UpdateEmployee(self):

        EmployeeID=input("Enter a EmployeeID : ")
        if EmployeeID not in self.employee:
            print("Employee not found")
            return 

        Name=input("Enter your Name : ")
        Department=input("Enter your Department : ")
        try:
            Age=int(input("Enter your Age : "))
            Salary=int(input("Enter your salary : "))
        except ValueError:
            print("Please enter valid numbers!")
            return
        self.employee[EmployeeID]={"name": Name,
                                "age": Age,
                                "department": Department,
                                "salary":Salary
                                    }

    def DeleteEmployee(self):
        EmployeeID=input("Enter a EmployeeID that you want to delete: ")

        if EmployeeID not in self.employee:
            print("employee not found")
            return 
        
        confirm=input("are you sure?(yes/no)").lower()

        if confirm=="yes":
            del self.employee[EmployeeID]
            print("Employee deleted successfully!")
        else:
            print("Deletion cancelled.")

        
e1=EmployeeManagementSystem()
e1.Main_Menu()








        



