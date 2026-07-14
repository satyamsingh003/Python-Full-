from abc import ABC, abstractmethod

class Pipeline(ABC):
    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass

class CustomPipeline(Pipeline):
    def extract(self):
        print("Reading customer data")

    def transform(self):
        print("Transforming the data")

    def load(self):
        print("Loading the data")

class TransactionPipeline(Pipeline):
    def extract(self):
        print("Reading transactional data")
    
    def transform(self):
        print("laoding transactional data")

    def load(self):
        print("Loading hte transactional data")

"""
Absrtraction vs Encapsulation 

| Encapsulation                                           | Abstraction                                       |
| ------------------------------------------------------- | ------------------------------------------------- |
| Protects data                                           | Hides implementation                              |
| Focuses on data access                                  | Focuses on simplifying usage                      |
| Achieved using private/protected members and properties | Achieved using abstract classes and interfaces    |
| Answers **"How do I protect this?"**                    | Answers **"What functionality should I expose?"** |

"""

"""
one concept can work both and can use hte  both concept simultaneously 
Encapsulation and Abstraction

Encapsulation 

Bank Account

Balance

↓

Protected

↓

Deposit()

Withdraw()

Goal:- Protect the balance from invalid modifications.



Abstraction 

ATM

↓

Withdraw()

↓

Thousands of internal operations

Goal :-  Hide complexity from the user.

class BankAccount(ABC):

    def __init__(self):
        self.__balance = 1000

    @abstractmethod
    def withdraw(self, amount):
        pass
"""