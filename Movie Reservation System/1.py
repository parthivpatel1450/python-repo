class MovieReservationSystem:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "admin"}
        }

        self.movies = {
            "M101": {
                "name": "Avengers",
                "showtime": "6 PM",
                "seats": 10
            }
        }

    # ---------------- MAIN MENU ----------------
    def main_menu(self):
        while True:
            print("\n--- Movie Reservation System ---")
            print("1. Login")
            print("2. Signup")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.signup()
            elif choice == "3":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

    # ---------------- SIGNUP ----------------
    def signup(self):
        username = input("Enter username: ")

        if username in self.users:
            print("User already exists!")
            return

        password = input("Enter password: ")

        self.users[username] = {
            "password": password,
            "role": "user"
        }

        print("Signup successful!")

    # ---------------- LOGIN ----------------
    def login(self):
        username = input("Enter username: ")

        if username not in self.users:
            print("User not found!")
            return

        for i in range(3):
            password = input("Enter password: ")

            if password == self.users[username]["password"]:
                print("Login successful!")

                if self.users[username]["role"] == "admin":
                    self.admin_menu()
                else:
                    self.user_menu(username)

                return
            else:
                print(f"Wrong password! Attempts left: {2 - i}")

        print("Too many attempts!")

    # ---------------- ADMIN MENU ----------------
    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Movie")
            print("2. View Movies")
            print("3. Delete Movie")
            print("4. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_movie()
            elif choice == "2":
                self.view_movies()
            elif choice == "3":
                self.delete_movie()
            elif choice == "4":
                return
            else:
                print("Invalid choice!")

    # ---------------- USER MENU ----------------
    def user_menu(self, username):
        while True:
            print("\n--- User Menu ---")
            print("1. View Movies")
            print("2. Book Ticket")
            print("3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.view_movies()
            elif choice == "2":
                self.book_ticket(username)
            elif choice == "3":
                return
            else:
                print("Invalid choice!")

    # ---------------- ADD MOVIE ----------------
    def add_movie(self):
        movie_id = input("Enter Movie ID: ")

        if movie_id in self.movies:
            print("Movie already exists!")
            return

        name = input("Enter Movie Name: ")
        showtime = input("Enter Showtime: ")

        try:
            seats = int(input("Enter total seats: "))
        except ValueError:
            print("Invalid number!")
            return

        self.movies[movie_id] = {
            "name": name,
            "showtime": showtime,
            "seats": seats
        }

        print("Movie added successfully!")

    # ---------------- VIEW MOVIES ----------------
    def view_movies(self):
        if not self.movies:
            print("No movies available.")
            return

        for mid, details in self.movies.items():
            print("-" * 30)
            print(f"Movie ID: {mid}")
            print(f"Name: {details['name']}")
            print(f"Showtime: {details['showtime']}")
            print(f"Available Seats: {details['seats']}")

    # ---------------- DELETE MOVIE ----------------
    def delete_movie(self):
        movie_id = input("Enter Movie ID to delete: ")

        if movie_id not in self.movies:
            print("Movie not found!")
            return

        del self.movies[movie_id]
        print("Movie deleted successfully!")

    # ---------------- BOOK TICKET ----------------
    def book_ticket(self, username):
        movie_id = input("Enter Movie ID: ")

        if movie_id not in self.movies:
            print("Movie not found!")
            return

        try:
            seats = int(input("Enter number of seats: "))
        except ValueError:
            print("Invalid number!")
            return

        if seats <= 0:
            print("Invalid seat count!")
            return

        if seats > self.movies[movie_id]["seats"]:
            print("Not enough seats available!")
            return

        self.movies[movie_id]["seats"] -= seats

        print(f"Booking successful for {username}!")
        print(f"Seats booked: {seats}")


# ---------------- RUN PROGRAM ----------------
system = MovieReservationSystem()
system.main_menu()