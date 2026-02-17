class Student:  
    def __init__(self, name: str, age: int, percent: float):  
        self.name = name  
        self.age = age  
        self.percent = percent  
    def __repr__(self):  
        return f"Student(name={self.name}, age={self.age}, percent={self.percent})"  
    def __eq__(self, other):  
        if not isinstance(other, Student):  
            return NotImplemented  
        return (self.name == other.name and self.age == other.age and self.percent == other.percent)
s1 = Student("Alice", 20, 90.0)
s2 = Student("Bob", 22, 85.5)
print(s1)
print(s1 == s2)