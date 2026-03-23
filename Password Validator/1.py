"""
Question: A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
 Example If the following passwords are given as input to the program:ABd1234@1,a F1#,2w3E*,2We3345
   Then, the output of the program should be: ABd1234@1
"""
def check_passwords(passwords):
    valid_passwords = []

    for p in passwords:
        if (6 <= len(p) <= 12 and
            any('a' <= ch <= 'z' for ch in p) and
            any('A' <= ch <= 'Z' for ch in p) and
            any('0' <= ch <= '9' for ch in p) and
            any(ch in "$#@" for ch in p)):
            
            valid_passwords.append(p)

    return ",".join(valid_passwords)

User_Name=input("Enter your Nmae: ")
user_input = input("Enter passwords (comma separated): ")

password_list = user_input.split(",")


print(check_passwords(password_list))

