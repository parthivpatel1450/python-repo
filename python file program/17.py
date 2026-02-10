import os

if os.path.exists("renamed_file.py"):
    os.rename("renamed_file.py", "final_file.py")
    print("File renamed safely")
else:
    print("File does not exist")
