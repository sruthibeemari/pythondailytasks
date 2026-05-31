# Server/database.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

DB_SCHEMA_CONTEXT = """
Database Name: employee_management

Table: employees
Columns:
id (INT)
employee_id (VARCHAR)
name (VARCHAR)
salary (VARCHAR)
email (VARCHAR)

Table: attendance
Columns:
id (INT)
employee_name (VARCHAR)
date (VARCHAR)
status (VARCHAR)

Table: leave_requests
Columns:
id (INT)
employee_name (VARCHAR)
leave_date (VARCHAR)
reason (VARCHAR)
status (VARCHAR)
"""


def execute_read_query(query):

    try:

        with engine.connect() as conn:

            result = conn.execute(text(query))

            columns = list(result.keys())

            rows = [list(row) for row in result.fetchall()]

            return columns, rows

    except Exception as e:

        return None, str(e)