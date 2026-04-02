"""
Q  :   Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""
num=range(1,21)
squre=filter(lambda x:x%2==0,num)
print(list(squre))