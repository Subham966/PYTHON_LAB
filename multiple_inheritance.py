# method 1
# class A:
#     def display(self):
#         print("1ST DISPLAY ")
        
# class B:
#     def display2(self,a,b):
#         print("2nd DISPLAY ")
#         print(a+b)

# class C(A,B):
#     def display3(self):
#         print("3rd DISPLAY ")    
   
# obj=C()
# obj.display()
# obj.display2(5,10)
# obj.display3()
        

# method 2
class cementdealer:
    def getcementcost(self,quantity):
        return quantity*300

class irondealer:
    def getironcost(self,quantity):
        return quantity*4500

class builder(cementdealer,irondealer):
    def gettotal(self,cm,ir):
        c_cost=self.getcementcost(cm)
        ir_cost=self.getironcost(ir)
        totalcost=c_cost+ir_cost
        return totalcost

cm=int(input("Enter cement quantity: "))
ir=int(input("Enter iron quantity: "))
obj=builder()
print(obj.gettotal(cm,ir))
