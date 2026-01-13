L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []
for x in L1:
    if x not in L2:
        L2.append(x)
print(L2)