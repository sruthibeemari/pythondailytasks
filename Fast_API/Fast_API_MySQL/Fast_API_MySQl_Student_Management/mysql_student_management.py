# ============================================================
# 🎓 FastAPI Student Management System - MySQL Version
# pip install fastapi uvicorn sqlalchemy pymysql
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
DATABASE_URL = "mysql+pymysql://root:root123@localhost:3306/student_db"

'''
mysql+pymysql://root:1234@localhost:3306/student_db
│      │         │    │    │         │    │
│      │         │    │    │         │    └── Database name
│      │         │    │    │         └────── Port
│      │         │    │    └──────────────── Hostname
│      │         │    └───────────────────── Password
│      │         └────────────────────────── Username
│      └──────────────────────────────────── Driver
└─────────────────────────────────────────── Database type
'''

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ------------------------------------------------------------
# 🧱 Table Model
# ------------------------------------------------------------
class StudentDB(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    age = Column(Integer)
    course = Column(String(255))
    marks = Column(Integer)

# Create Table
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Schema (Pydantic)
# ------------------------------------------------------------
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int

    class Config:
        from_attributes = True

# ------------------------------------------------------------
# 🔌 DB Dependency
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 Home
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "FastAPI + MySQL Student Management 🚀"}

# ------------------------------------------------------------
# ✅ CREATE STUDENT
# ------------------------------------------------------------
@app.post("/students")
def add_student(student: Student, db: Session = Depends(get_db)):

    existing_student = db.query(StudentDB).filter(
        StudentDB.id == student.id
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = StudentDB(
        id=student.id,
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student added successfully",
        "data": new_student
    }

# ------------------------------------------------------------
# ✅ GET ALL STUDENTS
# ------------------------------------------------------------
@app.get("/students")
def get_students(db: Session = Depends(get_db)):

    students = db.query(StudentDB).all()

    return {
        "count": len(students),
        "data": students
    }

# ------------------------------------------------------------
# ✅ GET STUDENT BY ID
# ------------------------------------------------------------
@app.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

# ------------------------------------------------------------
# ✅ UPDATE STUDENT
# ------------------------------------------------------------
@app.put("/students/{id}")
def update_student(
    id: int,
    updated_student: Student,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated_student.name
    student.age = updated_student.age
    student.course = updated_student.course
    student.marks = updated_student.marks

    db.commit()
    db.refresh(student)

    return {
        "message": "Student updated successfully",
        "data": student
    }

# ------------------------------------------------------------
# ✅ DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }