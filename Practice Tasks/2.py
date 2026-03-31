"""
Q :   With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.
"""

a=[12,24,35,24,88,120,155,88,120,155]
b=set(a)
c=list(b)
print(c)
d=c[::-1] 
print(d)