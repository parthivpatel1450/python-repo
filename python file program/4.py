with open("binary.py", "wb") as file:
    file.write(b"print('Binary write example')")

with open("binary.py", "rb") as file:
    print(file.read())
