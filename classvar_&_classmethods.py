class Employee:
    place = "Berhampur"       # Class variable = "Place"
    
    def __init__(self,nm,ag):
        self.name = nm   # name and age are instanace variable
        self.age = ag
        
    @classmethod
    def get_company_place(cls):
        print(f"company name is: ",cls.place)
        cls.place = "Ganjam"                  # Update comp name 
        print(f"company name is: ",cls.place)
  

e1 = Employee("subham",24)
e2 = Employee("raj",25)

print(Employee.place)   # By class print class variable
print(e1.place)        # By object print class variable
Employee.get_company_place()