import array as arr
a=arr.array('i',[10,20,30,40,100])
print(a)
sum=0
for x in range(len(a)):
    sum+=a[x]
avarage=sum/len(a)
print(avarage)
