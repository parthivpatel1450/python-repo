"""
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and 
the values are square of keys. The function should just print the keys only.
"""



def squregenerator(a):
    f={}
    for i in range(a+1):
        key=i
        value=i**2
        f[key]=value

    for i in f:
        print(i)

a=int(input("Enter your range between 1 to 20 : "))
squregenerator(a)