student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Modifying an existing key-value pair
student_info["age"]=22

# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)

del student_info["major"]

graduation_year= student_info.pop("graduation_year")
print(student_info)