from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

print("getattr(p,'x'):",getattr(p,'x'))
print("getattr(p,'y'):",getattr(p,'y'))