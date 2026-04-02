class student():
    def studentDetails(self,name,rollnum,marks):
        self.name=name
        self.rollnum=rollnum
        self.marks=marks
    def display(self):
        print("Name: ",self.name)
        print( "Roll Number: ",self.rollnum)
        print("Marks: ",self.marks)

student1=student()
student2=student()
student3=student()

student1.studentDetails("raju",2,70)
student2.studentDetails("rani",3,90)
student3.studentDetails("ramu",4,68)


student1.display()
student2.display()
student3.display()

    