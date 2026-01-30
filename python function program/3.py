def percentage(phy,maths,max_marks=200):
    val=(phy + maths) * 100/max_marks
    print(val)
    return val

maths=70
phy=60

result=percentage(phy,maths)
print(result)

phy=30
maths=40

result=percentage(phy,maths,100)
print(result)

percentage(phy,maths,176)