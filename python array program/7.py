import array as arr

a = arr.array('i', [111, 211, 311, 411, 511])

print ("Before removing:", a)

a.remove(311)
print ("After removing:", a)