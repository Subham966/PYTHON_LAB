class Employee:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag

    def display(self):
        print(f"name is {self.name} and age is {self.age}")

e1 = Employee("subham",24)
e2 = Employee("raj",25)


print(getattr(e1,"name"))

setattr(e1,"name","Rajnikant")
print(getattr(e1,"name"))
# print(e1.name)
print(e1.__dict__)

delattr(e1,"name")         #delete attribute
# getattr(e1,"name")
print(e1.__dict__)


print(hasattr(e1,"name"))