import os
import shutil

# Remove empty directory
os.rmdir("my_folder")

# Remove non-empty directory
shutil.rmtree("parent")

print("Directories removed successfully")
