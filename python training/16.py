# Traditional way
print("Using traditional way:")
results = []
for x in range(10):
    y = x * x
    if y > 20:
        results.append(y)
print(results, "\n")


# Simplify using walrus operator
print("Using walrus operator:")
results = [y for x in range(10) if (y := x * x) > 20]
print(results)