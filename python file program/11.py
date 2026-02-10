import os

print("Before:", os.getcwd())

os.chdir("my_folder")

print("After:", os.getcwd())
