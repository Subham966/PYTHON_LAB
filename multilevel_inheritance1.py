# Multilevel inheritance
class humanbeing:
    def __init__(self):      
        print("Parent constructor called") 
        self.name = "Human being"
        
class employee(humanbeing):
    def __init__(self):
        super().__init__()      
        print("child constructor called")
        self.salary = 100000 

class manager(employee):
    def __init__(self):      
        super().__init__()      
        print("grand_child constructor called") 
        self.bonus = 2000
        
m = manager()
print(m.name)
print(m.salary)
print(m.bonus)
