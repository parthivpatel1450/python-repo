from dataclasses import dataclass  

@dataclass  
class Student:  
    name: str  
    age: int  
    percent: float

s1 = Student("Alice", 20, 90.0)
s2 = Student("Bob", 22, 85.5)

print(s1)         
print(s1 == s2)   