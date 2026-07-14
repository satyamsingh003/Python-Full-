class Employee:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)

emp=Employee("Satyam")
emp.display()


"""
Python internally executes 

Employee.display(emp)
"""