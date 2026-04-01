name=input("enter student name: ")

file = open("attendance.txt","a")
file.write(name + "\n")
file.close()

file=open("attendance.txt","r")
print("Attendance record")
print(file.read())