class Employee:
    def employeedetails(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def displayDetalis(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
a=Manager()
a.employeedetails("Ram",85000)
a.displayDetalis()

