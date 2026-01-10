def pos(n):
    ## Write the code
    while(n>0):
        n-=1
        print(n, end=" ")
          
def neg(n):
    ##Write the code
     while(n<0):
        n+=1
        print(n, end=" ")

n=int(input("n= "))

if n>0:
    pos(n)
elif n<0:
    neg(n)
else:
    print("already zero")