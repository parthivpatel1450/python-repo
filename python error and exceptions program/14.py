a=10
b=0
try:
   print (a/b)
   try:
      print ("This is inner try block")
   except Exception:
      print ("General exception")
   finally:
      print ("inside inner finally block")

except ZeroDivisionError:
   print("division by 0")
finally:
   print("inside outer finally block")
   