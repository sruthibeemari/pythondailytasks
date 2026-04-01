
highest_salary = 0
highest_employee = ""

with open("employees.txt", "r") as file:
    print("Employee Details:\n")
    
    for line in file:
        name, salary = line.split()
        salary = int(salary)
        
        print(name, salary)
        
        if salary > highest_salary:
            highest_salary = salary
            highest_employee = name

print("\nHighest Salary Employee:")
print(highest_employee, highest_salary)

name = input("\nEnter new employee name: ")
salary = input("Enter salary: ")

with open("employees.txt", "a") as file:
    file.write(name + " " + salary + "\n")

print("New employee added.")