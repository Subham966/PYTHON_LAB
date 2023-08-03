class student:
    def std_details(self,name,roll,cls):
        self.name=name
        self.roll=roll
        self.cls=cls
        
    def std_result(self,mark,per,grade):
        self.mark=mark
        self.per=per
        self.grade=grade

    def display_deatils(self):
        print("Name of the student: ", self.name)
        print("Roll no of the student: ", self.roll)
        print("class of the student: ", self.cls)

    def display_result(self):
        print("Mark of the student: ", self.mark)
        print(" Percentage of the student: ", self.per)
        print("Grade of the student: ", self.grade)


st1=student()
st1.std_details("Subham",3,"Msc. DataScience")
st1.display_deatils()

st1.std_result(84,85,"o")
st1.display_result()
