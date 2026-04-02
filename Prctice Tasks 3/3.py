"""
Q  :   Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""
num=range(1,21)
squre=map(lambda x:x**2,num)
print(list(squre))