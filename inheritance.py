class Employee:
    bonus = 2000                                # inheritance uses for reusuability
    def display(self):
        print("This is a employee class method")       
        

class manager(Employee):
    bonus1 = 5000
    def show(self):
        print("This is a manager class method")       
        
   
e1 = Employee()
m1 = manager()

e1.display()
m1.show()
print(m1.bonus)