"""
Question: Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.

"""

class DivisablebySeven:
    def __init__(self,n):
        self.n=n

    def generate(self):
        for i in range(self.n + 1):
            if i%7==0:
                yield i

n=int(input("Enter your range : "))
obj=DivisablebySeven(n)
for num in obj.generate():
    print(num)
        

