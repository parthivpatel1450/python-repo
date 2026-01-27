import array as arr
import copy
a=arr.array('i',[10,20,30,40,50])
b=copy.deepcopy(a)
print(b)

print(id(a),id(b))
a[2]=24
print(a,b)