import calculator

while True:
    print("\n Simple Calculator")
    print (" you have 4 options")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5 Exit")
    choice=int(input("enter your choice (1-5): "))
    if choice==5:
        print("Exiting Calculator...")
        break
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if choice==1:
        print("result: ",calculator.addition(a,b))
    elif choice==2:
        print("result: ",calculator.subtraction(a,b))
    elif choice==3:
        print("result: ",calculator.multiplication(a,b))
    elif choice==4:
        print("result: ",calculator.division(a,b))
    else:
        print("invalid choice")

