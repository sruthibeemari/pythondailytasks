# ============================================================
# 👨‍💼 Employee Management System - FastAPI + MongoDB Atlas
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os
import certifi

# ============================================================
# 🚀 FastAPI App
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 Load Environment Variables
# ============================================================

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# ============================================================
# 🍃 MongoDB Atlas Connection
# ============================================================

client = MongoClient(
    MONGO_URL,
    tlsCAFile=certifi.where()
)

db = client[DATABASE_NAME]

employee_collection = db["employees"]
attendance_collection = db["attendance"]

# ============================================================
# 📝 Pydantic Schemas
# ============================================================

class Employee(BaseModel):
    employee_id: int
    name: str
    department: str
    salary: float
    email: str


class Attendance(BaseModel):
    status: str

# ============================================================
# 🔄 Serializer Functions
# ============================================================

def employee_serializer(employee) -> dict:
    return {
        "employee_id": employee["employee_id"],
        "name": employee["name"],
        "department": employee["department"],
        "salary": employee["salary"],
        "email": employee["email"]
    }


def attendance_serializer(attendance) -> dict:
    return {
        "employee_id": attendance["employee_id"],
        "status": attendance["status"],
        "date": attendance["date"]
    }

# ============================================================
# ➕ Add Employee
# ============================================================

@app.post("/employees")
def add_employee(employee: Employee):

    existing_employee = employee_collection.find_one(
        {"employee_id": employee.employee_id}
    )

    if existing_employee:
        raise HTTPException(
            status_code=400,
            detail="Employee ID already exists"
        )

    employee_collection.insert_one(
        employee.model_dump()
    )

    new_employee = employee_collection.find_one(
        {"employee_id": employee.employee_id}
    )

    return {
        "message": "Employee added successfully",
        "data": employee_serializer(new_employee)
    }

# ============================================================
# 📋 Get All Employees
# ============================================================

@app.get("/employees")
def get_all_employees():

    employees = employee_collection.find()

    return [
        employee_serializer(employee)
        for employee in employees
    ]

# ============================================================
# 🔍 Get Employee By ID
# ============================================================

@app.get("/employees/{id}")
def get_employee(id: int):

    employee = employee_collection.find_one(
        {"employee_id": id}
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee_serializer(employee)

# ============================================================
# ✏️ Update Employee
# ============================================================

@app.put("/employees/{id}")
def update_employee(id: int, employee: Employee):

    existing_employee = employee_collection.find_one(
        {"employee_id": id}
    )

    if not existing_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee_collection.update_one(
        {"employee_id": id},
        {
            "$set": {
                "name": employee.name,
                "department": employee.department,
                "salary": employee.salary,
                "email": employee.email
            }
        }
    )

    updated_employee = employee_collection.find_one(
        {"employee_id": id}
    )

    return {
        "message": "Employee updated successfully",
        "data": employee_serializer(updated_employee)
    }

# ============================================================
# ❌ Delete Employee
# ============================================================

@app.delete("/employees/{id}")
def delete_employee(id: int):

    employee = employee_collection.find_one(
        {"employee_id": id}
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee_collection.delete_one(
        {"employee_id": id}
    )

    return {
        "message": "Employee deleted successfully"
    }

# ============================================================
# 🏢 Get Employees By Department
# ============================================================

@app.get("/employees/department/{name}")
def employees_by_department(name: str):

    employees = employee_collection.find(
        {"department": name}
    )

    employee_list = [
        employee_serializer(employee)
        for employee in employees
    ]

    if not employee_list:
        raise HTTPException(
            status_code=404,
            detail="No employees found in this department"
        )

    return employee_list

# ============================================================
# 📅 Mark Attendance
# ============================================================

@app.post("/attendance/{id}")
def mark_attendance(id: int, attendance: Attendance):

    employee = employee_collection.find_one(
        {"employee_id": id}
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    attendance_data = {
        "employee_id": id,
        "status": attendance.status,
        "date": str(datetime.now().date())
    }

    attendance_collection.insert_one(
        attendance_data
    )

    return {
        "message": "Attendance marked successfully",
        "data": attendance_data
    }

# ============================================================
# 📋 Get Attendance Records
# ============================================================

@app.get("/attendance")
def get_attendance():

    records = attendance_collection.find()

    return [
        attendance_serializer(record)
        for record in records
    ]

# ============================================================
# 💰 High Salary Employees
# ============================================================

@app.get("/high-salary-employees")
def high_salary_employees():

    employees = employee_collection.find(
        {"salary": {"$gt": 50000}}
    )

    employee_list = [
        employee_serializer(employee)
        for employee in employees
    ]

    if not employee_list:
        raise HTTPException(
            status_code=404,
            detail="No high salary employees found"
        )

    return employee_list

# ============================================================
# 🔎 Search Employee By Name
# ============================================================

@app.get("/search-employee/{name}")
def search_employee(name: str):

    employees = employee_collection.find(
        {
            "name": {
                "$regex": name,
                "$options": "i"
            }
        }
    )

    employee_list = [
        employee_serializer(employee)
        for employee in employees
    ]

    if not employee_list:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee_list

# ============================================================
# Get Attendance By Date
# ============================================================

@app.get("/attendance/date/{date}")
def get_attendance_by_date(date: str):

    records = attendance_collection.find(
        {"date": date}
    )

    attendance_list = [
        attendance_serializer(record)
        for record in records
    ]

    if not attendance_list:
        raise HTTPException(
            status_code=404,
            detail="No attendance found for this date"
        )

    return attendance_list