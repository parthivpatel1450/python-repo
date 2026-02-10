with open("1.py", "r") as source:
    with open("copy.py", "w") as target:
        target.write(source.read())
