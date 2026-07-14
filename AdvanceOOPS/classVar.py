class Employee:

    company="OPENAI"

    def __init__(self,name):
        self.name=name

obj=Employee("Anthropic")
print(obj.company)


"""

Memory;- 


Employee Class

company = "OpenAI"

↓

e1 → name = "Satyam"

e2 → name = "Rahul"


We can change the name of hte company or assign a vlaue to any other by e1.company="Google"

"""




class Employee:
    company = "OpenAI"

e1 = Employee()
e2 = Employee()

e1.company = "Microsoft"

print(e1.company)
print(e2.company)
print(Employee.company)

"""
Output :-  

Microsoft
OpenAI
OpenAI
"""
        