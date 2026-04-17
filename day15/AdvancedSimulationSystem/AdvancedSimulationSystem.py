import random
import numpy as np
import pandas as pd
import math
#1
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.grade=self.assign_grade()

    def assign_grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return "B"
        elif self.marks>=50:
            return "C"
        else:
            return "Fail"
    def display(self):
        return f"{self.name} {self.marks} {self,self.grade}"
    
try:
#2
    names=[f"S{i+1}" for i in range(10)]
    marks=[random.randint(0,100) for _ in range(10)]
#3
    marks_array=np.array(marks)
#4
    df=pd.DataFrame({
        "Name":names,
        "Marks":marks_array
    })
#5
    students=[]
    for i in range(len(df)):
        s=Student(df.loc[i,"Name"],df.loc[i,"Marks"])
        students.append(s)
#6
    mean=math.fsum(marks_array)/len(marks_array)
    min=min(marks_array)
    max=max(marks_array)

#7
    with open("report.txt", "w") as f:
        f.write("Student Report\n")
        f.write("----------------\n")
        for s in students:
            f.write(s.display() + "\n")
            f.write(f"\nMean: {mean}\n")
            f.write(f"Max: {max}\n")
            f.write(f"Min: {min}\n")

#8
    print(df)
    print("\nStudent Grades:")
    for s in students:
        print(s.display())
        
        print("\nStatistics:")
        print("Mean:", mean)
        print("Max:", max)
        print("Min:", min)
except Exception as e:
    print("Error:", e)