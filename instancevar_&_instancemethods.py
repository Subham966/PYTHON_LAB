class Employee:
    "this is a oops programs"
    def __init__(self,nm,ag):
        self.name = nm   #name and age are instanace var
        self.age = ag

    def display(self):
        print(f"name is {self.name} and age is {self.age}")
        
    def change_name(self):
        self.name = input("Enter your name: ")
        self.age= int(input("Enter your age: "))
        print(f"Your name is {self.name} and age is {self.age}")

e1 = Employee("subham",24)
e2 = Employee("raj",25)

# print(e1.__dict__)
# e1.mark = 50
# print(e1.__dict__)

e2.change_name()


e2.change_name()
# print(e2.__dict__)
