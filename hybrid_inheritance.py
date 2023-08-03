class school:
    def fun1(self):
        print('Im the school class')

class teacher1(school):
    def fun2(self):
        print('Im a techer 1')

class teacher2(school):
    def fun3(self):
        print('Im a techer 2')

class student(teacher1,teacher2):
    def fun4(self):
        print('Im a student')
        
        
obj = student()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()