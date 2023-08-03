
# Encapsulation = Wrapping up data and methods working on data together in a single unit(i.e class) is called encapsulation.

# inside class (methods + variables)

# class Employee:
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
    
#     def display(self):
#         print(f"name is {self.name} and salary is {self.sal}")

# obj = Employee()
# obj.display()

class Finance:
    def __init__(self):
        self.__rev = 100000              # Private data(__) : We cannot access data outside the class by object
        self._sales = 114               #  Protected data(_)  
        
    def display(self):                               # create method to access private and protected data
        print(f"Revenue is {self.__rev} and sales is {self._sales}")               
        self.__rev = 200000             # we can update the private data also using methods
        self._sales = 200
        print(f"Revenue is {self.__rev} and sales is {self._sales}")

f1  = Finance()
f1.display()             # only using method we can access the private and protected data

print(f1.__dict__) 
print(f1._Finance__rev)



