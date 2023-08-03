class student:
    s1_name="sss666"
    x=100
    def st_info(self,name,roll):
        self.name=name
        self.roll=roll
    def st_show(self):
        print(self.name)
        print(self.roll)


st1=student()
st2=student()
print(st1.s1_name)
print(st1.x)
st1.st_info("subham",3)
st1.st_show()
st2.st_info("Pradhan",5)
st2.st_show()
