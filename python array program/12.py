import array as arr
a = arr.array('i', [110, 220, 330, 440, 550])
b=a
print("Copied array:",b)
print (id(a), id(b))