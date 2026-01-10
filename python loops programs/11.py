list = ["geeksforgeeks", "C++",
         "Java", "Python", "C", "MachineLearning"]

i=0
size=len(list)
while (i<size):
    print(list[i])
    i+=1

i=0
while(True):
    print(list[i])
    i+=1
    if (i<size and len(list[i]) < 10):
        continue
    else:
        break

