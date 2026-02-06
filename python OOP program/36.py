from dataclasses import dataclass, asdict
from typing import List 

@dataclass
class Student:
    name: str
    age: int
    grades: List[float]  

student = Student("Alice", 20, [88.5, 92.0, 79.5])
student_dict = asdict(student)
print(student_dict)