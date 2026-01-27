import array as arr
a=arr.array('i',[1,2,3,4,5,6,8,9])
b=arr.array('i')

for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(b)