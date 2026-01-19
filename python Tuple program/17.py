T1 = (36, 24, 3)
T2 = (84, 5, 81)

T3=[item for subtuple in [T1,T2] for item in subtuple]

print(T3)