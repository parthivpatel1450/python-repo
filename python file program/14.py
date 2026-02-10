import os

old_name = "created_by_2.py"
new_name = "renamed_file.py"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully")
else:
    print(f"Error: '{old_name}' file not found")
