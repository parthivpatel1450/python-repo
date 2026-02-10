import os

filename = "sample_delete.py"

if os.path.exists(filename):
    os.remove(filename)
    print("File deleted safely")
else:
    print("File not found")
