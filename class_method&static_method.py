class vsp:
    def a(self):
        print("Hello")
        
    @classmethod
    def b(cls):
        print("This is class method")

    @staticmethod
    def c():
        print("This is static method")

ob=vsp()
ob.a()

vsp.b()

vsp.c()