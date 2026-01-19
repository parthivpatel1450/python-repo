from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Replace a field value
p2 = p._replace(x=30)

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)