a=int(input("a="))
b=int(input("b="))
operator=int(input("operator="))

def sign(operator):
    if operator==1:
        print(a+b)
    elif operator==2:
        print(b-a)
    elif operator==3:
        print(a*b)
    else:
        print("invalid operation")

sign(operator)
    