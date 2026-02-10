import os

print("This program will NOT change any files.")
print("Listing all Python files in the current folder:\n")

files = os.listdir(".")

for file in files:
    if file.endswith(".py"):
        print(file)

print("\nDry run completed.")
print("All files remain unchanged.")
