class Father:
    def __init__(self):
        print("Father constructor called")       
        self.vehicle = "Scooter"
        
class Son(Father):
    def __init__(self):
        print("Son constructor called")       
        self.vehicle = "FZ" 
        
# f = Father()
s = Son()   
print(s.__dict__)


# Priority of child class constructor first if child class has his own constructor =constructor overriding
