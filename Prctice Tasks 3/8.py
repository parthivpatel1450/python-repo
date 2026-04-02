"""
Q   : Write a Python program to create a class-based decorator that logs the execution time of methods.
"""
import time

class LogTime:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self(instance, *args, **kwargs)

    def __call__(self, instance, *args, **kwargs):
        start = time.time()
        
        result = self.func(instance, *args, **kwargs)
        
        end = time.time()
        print(f"{self.func.__name__} took {end - start:.4f} sec")
        
        return result


class Test:
    @LogTime
    def show(self):
        time.sleep(1)
        print("Done")


# Run
t = Test()
t.show()