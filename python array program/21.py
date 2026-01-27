import array as arr
a = arr.array('i', [88, 99, 77, 66, 44, 22])
b = arr.array('i', [12, 17, 18, 11, 13, 10])

a.extend(b)
print(a)