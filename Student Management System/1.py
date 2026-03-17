class Student_Management_System:
    def __init__(self):
        self.students={
                    "1001":{"password":"12345","marks":[]},
                    "1002":{"password":"54321","marks":[10,40]}
                    }
        

    def Main_Menu(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Login")
            print("2. Registration")
            print("3. Exit")

            
            n=input("Enetr your choice : ")

            if n=="1":
                self.Login()
            elif n=="2":
                self.Register()
            elif n=="3":
                print("Thank you for visit")
                break
            else:
                print("please Enter Valid number")

    
    def Register(self):
        student_id=input("Create a student ID : ")

        if student_id in self.students:
            print("student ID is already exists")
            return 

        Password=input("create a Password : ")

        self.students[student_id]={
            "password":Password,
            "marks":[]
        }
        print("Registration successful!")

    
    def Login(self):
        student_id=input("Enter a student ID : ")

        if student_id not in self.students:
            print("User not found. Please register first.")
            return

        for i in range(3):
            password=input("Enter a Password : ")

            if password==self.students[student_id]["password"]:
                print("Login Successful")
                self.Student_Menu(student_id)
                return 
            else:
                print("Wrong password!")

        print("Too many attempts. Returning to main menu.")

    
    def Student_Menu(self,student_id):
        while True:
            print("""
                1. Add Marks
                2. View Marks
                3. Update Password
                4. Back to Main Menu
                5. Exit
                """)
            p=input("Enetr a choice : ")

            if p=="1":
                self.Add_Marks(student_id)
            elif p=="2":
                self.View_Marks(student_id)
            elif p=="3":
                self.Update_Password(student_id)
            elif p=="4":
                return
            elif p=="5":
                print("Goodbye!")
                exit()
            else:
                 print("Invalid choice!")
        
                
        
    def Add_Marks(self,student_id):
        try:
            mark = int(input("Enter your marks : "))
        except ValueError:
            print("Please enter a valid number!")
            return        
        if mark < 0 or mark > 100:
            print("Invalid marks!")
        else:
            self.students[student_id]["marks"].append(mark)
            print("Marks added successfully!")
        
    
    def View_Marks(self,student_id):
        marks = self.students[student_id]["marks"]

        if not marks:
            print("No marks available.")
        else:
            print("Marks:", marks)
            print("Average:", sum(marks) / len(marks))
        

    def Update_Password(self,student_id):
        new_Password=input("Enter a new password : ")
        self.students[student_id]["password"]=new_Password
        print("Password updated successfully!")
    

s1=Student_Management_System()
s1.Main_Menu()








        