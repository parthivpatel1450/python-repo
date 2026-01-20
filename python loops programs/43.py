n=int(input("N = "))

is_prime=True

for x in range(2,int(n ** 0.5) + 1):
    if n%x==0:
        is_prime=False
        break
    else:
        is_prime=True

if is_prime and n>1:
    print("True")
else:
    print("False")