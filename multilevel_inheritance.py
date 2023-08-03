# class A:
#     def display(self):
#         print("1ST DISPLAY ")
        
# class B(A):
#     def display2(self,a,b):
#         print("2nd DISPLAY ")
#         print(a+b)
# class C(B):
#     def display3(self):
#         print("3rd DISPLAY ")       
# obj=C()
# obj.display()
# obj.display2(5,10)
# obj.display3()

class university:
    def getUdetails(self):
        self.Uname=input("Enter University name: ")
        self.Uid=input("Enter University id: ")
    def showUdeatils(self):
        print("University name: ",self.Uname)
        print("University id: ",self.Uid)
    
class college(university):
    def getCdetails(self):
        self.Cname=input("Enter college name: ")
        self.Cid=input("Enter college id: ")
        self.getUdetails()
    def showCdeatils(self):
        print("College name: ",self.Cname)
        print("College id: ",self.Cid)
        self.showUdeatils()

class student(college):
    def getSdetails(self):
        self.Sname=input("Enter Student name: ")
        self.Sen=input("Enter Student Enrollment no: ")
        self.Sbranch=input("Enter your branch: ")
        self.getCdetails()
    def showSdeatils(self):
        print("Student name: ",self.Sname)
        print("Student Enrollment no: ",self.Sen)
        print("Student branch: ",self.Sbranch)
        self.showCdeatils()

obj=student()
obj.getSdetails()
obj.showSdeatils()        

