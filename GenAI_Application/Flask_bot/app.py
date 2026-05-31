import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        return jsonify({
            "response": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)