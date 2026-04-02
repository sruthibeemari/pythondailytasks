def BonusCalculator(func):
    def wrapper(self):
        bonus=self.salary*0.10
        self.salary=self.salary+bonus
        func(self)
    return wrapper
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @BonusCalculator
    def displaySalary(self):
        print("Employee Name: ",self.name)
        print("Salary: ",self.salary)


e1=Employee("Ram",50000)
e1.displaySalary()

