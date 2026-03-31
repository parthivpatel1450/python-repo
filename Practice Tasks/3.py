"""
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?
"""
from sympy import symbols, Eq, solve

head = int(input("Enter the number of heads:"))
legs = int(input("Enter the number of legs:"))
if legs%2==0:
    x , y = symbols('x y')
    eq1 = Eq(x + y, head)
    eq2 = Eq(4*x + 2*y, legs)

    solution = solve((eq1, eq2), (x, y))
else:
    print("Invalid number of legs")
print(f"Rabbits: {solution[x]} and Chickens: {solution[y]}")