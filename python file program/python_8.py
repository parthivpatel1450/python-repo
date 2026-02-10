lines = [
    "print('Line 1')\n",
    "print('Line 2')\n",
    "print('Line 3')"
]

file = open("multi.py", "w")
file.writelines(lines)
file.close()
