from typing import Optional

from fastapi import FastAPI, HTTPException
from sqlalchemy import func, inspect, text
from sqlalchemy.exc import IntegrityError
from database import SessionLocal, engine
from models import Base, Employee, Attendance, LeaveRequest
from schemas import EmployeeSchema, AttendanceSchema, LeaveSchema, LeaveStatusUpdate

Base.metadata.create_all(bind=engine)


def ensure_leave_status_column():
    inspector = inspect(engine)
    if "leave_requests" not in inspector.get_table_names():
        return
    columns = {column["name"] for column in inspector.get_columns("leave_requests")}
    if "status" not in columns:
        with engine.begin() as conn:
            conn.execute(
                text(
                    "ALTER TABLE leave_requests "
                    "ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'Pending'"
                )
            )


ensure_leave_status_column()

app = FastAPI()


def generate_next_employee_id(db):
    prefix = "EMP"
    max_num = 0
    for emp in db.query(Employee).all():
        eid = (emp.employee_id or "").upper()
        if eid.startswith(prefix):
            suffix = eid[len(prefix):]
            if suffix.isdigit():
                max_num = max(max_num, int(suffix))
    return f"{prefix}{max_num + 1:03d}"


def get_employee_by_employee_id(db, employee_id: str, exclude_id: Optional[int] = None):
    normalized = employee_id.strip().upper()
    query = db.query(Employee).filter(func.upper(Employee.employee_id) == normalized)
    if exclude_id is not None:
        query = query.filter(Employee.id != exclude_id)
    return query.first()


# ---------------- EMPLOYEE ---------------- #

@app.get("/next_employee_id")
def next_employee_id():
    db = SessionLocal()
    try:
        return {"employee_id": generate_next_employee_id(db)}
    finally:
        db.close()


@app.post("/add_employee")
def add_employee(employee: EmployeeSchema):
    db = SessionLocal()
    try:
        employee_id = employee.employee_id.strip()
        if get_employee_by_employee_id(db, employee_id):
            raise HTTPException(status_code=400, detail="Employee ID already exists.")

        new_employee = Employee(
            employee_id=employee_id,
            name=employee.name.strip(),
            salary=employee.salary.strip(),
            email=employee.email.strip(),
        )
        db.add(new_employee)
        db.commit()
        return {"message": "Employee Added Successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Employee ID already exists.")
    finally:
        db.close()


@app.get("/employees")
def get_employees():
    db = SessionLocal()
    try:
        return db.query(Employee).all()
    finally:
        db.close()


@app.get("/search_employee/{name}")
def search_employee(name: str):
    db = SessionLocal()
    try:
        return db.query(Employee).filter(Employee.name.like(f"%{name}%")).all()
    finally:
        db.close()


@app.put("/edit_employee/{id}")
def edit_employee(id: int, employee: EmployeeSchema):
    db = SessionLocal()
    try:
        emp = db.query(Employee).filter(Employee.id == id).first()
        if not emp:
            raise HTTPException(status_code=404, detail="Employee not found.")

        employee_id = employee.employee_id.strip()
        existing = get_employee_by_employee_id(db, employee_id, exclude_id=id)
        if existing:
            raise HTTPException(status_code=400, detail="Employee ID already exists.")

        emp.employee_id = employee_id
        emp.name = employee.name.strip()
        emp.salary = employee.salary.strip()
        emp.email = employee.email.strip()
        db.commit()
        return {"message": "Employee Updated Successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Employee ID already exists.")
    finally:
        db.close()


@app.delete("/delete_employee/{id}")
def delete_employee(id: int):
    db = SessionLocal()
    try:
        emp = db.query(Employee).filter(Employee.id == id).first()
        if not emp:
            raise HTTPException(status_code=404, detail="Employee not found.")
        db.delete(emp)
        db.commit()
        return {"message": "Employee Deleted Successfully"}
    finally:
        db.close()


# ---------------- ATTENDANCE ---------------- #

@app.post("/mark_attendance")
def mark_attendance(attendance: AttendanceSchema):
    db = SessionLocal()
    try:
        employee = get_employee_by_employee_id(db, attendance.employee_id)
        if not employee:
            raise HTTPException(status_code=400, detail="Employee ID does not exist.")

        new_attendance = Attendance(
            employee_name=employee.name,
            date=attendance.date,
            status=attendance.status,
        )
        db.add(new_attendance)
        db.commit()
        return {"message": "Attendance Marked"}
    finally:
        db.close()


@app.get("/attendance")
def get_attendance():
    db = SessionLocal()
    try:
        return db.query(Attendance).all()
    finally:
        db.close()


# ---------------- LEAVE ---------------- #

@app.post("/apply_leave")
def apply_leave(leave: LeaveSchema):
    db = SessionLocal()
    try:
        employee = get_employee_by_employee_id(db, leave.employee_id)
        if not employee:
            raise HTTPException(status_code=400, detail="Employee ID does not exist.")

        new_leave = LeaveRequest(
            employee_name=employee.name,
            leave_date=leave.leave_date,
            reason=leave.reason,
            status="Pending",
        )
        db.add(new_leave)
        db.commit()
        return {"message": "Leave Applied Successfully"}
    finally:
        db.close()


@app.get("/leave_requests")
def leave_requests():
    db = SessionLocal()
    try:
        return db.query(LeaveRequest).all()
    finally:
        db.close()


@app.patch("/leave_requests/{leave_id}/status")
def update_leave_status(leave_id: int, update: LeaveStatusUpdate):
    if update.status not in ("Approved", "Rejected"):
        raise HTTPException(status_code=400, detail="Status must be Approved or Rejected.")

    db = SessionLocal()
    try:
        leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
        if not leave:
            raise HTTPException(status_code=404, detail="Leave request not found.")

        leave.status = update.status
        db.commit()
        return {"message": f"Leave {update.status.lower()}.", "status": leave.status}
    finally:
        db.close()
