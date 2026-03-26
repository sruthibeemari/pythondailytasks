# find the student with the highest marks from a dictionary
students={
    "gopal":87,
    "govind":90,
    "mohan":60
}
top_student=max(students,key=students.get) #.get used to compare values values
print(top_student)

#without max

students={
    "gopal":87,
    "govind":90,
    "mohan":60
}
highest=0
top_student=""

for name in students:
    if students[name]>highest:
        highest=students[name]
        top_students= name

print(top_student,highest)