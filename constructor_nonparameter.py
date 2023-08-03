class Employee:
    def __init__(self):
        self.name = "subham"
        self.age = 24
    
    # def display(self):
        # print(self.name)

e1 = Employee()
# e1 = Employee("subham",24)
# e2 = Employee("raj",25)

print(e1.__dict__)