class BankManagementSystem:

    def __init__(self):
        # Default users dictionary
        self.users = {
            "1001": {"password": "admin123", "balance": 1000},
            "1002": {"password": "user123", "balance": 1500}
        }

    def start(self):
        while True:
            print("\n--- Bank Management System ---")
            print("1. Login")
            print("2. Registration")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.registration()
            elif choice == "3":
                print("Thank you for using the system.")
                break
            else:
                print("Invalid choice!")

    def login(self):
        user_id = input("Enter ID: ")

        if user_id not in self.users:
            print("User not found. Please register first.")
            return

        for i in range(3):
            password = input("Enter Password: ")

            if password == self.users[user_id]["password"]:
                print("Login successful!")
                self.account_menu(user_id)
                return
            else:
                print("Wrong password!")

        print("Too many attempts. Returning to main menu.")

    def registration(self):
        user_id = input("Create new ID: ")

        if user_id in self.users:
            print("User already exists!")
            return

        password = input("Create Password: ")

        self.users[user_id] = {
            "password": password,
            "balance": 0
        }

        print("Registration successful!")

    def account_menu(self, user_id):
        while True:
            print("\n--- Account Menu ---")
            print("1. Withdraw Amount")
            print("2. Deposit Amount")
            print("3. Check Balance")
            print("4. Back to Main Menu")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.withdraw(user_id)

            elif choice == "2":
                self.deposit(user_id)

            elif choice == "3":
                self.check_balance(user_id)

            elif choice == "4":
                return

            elif choice == "5":
                print("Goodbye!")
                exit()

            else:
                print("Invalid choice!")

    def withdraw(self, user_id):
        amount = int(input("Enter amount to withdraw: "))
        balance = self.users[user_id]["balance"]

        if amount <= 0:
            print("Amount cannot be negative or zero.")

        elif amount > balance:
            print("Insufficient balance!")

        else:
            self.users[user_id]["balance"] -= amount
            print(f"{amount} withdrawn successfully.")

    def deposit(self, user_id):
        amount = int(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount cannot be negative or zero.")

        else:
            self.users[user_id]["balance"] += amount
            print(f"{amount} deposited successfully.")

    def check_balance(self, user_id):
        print("Current Balance:", self.users[user_id]["balance"])


# Run Program
bank = BankManagementSystem()
bank.start()