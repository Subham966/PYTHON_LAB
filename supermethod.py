# class Computer:
#     def __init__(self):      
#         self.ram = "8gb"
#         self.storage = "512gb"
#         print("Parent constructor called") 
        
# class Mobile(Computer):
#     def __init__(self):
#         super().__init__()
#         self.model = "Google pixel 6A"       
#         self.vehicle = "FZ" 
#         print("Child constructor called")

# c = Mobile()   
# print(c.__dict__)


class Computer:
    def __init__(self,ram,storage):      
        self.ram = ram
        self.storage = storage
        print("Parent constructor called") 
    
    def display(self):
        print("Hello AWS")
        
class Mobile(Computer):
    def __init__(self,ram,storage):
        super().__init__(ram,storage)     #super().__init__("8gb","512gb")
        super().display()
        self.model = "Google pixel 6A"       
        self.vehicle = "FZ" 
        print("Child constructor called")

c = Mobile("8gb","512gb")   
print(c.__dict__)