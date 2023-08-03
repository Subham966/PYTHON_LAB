class Employee:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag

    def display(self):
        print(f"name is {self.name} and age is {self.age}")

e1 = Employee("subham",24)
e2 = Employee("raj",25)

print(e1.__dict__)
print(e1.name)
print(e2.age)
e2.age=30
print(e2.age)

e2.display()
