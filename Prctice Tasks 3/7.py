"""
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
"""
a=(1,2,3,4,5,6,7,8,9,10)
for i in range(0,len(a)//2):
    print(a[i],end=" ")
print()
for i in range(len(a)//2,len(a)):
    print(a[i],end=" ")
