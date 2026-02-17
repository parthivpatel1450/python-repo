class Duck:
   def sound(self):
      return "Quack, quack!"

class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"

def makeSound(duck):
   print(duck.sound())

duck = Duck()
anotherBird = AnotherBird()
makeSound(duck)   
makeSound(anotherBird) 