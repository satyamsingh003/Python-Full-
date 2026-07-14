# "Dunder" means Double UNDERscore.

"""
__init__

__str__

__repr__

__len__

__eq__

__add__

__call__
"""



# __str__

#Without __str__

class Employee:
    pass

emp = Employee()

print(emp)

# Output :- <__main__.Employee object at 0x104eb25d0>


#With __str__

class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee({self.name})"
print(Employee("Satyam"))

# Output :- Employee(Satyam)



#__repr__()

# __repr__ is aimed more at developers and debugging.

class Employee:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Employee(name='{self.name}')"

print(Employee("Satyam"))


# Output:- Employee(name='Satyam')

# A good __repr__ often looks like valid Python code that could recreate the object


# __len__


class Team:

    def __init__(self):
        self.members = ["A", "B", "C"]

    def __len__(self):
        return len(self.members)

team = Team()

print(len(team))

# Output:- 3



# __eq__().  :-  Use for object comparison

class Employee:

    def __init__(self, emp_id):
        self.emp_id = emp_id

    def __eq__(self, other):
        return self.emp_id == other.emp_id

e1 = Employee(101)
e2 = Employee(101)

print(e1 == e2)

# Output:- True

# Without __eq__, Python compares object identity (memory addresses), not logical equality.



# __add__()

#. Customize the + operator.


class Salary:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Salary(self.amount + other.amount)

    def __str__(self):
        return str(self.amount)
    
s1 = Salary(50000)
s2 = Salary(30000)

print(s1 + s2)

# Output:- 80000
# Without __str__ =  <__main__.Salary object at 0x1058fc3e0>


# __call__(). :-  Make an object behave like a function.

class Greeter:

    def __call__(self, name):
        print(f"Hello {name}")

g = Greeter()

g("Satyam")

# Output:- Hello Satyam

#. Notice that g is an object, but you can call it like a function.

# This pattern is used in frameworks like PyTorch, where model objects are callable.




# Iterators: __iter__() and __next__()


# Python for loop  works with iterators


class CountToThree:

    def __init__(self):
        self.current=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current>3:
            raise StopIteration
        value=self.current
        self.current+=1
        return value
    
for i in CountToThree():
    print(i)


# This is the mechanism behind iterating over lists, files, generators, and many framework objects.


# Context Managers: __enter__() and __exit__()


# with open("data.txt") as f:
#     data = f.read()

# how does with work?

# Behind the scene:-

class FileManager:

    def __enter__(self):
        print("Opening resource")
        return self
    
    def __exit__(self, exc_type, exc_value, trackback):
        print("Closing resource")

with FileManager():
    print("Using resource")


# Output:-  Opening resource
# Using resource
# Closing resource


"""
This ensures cleanup even if an exception occurs.

This pattern is used extensively for:

Database connections
Files
Network sockets
Locks
Spark sessions
Temporary resources
"""


# Real DE Example:

# with DatabaseConnection() as conn:
#     conn.execute("SELECT * FROM customers")


# When the with block exits, the connection is automatically closed.

# Without context managers, it's easy to forget cleanup and leak resources.


# Summary Diagram

"""
Advanced Python OOP

├── Variables
│   ├── Instance Variables
│   └── Class Variables
│
├── Methods
│   ├── Instance Methods
│   ├── Class Methods
│   └── Static Methods
│
├── Magic Methods
│   ├── __str__
│   ├── __repr__
│   ├── __len__
│   ├── __eq__
│   ├── __add__
│   ├── __call__
│   ├── __iter__
│   └── __next__
│
└── Context Managers
    ├── __enter__
    └── __exit__
"""
