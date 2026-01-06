# This function calculates the factorial of a number
def factorial(n):
   if n < 0:
      return "Factorial is not defined for negative numbers"
   result = 1
   for i in range(1, n + 1):
      result *= i
   return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")