class demo:
    pass

d1 = demo()

class Employee:
    "this is a oops programs"
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag

    def display(self):
        print(f"name is {self.name} and age is {self.age}")

e1 = Employee("subham",24)
e2 = Employee("raj",25)

print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__doc__)
print(Employee.__module__)

print(isinstance(e1,Employee))
print(isinstance(d1,Employee))