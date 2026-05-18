# ============================================================
# 🔐 FastAPI TODO App + JWT Authentication + MySQL
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
from typing import List

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

'''
Format:

mysql+pymysql://username:password@localhost/database_name
'''

DATABASE_URL = "mysql+pymysql://root:root123@localhost/fastapi_jwt"

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

class Todo(BaseModel):

    id: int
    title: str
    completed: bool = False

# ------------------------------------------------------------

class Login(BaseModel):

    username: str
    password: str

# ============================================================
# 🗃️ TEMPORARY TODO STORAGE
# ============================================================

todos: List[Todo] = []

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    # Copy data
    to_encode = data.copy()

    # Add expiry time
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({"exp": expire})

    # Generate JWT token
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

        # Decode token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract username
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
        "message": "FastAPI + JWT + MySQL 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(
    user: Login,
    db: Session = Depends(get_db)
):

    # Find user in database
    db_user = db.query(UserDB).filter(
        UserDB.username == user.username
    ).first()

    # Check credentials
    if not db_user or db_user.password != user.password:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Generate JWT token
    access_token = create_access_token(
        data={"sub": db_user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(
    todo: Todo,
    user: str = Depends(verify_token)
):

    # Check duplicate ID
    for existing in todos:

        if existing.id == todo.id:

            raise HTTPException(
                status_code=400,
                detail="ID already exists"
            )

    # Add todo
    todos.append(todo)

    return {
        "message": "Todo created",
        "data": todo
    }

# ============================================================
# ✅ READ ALL TODOS
# ============================================================

@app.get("/todos")
def get_all_todos(
    user: str = Depends(verify_token)
):

    return {
        "count": len(todos),
        "data": todos
    }

# ============================================================
# ✅ READ SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for todo in todos:

        if todo.id == todo_id:

            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    updated: Todo,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):

        if todo.id == todo_id:

            todos[index] = updated

            return {
                "message": "Todo updated successfully",
                "data": updated
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):

        if todo.id == todo_id:

            deleted = todos.pop(index)

            return {
                "message": "Todo deleted successfully",
                "data": deleted
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
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