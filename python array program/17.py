import array as arr
a=arr.array('i',[10,80,5,20,30,40])

for x in range(0,len(a)):
    for y in range(x+1,len(a)):
        if (a[x]>a[y]):
            temp=a[x]
            a[x]=a[y]
            a[y]=temp
print(a)


