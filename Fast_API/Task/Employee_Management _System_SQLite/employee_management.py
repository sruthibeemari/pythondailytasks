# ============================================================
# 👨‍💼 Employee Management System - FastAPI + SQLite
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Date
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import date

# ============================================================
# 🚀 FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ SQLite Database Connection
# ============================================================

DATABASE_URL = "sqlite:///./employee.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 📦 Models
# ============================================================

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    department = Column(String(100))
    salary = Column(Float)
    email = Column(String(100), unique=True)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    status = Column(String(20))
    date = Column(Date, default=date.today)

# ============================================================
# 📄 Create Tables
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 📝 Pydantic Schemas
# ============================================================

class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: float
    email: str


class AttendanceCreate(BaseModel):
    status: str

# ============================================================
# 🔌 Database Dependency
# ============================================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# ============================================================
# ➕ Add Employee
# ============================================================

@app.post("/employees")
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    new_employee = Employee(
        name=employee.name,
        department=employee.department,
        salary=employee.salary,
        email=employee.email
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "message": "Employee added successfully",
        "data": new_employee
    }

# ============================================================
# 📋 Get All Employees
# ============================================================

@app.get("/employees")
def get_all_employees(db: Session = Depends(get_db)):

    employees = db.query(Employee).all()

    return employees

# ============================================================
# 🔍 Get Employee By ID
# ============================================================

@app.get("/employees/{id}")
def get_employee(id: int, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(
        Employee.id == id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee

# ============================================================
# ✏️ Update Employee
# ============================================================

@app.put("/employees/{id}")
def update_employee(
    id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    db_employee = db.query(Employee).filter(
        Employee.id == id
    ).first()

    if not db_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db_employee.name = employee.name
    db_employee.department = employee.department
    db_employee.salary = employee.salary
    db_employee.email = employee.email

    db.commit()
    db.refresh(db_employee)

    return {
        "message": "Employee updated successfully",
        "data": db_employee
    }

# ============================================================
# ❌ Delete Employee
# ============================================================

@app.delete("/employees/{id}")
def delete_employee(id: int, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(
        Employee.id == id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }

# ============================================================
# 🏢 Get Employees By Department
# ============================================================

@app.get("/employees/department/{name}")
def employees_by_department(
    name: str,
    db: Session = Depends(get_db)
):

    employees = db.query(Employee).filter(
        Employee.department == name
    ).all()

    if not employees:
        raise HTTPException(
            status_code=404,
            detail="No employees found in this department"
        )

    return employees

# ============================================================
# 📅 Mark Attendance
# ============================================================

@app.post("/attendance/{id}")
def mark_attendance(
    id: int,
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    attendance_record = Attendance(
        employee_id=id,
        status=attendance.status
    )

    db.add(attendance_record)
    db.commit()
    db.refresh(attendance_record)

    return {
        "message": "Attendance marked successfully",
        "data": attendance_record
    }

# ============================================================
# 📋 Get Attendance Records
# ============================================================

@app.get("/attendance")
def get_attendance(db: Session = Depends(get_db)):

    records = db.query(Attendance).all()

    return records

# ============================================================
# 💰 High Salary Employees
# ============================================================

@app.get("/high-salary-employees")
def high_salary_employees(db: Session = Depends(get_db)):

    employees = db.query(Employee).filter(
        Employee.salary > 50000
    ).all()

    if not employees:
        raise HTTPException(
            status_code=404,
            detail="No high salary employees found"
        )

    return employees

# ============================================================
# 🔎 Search Employee By Name
# ============================================================

@app.get("/search-employee/{name}")
def search_employee(name: str, db: Session = Depends(get_db)):

    employees = db.query(Employee).filter(
        Employee.name.contains(name)
    ).all()

    if not employees:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employees

