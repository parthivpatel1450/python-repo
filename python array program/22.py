import array as arr
a=arr.array('i',[10,20,50,70,130,5,6])
largest=a[0]

for x in range(1,len(a)):
    if a[x]>largest:
        largest=a[x]

print(largest)