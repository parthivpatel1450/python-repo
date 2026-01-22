# Defining a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Iterating through the Nested Dictionary:
for student, details in students.items():
   print(f"Student: {student}")
   for key, value in details.items():
      print(f"  {key}: {value}")