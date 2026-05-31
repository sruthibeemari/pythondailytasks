# Server/app.py

import os
import re

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from google import genai

from database import (
    DB_SCHEMA_CONTEXT,
    execute_read_query
)

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class Question(BaseModel):
    question: str


def extract_sql(text):

    match = re.search(
        r"```sql\s*(.*?)\s*```",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1)

    return text


@app.post("/chat")
def chat(data: Question):

    prompt = f"""
    You are a MySQL Expert.

    Database Schema:

    {DB_SCHEMA_CONTEXT}

    Rules:

    1. Generate ONLY SELECT queries.
    2. Never generate INSERT.
    3. Never generate UPDATE.
    4. Never generate DELETE.
    5. Never generate DROP.
    6. If the question is not related to:
       - employees
       - attendance
       - leave requests

       Return ONLY:
       BLOCKED

    7. Greetings or casual messages like:
       hi
       hello
       ok
       thanks
       good morning
       good evening
       how are you

       must return:
       BLOCKED

    8. Return SQL only inside ```sql``` block.

    User Question:
    {data.question}
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_text = response.text.strip()

        # Block unrelated questions
        if "BLOCKED" in ai_text.upper():

            return {
                "message":
                "Please ask questions related to Employees, Attendance, or Leave Requests."
            }

        sql_query = extract_sql(ai_text)

        columns, rows = execute_read_query(sql_query)

        if columns is None:

            return {
                "error": rows
            }

        return {
            "sql": sql_query,
            "columns": columns,
            "rows": rows
        }

    except Exception as e:

        return {
            "error": str(e)
        }