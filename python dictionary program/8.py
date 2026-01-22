# Creating a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Using the items() method to get key-value pairs
all_items = student_info.items()
print("Items:", all_items)  
# Iterating through the key-value pairs
print("Iterating through key-value pairs:")
for key, value in all_items:
    print(f"{key}: {value}")