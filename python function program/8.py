def myfunction(x, /, y, *, z):
   print (x, y, z)
   
myfunction(10, y=20, z=30)
myfunction(10, 20, z=30)