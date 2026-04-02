"""
Q  :   Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""
num=range(1,11)
squre=map(lambda x:x**2,num)
b=list(squre)
even=filter(lambda x:x%2==0,b)
print(list(even))
