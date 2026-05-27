from pydantic import BaseModel

class EmployeeSchema(BaseModel):
    employee_id: str
    name: str
    salary: str
    email: str


class AttendanceSchema(BaseModel):
    employee_id: str
    date: str
    status: str


class LeaveSchema(BaseModel):
    employee_id: str
    leave_date: str
    reason: str


class LeaveStatusUpdate(BaseModel):
    status: str