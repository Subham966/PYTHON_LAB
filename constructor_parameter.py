class Employee:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag


e1 = Employee("subham",24)
e2 = Employee("raj",25)

print(e1.__dict__)