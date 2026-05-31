import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are a Senior Full Stack Developer Mentor.

Return ONLY valid JSON.

{
  "answer": "Short direct answer",
  "key_points": [
    "Point 1",
    "Point 2",
    "Point 3"
  ],
  "example": "Small example",
  "next_step": "Next topic to learn"
}

Do not wrap JSON in markdown.
Do not use ```json.
Return raw JSON only.
"""

def ask_mentor(question):

    prompt = f"""
    {SYSTEM_PROMPT}

    User Question:
    {question}
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = getattr(response, "text", str(response))

        # print("\n===== GEMINI RESPONSE =====")
        # print(text)
        # print("===========================\n")

        # Remove markdown fences if Gemini still adds them
        text = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(text)

        except Exception as e:
            print("JSON Parse Error:", e)

            return {
                "answer": text
            }

    except Exception as e:

        return {
            "error": str(e)
        }