n=int(input("N = "))

for i in range(1, n + 1):
    if i==1:
        print("*")
    elif i==n:
        print("* "*n)
    else:
        space=" " * (2 * (i-1)- 1)
        print("*" + space + "*")












        
        