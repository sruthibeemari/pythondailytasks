from sqlalchemy import Column, Integer, String
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(50), unique=True)
    name = Column(String(100))
    salary = Column(String(100))
    email = Column(String(100))


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String(100))
    date = Column(String(100))
    status = Column(String(20))


class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String(100))
    leave_date = Column(String(100))
    reason = Column(String(300))
    status = Column(String(20), default="Pending")