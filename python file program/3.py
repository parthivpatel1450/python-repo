file = open("9.py", "r")
words = file.read().split()
print("Total words:", len(words))
file.close()
