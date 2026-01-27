import array as arr

# creating array
numericArray = arr.array('i', [88, 99, 77, 55, 66])

print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array:",revArray)