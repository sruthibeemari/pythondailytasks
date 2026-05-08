from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Student Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int

# Temporary database
students = []

# Home API
@app.get("/")
def home():
    return {"message": "Student Management System"}

# Add Student
@app.post("/students")
def add_student(student: Student):

    students.append(student)

    return {
        "message": "Student added Successfully"
    }

# Get All Students
@app.get("/students")
def get_students():

    return students

# Get Student By ID
@app.get("/students/{id}")
def get_student(id: int):

    for student in students:

        if student.id == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# Update Student
@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.id == id:

            students[index] = updated_student

            return {
                "message": "Student updated successfully",
                "data": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# Delete Student
@app.delete("/students/{id}")
def delete_student(id: int):

    for index, student in enumerate(students):

        if student.id == id:

            students.pop(index)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )