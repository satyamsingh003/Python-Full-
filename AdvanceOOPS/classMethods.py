#  Suppose you want a method that works with the class, not individual objects.

# class Employee:

#     company="OPENAI"

#     @classmethod
#     def get_company(cls):
#         return cls.company
    
# print(Employee.get_company())

# instead of self we use here cls

# Why use class Method?


class DataBase:
    host="localhost"

    @classmethod

    def change_host(cls,new_host):
         cls.host=new_host

DataBase.change_host("db.company.com")
print(DataBase.host)


"""
Factory Methods

A common use of @classmethod is creating alternative constructors

"""


class Employee:
     
     def __init__(self,name,salary):
          self.name=name
          self.salary=salary

     @classmethod
     def from_string(cls,data):
          name, salary=data.split(',')
          return cls(name, int(salary))
     
emp= Employee.from_string("Satyam,8000")
print(emp.name)

# This is called a factory method because it constructs objects in a different way.

