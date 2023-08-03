# (polymorphism = poly(many) + morphs(forms))
class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    
    def getdetails(self):
        print("Name is : ",self.name)
        print("Color is : ",self.color)
        print("Price is : ",self.price)

    def max_speed(self):
        print("Maximum speed is 100 kmp/h") 
    
    def gear(self):
        print("Gear change is 6")
        
class Car(Vehicle):
    def max_speed(self):
        print("Maximum speed is 150 kmp/h") 
    
    def gear(self):
        print("Gear change is 7")

v1 = Vehicle("Moto","Red",1000000)
C1 = Car("Audi","Black",5000000)

v1.max_speed()
C1.max_speed()

v1.getdetails()
C1.getdetails()
