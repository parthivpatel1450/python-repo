student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023

}

for key in student_info:
    print("keys:",key, ":",student_info[key])

for value in student_info.values():
    print("values : ",value)

for key, value in student_info.items():
    print("key:value:",key, value)




