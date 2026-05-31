from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import ask_mentor

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/ask")
def ask_question(data: Question):

    return ask_mentor(data.question)