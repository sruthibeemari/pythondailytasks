# ============================================================
# 🔐 FastAPI Student Management + JWT + MySQL
# ============================================================

# ============================================================
# 📦 INSTALL PACKAGES
# ============================================================

'''
pip install fastapi uvicorn python-jose sqlalchemy pymysql
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta

# SQLAlchemy Imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MYSQL DATABASE CONNECTION
# ============================================================

DATABASE_URL = "mysql+pymysql://root:root123@localhost/student_db"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class
Base = declarative_base()

# ============================================================
# 👤 USER TABLE MODEL
# ============================================================

class UserDB(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True)

    password = Column(String(100))

# ============================================================
# 🎓 STUDENT TABLE MODEL
# ============================================================

class StudentDB(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    age = Column(Integer)

    course = Column(String(100))

    marks = Column(Integer)

# ============================================================
# ✅ CREATE TABLES
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 🔄 DATABASE SESSION
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)

# ============================================================
# 🧾 PYDANTIC MODELS
# ============================================================

class Student(BaseModel):

    id: int
    name: str
    age: int
    course: str
    marks: int

# ------------------------------------------------------------

class Login(BaseModel):

    username: str
    password: str

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    # Copy data
    to_encode = data.copy()

    # Add expiry time
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({"exp": expire})

    # Generate token
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ------------------------------------------------------------

def verify_token(token: str = Depends(oauth2_scheme)):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Student Management + JWT + MySQL 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(
    user: Login,
    db: Session = Depends(get_db)
):

    # Find user
    db_user = db.query(UserDB).filter(
        UserDB.username == user.username
    ).first()

    # Validate credentials
    if not db_user or db_user.password != user.password:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Generate token
    access_token = create_access_token(
        data={"sub": db_user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

# ============================================================
# ➕ ADD STUDENT
# ============================================================

@app.post("/students")
def add_student(
    student: Student,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    # Check duplicate ID
    existing_student = db.query(StudentDB).filter(
        StudentDB.id == student.id
    ).first()

    if existing_student:

        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    # Create student object
    new_student = StudentDB(
        id=student.id,
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    # Add into database
    db.add(new_student)

    db.commit()

    return {
        "message": "Student added successfully",
        "data": student
    }

# ============================================================
# 📄 GET ALL STUDENTS
# ============================================================

@app.get("/students")
def get_students(
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    students = db.query(StudentDB).all()

    return students

# ============================================================
# 🔍 GET STUDENT BY ID
# ============================================================

@app.get("/students/{id}")
def get_student(
    id: int,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if student:

        return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# ✏️ UPDATE STUDENT
# ============================================================

@app.put("/students/{id}")
def update_student(
    id: int,
    updated_student: Student,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if student:

        student.name = updated_student.name
        student.age = updated_student.age
        student.course = updated_student.course
        student.marks = updated_student.marks

        db.commit()

        return {
            "message": "Student updated successfully",
            "data": updated_student
        }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# ❌ DELETE STUDENT
# ============================================================

@app.delete("/students/{id}")
def delete_student(
    id: int,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if student:

        db.delete(student)

        db.commit()

        return {
            "message": "Student deleted successfully"
        }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ============================================================
# 🌐 RUN SERVER
# ============================================================

'''
uvicorn main:app --reload
'''

# ============================================================
# 🌐 SWAGGER DOCS
# ============================================================

'''
http://127.0.0.1:8000/docs
'''