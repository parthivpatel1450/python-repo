#User function Template for python3
a = int(input("a="))
b = int(input("b="))

# Your code here
if a<=b:
    for x in range(b,0,-1):
        if a%x==0 and b%x==0:
            break
    print(x)
        
