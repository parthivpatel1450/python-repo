a=10
b=0

try:
    print(a/b)
except Exception:
    print("General Exception")
finally:
    print("inside outer finally block")

    