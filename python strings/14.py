digits = [str(x) for x in range(10)]
mystr = 'He12llo, Py00th55on!'
chars = []
for x in mystr:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print (newstr)
