#METHOD 1
class cons:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x)
        print(self.y)

ob=cons(10,20)
print(ob.__dict__)
ob.show()

#METHOD 2
# class cons:
#     def __init__(self):
#         self.x=50
#         self.y=60
#     def show(self):
#         print(self.x)
#         print(self.y)
# ob=cons()
# ob.show()

#METHOD 3
# class cons:
#     def __init__(self):
#         self.x=50
#         self.y=60
#     def show(self,a,b):
#         print(self.x*a)
#         print(self.y*b)
#
# ob=cons()
# ob.show(2,3)

