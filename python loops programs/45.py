n = int(input("N="))

a = 0
b = 1
z = [0, 1]

for x in range(1, n+1):
    total = a + b
    z.append(total)
    a, b = b, total

fib = z[n]  # Move this AFTER the loop
print(fib)