class Employee:
    def setname(self,nm):        # Setter = Set the value 
        self.name = nm
        
    def getname(self):          # Getter = Fetch the value
        print(f"The Name is :",self.name)


e1 = Employee()
e2 = Employee()
e1.setname("Subham")
e2.setname("Rajesh")

print(e1.__dict__)
print(e2.__dict__)

e1.getname()
e2.getname()