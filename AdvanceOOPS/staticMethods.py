"""
Static Methods

Static methods belong to the class logically, but they don't need self or cls.

"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b
    
print(MathUtils.add(4,5))



"""
When to Use Static Methods?

Use them when the function:

Doesn't use instance variables
Doesn't use class variables
Is conceptually related to the class

For example:-
"""

class FileValidator:

    @staticmethod
    def is_csv(filename):
        return filename.endswith(".csv")
    
print(FileValidator.is_csv("customers.csv"))



"""
Comparison: Instance vs Class vs Static Methods

| Type            | First Parameter | Can Access Instance Data?      | Can Access Class Data?              | Typical Use                                      |
| --------------- | --------------- | ------------------------------ | ----------------------------------- | ------------------------------------------------ |
| Instance Method | `self`          | ✅ Yes                          | ✅ Yes                               | Operate on one object                            |
| Class Method    | `cls`           | ❌ No (unless object passed in) | ✅ Yes                               | Modify/access class-level state, factory methods |
| Static Method   | None            | ❌ No                           | ❌ No (unless referenced explicitly) | Utility/helper functions                         |

"""

