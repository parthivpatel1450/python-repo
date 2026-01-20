n = int(input("N="))

a=0
b=1
z=[0,1]

for x in range(1,n+1):
    sum=a+b
    z.append(sum)
    a,b=b,sum
    
fib = z[n]
print(fib)
