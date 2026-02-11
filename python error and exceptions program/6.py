try:
   dividend = int(input("Enter the dividend: "))
   divisor = int(input("Enter the divisor: "))
   result = dividend / divisor
   print(f"Result of division: {result}")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")