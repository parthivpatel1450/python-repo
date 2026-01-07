age=int(input("Enter your age = "))
y=input("are you a citizen(yes/no)?")

if age >= 18:
	if y.lower()=="yes":
		print("you are eligible to vote")
	else:
		print("must be a citizen")
else:
	print("you are not eligible for vote")