a=5
b=0

try:
    print("this is outer try block")
    try:
        print(a/b)
    except ZeroDivisionError:
        print("division by 0")
    finally:
        print("inside inner finally block")
except Exception:
    print("General Exception")
finally:
    print("inside outer finallly block")
    