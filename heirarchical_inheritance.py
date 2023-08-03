class base:
    a,b=10,20
    
class derived(base):
    def sum(self):
        add=self.a+self.b
        print(f"addition is : ",add)
        
class derived2(base):
    def multi(self):
        multiplication=self.a*self.b
        print(f"Multiplication is : ",multiplication)

obj=derived()
obj.sum()

obj2=derived2()
obj2.multi()
