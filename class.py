class firstclass:
    a=100
    b=200
    def fun(self,a,b):
        print(a+b)
    def fun2(self,a,b):
        print(a-b)
ob=firstclass()
print(ob.a)
print(ob.b)
ob.fun(10,5)
ob.fun2(10,5)