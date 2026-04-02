class staff:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
    def display(self):
        print("Name: ",self.name)
        print("Designation: ",self.designation)
class Professor(staff):
    pass
class LabAssistant(staff):
    pass
class Administrator(staff):
    pass

p1=Professor("Ramu","Professor")
p2=LabAssistant("Rani", "Lab Asssistant") 
p3=Administrator("Shiva","Administrator")

p1.display()
p2.display()
p3.display()