class Employee:
    def __init__(self,emply_id,name,salary):
        self.emply_id=emply_id
        self.name=name
        self.salary=salary

    def display(self):
        return f"{self.emply_id,self.name,self.salary}"

employees={}

while True:
    emply_id=input("Enter Employee ID(or 'exit'): ")
    if emply_id.lower()=='exit':
        break
    name=input("Enter name:")


    try:
        salary=float(input("Enter Salary: "))
    except ValueError:
        print(" Invalid! please enter only number")
        continue

    emp=Employee(name,emply_id,salary)
    employees[emply_id]=emp


with open("emp.txt", "w") as file:
    for emp in employees.values():
        file.write(emp.display()+"\n")


print("All employess: \n")
for emp in employees.values():
    print(emp.display())
