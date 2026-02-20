"""Abstraction in Python
Difficulty: EasyAccuracy: 68.1%Submissions: 7K+Points: 2
Implement the following classes to understand abstraction in Python :
Note: Driver code makes all the function calls and print statements

Class Name: Shape (Abstract Class)
Attributes: color (String)
Constructor: Shape(c) -> assign value of c to color attribute
Methods: get_color() -> returns value of color
         get_area() -> abstract method with float return type
Class Name: Square (extends Shape)
Attributes: side (float)
Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
Methods: get_area() -> returns the area of the square (side * side).
Example:

Input: color = "red", side = 5.0
Output: 
red 25.0
"""

from abc import ABC, abstractmethod
#User function Template for python3
#  Implement both the classes here
class Shape:
    color=""
    def __Shape__(self,c):
        self.c="c"
    
    def get_color(self):
        return self.color
        
    @abstractmethod
    def  get_area(self) -> float:
        pass
    
class Square(Shape):
    side = None
    def __init__(self, c, side):
        super().__init__() 
        self.side = side 
    
    def get_area(self):
        return (self.side * self.side)
        