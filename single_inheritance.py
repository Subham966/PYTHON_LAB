# INHERITANCE: Process of copying methods and properties of a class into another class.
# It makes acode reusable.
# Important feature of OOPS.

class base:
    def display(self,a,b):
        print("1ST DISPLAY ")
        return a+b
        
class derived(base):
    def display2(self,a,b):
        print("2nd DISPLAY ")
        return a*b
        
obj=derived()
print(obj.display(10,20))
print(obj.display2(50,60))