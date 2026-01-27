import array as arr

numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)

b=numericArray.tolist()
b.reverse()

revarray=arr.array('i',b)
print(revarray)