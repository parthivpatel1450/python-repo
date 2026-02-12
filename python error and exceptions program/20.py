try:
   num = int(input('Enter a number: '))
   assert num >= 0, "Only non-negative numbers are accepted"
   print(num)
except AssertionError as msg:
   print(msg)