"""
Write a Python program to create a data validation library using Python's dataclasses and type hints.
"""
from dataclasses import dataclass, field, fields

def validate(instance):
    for f in fields(instance):
        value = getattr(instance, f.name)
        expected_type = f.type

        
        if expected_type == float:
            if not isinstance(value, (int, float)):
                raise TypeError(f"{f.name} must be float")
        elif not isinstance(value, expected_type):
            raise TypeError(f"{f.name} must be {expected_type}")

        
        if f.metadata.get("min") is not None:
            if value < f.metadata["min"]:
                raise ValueError(f"{f.name} must be >= {f.metadata['min']}")

        
        if f.metadata.get("max") is not None:
            if value > f.metadata["max"]:
                raise ValueError(f"{f.name} must be <= {f.metadata['max']}")

@dataclass
class User:
    name: str
    age: int = field(metadata={"min": 18, "max": 60})
    salary: float = field(metadata={"min": 1000})

    def __post_init__(self):
        validate(self)



u1 = User("John", 25, 5000)   
print(u1)


u2 = User("Alice", 15, 500)