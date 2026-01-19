from collections import namedtuple

vertex=namedtuple("vertex",['x','y','z'])

v=vertex(10,20,30)

print("vertex 1:",v.x)
print("vertex 2:",v[1])
print("vertex 3:",getattr(v,'z'))

