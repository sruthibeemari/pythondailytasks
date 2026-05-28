from fastapi import APIRouter
from services.gemini_service import ask_gemini

router = APIRouter()

@router.post("/ask")
def ask_question(data: dict):
    question = data.get("question")
    response = ask_gemini(question)

    return {"response": response}