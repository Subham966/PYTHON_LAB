class student:
    def std_details(self,name,roll,cls):
        print("Name of the student: ",name)
        print("Roll no of the student: ",roll )
        print("class of the student: ",cls)

    def std_result(self,mark,per,grade):
        print("Mark of the student: ",mark)
        print(" Percentage of the student: ",per )
        print("Grade of the student: ",grade)
st1=student()
st2=student()

print("Student1 records: ")
st1.std_details("Subham",3,"Msc. DataScience")
st1.std_result(84,85,"o")

print("Student2 records: ")
st2.std_details("Pradhan",5,"MCA")
st2.std_result(80,90,"A")