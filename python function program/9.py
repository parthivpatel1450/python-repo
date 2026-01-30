# arbitary arguments
def add(*a):
    total=0
    for x in a:
        total+=x
    return total

b=add(10,20,30,40)
print(b)